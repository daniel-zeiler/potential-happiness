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

    # def test_min_window(self):
    #     s = "ADOBECODEBANC"
    #     t = "ABC"
    #     output = "BANC"
    #     self.assertEqual(sliding_window.min_window(s, t), output)
    #     s = "a"
    #     t = "a"
    #     output = "a"
    #     self.assertEqual(sliding_window.min_window(s, t), output)
    #     s = "a"
    #     t = "aa"
    #     output = ""
    #     self.assertEqual(sliding_window.min_window(s, t), output)

    def test_longest_ones(self):
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2
        output = 6
        self.assertEqual(sliding_window.longest_ones(nums, k), output)
        nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        k = 3
        output = 10
        self.assertEqual(sliding_window.longest_ones(nums, k), output)

    def test_max_satisfied(self):
        customers = [1, 0, 1, 2, 1, 1, 7, 5]
        grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
        minutes = 3
        output = 16
        self.assertEqual(sliding_window.max_satisfied(customers, grumpy, minutes), output)
        customers = [1]
        grumpy = [0]
        minutes = 1
        output = 1
        self.assertEqual(sliding_window.max_satisfied(customers, grumpy, minutes), output)


if __name__ == '__main__':
    unittest.main()
