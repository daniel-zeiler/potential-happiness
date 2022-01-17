import unittest
from typing import List

import Hard.Trie.Solution as trie_problem


class SolutionsTest(unittest.TestCase):

    def test_find_words(self):
        board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
        words = ["oath", "pea", "eat", "rain"]
        output = ["eat", "oath"]
        self.assertCountEqual(output, trie_problem.findWords(board, words))

        board = [["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]]
        words = ["oa", "oaa"]
        output = ["oa", "oaa"]
        self.assertCountEqual(output, trie_problem.findWords(board, words))

        board = [["a", "a"]]
        words = ["aaa"]
        output = []
        self.assertCountEqual(output, trie_problem.findWords(board, words))


if __name__ == '__main__':
    unittest.main()
