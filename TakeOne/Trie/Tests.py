import unittest
import TakeOne.Trie.Solutions as trie
import TakeOne.Trie.Solutions_Two as trie_two


class SolutionsTest(unittest.TestCase):
    def test_trie(self):
        a_trie = trie_two.Trie()
        a_trie.insert("apple")
        self.assertEqual(True, a_trie.search("apple"))
        self.assertEqual(False, a_trie.search("app"))
        self.assertEqual(True, a_trie.starts_with("app"))
        a_trie.insert("app")
        self.assertEqual(True, a_trie.search("app"))

    def test_word_dictionary(self):
        word_dictionary = trie_two.WordDictionary()
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

    def test_magic_dictionary(self):
        magic_dictionary = trie.MagicDictionary()
        magic_dictionary.buildDict(["hello", "leetcode"])
        self.assertEqual(False, magic_dictionary.search("hello"))
        self.assertEqual(True, magic_dictionary.search("hhllo"))
        self.assertEqual(False, magic_dictionary.search("hell"))
        self.assertEqual(False, magic_dictionary.search("leetcoded"))

    def test_map_sum(self):
        map_sum = trie.MapSum()
        map_sum.insert("apple", 3)
        self.assertEqual(3, map_sum.sum("ap"))
        map_sum.insert("app", 2)
        self.assertEqual(5, map_sum.sum("ap"))

    def test_find_words(self):
        board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
        words = [
            "oath", "pea",
            "eat", "rain"]
        output = ["eat", "oath"]
        self.assertCountEqual(output, trie.findWords(board, words))


if __name__ == '__main__':
    unittest.main()
