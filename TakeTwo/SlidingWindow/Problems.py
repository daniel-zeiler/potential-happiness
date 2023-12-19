# 8 problems

import collections
from typing import List

"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
"""


def length_of_longest_substring(s: str) -> int:
    pass


"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that 
every character in t (including duplicates) is included in the window. If there is no such substring, return the 
empty string "". 

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""


def min_window(s: str, t: str) -> str:
    pass


"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can 
flip at most k 0's. 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""


def longest_ones(nums: List[int], k: int) -> int:
    pass


"""
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the 
store. You are given an integer array customers of length n where customers[i] is the number of the customer that 
enters the store at the start of the ith minute and all those customers leave after the end of that minute. 

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the 
bookstore owner is grumpy during the ith minute, and is 0 otherwise. 

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, 
but can only use it once. 

Return the maximum number of customers that can be satisfied throughout the day.

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
Example 2:

Input: customers = [1], grumpy = [0], minutes = 1
Output: 1
"""


def max_satisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    pass


"""
Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
Example 4:

Input: s = "rhythms", k = 4
Output: 0
Explanation: We can see that s doesn't have any vowel letters.
Example 5:

Input: s = "tryhard", k = 4
Output: 1
"""


def maxVowels(s: str, k: int) -> int:
    pass


"""Given a string s and an integer k, return the length of the longest substring of s that contains at most k 
distinct characters. 

 

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
"""


def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    pass


"""You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are 
represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces. 

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of 
fruit each basket can hold. Starting from any tree of your choice, you must pick exactly one fruit from every tree (
including the start tree) while moving to the right. The picked fruits must fit in one of your baskets. Once you 
reach a tree with fruit that cannot fit in your baskets, you must stop. Given the integer array fruits, return the 
maximum number of fruits you can pick. 

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2]
"""


def totalFruit(self, fruits: List[int]) -> int:
    pass
