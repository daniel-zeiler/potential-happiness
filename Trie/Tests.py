import unittest
import Trie.Solutions as trie


class SolutionsTest(unittest.TestCase):
    def test_trie(self):
        a_trie = trie.Trie()
        a_trie.insert("apple")
        self.assertEqual(True, a_trie.search("apple"))
        self.assertEqual(False, a_trie.search("app"))
        self.assertEqual(True, a_trie.starts_with("app"))
        a_trie.insert("app")
        self.assertEqual(True, a_trie.search("app"))

    def test_word_dictionary(self):
        word_dictionary = trie.WordDictionary()
        word_dictionary.addWord("bad")
        word_dictionary.addWord("dad")
        word_dictionary.addWord("mad")
        self.assertEqual(False, word_dictionary.search("pad"))
        self.assertEqual(True, word_dictionary.search("bad"))
        self.assertEqual(True, word_dictionary.search(".ad"))
        self.assertEqual(True, word_dictionary.search("b.."))

    def test_replace_words(self):
        dictionary = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        output = "the cat was rat by the bat"
        self.assertEqual(output, trie.replaceWords(dictionary, sentence))
        dictionary = ["a", "b", "c"]
        sentence = "aadsfasf absbs bbab cadsfafs"
        output = "a a b c"
        self.assertEqual(output, trie.replaceWords(dictionary, sentence))
