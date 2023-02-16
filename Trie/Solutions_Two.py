from typing import List
import collections


class TrieNode:

    def __init__(self, children=None, word=False):
        if children is None:
            children = collections.defaultdict(TrieNode)
        self.word = word
        self.children = children


class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        def recursive_insert(word_remaining, node):
            if not word_remaining:
                node.word = word
                return
            elif word_remaining[0] not in node.children:
                child_node = TrieNode()
                node.children[word_remaining[0]] = child_node
            recursive_insert(word_remaining[1:], node.children[word_remaining[0]])

        recursive_insert(word, self.head)

    def search(self, word: str) -> bool:
        def recursive_search(word_remaining, node):
            if not word_remaining:
                if node.word == word:
                    return True
                return False
            if word_remaining[0] not in node.children:
                return False
            return recursive_search(word_remaining[1:], node.children[word_remaining[0]])

        return recursive_search(word, self.head)

    def starts_with(self, prefix: str) -> bool:
        def traverse_down(prefix_remaining, node):
            if not prefix_remaining:
                return True
            if prefix_remaining[0] not in node.children:
                return False
            return traverse_down(prefix_remaining[1:], node.children[prefix_remaining[0]])

        return traverse_down(prefix, self.head)


class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        def recursive_add(word_remaining, node):
            if not word_remaining:
                node.word = word
                return
            elif word_remaining[0] not in node.children:
                node.children[word_remaining[0]] = TrieNode()
            recursive_add(word_remaining[1:], node.children[word_remaining[0]])

        recursive_add(word, self.head)

    def search(self, word: str) -> bool:
        def recursive_search(word_remaining, node):
            if not word_remaining:
                return True
            if word_remaining[0] == ".":
                for key in node.children.keys():
                    if recursive_search(word_remaining[1:], node.children[key]):
                        return True
            elif word_remaining[0] in node.children:
                return recursive_search(word_remaining[1:], node.children[word_remaining[0]])
            return False

        return recursive_search(word, self.head)
