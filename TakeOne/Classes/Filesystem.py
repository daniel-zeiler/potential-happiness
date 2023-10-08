import unittest


class File:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents


class Directory:
    def __init__(self, name):
        self.name = name
        self.child_directories = {}
        self.child_files = {}


class FileSystem:
    def __init__(self):
        self.root = Directory('')

    def traverse_to_parent_directory(self, node, file_path):
        if len(file_path) == 1:
            return node
        directory = file_path[0]
        if directory == '':
            return self.traverse_to_parent_directory(node, file_path[1:])
        if directory not in node.child_directories:
            return None
        return self.traverse_to_parent_directory(node.child_directories[directory], file_path[1:])

    def add_file(self, file_path, contents):
        file_path = file_path.split('/')
        node = self.traverse_to_parent_directory(self.root, file_path)
        file_name = file_path[-1]
        if node and file_name not in node.child_directories:
            if file_name in node.child_files:
                node.child_files[file_name].contents += contents
            else:
                node.child_files[file_name] = File(file_name, contents)

    def add_directory(self, file_path):
        file_path = file_path.split('/')

        def recursive_add_directory(node, path_remaining):
            if path_remaining:
                dir_name = path_remaining[0]
                if dir_name == '':
                    recursive_add_directory(node, path_remaining[1:])
                    return
                if dir_name in node.child_files:
                    return
                elif dir_name not in node.child_directories:
                    node.child_directories[dir_name] = Directory(dir_name)
                recursive_add_directory(node.child_directories[dir_name], path_remaining[1:])

        recursive_add_directory(self.root, file_path)

    def list_directory(self, file_path):
        file_path = file_path.split('/')

        def recursive_list(node, path_remaining):
            if not path_remaining:
                return list(node.child_directories.keys()) + list(node.child_files.keys())
            next_directory = path_remaining[0]
            if next_directory == '':
                return recursive_list(node, path_remaining[1:])
            if next_directory not in node.child_directories:
                return []
            return recursive_list(node.child_directories[next_directory], path_remaining[1:])

        return recursive_list(self.root, file_path)

    def read_file(self, file_path):
        file_path = file_path.split('/')
        node = self.traverse_to_parent_directory(self.root, file_path)
        file_name = file_path[-1]
        if node and file_name in node.child_files:
            return node.child_files[file_name].contents


class TestingFileSystem(unittest.TestCase):
    def test_file_system(self):
        file_system = FileSystem()
        file_system.add_file('/something.txt', 'this is the contents of the file')
        self.assertEqual('this is the contents of the file', file_system.read_file('/something.txt'))
        file_system.add_file('/something.txt', 'this is the contents of the file')
        file_system.add_directory('/a_dir')
        file_system.add_file('/a_dir/something_else.txt', 'how now brown cow')
        self.assertEqual('how now brown cow', file_system.read_file('a_dir/something_else.txt'))
        self.assertListEqual(['something_else.txt'], file_system.list_directory('/a_dir'))
        self.assertListEqual(['a_dir', 'something.txt'], file_system.list_directory(''))
