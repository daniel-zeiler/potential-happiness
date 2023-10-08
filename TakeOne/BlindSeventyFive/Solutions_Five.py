from typing import List


def twoSum(nums, target):
    compliment_set = {}
    for i, num in enumerate(nums):
        if target - num not in compliment_set:
            compliment_set[num] = i
        else:
            return [compliment_set[target - num], i]


def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    max_list = [price for price in prices]
    for i in range(len(prices) - 1, -1, -1):
        if i != len(max_list) - 1:
            max_profit = max(max_profit, max_list[i + 1] - prices[i])
            max_list[i] = max(max_list[i + 1], max_list[i])
    return max_profit


def containsDuplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)


def productExceptSelf(nums: List[int]) -> List[int]:
    forward = [num for num in nums]
    backward = [num for num in nums]
    for i in range(len(nums)):
        if i > 0:
            forward[i] *= forward[i - 1]
    for i in reversed(range(len(nums))):
        if i < len(nums) - 1:
            backward[i] *= backward[i + 1]
    result = [1 for _ in range(len(nums))]
    for i in range(len(result)):
        if i == 0:
            result[i] = backward[i + 1]
        elif i == len(result) - 1:
            result[i] = forward[i - 1]
        else:
            result[i] = backward[i + 1] * forward[i - 1]
    return result


def maxSubArray(nums: List[int]) -> int:
    max_subarray = 0
    curr_values = [0 for _ in range(len(nums))]
    for i, number in enumerate(nums):
        if i == 0:
            curr_values[i] = number
        else:
            curr_values[i] = max(number, number + curr_values[i - 1])
        max_subarray = max(max_subarray, curr_values[i])
    return max_subarray


def maxProduct(nums: List[int]) -> int:
    max_product = 0
    temp_values = [0 for _ in range(len(nums))]
    min_values = [0 for _ in range(len(nums))]
    for i, number in enumerate(nums):
        if i == 0:
            temp_values[i] = number
            min_values[i] = number
        else:
            min_values[i] = min(number, min_values[i - 1] * number)
            temp_values[i] = max(number, min_values[i - 1] * number, temp_values[i - 1] * number)
        max_product = max(max_product, temp_values[i])
    return max_product


def threeSum(nums: List[int]) -> List[List[int]]:
    def test_sum(nums_remaining, num_left, nums_so_far):
        result = []
        if len(nums_so_far) == 3 and num_left == 0:
            result.append(nums_so_far)
        if len(nums_so_far) < 3:
            for i, number in enumerate(nums_remaining):
                if i == 0 or number != nums_remaining[i - 1]:
                    result.extend(test_sum(nums_remaining[i + 1:], num_left + number, nums_so_far + [number]))
        return result

    result = []
    nums.sort()
    for i, number in enumerate(nums):
        if i == 0 or number != nums[i - 1]:
            result.extend(test_sum(nums[i + 1:], number, [number]))
    return result


def lengthOfLongestSubstring(s: str) -> int:
    longest_substring = 0
    pointer_a = 0
    character_set = set()
    for pointer_b, character in enumerate(s):
        while character in character_set:
            character_set.remove(s[pointer_a])
            pointer_a += 1
        character_set.add(character)
        longest_substring = max(longest_substring, pointer_b - pointer_a + 1)
    return longest_substring


def setZeroes(matrix: List[List[int]]) -> None:
    x_list = set()
    y_list = set()
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if value == 0:
                x_list.add(x)
                y_list.add(y)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if x in x_list or y in y_list:
                matrix[x][y] = 0


def exist(board: List[List[str]], word: str) -> bool:
    pass