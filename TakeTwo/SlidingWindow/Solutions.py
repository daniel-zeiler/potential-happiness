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


def min_window(s: str, t: str) -> str:
    pass
