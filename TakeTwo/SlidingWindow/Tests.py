import unittest
import TakeTwo.SlidingWindow.Solutions as sliding_window


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

    def test_min_window(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        output = "BANC"
        self.assertEqual(sliding_window.min_window(s, t), output)
        s = "a"
        t = "a"
        output = "a"
        self.assertEqual(sliding_window.min_window(s, t), output)
        s = "a"
        t = "aa"
        output = ""
        self.assertEqual(sliding_window.min_window(s, t), output)

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

    def test_max_vowels(self):
        s = "abciiidef"
        k = 3
        output = 3
        self.assertEqual(output, sliding_window.maxVowels(s, k))
        s = "aeiou"
        k = 2
        output = 2
        self.assertEqual(output, sliding_window.maxVowels(s, k))
        s = "leetcode"
        k = 3
        output = 2
        self.assertEqual(output, sliding_window.maxVowels(s, k))
        s = "rhythms"
        k = 4
        output = 0
        self.assertEqual(output, sliding_window.maxVowels(s, k))

    def test_longest_substring_k_distrinct(self):
        s = "eceba"
        k = 2
        output = 3
        self.assertEqual(output, sliding_window.lengthOfLongestSubstringKDistinct(s, k))
        s = "aa"
        k = 1
        output = 2
        self.assertEqual(output, sliding_window.lengthOfLongestSubstringKDistinct(s, k))

    def test_length_longest_distinct(self):
        s = "eceba"
        k = 2
        output = 3
        self.assertEqual(output, sliding_window_two.lengthOfLongestSubstringKDistinct(s, k))
        s = "aa"
        k = 1
        output = 2
        self.assertEqual(output, sliding_window_two.lengthOfLongestSubstringKDistinct(s, k))

    def test_most_fruit(self):
        fruits = [1, 2, 1]
        output = 3
        self.assertEqual(output, sliding_window.totalFruit(fruits))
        fruits = [0, 1, 2, 2]
        output = 3
        self.assertEqual(output, sliding_window.totalFruit(fruits))
        fruits = [1, 2, 3, 2, 2]
        output = 4
        self.assertEqual(output, sliding_window.totalFruit(fruits))


if __name__ == '__main__':
    unittest.main()
