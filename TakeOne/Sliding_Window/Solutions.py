from typing import List


def length_of_longest_substring(s: str) -> int:
    character_set = set()
    pointer_a = 0
    pointer_b = 0
    length_of_longest = 0
    while pointer_b < len(s):
        while s[pointer_b] in character_set:
            character_set.remove(s[pointer_a])
            pointer_a += 1
        character_set.add(s[pointer_b])
        pointer_b += 1
        length_of_longest = max(length_of_longest, len(character_set))

    return length_of_longest


def longest_ones(nums: List[int], k: int) -> int:
    start_pointer = 0
    end_pointer = 0
    zeros_flipped = 0
    longest = float('-inf')
    while end_pointer < len(nums):
        if nums[end_pointer] == 0:
            zeros_flipped += 1
        while zeros_flipped > k:
            if nums[start_pointer] == 0:
                zeros_flipped -= 1
            start_pointer += 1
        longest = max(longest, end_pointer - start_pointer + 1)
        end_pointer += 1
    return longest


def max_satisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    pass
