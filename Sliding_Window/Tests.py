import unittest
import Sliding_Window.Solutions as sliding_window


class SolutionsTest(unittest.TestCase):
    def test_length_of_longest_substring(self):
        s = "abcabcbb"
        output = 3
        self.assertEqual(sliding_window.length_of_longest_substring(s), output)
        s = "bbbbb"
        output = 1
        self.assertEqual(sliding_window.length_of_longest_substring(s), output)
        s = "pwwkew"
        output = 3
        self.assertEqual(sliding_window.length_of_longest_substring(s), output)
        s = ""
        output = 0
        self.assertEqual(sliding_window.length_of_longest_substring(s), output)
