from typing import List


def two_sum(nums, target) -> List[int]:
    num_dict = {}
    for i, num in enumerate(nums):
        if target - num in num_dict:
            return [num_dict[target - num], i]
        num_dict[num] = i
    return []


def max_profit(prices: List[int]) -> int:
    maximum_profit, min_so_far = 0, prices[0]
    for i, price in enumerate(prices):
        maximum_profit, min_so_far = max(maximum_profit, price - min_so_far), min(min_so_far, price)
    return maximum_profit


def contains_duplicates(nums: List[int]) -> bool:
    num_set = set(nums)
    return len(num_set) != len(nums)


def product_except_self(nums: List[int]) -> List[int]:
    result = [1 for _ in nums]
    result_forward = [num for num in nums]
    result_backwards = [num for num in nums]
    for i in range(1, len(nums)):
        result_forward[i] *= result_backwards[i - 1]
    for i in range(len(nums) - 2, -1, -1):
        result_backwards[i] *= result_backwards[i + 1]

    for i in range(len(nums)):
        if i == 0:
            result[i] = result_backwards[i + 1]
        elif i == len(nums) - 1:
            result[i] = result_forward[i - 1]
        else:
            result[i] = result_backwards[i + 1] * result_forward[i - 1]

    return result


def max_sub_array(nums: List[int]) -> int:
    if not nums:
        return 0
    max_num = nums[0]
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i - 1] + nums[i])
        max_num = max(max_num, nums[i])
    return max_num


def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    def two_sum(target, numbers):
        num_set = set()
        result = []
        for i, num in enumerate(numbers):
            if not result or num != result[-1][-1]:
                if target - num in num_set:
                    result.append([-target, num, num - target])
            num_set.add(num)
        return result

    for i, num in enumerate(nums):
        if not i or nums[i - 1] != num:
            result.extend(two_sum(-num, nums[i + 1:]))
    return result


def maxArea(height: List[int]) -> int:
    left_pointer, right_pointer = 0, len(height) - 1
    max_area = 0
    while left_pointer < right_pointer:
        left_height, right_height = height[left_pointer], height[right_pointer]
        max_area = max(max_area, min(left_height, right_height) * abs(left_pointer - right_pointer))
        if left_height < right_height:
            left_pointer += 1
        else:
            right_pointer -= 1
    return max_area


def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    letter_set = set()
    pointer_head = 0
    for i, character in enumerate(s):
        while character in letter_set:
            letter_set.remove(s[pointer_head])
            pointer_head += 1
        max_len = max(max_len, i - pointer_head + 1)
        letter_set.add(character)
    return max_len
