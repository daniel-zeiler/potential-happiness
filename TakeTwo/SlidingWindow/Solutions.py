import collections


def length_of_longest_substring(s: str) -> int:
    pointer_a, pointer_b, longest, letter_dict = 0, 0, 0, collections.defaultdict(int)
    while pointer_b < len(s):
        while letter_dict[s[pointer_b]] == 1:
            letter_dict[s[pointer_a]] -= 1
            pointer_a += 1
        letter_dict[s[pointer_b]] += 1
        longest = max(longest, pointer_b - pointer_a + 1)
        pointer_b += 1
    return longest


from collections import defaultdict


def min_window(s: str, t: str) -> str:
    t_counter, s_counter = defaultdict(int), defaultdict(int)
    for character in t:
        t_counter[character] += 1

    pointer_a, pointer_b, formed, number_to_form, min_length, result = 0, 0, 0, len(t_counter), float('inf'), ""

    while pointer_b < len(s):
        b_character = s[pointer_b]
        if b_character in t_counter:
            s_counter[b_character] += 1
            if s_counter[b_character] == t_counter[b_character]:
                formed += 1

            while pointer_a <= pointer_b and formed == number_to_form:
                if pointer_b - pointer_a + 1 < min_length:
                    min_length = pointer_b - pointer_a + 1
                    result = s[pointer_a:pointer_b + 1]

                a_character = s[pointer_a]
                s_counter[a_character] -= 1
                if a_character in t_counter and s_counter[a_character] < t_counter[a_character]:
                    formed -= 1
                pointer_a += 1

        pointer_b += 1

    return result


from typing import List


def longest_ones(nums: List[int], k: int) -> int:
    pointer_a, pointer_b, flipped, longest_length = 0, 0, 0, 0

    while pointer_b < len(nums):
        pointer_b_value = nums[pointer_b]

        while pointer_b_value == 0 and flipped == k:
            pointer_a_value = nums[pointer_a]
            if pointer_a_value == 0:
                flipped -= 1
            pointer_a += 1

        if pointer_b_value == 0:
            flipped += 1

        pointer_b += 1
        longest_length = max(longest_length, pointer_b - pointer_a)

    return longest_length


def max_satisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    result = 0
    for num_customers, grump_status in zip(customers, grumpy):
        if not grump_status:
            result += num_customers

    window, pointer_a, pointer_b = 0, 0, 0
    for _ in range(minutes):
        if grumpy[pointer_b]:
            window += customers[pointer_b]
        pointer_b += 1

    max_in_window = window
    while pointer_b < len(grumpy):
        if grumpy[pointer_a]:
            window -= customers[pointer_a]
        if grumpy[pointer_b]:
            window += customers[pointer_b]
        max_in_window = max(max_in_window, window)
        pointer_a += 1
        pointer_b += 1

    return max_in_window + result


def maxVowels(s: str, k: int) -> int:
    vowels_in_window, pointer_a, pointer_b = 0, 0, 0
    vowels = {"a", "e", "i", "o", "u"}
    for _ in range(k):
        if s[pointer_b] in vowels:
            vowels_in_window += 1
        pointer_b += 1
    max_vowels_in_window = vowels_in_window

    while pointer_b < len(s):
        if s[pointer_a] in vowels:
            vowels_in_window -= 1
        if s[pointer_b] in vowels:
            vowels_in_window += 1
        max_vowels_in_window = max(max_vowels_in_window, vowels_in_window)
        pointer_a += 1
        pointer_b += 1
    return max_vowels_in_window


def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    distinct_letter_dict = defaultdict(int)
    pointer_a, pointer_b, max_length = 0, 0, 0
    while pointer_b < len(s):
        distinct_letter_dict[pointer_b] += 1
        max_length = max(max_length, pointer_b - pointer_a + 1)
        pointer_b += 1
        while len(distinct_letter_dict) > k and pointer_a < pointer_b:
            distinct_letter_dict[s[pointer_a]] -= 1
            if not distinct_letter_dict[s[pointer_a]]:
                del distinct_letter_dict[s[pointer_a]]
            pointer_a += 1
    return max_length


def totalFruit(fruits: List[int]) -> int:
    pointer_a, pointer_b, baskets = 0, 0, defaultdict(int)
    max_fruit = 0
    while pointer_b < len(fruits):
        fruit = fruits[pointer_b]
        while fruit not in baskets and len(baskets) == 2:
            baskets[fruits[pointer_a]] -= 1
            if baskets[fruits[pointer_a]] == 0:
                del baskets[fruits[pointer_a]]
            pointer_a += 1

        baskets[fruit] += 1
        pointer_b += 1
        max_fruit = max(max_fruit, pointer_b - pointer_a)
    return max_fruit
