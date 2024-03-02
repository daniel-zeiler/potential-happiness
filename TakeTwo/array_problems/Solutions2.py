from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    result = []
    for i, interval in enumerate(intervals):
        if not result or interval[0] > result[-1][1]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])

    return result


def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    result = 0
    for i in range(1, len(nums), 2):
        result += min(nums[i], nums[i - 1])
    return result


def sortArrayByParity(nums: List[int]) -> List[int]:
    return sorted(nums, key=lambda x: x % 2)


def replaceElements(arr: List[int]) -> List[int]:
    max_on_right = arr[len(arr) - 1]
    for i in range(len(arr) - 2, -1, -1):
        arr[i], max_on_right = max_on_right, max(arr[i], max_on_right)
    arr[-1] = -1
    return arr


def intervalIntersection(first_list: List[List[int]], second_list: List[List[int]]) -> List[List[int]]:
    result = []
    pointer_first, pointer_second = 0, 0
    while pointer_first < len(first_list) and pointer_second < len(second_list):
        first_interval = first_list[pointer_first]
        second_interval = second_list[pointer_second]
        if first_interval[1] >= second_interval[0] and second_interval[1] >= first_interval[0]:
            result.append([max(first_interval[0], second_interval[0]), min(first_interval[1], second_interval[1])])

        if first_interval[1] <= second_interval[1]:
            pointer_first += 1
        else:
            pointer_second += 1
    return result


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    def permute_helper(nums, temp_result):
        if not nums:
            result.append(temp_result)
        else:
            for i, number in enumerate(nums):
                permute_helper(nums[:i] + nums[i + 1:], temp_result + [number])

    permute_helper(nums, [])
    return result


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def subset_helper(nums, temp_result):
        result.append(temp_result)
        for i, number in enumerate(nums):
            subset_helper(nums[i + 1:], temp_result + [number])

    subset_helper(nums, [])
    return result


def cal_points(ops: List[str]) -> int:
    stack = []
    for i, operation in enumerate(ops):
        if operation == "C":
            stack.pop()
        elif operation == "D":
            stack.append(stack[-1] * 2)
        elif operation == "+":
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(operation))
    return sum(stack)
