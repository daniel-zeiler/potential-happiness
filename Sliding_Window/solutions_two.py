import collections
from typing import List


def length_of_longest_substring(s: str) -> int:
    start_pointer = 0
    character_set = set()
    result = 0
    for i, character in enumerate(s):
        while character in character_set:
            del character[s[start_pointer]]
            start_pointer += 1
        character_set.add(character)
        result = max(i - start_pointer + 1, result)
    return result


def compare_counts(character_count_s, character_count_t):
    for key, value in character_count_t.items():
        if key not in character_count_s or value > character_count_s[key]:
            return False
    return True


def min_window(s: str, t: str) -> str:
    character_count_t = collections.defaultdict(int)
    character_count_s = collections.defaultdict(int)

    for char in t:
        character_count_t[char] += 1

    pointer_start = 0
    min_length = float('inf')
    result = ''

    for i, value in enumerate(s):
        if value in t:
            character_count_s[value] += 1

        while compare_counts(character_count_s, character_count_t):
            if i - pointer_start + 1 < min_length:
                min_length = i - pointer_start + 1
                result = s[pointer_start:i + 1]
            if s[pointer_start] in t:
                character_count_s[s[pointer_start]] -= 1
            pointer_start += 1

    return result


def longest_ones(nums: List[int], k: int) -> int:
    ones_flipped = 0
    pointer_start = 0
    result = 0
    for i, num in enumerate(nums):
        if num == 0:
            ones_flipped += 1

        while ones_flipped > k:
            if nums[pointer_start] == 0:
                ones_flipped -= 1
            pointer_start += 1

        result = max(result, i - pointer_start + 1)

    return result


def max_satisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    result = 0
    pointer_end = 0
    pointer_start = 0
    grumpy_in_window = 0

    for _ in range(minutes):
        if grumpy[pointer_end]:
            grumpy_in_window += customers[pointer_end]
        else:
            result += customers[pointer_end]
        pointer_end += 1

    max_grumpy_in_window = grumpy_in_window

    while pointer_end < len(grumpy):
        if grumpy[pointer_end]:
            grumpy_in_window += customers[pointer_end]
        else:
            result += customers[pointer_end]
        if grumpy[pointer_start]:
            grumpy_in_window -= customers[pointer_start]
        pointer_end += 1
        pointer_start += 1
        max_grumpy_in_window = max(max_grumpy_in_window, grumpy_in_window)

    return result + max_grumpy_in_window


def maxVowels(s: str, k: int) -> int:
    vowels = {"a", "e", "i", "o", "u"}

    pointer_end = 0
    pointer_start = 0
    vowels_in_window = 0

    for _ in range(k):
        if s[pointer_end] in vowels:
            vowels_in_window += 1
        pointer_end += 1

    max_vowels = vowels_in_window

    while pointer_end < len(s):
        if s[pointer_end] in vowels:
            vowels_in_window += 1
        if s[pointer_start] in vowels:
            vowels_in_window -= 1
        max_vowels = max(max_vowels, vowels_in_window)
        pointer_end += 1
        pointer_start += 1

    return max_vowels


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    distinct_character_set = collections.defaultdict(int)
    longest_length = 0
    pointer_a = 0

    for index, character in enumerate(s):
        distinct_character_set[character] += 1

        while len(distinct_character_set) > k:
            distinct_character_set[s[pointer_a]] -= 1
            if distinct_character_set[s[pointer_a]] == 0:
                del distinct_character_set[s[pointer_a]]
            pointer_a += 1

        longest_length = max(longest_length, index - pointer_a + 1)

    return longest_length
