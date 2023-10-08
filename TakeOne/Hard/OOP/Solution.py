import collections
from typing import List


class File:
    def __init__(self, file_name, file_contents):
        self.file_name = file_name
        self.file_contents = file_contents


class Directory:
    def __init__(self, directory_name):
        self.child_directories = collections.defaultdict(Directory)
        self.child_files = collections.defaultdict(File)
        self.directory_name = directory_name

    def add_file(self, file_name, file_contents):
        self.child_files[file_name] = File(file_name, file_contents)

    def add_directory(self, directory_name):
        self.child_directories[directory_name] = Directory(directory_name)


class FileSystem:

    def __init__(self):
        self.root = Directory('')

    def recursive_traverse(self, directory, path_remaining):
        if not path_remaining or len(path_remaining) == 1:
            return directory
        next_directory_name = path_remaining[0]
        if next_directory_name in directory.child_directories:
            return self.recursive_traverse(directory.child_directories[next_directory_name], path_remaining[1:])
        else:
            raise Exception('Invalid Path')

    def ls(self, path: str = '') -> List[str]:
        path = path.split('/')
        final_path = path[-1]
        parent_directory = self.recursive_traverse(self.root, path)
        if final_path in parent_directory.child_directories:
            directory = parent_directory.child_directories[final_path]
            return sorted(directory.child_directories + directory.child_files)
        elif final_path in parent_directory.child_files:
            return [final_path]
        else:
            raise Exception('Invalid path')

    def mkdir(self, path: str) -> None:

        def recursive_make(directory, path_remaining):
            if not path_remaining:
                return
            directory_name = path_remaining[0]
            if directory_name not in directory.child_directories:
                directory.child_directories[directory_name] = Directory(directory_name)
            recursive_make(directory.child_directories[directory_name], path_remaining[1:])

        path = path.split('/')
        recursive_make(self.root, path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath.split('/')
        file_name = path[-1]
        parent_directory = self.recursive_traverse(self.root, path)
        if file_name in parent_directory.child_directories:
            raise Exception('Invalid path')
        elif file_name in parent_directory.child_files:
            parent_directory.child_files[file_name].file_contents += content
        else:
            parent_directory.child_files[file_name] = File(file_name, content)

    def readContentFromFile(self, filePath: str) -> str:
        path = filePath.split('/')
        file_name = path[-1]
        parent_directory = self.recursive_traverse(self.root, path)
        if file_name not in parent_directory.child_files:
            raise Exception('invalid path')
        else:
            return parent_directory.child_files[file_name].file_contents

    def sudo_rm_dash_rf(self):
        # sudo remove recursive force
        # dangerous functionality!
        pass

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
