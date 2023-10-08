import collections
from typing import List


def length_of_longest_substring(s: str) -> int:
    pointer_a = 0
    letter_set = set()
    length = 0
    for pointer_b, letter in enumerate(s):
        while letter in letter_set:
            letter_set.remove(s[pointer_a])
            pointer_a += 1
        letter_set.add(letter)
        length = max(length, len(letter_set))
    return length


def min_window(s: str, t: str) -> str:
    t_count = collections.defaultdict(int)
    for character in t:
        t_count[character] += 1
    pointer_a = 0
    s_count = collections.defaultdict(int)
    min_window = ""
    for pointer_b, character in enumerate(s):
        if character in t_count:
            s_count[character] += 1
            while len(s_count) == len(t_count) and s_count[character] == t_count[character]:
                if len(min_window) > pointer_b - pointer_a or min_window == "":
                    min_window = s[pointer_a:pointer_b + 1]
                if s[pointer_a] in s_count:
                    s_count[s[pointer_a]] -= 1
                    if s_count[s[pointer_a]] == 0:
                        del s_count[s[pointer_a]]
                pointer_a += 1

    return min_window


def longest_ones(nums: List[int], k: int) -> int:
    flipped_ones = 0
    longest = 0
    pointer_a = 0
    for pointer_b, number in enumerate(nums):
        if number == 0:
            while flipped_ones == k:
                if nums[pointer_a] == 0:
                    flipped_ones -= 1
                pointer_a += 1
            flipped_ones += 1
        longest = max(pointer_b - pointer_a + 1, longest)
    return longest


def max_satisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    number_non_grumpy = 0
    max_number_grumpy_window = 0
    current_number_grumpy_window = 0
    for i, (customer, grump) in enumerate(zip(customers, grumpy)):
        if not grump:
            number_non_grumpy += customer

    for i, (customer, grump) in enumerate(zip(customers, grumpy)):
        if i < minutes - 1:
            if grump:
                current_number_grumpy_window += customer
            max_number_grumpy_window = max(max_number_grumpy_window, current_number_grumpy_window)
        else:
            if grump:
                current_number_grumpy_window += customer
            max_number_grumpy_window = max(max_number_grumpy_window, current_number_grumpy_window)
            if grumpy[i - minutes + 1]:
                current_number_grumpy_window -= customers[i - minutes + 1]

    return max_number_grumpy_window + number_non_grumpy


def maxVowels(s: str, k: int) -> int:
    pass
