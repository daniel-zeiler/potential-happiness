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


def relative_sort_array(arr1: List[int], arr2: List[int]) -> List[int]:
    index_map = {num: i for i, num in enumerate(arr2)}
    max_num = max([i for i in index_map.values()])

    def custom_sort(a: int) -> int:
        if a in index_map:
            a = index_map[a]
        else:
            a += max_num
        return a

    arr1.sort(key=custom_sort)
    return arr1


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1).intersection(set(nums2)))


def min_falling_path_sum(matrix: List[List[int]]) -> int:
    for x in range(1, len(matrix)):
        for y in range(len(matrix[0])):
            if y == 0:
                matrix[x][y] += min(matrix[x - 1][y], matrix[x - 1][y + 1])
            elif y == len(matrix[0]) - 1:
                matrix[x][y] += min(matrix[x - 1][y], matrix[x - 1][y - 1])
            else:
                matrix[x][y] += min(matrix[x - 1][y], matrix[x - 1][y - 1], matrix[x - 1][y + 1])

    return min(matrix[-1])


import math
from heapq import heappop, heappush, heapify


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    result = []
    for x, y in points:
        distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
        heappush(result, (-distance, [x, y]))
        if len(result) > k:
            heappop(result)
    return [coords for distance, coords in result]


def validate_stack_sequence(pushed: List[int], popped: List[int]) -> bool:
    stack, pointer_pushed, pointer_popped = [], 0, 0
    while pointer_pushed < len(pushed) and pointer_popped < len(popped):
        if not stack or stack[-1] != popped[pointer_popped]:
            stack.append(pushed[pointer_pushed])
            pointer_pushed += 1
        else:
            stack.pop()
            pointer_popped += 1

    while pointer_pushed < len(pushed):
        stack.append(pushed[pointer_pushed])
        pointer_pushed += 1

    while pointer_popped < len(popped) and stack[-1] == popped[pointer_popped]:
        stack.pop()
        pointer_popped += 1

    return not stack


def last_stone_weight(stones: List[int]) -> int:
    if not stones:
        return 0
    stones = [-stone for stone in stones]
    heapify(stones)
    while len(stones) > 1:
        stone_a = -heappop(stones)
        stone_b = -heappop(stones)
        if stone_a != stone_b:
            heappush(stones, -(abs(stone_a - stone_b)))
    return -stones[0]


from collections import deque


def can_reach(arr: List[int], start: int) -> bool:
    visited = {start}
    queue = deque([start])
    while queue:
        position = queue.popleft()
        visited.add(position)
        value = arr[position]
        if value == 0:
            return True

        left_position, right_position = position - value, position + value
        if len(arr) > left_position >= 0 and left_position not in visited:
            queue.append(left_position)
            visited.add(left_position)
        if 0 <= right_position < len(arr) and right_position not in visited:
            queue.append(right_position)
            visited.add(right_position)
    return False


def longest_ones(nums: List[int], k: int) -> int:
    longest_ones, pointer_a, pointer_b, flipped = 0, 0, 0, 0
    while pointer_b < len(nums):
        while nums[pointer_b] == 0 and flipped == k:
            if nums[pointer_a] == 0:
                flipped -= 1
            pointer_a += 1

        if nums[pointer_b] == 0:
            flipped += 1
        pointer_b += 1
        longest_ones = max(longest_ones, pointer_b - pointer_a)

    return longest_ones


def min_cost_climbing_stairs(cost: List[int]) -> int:
    if len(cost) <= 2:
        return min(cost)
    for i in range(2, len(cost)):
        cost[i] += min(cost[i - 1], cost[i - 2])
    return min(cost[-1], cost[-2])


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    result, pointer_one, pointer_two = [], 0, 0
    nums1.sort()
    nums2.sort()
    while pointer_one < len(nums1) and pointer_two < len(nums2):
        num_one = nums1[pointer_one]
        num_two = nums2[pointer_two]
        if num_one == num_two:
            result.append(num_one)
            pointer_one += 1
            pointer_two += 1
        elif num_one < num_two:
            pointer_one += 1
        else:
            pointer_two += 1
    return result


def maxArea(height: List[int]) -> int:
    pointer_a, pointer_b, max_area = 0, len(height) - 1, 0
    while pointer_a < pointer_b:
        max_area = max(min(height[pointer_a], height[pointer_b]) * (pointer_b - pointer_a), max_area)
        pointer_a, pointer_b = (pointer_a + 1, pointer_b) if height[pointer_a] <= height[pointer_b] else (
            pointer_a, pointer_b - 1)
    return max_area


def maxProfit(prices: List[int]) -> int:
    min_so_far, max_profit = prices[0], 0
    for i in range(1, len(prices)):
        max_profit = max(max_profit, prices[i] - min_so_far)
        min_so_far = min(min_so_far, prices[i])
    return max_profit


def isAlienSorted(words: List[str], order: str) -> bool:
    ordering_map = {letter: i for i, letter in enumerate(order)}

    def compare(word_one: str, word_two: str) -> bool:
        for letter_one, letter_two in zip(word_one, word_two):
            if letter_one != letter_two:
                return ordering_map[letter_one] < ordering_map[letter_two]
        return len(word_two) >= len(word_one)

    for i in range(1, len(words)):
        if not compare(words[i - 1], words[i]):
            return False
    return True


def removeElement(nums: List[int], val: int) -> int:
    pointer_a, pointer_b = 0, 0
    while pointer_b < len(nums):
        if nums[pointer_b] != val:
            nums[pointer_a] = nums[pointer_b]
            pointer_a += 1
        pointer_b += 1
    return pointer_a


def maxSubArray(nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i - 1])
    return max(nums)


def lengthOfLIS(nums: List[int]) -> int:
    result = [1 for _ in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                result[i] = max(result[i], 1 + result[j])
    return max(result)


def merge_2(intervals: List[List[int]]) -> List[List[int]]:
    result = []
    intervals.sort()
    for interval in intervals:
        if result and result[-1][1] >= interval[0]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result


def canJump(nums: List[int]) -> bool:
    max_distance = 0
    for i, num in enumerate(nums):
        if i > max_distance:
            return False
        max_distance = max(max_distance, i + num)
    return True


def first_and_last_of_k(nums: List[int], k: int) -> List[int]:
    def binary_search_left():
        low, high = 0, len(nums) - 1
        while low <= high:
            mid_pointer = (low + high) // 2
            if nums[mid_pointer] < k:
                low = mid_pointer + 1
            else:
                high = mid_pointer - 1
        return low

    def binary_search_right():
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > k:
                high = mid - 1
            else:
                low = mid + 1
        return high

    left, right = binary_search_left(), binary_search_right()
    if left > right:
        return [-1, -1]
    return [left, right]
