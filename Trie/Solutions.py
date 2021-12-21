import collections
from typing import List


class TrieNode:
    def __init__(self, word=None):
        self.word = word
        self.children = collections.defaultdict(TrieNode)


class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        def insert_char(remaining_word, node):
            if not remaining_word:
                node.word = word
                return
            if remaining_word[0] not in node.children:
                node.children[remaining_word[0]] = TrieNode()
            node = node.children[remaining_word[0]]
            insert_char(remaining_word[1:], node)

        insert_char(word, self.head)

    def search(self, word: str) -> bool:
        def search_char(remaining_word, node):
            if not remaining_word:
                return node.word is not None
            if remaining_word[0] not in node.children:
                return False
            elif search_char(remaining_word[1:], node.children[remaining_word[0]]):
                return True
            return False

        return search_char(word, self.head)

    def starts_with(self, prefix: str) -> bool:
        def starts_with_char(remaining_prefix, node):
            if not remaining_prefix:
                return True
            elif remaining_prefix[0] not in node.children:
                return False
            else:
                return starts_with_char(remaining_prefix[1:], node.children[remaining_prefix[0]])

        return starts_with_char(prefix, self.head)


class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        def add_char(word_remaining, node):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    node.children[word_remaining[0]] = TrieNode()
                node = node.children[word_remaining[0]]
                add_char(word_remaining[1:], node)

        add_char(word, self.head)

    def search(self, word: str) -> bool:
        def search_char(word_remaining, node):
            if not word_remaining:
                return node.word is not None
            if word_remaining[0] == '.':
                for key in node.children:
                    if search_char(word_remaining[1:], node.children[key]):
                        return True
                return False
            elif word_remaining[0] not in node.children:
                return False
            else:
                return search_char(word_remaining[1:], node.children[word_remaining[0]])

        return search_char(word, self.head)


class ReplaceWordTrie:
    def __init__(self):
        self.head = TrieNode()

    def add(self, word):
        def add_character(word_remaining, node):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    node.children[word_remaining[0]] = TrieNode()
                node = node.children[word_remaining[0]]
                add_character(word_remaining[1:], node)

        add_character(word, self.head)

    def starts_with(self, word):
        def starts_with_character(word_remaining, node):
            if node.word:
                return node.word
            elif word_remaining[0] not in node.children:
                return None
            else:
                return starts_with_character(word_remaining[1:], node.children[word_remaining[0]])

        return starts_with_character(word, self.head)


def replaceWords(dictionary: List[str], sentence: str) -> str:
    trie = ReplaceWordTrie()
    for word in dictionary:
        trie.add(word)

    result = []
    for word in sentence.split(' '):
        replacement = trie.starts_with(word)
        if replacement:
            result.append(replacement)
        else:
            result.append(word)
    return ' '.join(result)


class MagicDictionary:

    def __init__(self):
        pass

    def buildDict(self, dictionary: List[str]) -> None:
        pass

    def search(self, searchWord: str) -> bool:
        pass
