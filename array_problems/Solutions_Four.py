import collections
import heapq
import random
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    result = []
    intervals.sort(key=lambda x: x[0])
    for interval in intervals:
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(interval[1], result[-1][1])
    return result


def largest_parameter(input):
    def yield_directions(x, y):
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        on_parameter = False
        valid_directions = []
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(input) and 0 <= y_target < len(input[0]):
                if input[x_target][y_target] == 1:
                    valid_directions.append([x_target, y_target])
                elif input[x_target][y_target] == 0:
                    on_parameter = True
            else:
                on_parameter = True
        return on_parameter, valid_directions

    def traverse(x, y):
        result = 0
        input[x][y] = -1
        on_parameter, valid_directions = yield_directions(x, y)
        if on_parameter:
            result += 1
        for x_direction, y_direction in valid_directions:
            if input[x_direction][y_direction] == 1:
                result += traverse(x_direction, y_direction)
        return result

    result = 0
    for x, row in enumerate(input):
        for y, value in enumerate(row):
            if value == 1:
                result = max(result, traverse(x, y))
    return result


def maxIncreaseKeepingSkyline(grid: List[List[int]]) -> int:
    max_x = [float('-inf') for _ in range(len(grid))]
    max_y = [float('-inf') for _ in range(len(grid[0]))]

    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            max_x[x] = max(max_x[x], value)
            max_y[y] = max(max_y[y], value)

    result = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            result += min(max_x[x], max_y[y]) - value

    return result


def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    pair_sum = 0
    for i in range(0, len(nums), 2):
        pair_sum += min(nums[i], nums[i + 1])
    return pair_sum


def sortArrayByParity(nums: List[int]) -> List[int]:
    write_pointer = 0
    for read_pointer, num in enumerate(nums):
        if num % 2 == 0:
            nums[read_pointer], nums[write_pointer] = nums[write_pointer], nums[read_pointer]
            write_pointer += 1
    return nums


def replaceElements(arr: List[int]) -> List[int]:
    max_val = -1
    for i, value in reversed(list(enumerate(arr))):
        arr[i] = max_val
        max_val = max(max_val, value)
    return arr


def countSquares(matrix: List[List[int]]) -> int:
    result = 0
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if x != 0 and y != 0:
                if matrix[x][y] == 1:
                    matrix[x][y] = min(matrix[x - 1][y], matrix[x - 1][y - 1], matrix[x][y - 1]) + 1
            result += matrix[x][y]

    return result


def countBattleships(board: List[List[str]]) -> int:
    def yield_valid_directions(x, y):
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(board) and 0 <= y_target < len(board[0]):
                if board[x_target][y_target] == 'X':
                    yield x_target, y_target

    def traverse(x, y):
        board[x][y] = 0
        for x_direction, y_direction in yield_valid_directions(x, y):
            traverse(x_direction, y_direction)

    result = 0
    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == 'X':
                result += 1
                traverse(x, y)
    return result


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[
    List[int]]:
    pointer_first = 0
    pointer_second = 0
    result = []
    while pointer_first < len(firstList) and pointer_second < len(secondList):
        first_interval = firstList[pointer_first]
        second_interval = secondList[pointer_second]
        if first_interval[0] <= second_interval[0] <= first_interval[1] or first_interval[0] <= second_interval[1] <= \
                first_interval[1]:
            result.append([max(first_interval[0], second_interval[0]), min(first_interval[1], second_interval[1])])
        elif second_interval[0] <= first_interval[0] <= second_interval[1] or second_interval[0] <= first_interval[0] <= \
                second_interval[1]:
            result.append([max(first_interval[0], second_interval[0]), min(first_interval[1], second_interval[1])])

        if first_interval[0] > second_interval[0]:
            pointer_second += 1
        else:
            pointer_first += 1

    return result


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    def permute_function(nums_remaining, result_so_far):
        if not nums_remaining:
            result.append(result_so_far)
        else:
            for i, number in enumerate(nums_remaining):
                permute_function(nums_remaining[:i] + nums_remaining[i + 1:], result_so_far + [number])

    permute_function(nums, [])
    return result


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def subset_function(nums_remaining, result_so_far):
        result.append(result_so_far)
        for i, number in enumerate(nums_remaining):
            subset_function(nums_remaining[i + 1:], result_so_far + [number])

    subset_function(nums, [])
    return result


def calPoints(ops: List[str]) -> int:
    point_stack = []
    total_points = 0
    for operation in ops:
        if operation == '+':
            point_stack.append(point_stack[-1] + point_stack[-2])
            total_points += point_stack[-1]
        elif operation == 'D':
            point_stack.append(point_stack[-1] * 2)
            total_points += point_stack[-1]
        elif operation == 'C':
            total_points -= point_stack[-1]
            point_stack.pop()
        else:
            point_stack.append(int(operation))
            total_points += point_stack[-1]
    return total_points


def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    ordering_dict = {}
    max_value = float('-inf')
    for i, value in enumerate(arr2):
        ordering_dict[value] = i
        max_value = max(max_value, value)
    if not arr2:
        max_value = 0

    def custom_comparator(value):
        if value in ordering_dict:
            return ordering_dict[value]
        return value + max_value

    arr1.sort(key=lambda x: custom_comparator(x))
    return arr1


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))


def minFallingPathSum(matrix: List[List[int]]) -> int:
    result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if x == 0:
                result[x][y] = matrix[x][y]
            elif y == 0:
                result[x][y] = min(result[x - 1][y], result[x - 1][y + 1]) + matrix[x][y]
            elif y == len(matrix[0]) - 1:
                result[x][y] = min(result[x - 1][y - 1], result[x - 1][y]) + matrix[x][y]
            else:
                result[x][y] = min(result[x - 1][y - 1], result[x - 1][y], result[x - 1][y + 1]) + matrix[x][y]

    return min(result[-1])


def getMaximumGold(grid: List[List[int]]) -> int:
    def yield_valid_direction(x, y):
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]):
                if grid[x_target][y_target] != 0:
                    yield x_target, y_target

    def traverse(x, y):
        grid[x][y], temp = 0, grid[x][y]
        max_path = 0
        for x_direciton, y_direction in yield_valid_direction(x, y):
            max_path = max(max_path, traverse(x_direciton, y_direction))
        grid[x][y] = temp
        return max_path + temp

    max_gold = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value != 0:
                max_gold = max(max_gold, traverse(x, y))
    return max_gold


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    stack = []
    pushed = collections.deque(pushed)
    popped = collections.deque(popped)
    while pushed and popped:
        while stack and stack[-1] == popped[0]:
            stack.pop()
            popped.popleft()
        stack.append(pushed.popleft())

    while stack and stack[-1] == popped[0]:
        stack.pop()
        popped.popleft()

    return not pushed and not popped


def rotate(matrix: List[List[int]]) -> None:
    def transpose():
        for x in range(len(matrix)):
            for y in range(x, len(matrix)):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    def reverse():
        for x in range(len(matrix)):
            matrix[x] = matrix[x][::-1]

    transpose()
    reverse()


def lastStoneWeight(stones: List[int]) -> int:
    stones = [-x for x in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        stone_one = -heapq.heappop(stones)
        stone_two = -heapq.heappop(stones)
        if stone_two != stone_one:
            heapq.heappush(stones, -abs(stone_one - stone_two))
    return -stones[0]


def canReach(arr: List[int], start: int) -> bool:
    visited = {start}
    queue = collections.deque([start])
    while queue:
        index = queue.popleft()
        if arr[index] == 0:
            return True

        if 0 <= index - arr[index] < len(arr) and index - arr[index] not in visited:
            visited.add(index - arr[index])
            queue.append(index - arr[index])

        if 0 <= index + arr[index] < len(arr) and index + arr[index] not in visited:
            visited.add(index + arr[index])
            queue.append(index + arr[index])

    return False


def longestOnes(nums: List[int], k: int) -> int:
    result = 0
    flipped = 0
    pointer_a = 0
    for i, number in enumerate(nums):
        while flipped > k:
            if nums[pointer_a] == 0:
                flipped -= 1
            pointer_a += 1
        if number == 0:
            flipped += 1
        result = max(result, i - pointer_a)
    return result


def minPathSum(grid: List[List[int]]) -> int:
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if x == 0 and y == 0:
                pass
            elif x == 0:
                grid[x][y] += grid[x][y - 1]
            elif y == 0:
                grid[x][y] += grid[x - 1][y]
            else:
                grid[x][y] += min(grid[x - 1][y], grid[x][y - 1])

    return grid[-1][-1]


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    if newColor == image[sr][sc]:
        return image

    def yield_directions(x, y, old_color):
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(image) and 0 <= y_target < len(image[0]):
                if image[x_target][y_target] == old_color:
                    yield x_target, y_target

    def traverse(x, y, old_color):
        image[x][y] = newColor
        for x_direction, y_direction in yield_directions(x, y, old_color):
            traverse(x_direction, y_direction, old_color)

    traverse(sr, sc, image[sr][sc])
    return image


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    pointer_one = 0
    pointer_two = 0
    result = []
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
    pointer_a = 0
    pointer_b = len(height) - 1
    max_area = 0
    while pointer_a < pointer_b:
        length = pointer_b - pointer_a
        max_area = max(max_area, length * min(height[pointer_a], height[pointer_b]))
        if height[pointer_a] < height[pointer_b]:
            pointer_a += 1
        else:
            pointer_b -= 1
    return max_area


def isAlienSorted(words: List[str], order: str) -> bool:
    pass


class RandomizedSet:

    def __init__(self):
        self.a_set = set()

    def insert(self, val: int) -> bool:
        if val not in self.a_set:
            self.a_set.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.a_set:
            self.a_set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.a_set))


def orangesRotting(grid: List[List[int]]) -> int:
    rotten_oranges = collections.deque([])
    number_fresh = 0

    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == 2:
                rotten_oranges.append([0, [x, y]])
            elif value == 1:
                number_fresh += 1

    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    max_time = 0
    while rotten_oranges:
        time, [x, y] = rotten_oranges.popleft()
        max_time = max(max_time, time)
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]) and grid[x_target][y_target] == 1:
                number_fresh -= 1
                grid[x_target][y_target] = 2
                rotten_oranges.append([time + 1, [x_target, y_target]])

    if number_fresh == 0:
        return max_time
    return -1


def removeElement(nums: List[int], val: int) -> int:
    write_pointer = 0
    for read_pointer, number in enumerate(nums):
        if number != val:
            nums[write_pointer], nums[read_pointer] = nums[read_pointer], nums[write_pointer]
            write_pointer += 1
    return write_pointer


def findJudge(n: int, trust: List[List[int]]) -> int:
    out_degree = {i for i in range(1, n + 1)}
    in_degree = {i: 0 for i in range(1, n + 1)}

    for origin, destination in trust:
        if origin in out_degree:
            out_degree.remove(origin)
        in_degree[destination] += 1

    if len(out_degree) != 1:
        return -1
    candidate = list(out_degree)[0]
    if in_degree[candidate] == n - 1:
        return candidate
    return -1


def maxSubArray(nums: List[int]) -> int:
    result = [0 for _ in range(len(nums))]
    max_value = float('-inf')
    for i, number in enumerate(nums):
        if i == 0:
            result[i] = number
        else:
            result[i] = max(number, result[i - 1] + number)
        max_value = max(result[i], max_value)

    return max_value


def lengthOfLIS(nums: List[int]) -> int:
    max_len = 0
    result = [1 for _ in range(len(nums))]
    for i, number in enumerate(nums):
        for j in range(i, -1, -1):
            if nums[j] < number:
                result[i] = max(result[j] + 1, result[i])
        max_len = max(max_len, result[i])
    return max_len


def merge_2(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    result = []
    for i, interval in enumerate(intervals):
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result


def maximalSquare(matrix: List[List[str]]) -> int:
    max_area = 0
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            value = int(value)
            matrix[x][y] = value
            if x != 0 and y != 0 and value == 1:
                matrix[x][y] += min(matrix[x - 1][y], matrix[x][y - 1], matrix[x - 1][y - 1])
            max_area = max(max_area, matrix[x][y] ** 2)
    return max_area


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    if grid[0][0] == 1:
        return -1

    grid[0][0] = 1
    queue = collections.deque([[1, [0, 0]]])
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

    while queue:
        step, [x, y] = queue.popleft()
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            return step
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]) and grid[x_target][y_target] == 0:
                grid[x_target][y_target] = 1
                queue.append([step + 1, [x_target, y_target]])

    return -1


def canJump(nums: List[int]) -> bool:
    max_jump_length = 0
    for i, number in enumerate(nums):
        if i > max_jump_length:
            return False
        max_jump_length = max(max_jump_length, i + number)
    return True


def first_and_last_of_k(nums: List[int], k: int) -> List[int]:
    def binary_search(low, high):
        if low > high:
            return -1
        mid_index = (low + high) // 2
        mid_value = nums[mid_index]
        if mid_value == k:
            return mid_index
        if mid_value < k:
            return binary_search(mid_index + 1, high)
        return binary_search(low, mid_index - 1)

    index = binary_search(0, len(nums) - 1)
    if index == -1:
        return [-1, -1]
    result = [index, index]

    def binary_search_lowest(low, high):
        if low > high:
            return
        mid_index = (low + high) // 2
        mid_value = nums[mid_index]
        if mid_value == k:
            result[0] = mid_index
            binary_search_lowest(low, mid_index - 1)
        else:
            binary_search_lowest(mid_index + 1, high)

    def binary_search_highest(low, high):
        if low > high:
            return
        mid_index = (low + high) // 2
        mid_value = nums[mid_index]
        if mid_value == k:
            result[1] = mid_index
            binary_search_highest(mid_index + 1, high)
        else:
            binary_search_highest(low, mid_index - 1)

    binary_search_lowest(0, index)
    binary_search_highest(index, len(nums) - 1)
    return result


def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if x != 0 and y != 0 and matrix[x - 1][y - 1] != value:
                return False
    return True


def plus_one_large_number(input: List[List[int]]) -> List[int]:
    values = []
    for row in input:
        for i, a_value in enumerate(row[::-1]):
            if len(values) == i:
                values.append(a_value)
            else:
                values[i] += a_value

    pass_on_pointer = 0
    while pass_on_pointer < len(values):
        while values[pass_on_pointer] >= 10:
            values[pass_on_pointer] -= 10
            if pass_on_pointer == len(values) - 1:
                values.append(1)
            else:
                values[pass_on_pointer + 1] += 1
        pass_on_pointer += 1

    return values[::-1]


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
    for i, interval in enumerate(intervals):
        if i and interval[0] < intervals[i - 1][1]:
            return False
    return True


def numberMeetingRooms(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[0])
    meeting_rooms = []
    for i, interval in enumerate(intervals):
        for meeting_room in meeting_rooms:
            if meeting_room[-1][1] < interval[0]:
                meeting_room.append(interval)
                break
        else:
            meeting_rooms.append([interval])

    return len(meeting_rooms)
