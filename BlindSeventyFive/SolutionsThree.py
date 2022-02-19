from typing import List


def twoSum(nums, target):
    compliment_dict = {}
    for i, num in enumerate(nums):
        if target - num in compliment_dict:
            return [compliment_dict[target - num], i]
        compliment_dict[num] = i
    return []


def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    min_so_far = prices[0]
    for price in prices:
        min_so_far = min(price, min_so_far)
        max_profit = max(max_profit, price - min_so_far)
    return max_profit


def containsDuplicate(nums: List[int]) -> bool:
    nums.sort()
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            return True
    return False


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


"""
O(n) time complexity
O(1) space complexity
"""


def maxSubArray(nums: List[int]) -> int:
    temp_val = 0
    result = 0
    for i, num in enumerate(nums):
        if i == 0:
            temp_val = num
        else:
            temp_val = max(num, num + temp_val)
        result = max(result, temp_val)
    return result


"""
O(n) time complexity
O(1) space complexity
"""


def maxProduct(nums: List[int]) -> int:
    temp_min = 1
    temp_val = 1
    result = 0

    for i, num in enumerate(nums):
        if i == 0:
            temp_min, temp_val = num, num
        else:
            temp_val, temp_min = max(num * temp_min, num * temp_val, num), min(num * temp_min, num * temp_val, num)
        result = max(result, temp_val, temp_min)

    return result


def findMin(nums: List[int]) -> int:
    def binary_search(low, high):
        if nums[low] < nums[high]:
            return nums[low]
        mid = (low + high) // 2
        result = nums[mid]
        if nums[mid] >= nums[low]:
            result = min(result, binary_search(mid + 1, high))
        else:
            result = min(result, binary_search(low, mid - 1))
        return result

    return binary_search(0, len(nums) - 1)


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []

    def two_sum(nums, target):
        compliment_set = set()
        pointer = 0
        while pointer < len(nums):
            num = nums[pointer]
            if target - num in compliment_set:
                result.append([-target, target - num, num])
                while pointer < len(nums) and nums[pointer] == num:
                    pointer += 1
            else:
                pointer += 1
            compliment_set.add(num)

    for i, num in enumerate(nums):
        if i == 0 or num != nums[i - 1]:
            two_sum(nums[i + 1:], -num)
    return result


"""
O(n)
O(1)
"""


def lengthOfLongestSubstring(s: str) -> int:
    pointer_start = 0
    character_set = set()
    result = 0
    for pointer_end, character in enumerate(s):
        while character in character_set:
            character_set.remove(s[pointer_start])
            pointer_start += 1
        character_set.add(character)
        result = max(result, pointer_end - pointer_start + 1)
    return result


def characterReplacement(s: str, k: int) -> int:
    character_list = list(set(s))
    result = 0

    for target_character in character_list:
        current_replacements = 0
        start_pointer = 0
        for read_pointer, character in enumerate(s):
            while character != target_character and current_replacements == k:
                if s[start_pointer] != target_character:
                    current_replacements -= 1
                start_pointer += 1
            if character != target_character:
                current_replacements += 1
            result = max(result, read_pointer - start_pointer + 1)
    return result
