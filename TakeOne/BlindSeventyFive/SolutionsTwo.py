import collections
from typing import List, Optional
from binarytree import Node


def twoSum(nums, target):
    num_set = {}
    for i, num in enumerate(nums):
        if target - num in num_set:
            return [num_set[target - num], i]
        num_set[num] = i
    return []


def maxProfit(prices: List[int]) -> int:
    result = 0
    min_so_far = prices[0]
    for price in prices:
        result = max(result, price - min_so_far)
        min_so_far = min(min_so_far, price)
    return result


def containsDuplicate(nums: List[int]) -> bool:
    nums.sort()
    for i, num in enumerate(nums):
        if i > 0:
            if num == nums[i - 1]:
                return True
    return False


def productExceptSelf(nums: List[int]) -> List[int]:
    forward = [1 for _ in range(len(nums))]
    backward = [1 for _ in range(len(nums))]
    for i, value in enumerate(nums):
        if i == 0:
            forward[i] = value
        else:
            forward[i] = forward[i - 1] * value

    for i, value in reversed(list(enumerate(nums))):
        if i == len(nums) - 1:
            backward[i] = value
        else:
            backward[i] = backward[i + 1] * value

    result = [0 for _ in range(len(nums))]

    for i in range(len(nums)):
        if i == 0:
            result[i] = backward[i + 1]
        elif i == len(nums) - 1:
            result[i] = forward[i - 1]
        else:
            result[i] = backward[i + 1] * forward[i - 1]
    return result


def maxSubArray(nums: List[int]) -> int:
    if not nums:
        return 0
    result = [num for num in nums]
    for i, number in enumerate(nums):
        if i > 0:
            result[i] = max(number, result[i - 1] + number)
    return max(result)


def maxProduct(nums: List[int]) -> int:
    min_array = [num for num in nums]
    max_array = [num for num in nums]
    for i, num in enumerate(nums):
        if i > 0:
            min_array[i] = min(min_array[i - 1] * num, max_array[i - 1] * num, num)
            max_array[i] = max(min_array[i - 1] * num, max_array[i - 1] * num, num)
    return max(max_array)


def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    def two_sum(nums, target):
        temp_set = set()
        for i, num in enumerate(nums):
            if result and result[-1][-1] == num:
                continue
            if target - num in temp_set:
                result.append([-target, target - num, num])
            temp_set.add(num)

    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            two_sum(nums[i + 1:], -nums[i])

    return result


def maxArea(height: List[int]) -> int:
    pointer_a = 0
    pointer_b = len(height) - 1
    max_area = 0
    while pointer_a < pointer_b:
        height_a = height[pointer_a]
        height_b = height[pointer_b]
        max_area = max(min(height_a, height_b) * (pointer_b - pointer_a), max_area)
        if height_a < height_b:
            pointer_a += 1
        else:
            pointer_b -= 1
    return max_area


def lengthOfLongestSubstring(s: str) -> int:
    window_set = set()
    start_pointer = 0
    longest_length = 0
    for end_pointer, letter in enumerate(s):
        while letter in window_set:
            window_set.remove(s[start_pointer])
            start_pointer += 1
        window_set.add(letter)
        longest_length = max(end_pointer - start_pointer + 1, longest_length)
    return longest_length


def characterReplacement(s, k):
    count_dict = collections.defaultdict(int)
    start_pointer = 0
    result = 0
    max_count = 0
    for i, character in enumerate(s):
        count_dict[character] += 1
        max_count = max(max_count, count_dict[character])
        if i - start_pointer + 1 - max_count > k:
            count_dict[s[start_pointer]] -= 1
            start_pointer += 1
        result = max(result, i - start_pointer + 1)
    return result


def minWindow(s: str, t: str) -> str:
    count_t = collections.defaultdict(int)
    count_s = collections.defaultdict(int)

    for char in t:
        count_t[char] += 1
    min_window = float('inf')
    window_index = []
    start_pointer = 0
    formed = 0
    required = len(count_t)
    for end_pointer, character in enumerate(s):
        if character in count_t:
            count_s[character] += 1
            if count_s[character] == count_t[character]:
                formed += 1
        while start_pointer <= end_pointer and formed == required:
            start_character = s[start_pointer]
            if end_pointer - start_pointer < min_window:
                min_window = end_pointer - start_pointer
                window_index = [start_pointer, end_pointer]
            if start_character in count_s:
                count_s[start_character] -= 1
                if count_s[start_character] < count_t[start_character]:
                    formed -= 1
            start_pointer += 1
    if window_index:
        return s[window_index[0]:window_index[1] + 1]
    return ''


def isAnagram(s: str, t: str) -> bool:
    count_s = collections.Counter(s)
    count_t = collections.Counter(t)
    return count_s == count_t


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = collections.defaultdict(list)
    for word in strs:
        key = [0 for _ in range(26)]
        for character in word:
            key[ord(character) - ord('a')] += 1
        groups[tuple(key)].append(word)
    return list(groups.values())


def isPalindrome(s: str) -> bool:
    pointer_start = 0
    pointer_end = len(s) - 1
    while pointer_start < pointer_end:
        start_char = s[pointer_start]
        end_char = s[pointer_end]
        if not start_char.isalpha():
            pointer_start += 1
            continue
        elif not end_char.isalpha():
            pointer_end -= 1
            continue
        elif start_char.lower() != end_char.lower():
            return False
        pointer_start += 1
        pointer_end -= 1
    return True


def isValid(s: str) -> bool:
    curl = 0
    square = 0
    paren = 0
    for char in s:
        if char == ')':
            paren -= 1
        elif char == ']':
            square -= 1
        elif char == '}':
            curl -= 1
        elif char == '(':
            paren += 1
        elif char == '[':
            square += 1
        elif char == '{':
            curl += 1
    if curl < 0 or square < 0 or paren < 0:
        return False
    return curl == 0 and square == 0 and paren == 0


def longestPalindrome(s: str) -> str:
    def check_longest(lower, upper):
        while s[lower] == s[upper] and lower >= 0 and upper <= len(s) - 1:
            lower -= 1
            upper += 1
        return s[lower + 1:upper]

    result = ''

    for index in range(1, len(s) - 1):
        if s[index] == s[index - 1]:
            temp_result = check_longest(index - 1, index)
            if len(temp_result) > len(result):
                result = temp_result
        if s[index] == s[index + 1]:
            temp_result = check_longest(index, index + 1)
            if len(temp_result) > len(result):
                result = temp_result
        if s[index - 1] == s[index + 1]:
            temp_result = check_longest(index - 1, index + 1)
            if len(temp_result) > len(result):
                result = temp_result

    return result


def countSubstrings(s: str) -> int:
    def count_sub(lower, upper):
        temp_result = 0
        while lower >= 0 and upper <= len(s) - 1 and s[lower] == s[upper]:
            temp_result += 1
            lower -= 1
            upper += 1
        return temp_result

    result = 0
    for index, character in enumerate(s):
        result += 1
        if index != len(s) - 1:
            if character == s[index + 1]:
                result += count_sub(index, index + 1)
            if index != 0:
                if s[index - 1] == s[index + 1]:
                    result += count_sub(index - 1, index + 1)
    return result


def setZeroes(matrix: List[List[int]]) -> None:
    x_zeros = set()
    y_zeros = set()
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if value == 0:
                x_zeros.add(x)
                y_zeros.add(y)

    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if x in x_zeros or y in y_zeros:
                matrix[x][y] = 0


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction_pointer = 0
    result = []
    position_queue = [[0, 0]]

    def get_next_position(x, y):
        nonlocal direction_pointer
        for _ in range(2):
            x_direction, y_direction = directions[direction_pointer]
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(matrix) and 0 <= y_target < len(matrix[0]):
                if matrix[x_target][y_target] is not None:
                    return [x_target, y_target]
            direction_pointer = (direction_pointer + 1) % len(directions)
        return None

    while position_queue:
        x, y = position_queue.pop()
        result.append(matrix[x][y])
        matrix[x][y] = None
        next_position = get_next_position(x, y)
        if next_position:
            position_queue.append(next_position)

    return result


def exist(board: List[List[str]], word: str) -> bool:
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def traverse(x, y, word_remaining):
        if not word_remaining:
            return True
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(board) and 0 <= y_target < len(board[0]):
                if board[x_target][y_target] == word_remaining[0]:
                    temp, board[x_target][y_target] = board[x_target][y_target], None
                    if traverse(x_target, y_target, word_remaining[1:]):
                        return True
                    board[x_target][y_target] = temp
        return False

    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == word[0]:
                board[x][y] = None
                if traverse(x, y, word[1:]):
                    return True
                board[x][y] = value

    return False


def maxDepth(root: Optional[Node]) -> int:
    def traverse(node):
        result = 0
        if node:
            result += 1
            result += max(traverse(node.left), traverse(node.right))
        return result

    return traverse(root)

