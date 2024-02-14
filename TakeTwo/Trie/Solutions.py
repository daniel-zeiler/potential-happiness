from typing import List
import collections


class TrieNode:
    def __init__(self, word: str = None):
        self.word = word
        self.children = collections.defaultdict(TrieNode)


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


class ReplaceWordsTrie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str):
        def insert_helper(node, word_remaining):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    node.children[word_remaining[0]] = TrieNode()
                insert_helper(node.children[word_remaining[0]], word_remaining[1:])

        insert_helper(self.head, word)

    def find_first(self, word: str) -> str:
        def find_first_helper(node: TrieNode, word_remaining: str) -> str:
            if node.word:
                return node.word
            if not word_remaining or word_remaining[0] not in node.children:
                return word
            return find_first_helper(node.children[word_remaining[0]], word_remaining[1:])

        return find_first_helper(self.head, word)


def replaceWords(dictionary: List[str], sentence: str) -> str:
    replace_words_trie = ReplaceWordsTrie()
    for word in dictionary:
        replace_words_trie.insert(word)
    result = []
    for word in sentence.split(" "):
        result.append(replace_words_trie.find_first(word))
    return " ".join(result)


class MagicWordNode:
    def __init__(self):
        self.children = collections.defaultdict(MagicWordNode)
        self.word = None


class MagicDictionary:

    def __init__(self):
        self.head = MagicWordNode()

    def buildDict(self, dictionary: List[str]) -> None:
        def build_dict_helper(node, word_remaining, word):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    node.children[word_remaining[0]] = TrieNode()
                build_dict_helper(node.children[word_remaining[0]], word_remaining[1:], word)

        for word in dictionary:
            build_dict_helper(self.head, word, word)

    def search(self, searchWord: str) -> bool:
        def search_word_helper(node, word_remaining, flipped):
            if not word_remaining:
                return node.word is not None and flipped
            else:
                if word_remaining[0] not in node.children:
                    if flipped:
                        return False
                    for child in node.children.values():
                        if search_word_helper(child, word_remaining[1:], True):
                            return True
                    return False
                else:
                    return search_word_helper(node.children[word_remaining[0]], word_remaining[1:], flipped)

        return search_word_helper(self.head, searchWord, False)


class MapSumNode:
    def __init__(self, key=None, val=0):
        self.key = key
        self.children = collections.defaultdict(MapSumNode)
        self.val = val


class MapSum:

    def __init__(self):
        self.head = MapSumNode()

    def insert(self, key: str, val: int) -> None:
        def insert_helper(node, word_remaining):
            if not word_remaining:
                node.key, node.val = key, val
            else:
                if word_remaining[0] not in node.children:
                    node.children[word_remaining[0]] = MapSumNode()
                insert_helper(node.children[word_remaining[0]], word_remaining[1:])

        insert_helper(self.head, key)

    def sum(self, prefix: str) -> int:
        def traverse(node, prefix_remaining) -> int:
            if not prefix_remaining:
                return gather(node)
            if prefix_remaining[0] not in node.children:
                return 0
            return traverse(node.children[prefix_remaining[0]], prefix_remaining[1:])

        def gather(node) -> int:
            return sum(gather(child) for child in node.children.values()) + node.val

        return traverse(self.head, prefix)


class LongestWordNode:
    def __init__(self, word=None):
        self.children = collections.defaultdict(LongestWordNode)


class LongestWordTrie:
    def __init__(self):
        self.head = LongestWordNode()

    def insert_word(self, word) -> bool:
        def insert_helper(node, word_remaining):
            if not word_remaining:
                return True
            if word_remaining[0] not in node.children:
                if len(word_remaining) > 1:
                    return False
                node.children[word_remaining[0]] = LongestWordNode()
            return insert_helper(node.children[word_remaining[0]], word_remaining[1:])

        return insert_helper(self.head, word)


def longestWord(words: List[str]) -> str:
    words.sort(key=lambda x: len(x))
    longest_word_trie = LongestWordTrie()
    result = [word for word in words if longest_word_trie.insert_word(word)]
    return result[-1]


class CamelMatchNode:
    def __init__(self, terms=None):
        self.terms = terms
        self.children = collections.defaultdict(CamelMatchNode)


class CamelMatchTrie:
    def __init__(self):
        self.head = CamelMatchNode()

    def add_terms(self, terms):
        def add_terms_helper(node, terms_remaining):
            if not terms_remaining:
                node.terms = terms
                return
            if terms_remaining[0] not in node.children:
                node.children[terms_remaining[0]] = CamelMatchNode()
            add_terms_helper(node.children[terms_remaining[0]], terms_remaining[1:])

        add_terms_helper(self.head, terms)

    def match_terms(self, terms) -> bool:
        def match_terms_helper(node, terms_remaining) -> bool:
            if not terms_remaining:
                return node.terms is not None
            for term in node.children.keys():
                if terms_remaining[0][:len(term)] == term:
                    return match_terms_helper(node.children[term], terms_remaining[1:])
            return False

        return match_terms_helper(self.head, terms)


import re


def split_by_uppercase(s):
    return re.findall('[A-Z][^A-Z]*', s)


def camelMatch(queries: List[str], pattern: str) -> List[bool]:
    camel_match_trie = CamelMatchTrie()
    camel_match_trie.add_terms(split_by_uppercase(pattern))
    return [camel_match_trie.match_terms(split_by_uppercase(query)) for query in queries]
