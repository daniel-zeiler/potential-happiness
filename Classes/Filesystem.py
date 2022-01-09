import collections
from typing import Any


class Directory:
    def __init__(self, path, directory_name):
        self.children = collections.defaultdict(Any)
        self.path = path
        self.directory_name = directory_name

    def add_file(self, file_name, path, contents):
        if file_name in self.children:
            if not isinstance(self.children[file_name], File):
                raise Exception('invalid filename %', file_name)
            self.children[file_name].contents += contents
        else:
            self.children[file_name] = File(path, file_name, contents)

    def add_directory(self, filename, directory):
        self.children[filename] = directory


class File:
    def __init__(self, path, filename, contents):
        self.filename = filename
        self.path = path
        self.contents = contents


class Filesystem:
    def __init__(self):
        self.root = Directory('', '')

    def traverse_to(self, current_directory, path):
        if not path:
            return current_directory
        elif path[0] not in current_directory.children or not isinstance(current_directory.children[path[0]],
                                                                         Directory):
            raise Exception('invalid path %s', path)
        else:
            return self.traverse_to(current_directory.children[path[0]], path[1:])

    def add_file(self, path, contents):
        split_path = path.split('/')
        target_directory = split_path[1:-1]
        file_name = split_path[-1]
        directory = self.traverse_to(self.root, target_directory)
        directory.add_file(file_name, path, contents)

    def list_path(self, path):
        split_path = path.split('/')
        target_directory = split_path[1:-1]
        directory = self.traverse_to(self.root, target_directory)
        result = []
        for child in directory.children.values():
            if isinstance(child, File):
                result.append(child.filename)
            else:
                result.append('/' + child.directory_name)
        return result

    def read_contents(self, path):
        split_path = path.split('/')
        target_directory = split_path[1:-1]
        file_name = split_path[-1]
        directory = self.traverse_to(self.root, target_directory)
        if file_name not in directory.children or not isinstance(directory.children[file_name], File):
            raise Exception('invalid file name %s', file_name)
        else:
            return directory.children[file_name].contents

    def add_directory(self, path):
        split_path = path.split('/')
        target_directory = split_path[1:-1]
        directory_name = split_path[-1]
        directory = self.traverse_to(self.root, target_directory)
        directory.add_directory(directory_name, Directory(path, directory_name))


file_system = Filesystem()
file_system.add_file('/something.txt', 'this is the contents of the file')
file_system.add_file('/something.txt', 'this is the contents of the file')
file_system.add_directory('/a_dir')
file_system.add_file('/a_dir/something_else.txt', 'how now brown cow')
print(file_system.read_contents('/something.txt'))
print(file_system.list_path('/a_dir/'))
