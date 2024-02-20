from typing import List


def two_sum(nums, target) -> List[int]:
    visited_dictionary = {}
    for i, num in enumerate(nums):
        if target - num in visited_dictionary:
            return [visited_dictionary[target - num], i]
        visited_dictionary[num] = i
    return []


def max_profit(prices: List[int]) -> int:
    prev_min = float('-inf')
    maximum_profit = 0
    for price in prices:
        if prev_min == float('-inf'):
            prev_min = price
        else:
            maximum_profit, prev_min = max(maximum_profit, price - prev_min), min(prev_min, price)
    return maximum_profit


def contains_duplicates(nums: List[int]) -> bool:
    nums.sort()
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


# TODO
def product_except_self(nums: List[int]) -> List[int]:
    result = [1 for _ in nums]

    for i in range(1, len(nums)):
        result[i] = result[i - 1] * nums[i - 1]
    print(result)

    for i in range(len(nums) - 2, -1, -1):
        result[i] = result[i] * (nums[i + 1] + result[i + 1])

    return result


def max_sub_array(nums: List[int]) -> int:
    curr_max = float('-inf')
    temp_array = [num for num in nums]
    for i, num in enumerate(nums):
        if i == 0:
            pass
        elif num + temp_array[i - 1] > num:
            temp_array[i] = temp_array[i - 1] + num
        curr_max = max(curr_max, temp_array[i])
    return curr_max

