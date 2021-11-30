import unittest
import Trie

word_one = 'cat'
word_two = 'cathar'
word_three = 'dog'
word_four = 'c'
word_five = 'cinema'
word_list = ['cat', 'cathar', 'dog', 'c', 'cinema']
search_list = ['dog', 'cin', 'cinema', 'c', 'cathary']
search_list_result = [True, False, True, True, False]
trie = Trie.Trie()
for word in word_list:
    trie.insert(word)


class TestTrieNode(unittest.TestCase):

    def test_insert(self):
        self.assertCountEqual(trie.print(), word_list)

    def test_search(self):
        self.assertCountEqual([trie.search(word) for word in search_list], search_list_result)
