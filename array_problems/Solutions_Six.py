import collections
import heapq
import math
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged_intervals = []
    for interval in intervals:
        if not merged_intervals:
            merged_intervals.append(interval)
        elif interval[0] > merged_intervals[-1][1]:
            merged_intervals.append(interval)
        elif interval[1] > merged_intervals[-1][1]:
            merged_intervals[-1][1] = interval[1]
    return merged_intervals


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize
        self.current_size = 0

    def push(self, x: int) -> None:
        if self.current_size != self.max_size:
            self.stack.append(x)
            self.current_size += 1

    def pop(self) -> int:
        if self.current_size != 0:
            self.current_size -= 1
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for x in range(1, min(self.current_size, k)):
            self.stack[x] += val


def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    result = 0
    for x in range(0, len(nums), 2):
        result += min(nums[x], nums[x + 1])
    return result


def sortArrayByParity(nums: List[int]) -> List[int]:
    pointer_a = 0
    for pointer_b, num in enumerate(nums):
        if num % 2 == 0:
            nums[pointer_a], nums[pointer_b] = nums[pointer_b], nums[pointer_a]
            pointer_a += 1
    return nums


def replaceElements(arr: List[int]) -> List[int]:
    max_element_right = float('-inf')
    for i in range(len(arr) - 1, -1, -1):
        if i != len(arr) - 1:
            max_element_right, arr[i] = max(max_element_right, arr[i]), max_element_right
        else:
            max_element_right, arr[i] = arr[i], -1
    return arr


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    first_list_pointer = 0
    second_list_pointer = 0
    result_list = []
    while first_list_pointer < len(firstList) and second_list_pointer < len(secondList):
        first_element = firstList[first_list_pointer]
        second_element = secondList[second_list_pointer]
        if second_element[0] <= first_element[0] <= second_element[1]:
            result_list.append([first_element[0], min(first_element[1], second_element[1])])
        elif first_element[0] <= second_element[0] <= first_element[1]:
            result_list.append([second_element[0], min(second_element[1], first_element[1])])

        if first_element[0] < second_element[0]:
            first_list_pointer += 1
        else:
            second_list_pointer += 1
    return result_list


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    def permute_helper(nums_remaining, temp):
        if not nums_remaining:
            result.append(temp)
        else:
            for i, num in enumerate(nums_remaining):
                permute_helper(nums_remaining[:i] + nums_remaining[i + 1:], temp + [num])

    permute_helper(nums, [])
    return result


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def subsets_helper(nums_remaining, temp):
        result.append(temp)
        for i, num in enumerate(nums_remaining):
            subsets_helper(nums_remaining[i + 1:], temp + [num])

    subsets_helper(nums, [])
    return result


def calPoints(ops: List[str]) -> int:
    record = []
    sum = 0
    for operation in ops:
        if operation == "+":
            record.append(record[-1] + record[-2])
            sum += record[-1]
        elif operation == "D":
            record.append(record[-1] * 2)
            sum += record[-1]
        elif operation == "C":
            sum -= record.pop()
        else:
            record.append(int(operation))
            sum += record[-1]
    return sum


def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    sort_map = {}
    max_value = float('-inf')
    for i, value in enumerate(arr2):
        sort_map[value] = i
        max_value = max(max_value, value)
    arr1.sort(key=lambda x: sort_map[x] if x in sort_map else max_value + 1)
    return arr1


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1).intersection(set(nums2)))


def minFallingPathSum(matrix: List[List[int]]) -> int:
    result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if x == 0:
                result[x][y] = value
            elif y == 0:
                result[x][y] = min(result[x - 1][y], result[x - 1][y + 1]) + value
            elif y == len(row) - 1:
                result[x][y] = min(result[x - 1][y - 1], result[x - 1][y]) + value
            else:
                result[x][y] = min(result[x - 1][y - 1], result[x - 1][y], result[x - 1][y + 1]) + value
    return min(result[-1])


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    points.sort(key=lambda x: math.sqrt(math.pow(x[0], 2) + math.pow(x[1], 2)))
    return points[:k]


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    stack = []
    pushed_pointer = 0
    popped_pointer = 0
    while pushed_pointer != len(pushed):
        if not stack or stack[-1] != popped[popped_pointer]:
            stack.append(pushed[pushed_pointer])
            pushed_pointer += 1
        else:
            stack.pop()
            popped_pointer += 1

    while stack and popped_pointer < len(popped) and stack[-1] == popped[popped_pointer]:
        stack.pop()
        popped_pointer += 1

    return pushed_pointer == len(pushed) and popped_pointer == len(popped)


def lastStoneWeight(stones: List[int]) -> int:
    stones = [-stone for stone in stones]
    heapq.heapify(stones)
    while len(stones) != 1:
        stone_a = heapq.heappop(stones)
        stone_b = heapq.heappop(stones)
        if stone_a != stone_b:
            heapq.heappush(stones, -abs(-stone_a - -stone_b))
    return -stones[0]


def canReach(arr: List[int], start: int) -> bool:
    queue = collections.deque([start])
    visited = {start}
    while queue:
        index = queue.popleft()
        if arr[index] == 0:
            return True
        neg_index = index - arr[index]
        pos_index = index + arr[index]
        if neg_index >= 0 and neg_index not in visited:
            visited.add(neg_index)
            queue.append(neg_index)
        if pos_index < len(arr) and pos_index not in visited:
            visited.add(pos_index)
            queue.append(pos_index)
    return False


def minCostClimbingStairs(cost: List[int]) -> int:
    pass
