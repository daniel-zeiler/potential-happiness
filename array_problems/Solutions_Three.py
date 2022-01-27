import collections
import heapq
import random
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    result = []
    intervals.sort(key=lambda x: x[0])
    for i, interval in enumerate(intervals):
        if not result:
            result.append(interval)
        else:
            if result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
    return result


def largest_parameter(input):
    def get_valid_directions(x, y):
        valid_directions = []
        on_parimeter = False
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        for x_direction, y_direction in directions:
            new_x = x + x_direction
            new_y = y + y_direction
            if 0 <= new_x < len(input) and 0 <= new_y < len(input[0]):
                if input[new_x][new_y] == 1:
                    valid_directions.append([new_x, new_y])
                elif input[new_x][new_y] == 0:
                    on_parimeter = True
            else:
                on_parimeter = True
        return on_parimeter, valid_directions

    def traverse(x, y):
        area = 0
        if input[x][y] == 1:
            input[x][y] = 2
            is_on_perimeter, new_directions = get_valid_directions(x, y)
            if is_on_perimeter:
                area += 1
            for x_direction, y_direction in new_directions:
                area += traverse(x_direction, y_direction)
        return area

    largest_parameter = 0
    for x, row in enumerate(input):
        for y, value in enumerate(row):
            largest_parameter = max(largest_parameter, traverse(x, y))
    return largest_parameter


def maxIncreaseKeepingSkyline(grid: List[List[int]]) -> int:
    max_x_values = [float('-inf') for _ in range(len(grid))]
    max_y_values = [float('-inf') for _ in range(len(grid[0]))]
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            max_x_values[x] = max(max_x_values[x], value)
            max_y_values[y] = max(max_y_values[y], value)

    max_increase_keep_skyline = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            max_increase_keep_skyline += min(max_x_values[x] - value, max_y_values[y] - value)
    return max_increase_keep_skyline


def replaceElements(arr: List[int]) -> List[int]:
    max_element_right = -1
    for i in reversed(range(len(arr))):
        arr[i], max_element_right = max_element_right, max(max_element_right, arr[i])
    return arr


def countSquares(matrix: List[List[int]]) -> int:
    result = 0

    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if x > 0 and y > 0:
                if matrix[x][y] == 1:
                    matrix[x][y] += min(matrix[x - 1][y - 1], matrix[x - 1][y], matrix[x][y - 1])
            result += matrix[x][y]
    return result


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[
    List[int]]:
    pointer_a = 0
    pointer_b = 0
    firstList.sort(key=lambda x: x[0])
    secondList.sort(key=lambda x: x[0])
    result = []
    while pointer_a < len(firstList) and pointer_b < len(secondList):
        first_interval = firstList[pointer_a]
        second_interval = secondList[pointer_b]

        if second_interval[0] <= first_interval[0] <= second_interval[1]:
            result.append([first_interval[0], min(first_interval[1], second_interval[1])])
        elif first_interval[0] <= second_interval[0] <= first_interval[1]:
            result.append([second_interval[0], min(first_interval[1], second_interval[1])])

        if first_interval[1] < second_interval[1]:
            pointer_a += 1
        else:
            pointer_b += 1

    return result


def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    max_val = 0
    relative_map = {}
    for i, value in enumerate(arr2):
        max_val = max(max_val, value)
        relative_map[value] = i

    arr1.sort(key=lambda x: relative_map[x] if x in relative_map else x + max_val)
    return arr1


"""
So this is a dynamic programming problem.  Why?  Because it can be solved iteratively
and the result is depdendent upon other subproblem results.  
Result[x][y] = Min(Result[x-1][y-1],Result[x-1][y],Result[x-1][y+1])

"""


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


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    stack = []
    pushed = collections.deque(pushed)
    popped = collections.deque(popped)
    while pushed:
        while stack and popped and stack[-1] == popped[0]:
            stack.pop()
            popped.popleft()
        stack.append(pushed.popleft())

    while stack and popped and stack[-1] == popped[0]:
        stack.pop()
        popped.popleft()

    return not stack and not popped and not pushed


def canReach(arr: List[int], start: int) -> bool:
    queue = collections.deque([start])
    visited = set()
    while queue:
        index = queue.popleft()
        if index not in visited:
            visited.add(index)
            distance = arr[index]

            if distance == 0:
                return True

            left = index - distance
            right = index + distance

            if left >= 0 and left not in visited:
                queue.append(left)
            if right < len(arr) and right not in visited:
                queue.append(right)

    return False


"""
This is a sliding window problem.  While flipped <= k i'm going to slide forward.  While flipped > k.
I'm going to slide the tail up.
"""


def longestOnes(nums: List[int], k: int) -> int:
    pointer_a = 0
    result = 0
    flipped = 0
    for i, num in enumerate(nums):
        while flipped > k:
            if nums[pointer_a] == 0:
                flipped -= 1
            pointer_a += 1
        if num == 0:
            flipped += 1
        result = max(result, i - pointer_a)
    return result


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    max_con = nums[0]
    for i, num in enumerate(nums):
        if i and num == 1:
            nums[i] = nums[i - 1] + 1
            max_con = max(nums[i], max_con)
    return max_con


input = [1, 1, 0, 1]


def maxSubArray(nums: List[int]) -> int:
    result = [0 for _ in range(len(nums))]
    max_sub_array = float('-inf')
    for i, num in enumerate(nums):
        if i == 0:
            result[i] = num
        else:
            result[i] = max(result[i - 1] + num, num)
        max_sub_array = max(max_sub_array, result[i])
    return max_sub_array


def lengthOfLIS(nums: List[int]) -> int:
    result = [1 for _ in range(len(nums))]
    for i, num in enumerate(nums):
        for j in range(i):
            if nums[j] < num:
                result[i] = max(result[j] + 1, result[i])
    return max(result)


def merge_2(intervals: List[List[int]]) -> List[List[int]]:
    result = []
    intervals.sort(key=lambda x: x[0])
    for i, interval in enumerate(intervals):
        if not result or interval[0] > result[-1][1]:
            result.append(interval)
        else:
            result[-1][1] = max(interval[1], result[-1][1])
    return result


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    queue = [(1, 0, 0)]
    heapq.heapify(queue)

    directions = [[1, 0], [-1, 0], [1, 1], [-1, 1], [0, 1], [0, -1], [-1, -1], [1, -1]]
    visited = set()

    while queue:
        distance, x, y = heapq.heappop(queue)
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            return distance
        elif grid[x][y] == 0:
            visited.add((x, y))
            for x_direction, y_direction in directions:
                x_target, y_target = x + x_direction, y + y_direction
                if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]):
                    if grid[x_target][y_target] == 0 and (x_target, y_target) not in visited:
                        heapq.heappush(queue, (distance + 1, x_target, y_target))

    return -1


def first_and_last_of_k(nums: List[int], k: int) -> List[int]:
    def find_an_index(low, high):
        if low > high:
            return -1
        mid_point = int((high + low) / 2)
        value = nums[mid_point]

        if value == k:
            return mid_point
        elif value > k:
            return find_an_index(low, mid_point - 1)
        else:
            return find_an_index(mid_point + 1, high)

    index = find_an_index(0, len(nums) - 1)
    if index == -1:
        return [-1, -1]
    result = [index, index]

    def find_left(low, high):
        if low > high:
            return
        mid_pointer = int((high + low) / 2)
        value = nums[mid_pointer]
        if value == k:
            result[0] = mid_pointer
            find_left(low, mid_pointer - 1)
        else:
            find_left(mid_pointer + 1, high)

    def find_right(low, high):
        if low > high:
            return
        mid_pointer = int((high + low) / 2)
        value = nums[mid_pointer]
        if value == k:
            result[1] = mid_pointer
            find_right(mid_pointer + 1, high)
        else:
            find_right(low, mid_pointer - 1)

    find_left(0, index)
    find_right(index, len(nums) - 1)
    return result


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
    for i, interval in enumerate(intervals):
        if i and interval[0] < intervals[i - 1][1]:
            return False
    return True


def numberMeetingRooms(intervals: List[List[int]]) -> int:
    meeting_rooms = []
    intervals.sort(key=lambda x: x[0])
    for i, meeting in enumerate(intervals):
        if not meeting_rooms:
            meeting_rooms.append([meeting])
        else:
            for meeting_room in meeting_rooms:
                if meeting[0] >= meeting_room[-1][1]:
                    meeting_room.append(meeting)
                    break
            else:
                meeting_rooms.append([meeting])
    return len(meeting_rooms)


def meeting_room_conflicts(calendar: List[List[int]], rooms: int, queries: list[List[int]]) -> List[bool]:
    rooms = [[] for _ in range(rooms)]
    calendar.sort(key=lambda x: x[0])
    for meeting in calendar:
        for room in rooms:
            if not room or meeting[0] >= room[-1][1]:
                room.append(meeting)
                break

    def check_conflict(mid_interval, target_interval):
        return mid_interval[0] < target_interval[0] < mid_interval[1] \
               or mid_interval[0] < target_interval[1] < mid_interval[1] \
               or target_interval[0] < mid_interval[0] < target_interval[1] \
               or target_interval[0] < mid_interval[1] < target_interval[1]

    def binary_search(query, room, low, high):
        if low > high:
            return True
        mid_point = (low + high) // 2
        mid_interval = room[mid_point]
        if check_conflict(query, mid_interval):
            return False
        if mid_interval[1] > query[0]:
            return binary_search(query, room, low, mid_point - 1)
        return binary_search(query, room, mid_point + 1, high)

    return [any(binary_search(query, room, 0, len(room) - 1) for room in rooms) for query in queries]


class PickWeightedRandom:

    def __init__(self, w: List[int]):
        self.sum = sum(w)
        self.range_pointer = 0
        self.ranges = []
        for weight in w:
            self.ranges.append([self.range_pointer, weight + self.range_pointer - 1])
            self.range_pointer = self.ranges[-1][1] + 1

    def pickIndex(self) -> int:
        rand_value = random.randrange(0, self.sum)

        def binary_search(target, low, high):
            mid_pointer = (low + high) // 2
            mid_range = self.ranges[mid_pointer]
            if mid_range[0] <= target <= mid_range[1]:
                return mid_pointer
            if target < mid_range[0]:
                return binary_search(target, low, mid_pointer - 1)
            return binary_search(target, mid_pointer + 1, high)

        return binary_search(rand_value, 0, len(self.ranges))


def process_last():
    pass


def process_only_one(spaces_to_add, temp_result):
    if len(temp_result) > 1:
        for i in range(0, len(temp_result) - 1):
            temp_result[i] += ' '
    temp_result += ' ' * spaces_to_add
    return ''.join(temp_result)


def process_multiple(spaces_to_add, temp_result):
    for i in range(spaces_to_add + len(temp_result) - 1):
        temp_result[i % (len(temp_result) - 1)] += ' '
    return ''.join(temp_result)


def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    result = []
    words = collections.deque(words)

    while words:
        temp_result = ''
        cur_width = 0
        while words and cur_width + len(words[0]) < maxWidth:
            if len(temp_result) > 0:
                temp_result += ' ' + words.popleft()
            else:
                temp_result += words.popleft()
            cur_width = len(temp_result)

        spaces_to_add = maxWidth - len(temp_result)
        temp_result = temp_result.split(' ')

        if not words or len(temp_result) == 1:
            result.append(process_only_one(spaces_to_add, temp_result))
        else:
            result.append(process_multiple(spaces_to_add, temp_result))

    return result


def valid_mount_array(input_array):
    if len(input_array) < 3:
        return False
    increasing = True
    for i, value in enumerate(input_array):
        if i == 0:
            if value > input_array[i + 1]:
                return False
        elif value == input_array[i - 1]:
            return False
        elif increasing:
            if value < input_array[i - 1]:
                increasing = False
        else:
            if value > input_array[i - 1]:
                return False
    return not increasing


def rotate_matrix(input_matrix):
    def transpose():
        for x in range(len(input_matrix)):
            for y in range(x + 1, len(input_matrix[0])):
                input_matrix[x][y], input_matrix[y][x] = input_matrix[y][x], input_matrix[x][y]

    def reverse():
        for x, row in enumerate(input_matrix):
            input_matrix[x] = row[::-1]

    transpose()
    reverse()


def fallAndCrush2(board):
    directions = [[-1, 0], [1, 0], [1, 1], [1, -1], [-1, -1], [0, 1], [0, -1], [-1, 1]]

    def explode(x, y):
        board[x][y] = '.'
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(board) and 0 <= y_target < len(board[0]):
                board[x_target][y_target] = '.'

    explosion_set = set()
    processing = True

    while processing:
        processing = False
        for x in range(len(board) - 1, -1, -1):
            for y in range(len(board[0])):
                if board[x][y] == '#':
                    if x == len(board) - 1 or board[x + 1][y] == '#':
                        continue
                    elif board[x + 1][y] == '*':
                        explosion_set.add((x + 1, y))
                        processing = True
                    else:
                        board[x][y] = '.'
                        board[x + 1][y] = '#'
                        processing = True
        for (x, y) in explosion_set:
            explode(x, y)
        explosion_set = set()

    return board


def number_of_markers_on_road(coordinates):
    intervals = []
    coordinates.sort(key=lambda x: x[0])
    for interval in coordinates:
        if not intervals or intervals[-1][1] < interval[0]:
            intervals.append(interval)
        else:
            intervals[-1][1] = max(intervals[-1][1], interval[1])

    return sum([x[1] - x[0] + 1 for x in intervals])


def shortestBridge(grid: List[List[int]]) -> int:
    island_one = collections.deque([])
    island_two = collections.deque([])
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def yield_directions(x, y):
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]):
                if grid[x_target][y_target] == 1:
                    yield x_target, y_target

    def traverse(x, y, island):
        island.append((0, x, y))
        grid[x][y] = -1
        for x_direction, y_direction in yield_directions(x, y):
            traverse(x_direction, y_direction, island)

    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == 1:
                if not island_one:
                    traverse(x, y, island_one)
                else:
                    traverse(x, y, island_two)
    visited_island_one = {(x[1], x[2]): 0 for x in list(island_one)}
    visited_island_two = {(x[1], x[2]): 0 for x in list(island_two)}

    def get_next_directions(x, y, visited):
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]):
                if (x_target, y_target) not in visited:
                    yield x_target, y_target

    while island_one:
        distance, x, y = island_one.popleft()
        for x_direction, y_direction in get_next_directions(x, y, visited_island_one):
            if (x_direction, y_direction) in visited_island_two:
                return visited_island_two[(x_direction, y_direction)] + distance
            if (x_direction, y_direction) not in visited_island_one:
                visited_island_one[x_direction, y_direction] = distance + 1
                island_one.append((distance + 1, x_direction, y_direction))
    return -1
