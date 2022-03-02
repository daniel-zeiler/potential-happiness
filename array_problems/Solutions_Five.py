import collections
import heapq
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for i, interval in enumerate(intervals):
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    sum = 0
    for i in range(0, len(nums), 2):
        sum += min(nums[i], nums[i + 1])
    return sum


def sortArrayByParity(nums: List[int]) -> List[int]:
    even_pointer = 0
    for odd_pointer, num in enumerate(nums):
        if num % 2 == 0:
            nums[even_pointer], nums[odd_pointer] = nums[odd_pointer], nums[even_pointer]
            even_pointer += 1
    return nums


def replaceElements(arr: List[int]) -> List[int]:
    max_so_far = -1
    for i in range(len(arr) - 1, -1, -1):
        max_so_far, arr[i] = max(max_so_far, arr[i]), max_so_far
    return arr


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[
    List[int]]:
    first_pointer = 0
    second_pointer = 0
    result = []
    while first_pointer < len(firstList) and second_pointer < len(secondList):
        first_interval = firstList[first_pointer]
        second_interval = secondList[second_pointer]
        if second_interval[0] <= first_interval[0] <= second_interval[1] or first_interval[0] <= second_interval[0] <= \
                first_interval[1]:
            result.append([max(first_interval[0], second_interval[0]), min(first_interval[1], second_interval[1])])
        if first_interval[0] < second_interval[0]:
            first_pointer += 1
        else:
            second_pointer += 1
    return result


def permute(nums: List[int]) -> List[List[int]]:
    def backtracking_function(nums_remaining, nums_so_far):
        result = []
        if not nums_remaining:
            result.append(nums_so_far)
        for i, number in enumerate(nums_remaining):
            result.extend(backtracking_function(nums_remaining[:i] + nums_remaining[i + 1:], nums_so_far + [number]))
        return result

    return backtracking_function(nums, [])


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def backtracking_function(nums_remaining, nums_so_far):
        result.append(nums_so_far)
        for i, number in enumerate(nums_remaining):
            backtracking_function(nums_remaining[i + 1:], nums_so_far + [number])

    backtracking_function(nums, [])
    return result


def calPoints(ops: List[str]) -> int:
    total_points = 0
    points_stack = []
    for operation in ops:
        if operation == 'C':
            total_points -= points_stack.pop()
        else:
            if operation == 'D':
                points_stack.append(points_stack[-1] * 2)
            elif operation == '+':
                points_stack.append(points_stack[-2] + points_stack[-1])
            else:
                points_stack.append(int(operation))
            total_points += points_stack[-1]
    return total_points


def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    ordering_map = {x: i for i, x in enumerate(arr2)}
    max_ord = len(arr2)
    arr1.sort(key=lambda x: ordering_map[x] if x in ordering_map else x + max_ord)
    return arr1


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1).intersection(set(nums2)))


def minFallingPathSum(matrix: List[List[int]]) -> int:
    level_sum = None
    for x, row in enumerate(matrix):
        if x == 0:
            level_sum = row
        else:
            temp_level = [None for _ in range(len(row))]
            for y, value in enumerate(row):
                if y == 0:
                    temp_level[y] = min(level_sum[y], level_sum[y + 1]) + value
                elif y == len(row) - 1:
                    temp_level[y] = min(level_sum[y], level_sum[y - 1]) + value
                else:
                    temp_level[y] = min(level_sum[y], level_sum[y - 1], level_sum[y + 1]) + value
            level_sum = temp_level
    return min(level_sum)


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    for x in range(len(matrix)):
        for y in range(x + 1, len(matrix)):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    for x, row in enumerate(matrix):
        matrix[x] = matrix[x][::-1]


def lastStoneWeight(stones: List[int]) -> int:
    heap = [-stone for stone in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        heapq.heappush(heap, abs(-heapq.heappop(heap) - -heapq.heappop(heap)))
    return heap[0]


def canReach(arr: List[int], start: int) -> bool:
    visited = {start}
    queue = collections.deque([start])

    while queue:
        position = queue.popleft()
        distance = arr[position]
        if distance == 0:
            return True

        left = position - distance
        right = position + distance

        if left >= 0 and left not in visited:
            visited.add(left)
            queue.append(left)
        if right < len(arr) and right not in visited:
            visited.add(right)
            queue.append(right)

    return False


def longestOnes(nums: List[int], k: int) -> int:
    number_flipped = 0
    start_pointer = 0
    result = float('-inf')
    for end_pointer, number in enumerate(nums):
        while number == 0 and number_flipped == k:
            if nums[start_pointer] == 0:
                number_flipped -= 1
            start_pointer += 1
        if number == 0:
            number_flipped += 1
        result = max(result, end_pointer - start_pointer + 1)
    return result


def minCostClimbingStairs(cost: List[int]) -> int:
    min_cost = [a_cost for a_cost in cost]
    for i, cost in enumerate(cost):
        if i == 0 or i == 1:
            continue
        else:
            min_cost[i] += min(min_cost[i - 1], min_cost[i - 2])
    return min(min_cost[-1], min_cost[-2])


def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    result = 0
    for customer_count, grump_value in zip(customers, grumpy):
        if not grump_value:
            result += customer_count
    flipped_window = 0
    for i in range(minutes):
        if grumpy[i]:
            flipped_window += customers[i]

    max_flipped_window = flipped_window
    start_pointer = 0
    for end_pointer in range(minutes, len(grumpy)):
        if grumpy[end_pointer]:
            flipped_window += customers[end_pointer]
        if grumpy[start_pointer]:
            flipped_window -= customers[start_pointer]
        max_flipped_window = max(flipped_window, max_flipped_window)
        start_pointer += 1

    return max_flipped_window + result


def reorderLogFiles(logs: List[str]) -> List[str]:
    def sort_function(log):
        log = log.split(' ')
        if log[1].isalpha():
            return ''.join(log[1:]) + log[0]
        else:
            return 'z'

    logs.sort(key=lambda x: sort_function(x))
    return logs


def maxArea(height: List[int]) -> int:
    max_area = 0
    start_pointer = 0
    end_pointer = len(height) - 1
    while start_pointer < end_pointer:
        max_area = max(min(height[end_pointer], height[start_pointer]) * (end_pointer - start_pointer), max_area)
        if height[end_pointer] < height[start_pointer]:
            end_pointer -= 1
        else:
            start_pointer += 1
    return max_area


def maxProfit(prices: List[int]) -> int:
    min_so_far = float('inf')
    max_result = 0
    for i, price in enumerate(prices):
        if i != 0:
            max_result = max(max_result, price - min_so_far)
        min_so_far = min(min_so_far, price)
    return max_result


def isAlienSorted(words: List[str], order: str) -> bool:
    order_map = {x: i for i, x in enumerate(order)}
    for i, word in enumerate(words):
        if i > 0:
            for letter_a, letter_b in zip(words[i - 1], word):
                if letter_a != letter_b:
                    if order_map[letter_a] > order_map[letter_b]:
                        return False
                    break
            else:
                if len(words[i - 1]) > len(word):
                    return False
    return True


def removeElement(nums: List[int], val: int) -> int:
    write_pointer = 0
    for read_pointer, num in enumerate(nums):
        if num != val:
            nums[write_pointer] = num
            write_pointer += 1
    return write_pointer


def findJudge(n: int, trust: List[List[int]]) -> int:
    in_degree = {i: 0 for i in range(1, n + 1)}
    out_degree = {i: 0 for i in range(1, n + 1)}
    for origin, destination in trust:
        in_degree[destination] += 1
        out_degree[origin] += 1
    judge = list(filter(lambda x: out_degree[x] == 0 and in_degree[x] == n - 1, in_degree.keys()))
    if len(judge) == 1:
        return judge[0]
    return -1


def maxSubArray(nums: List[int]) -> int:
    temp = [num for num in nums]
    for i, num in enumerate(nums):
        if i != 0:
            temp[i] = max(temp[i], temp[i - 1] + num)
    return max(temp)


def lengthOfLIS(nums: List[int]) -> int:
    temp_result_list = [1 for _ in range(len(nums))]
    for i, num in enumerate(nums):
        for j in range(i - 1, -1, -1):
            if nums[j] < num:
                temp_result_list[i] = max(temp_result_list[i], temp_result_list[j] + 1)
    return max(temp_result_list)


def rob(nums: List[int]) -> int:
    result = [num for num in nums]
    for i, num in enumerate(nums):
        if i == 0 or i == 1:
            continue
        elif i == 2:
            result[i] += result[i - 2]
        else:
            result[i] += max(result[i - 2], result[i - 3])
    return max(result[-2], result[-1])


def merge_2(intervals: List[List[int]]) -> List[List[int]]:
    result = []
    for i, interval in enumerate(intervals):
        if i == 0 or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result


def plusOne(digits: List[int]) -> List[int]:
    digits[-1] += 1
    pointer = len(digits) - 1
    while digits[pointer] == 10 and pointer != 0:
        digits[pointer] = 0
        digits[pointer - 1] += 1
    if digits[0] == 10:
        digits[0] = 1
        digits.append(0)
    return digits


def canJump(nums: List[int]) -> bool:
    max_distance = 0
    read_pointer = 0
    while read_pointer < len(nums) - 1 and read_pointer <= max_distance:
        max_distance = max(max_distance, read_pointer + nums[read_pointer])
        read_pointer += 1
    return max_distance >= len(nums) - 1


def plus_one_large_number(input: List[List[int]]) -> List[int]:
    adding = []
    for a_list in input:
        for i, value in enumerate(a_list[::-1]):
            if i == len(adding):
                adding.append(value)
            else:
                adding[i] += value

    pointer = 0
    while pointer < len(adding) and adding[pointer] > 10:
        while adding[pointer] > 10:
            adding[pointer] = adding[pointer] - 10
            if pointer == len(adding) - 1:
                adding.append(0)
            adding[pointer + 1] += 1
        pointer += 1

    return adding[::-1]


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
    for i, interval in enumerate(intervals):
        if i != 0 and intervals[i - 1][1] > interval[0]:
            return False
    return True


def numberMeetingRooms(intervals: List[List[int]]) -> int:
    meeting_rooms = []
    intervals.sort(key=lambda x: x[0])
    for i, interval in enumerate(intervals):
        for meeting_room in meeting_rooms:
            if meeting_room[-1][1] < interval[0]:
                meeting_room.append(interval)
                break
        else:
            meeting_rooms.append([interval])
    return len(meeting_rooms)


def number_of_markers_on_road(coordinates):
    coordinates.sort(key=lambda x: x[0])
    merged = []
    for i, coordinate in enumerate(coordinates):
        if not merged or merged[-1][1] < coordinate[0]:
            merged.append(coordinate)
        else:
            merged[-1][1] = max(merged[-1][1], coordinate[1])
    return sum(x[1] - x[0] + 1 for x in merged)
