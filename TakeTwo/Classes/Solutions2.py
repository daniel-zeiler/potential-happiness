from typing import List, Optional
from collections import defaultdict


class AutoCompleteSystemNode:
    def __init__(self):
        self.word = None
        self.times = 0
        self.children = defaultdict(AutoCompleteSystemNode)


class AutocompleteSystem:
    def __init__(self, words: List[str], times: [int]):
        self.root = AutoCompleteSystemNode()
        self.current_input = ""
        self.cursor = self.root
        for word, time in zip(words, times):
            self.insert(word, time)

    def insert(self, word, time):
        self.insert_helper(self.root, word, word, time)

    def insert_helper(self, node, word_remaining, word, time):
        if not word_remaining:
            node.word = word
            node.times = time
        else:
            if word_remaining[0] not in node.children:
                node.children[word_remaining[0]] = AutoCompleteSystemNode()
            self.insert_helper(node.children[word_remaining[0]], word_remaining[1:], word, time)

    def input_character(self, character: str) -> List[str]:
        if character == "#":
            if self.current_input:
                if self.cursor:
                    self.insert_helper(self.cursor, character, self.current_input, 1)
                else:
                    self.insert_helper(self.root, self.current_input, self.current_input, 1)
            self.cursor = self.root
            self.current_input = ""
        else:
            self.current_input += character
            if self.cursor and character in self.cursor.children:
                self.cursor = self.cursor.children[character]
                result = sorted(self.gather(self.cursor), key=lambda x: -x[0])
                return [x[1] for x in result[:min(3, len(result))]]
            else:
                self.cursor = None
        return []

    def gather(self, node) -> List[str]:
        result = []
        if node.word:
            result.append((node.times, node.word))
        for child_node in node.children.values():
            result.extend(self.gather(child_node))
        return result


class File:
    def __init__(self, file_name: str = None, file_contents: str = None):
        self.file_name = file_name
        self.file_contents = file_contents


class Directory:
    def __init__(self, directory_name: str = None):
        self.files = defaultdict(File)
        self.directories = defaultdict(Directory)
        self.directory_name = directory_name
        self.parent_directory = None


class FileSystem:
    def __init__(self):
        self.root = Directory()
        self.cursor = self.root

    def add_file(self, file_path, contents):
        if not file_path:
            return Exception("Invalid File Path")
        file_path = file_path.split("/")
        target_directory = self.find_target_directory(self.cursor, file_path)
        target_directory.files[file_path[-1]] = File(file_path[-1], contents)

    def add_directory(self, file_path):
        if not file_path:
            return Exception("Invalid File Path")
        file_path = file_path.split("/")
        target_directory = self.find_target_directory(self.cursor, file_path)
        target_directory.directories[file_path[-1]] = Directory(file_path[-1])

    def list_directory(self, file_path):
        if not file_path:
            return (list(self.cursor.directories.keys()) +
                    list(self.cursor.files.keys()))
        file_path = file_path.split("/")
        target_directory = self.find_target_directory(self.cursor, file_path)
        if file_path[-1] in target_directory.directories:
            return (list(target_directory.directories[file_path[-1]].directories.keys()) +
                    list(target_directory.directories[file_path[-1]].files.keys()))
        raise Exception("Invalid file path")

    def read_file(self, file_path):
        if not file_path:
            return Exception("Invalid File Path")
        file_path = file_path.split("/")
        target_directory = self.find_target_directory(self.cursor, file_path)
        if file_path[-1] in target_directory.files:
            return target_directory.files[file_path[-1]].file_contents
        raise Exception("File not found")

    def change_directory(self, file_path):
        temp = self.cursor
        for dir in file_path.split("/"):
            if dir in self.cursor.directories:
                self.cursor = self.cursor.directories[dir]
            elif dir == "..":
                if self.cursor.parent_folder:
                    self.cursor = self.cursor.parent_folder
            else:
                self.cursor = temp

    def find_target_directory(self, directory: Directory, file_path_remaining) -> Directory:
        if len(file_path_remaining) == 1:
            return directory
        elif file_path_remaining[0] == ".." and directory.parent_directory:
            return self.find_target_directory(directory.parent_directory, file_path_remaining[1:])
        elif file_path_remaining[0] in directory.directories:
            return self.find_target_directory(directory.directories[file_path_remaining[0]], file_path_remaining[1:])
        raise Exception("invalid file path")
