from typing import List
import collections


class TrieNode:
    def __init__(self, word: str = None):
        self.word = word
        self.children = collections.defaultdict(dict)


class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        def insert_helper(node, word_remaining):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    child = TrieNode()
                    node.children[word_remaining[0]] = child
                insert_helper(node.children[word_remaining[0]], word_remaining[1:])

        insert_helper(self.head, word)

    def search(self, word: str) -> bool:
        def search_helper(node, word_remaining) -> bool:
            if not word_remaining:
                return node.word is not None
            return word_remaining[0] in node.children and search_helper(node.children[word_remaining[0]],
                                                                        word_remaining[1:])

        return search_helper(self.head, word)

    def starts_with(self, prefix: str) -> bool:
        def starts_with_helper(node, prefix_remaining):
            if not prefix_remaining:
                return len(node.children.keys()) != 0 or node.word is not None
            return prefix_remaining[0] in node.children and starts_with_helper(node.children[prefix_remaining[0]],
                                                                               prefix_remaining[1:])

        return starts_with_helper(self.head, prefix)


class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        def add_word_helper(node, word_remaining):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    child = TrieNode()
                    node.children[word_remaining[0]] = child
                add_word_helper(node.children[word_remaining[0]], word_remaining[1:])

        add_word_helper(self.head, word)

    def search(self, word: str) -> bool:
        def search_helper(node, word_remaining):
            if not word_remaining:
                return node.word is not None
            if word_remaining[0] == ".":
                for child in node.children.keys():
                    if search_helper(node.children[child], word_remaining[1:]):
                        return True
            return word_remaining[0] in node.children and search_helper(node.children[word_remaining[0]],
                                                                        word_remaining[1:])

        return search_helper(self.head, word)
