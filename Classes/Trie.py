import collections
import unittest
from typing import List


class TrieNode:
    def __init__(self, word=None):
        self.word = word
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def search(self, word: str) -> bool:
        def search_node(node, word_remaining):
            if not word_remaining:
                return word == node.word
            if word_remaining[0] in node.children:
                return search_node(node.children[word_remaining[0]], word_remaining[1:])
            else:
                return False

        return search_node(self.head, word)

    def gather(self, node):
        result = []
        if node.word:
            result.append(node.word)
        for child in node.children.values():
            result.extend(self.gather(child))
        return result

    def prefix_search(self, prefix: str) -> List[str]:

        def prefix_function(node, prefix_remaining):
            if not prefix_remaining:
                return self.gather(node)
            elif prefix_remaining[0] in node.children:
                return prefix_function(node.children[prefix_remaining[0]], prefix_remaining[1:])
            else:
                return []

        return prefix_function(self.head, prefix)

    def delete(self, word: str):
        def traverse(node, word_remaining):
            if not word_remaining:
                node.word = None
                return not node.children
            elif word_remaining[0] in node.children:
                delete = traverse(node.children[word_remaining[0]], word_remaining[1:])
                if delete:
                    del node.children[word_remaining[0]]
                return not node.children
            else:
                return False

        traverse(self.head, word)

    def add(self, word: str):

        def add_recursive(current_node, word_remaining):
            if word_remaining[0] not in current_node.children:
                node = TrieNode()
                current_node.children[word_remaining[0]] = node
            node = current_node.children[word_remaining[0]]
            if len(word_remaining) == 1:
                node.word = word
                return node
            return add_recursive(node, word_remaining[1:])

        add_recursive(self.head, word)

    def print_trie(self):
        print(self.gather(self.head))


class TestTrie(unittest.TestCase):
    def test_trie(self):
        words = ['asdfasdff', 'a', 'alot', 'cat', 'catdog', 'call', 'cats']
        trie = Trie()
        for word in words:
            trie.add(word)
        trie.print_trie()
        input = 'c'
        output = ['cat', 'catdog', 'call', 'cats']
        self.assertCountEqual(output, trie.prefix_search(input))
        self.assertEqual(False, trie.search('catdogs'))
        self.assertEqual(False, trie.search('catdo'))
        self.assertEqual(True, trie.search('catdog'))
        trie.delete('catdog')
        self.assertEqual(False, trie.search('catdog'))
        self.assertEqual(True, trie.search('cat'))
        trie.delete('cat')
        self.assertEqual(True, trie.search('cats'))
        self.assertEqual(False, trie.search('cat'))
