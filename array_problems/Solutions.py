import collections
import heapq
import math
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return intervals

    queue = [intervals[0]]
    intervals.sort(key=lambda x: x[0])

    index = 1

    while index != len(intervals):
        if intervals[index][0] <= queue[-1][1]:
            queue[-1][1] = max(intervals[index][1], queue[-1][1])
        else:
            queue.append(intervals[index])
        index += 1

    return queue


def largest_parameter(input):
    def check_directions(x, y):
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

    def gather_perimeter_size(x, y):
        if input[x][y] == 1:
            input[x][y] = -1
            on_parimeter = 0
            parameter, new_directions = check_directions(x, y)

            if parameter:
                on_parimeter += 1
            if new_directions:
                for new_x, new_y in new_directions:
                    size = gather_perimeter_size(new_x, new_y)
                    on_parimeter += size
            return on_parimeter
        return 0

    max_parameter = 0
    for x, row in enumerate(input):
        for y, value in enumerate(row):
            if input[x][y] == 1:
                max_parameter = max(max_parameter, gather_perimeter_size(x, y))

    return max_parameter


def findNumbers(nums: List[int]) -> int:
    number_even = 0
    for num in str(nums):
        if len(num) % 2 == 0:
            number_even += 1
    return number_even


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) != self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i < len(self.stack):
                self.stack[i] += val


def sortArrayByParity(nums: List[int]) -> List[int]:
    odd_pointer = 0
    even_pointer = 0

    while even_pointer < len(nums) and odd_pointer < len(nums):
        if nums[odd_pointer] % 2 == 0:
            nums[odd_pointer], nums[even_pointer] = nums[even_pointer], nums[odd_pointer]
            even_pointer += 1
        else:
            odd_pointer += 1
    print(nums)
    return nums


def replaceElements(arr: List[int]) -> List[int]:
    max_so_far = -1
    for i in range(len(arr) - 1, -1, -1):
        max_so_far, arr[i] = max(max_so_far, arr[i]), max_so_far
    return arr


def countSquares(matrix: List[List[int]]) -> int:
    result = 0
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if x != 0 and y != 0:
                matrix[x][y] += min(matrix[x - 1][y], matrix[x][y - 1], matrix[x - 1][y - 1])
            result += matrix[x][y]
    return result


def countBattleships(board: List[List[str]]) -> int:
    def yield_directions(x, y):
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for x_direction, y_direction in directions:
            new_x = x_direction + x
            new_y = y_direction + y
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                if board[new_x][new_y] == 'X':
                    yield new_x, new_y

    def traverse(x, y):
        board[x][y] = "."
        for new_x, new_y in yield_directions(x, y):
            traverse(new_x, new_y)

    battleship_count = 0
    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == "X":
                battleship_count += 1
                traverse(x, y)

    return battleship_count


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[
    List[int]]:
    result_set = []

    pointer_a = 0
    pointer_b = 0

    while pointer_a < len(firstList) and pointer_b < len(secondList):
        if secondList[pointer_b][0] <= firstList[pointer_a][0] <= secondList[pointer_b][1] or \
                firstList[pointer_a][0] <= secondList[pointer_b][0] <= firstList[pointer_a][1]:
            result_set.append(
                [
                    max(firstList[pointer_a][0], secondList[pointer_b][0]),
                    min(firstList[pointer_a][1], secondList[pointer_b][1])
                ]
            )
        if firstList[pointer_a][0] <= secondList[pointer_b][0]:
            pointer_a += 1
        else:
            pointer_b += 1
    return result_set


def permute(nums: List[int]) -> List[List[int]]:
    def permutation_function(numbers, temp_result):
        result = []
        if not numbers:
            result.append(temp_result)
        else:
            for index, number in enumerate(numbers):
                result.extend(
                    permutation_function(numbers[:index] + numbers[index + 1:], temp_result + [number]))
        return result

    return permutation_function(nums, [])


def minFallingPathSum(matrix: List[List[int]]) -> int:
    result = [[float('inf') for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if x == 0:
                result[x][y] = value
            elif y == 0:
                result[x][y] = min(result[x - 1][y], result[x - 1][y + 1]) + matrix[x][y]
            elif y == len(matrix[0]) - 1:
                result[x][y] = min(result[x - 1][y - 1], result[x - 1][y]) + matrix[x][y]
            else:
                result[x][y] = min(result[x - 1][y - 1], result[x - 1][y], result[x - 1][y + 1]) + \
                               matrix[x][y]

    return min(result[-1])


def getMaximumGold(grid: List[List[int]]) -> int:
    def yield_valid_directions(x, y):
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for x_direction, y_direction in directions:
            x_position, y_position = x + x_direction, y + y_direction
            if 0 <= x_position < len(grid) and 0 <= y_position < len(grid[0]) and grid[x_position][
                y_position] != 0:
                yield x_position, y_position

    def traverse(x, y):
        gold_at_position, grid[x][y] = grid[x][y], 0
        max_path_gold = 0
        for x_position, y_position in yield_valid_directions(x, y):
            max_path_gold = max(max_path_gold, traverse(x_position, y_position))

        grid[x][y] = gold_at_position
        return max_path_gold + gold_at_position

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

    while True:
        if not popped and not pushed and not stack:
            return True
        if not pushed and popped and popped[0] != stack[-1]:
            return False
        if not stack and pushed or popped[0] != stack[-1]:
            stack.append(pushed.popleft())
        else:
            popped.popleft()
            stack.pop()


def minesweeper(board, click):
    def get_valid_directions(x, y):
        directions = [[-1, 0], [1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, -1], [-1, 1]]
        new_directions = []
        number_of_mines = 0
        for x_direction, y_direction in directions:
            x_position, y_position = x + x_direction, y + y_direction
            if 0 <= x_position < len(board) and 0 <= y_position < len(board[0]):
                if board[x_position][y_position] == 'M':
                    number_of_mines += 1
                elif board[x_position][y_position] == 'E':
                    new_directions.append([x_position, y_position])

        return number_of_mines, new_directions

    def traverse(x, y):
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            number_of_mines, new_directions = get_valid_directions(x, y)
            if number_of_mines:
                board[x][y] = str(number_of_mines)
            else:
                board[x][y] = 'B'
                for x_direction, y_direction in new_directions:
                    traverse(x_direction, y_direction)

    traverse(click[0], click[1])

    return board


def lastStoneWeight(stones: List[int]) -> int:
    stones = [-x for x in stones]
    heapq.heapify([-x for x in stones])
    while len(stones) != 1:
        heaviest = heapq.heappop(stones)
        second_heaviest = heapq.heappop(stones)
        if heaviest != second_heaviest:
            heapq.heappush(stones, -abs(heaviest - second_heaviest))
    return abs(stones.pop())


def canReach(arr: List[int], start: int) -> bool:
    queue = collections.deque([start])
    while queue:
        index = queue.popleft()
        if arr[index] == 0:
            return True
        if arr[index] != -1:
            position_magnitude, arr[index] = arr[index], -1
            if 0 <= index + position_magnitude < len(arr) and arr[index + position_magnitude] != -1:
                queue.append(index + position_magnitude)
            if 0 <= index - position_magnitude < len(arr) and arr[index - position_magnitude] != -1:
                queue.append(index - position_magnitude)

    return False


def longestOnes(nums: List[int], k: int) -> int:
    changed_zeros = 0
    pointer_start = 0
    pointer_end = 0
    longest = 0

    while pointer_end != len(nums):
        while changed_zeros == k and nums[pointer_end] == 0:
            if nums[pointer_start] == 0:
                changed_zeros -= 1
            pointer_start += 1
        if nums[pointer_end] == 0:
            changed_zeros += 1

        longest = max(longest, pointer_end - pointer_start + 1)
        pointer_end += 1
    return longest


def numEnclaves(grid: List[List[int]]) -> int:
    def get_valid_directions(x, y):
        on_boundary = False
        new_positions = []
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for x_direction, y_direction in directions:
            x_position = x + x_direction
            y_position = y + y_direction
            if 0 <= x_position < len(grid) and 0 <= y_position < len(grid[0]):
                if grid[x_position][y_position] == 1:
                    new_positions.append([x_position, y_position])
            else:
                on_boundary = True
        return on_boundary, new_positions

    def traverse(x, y):
        area = 1
        grid[x][y] = 0
        boundary, new_positions = get_valid_directions(x, y)
        for x_position, y_position in new_positions:
            position_boundary, position_area = traverse(x_position, y_position)
            boundary = boundary or position_boundary
            area += position_area
        return boundary, area

    full_area = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == 1:
                boundary, area = traverse(x, y)
                if not boundary:
                    full_area += area
    return full_area


def minPathSum(grid: List[List[int]]) -> int:
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    priority_queue = [(0, [0, 0])]
    heapq.heapify(priority_queue)

    while priority_queue:
        sum_so_far, position = heapq.heappop(priority_queue)
        x = position[0]
        y = position[1]
        if grid[x][y] != 0:
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return sum_so_far + grid[-1][-1]

            grid[x][y], sum_so_far = 0, sum_so_far + grid[x][y]

            for x_direction, y_direction in directions:
                x_position = x + x_direction
                y_position = y + y_direction
                if 0 <= x_position < len(grid) and 0 <= y_position < len(grid[0]) and grid[x_position][
                    y_position] != 0:
                    heapq.heappush(priority_queue, (sum_so_far, [x_position, y_position]))


def isMonotonic(nums: List[int]) -> bool:
    increasing = None
    for i, num in enumerate(nums):
        if i:
            if increasing is None:
                if num > nums[i - 1]:
                    increasing = True
                elif num < nums[i - 1]:
                    increasing = False
            elif increasing and num < nums[i - 1]:
                return False
            elif not increasing and num > nums[i - 1]:
                return False
    return True


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    def yield_valid_directions(color, x, y):
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for x_direction, y_direction in directions:
            new_x = x + x_direction
            new_y = y + y_direction
            if 0 <= new_x < len(image) and 0 <= new_y < len(image[0]) and image[new_x][new_y] == color:
                yield new_x, new_y

    original_color = image[sr][sc]
    if original_color == newColor:
        return image

    def traverse(x, y, color):
        image[x][y] = newColor
        for new_x, new_y in yield_valid_directions(color, x, y):
            traverse(new_x, new_y, color)

    traverse(sr, sc, original_color)
    return image


class CircularDequeNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = k
        self.current_size = 0
        self.head = CircularDequeNode()
        self.tail = CircularDequeNode()
        self.head.next, self.tail.prev = self.tail, self.head

    def insertFront(self, value: int) -> bool:
        if self.current_size == self.max_size:
            return False
        node = CircularDequeNode(value)
        self.current_size += 1
        self.head.next, self.head.next.prev, node.next, node.prev = node, node, self.head.next, \
                                                                    self.head
        return True

    def insertLast(self, value: int) -> bool:
        if self.current_size == self.max_size:
            return True
        node = CircularDequeNode(value)
        self.tail.prev, self.tail.prev.next, node.prev, node.next = node, node, self.tail.prev, \
                                                                    self.tail
        self.current_size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head.next, self.head.next.next.prev = self.head.next.next, self.head
        self.current_size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail.prev, self.tail.prev.prev.next = self.tail.prev.prev, self.tail
        self.current_size -= 1
        return True

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.head.next.value
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.tail.prev.value
        return -1

    def isEmpty(self) -> bool:
        return self.current_size == 0

    def isFull(self) -> bool:
        return self.current_size == self.max_size


def minCostClimbingStairs(cost: List[int]) -> int:
    result = [0 for _ in range(len(cost))]
    for i in range(len(cost)):
        if i == 0 or i == 1:
            result[i] = cost[i]
        else:
            result[i] = min(result[i - 1], result[i - 2]) + cost[i]
    return min(result[-1], result[-2])


def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    pointer_start = 0
    pointer_end = minutes
    result = 0
    current_grumpy_in_window = 0

    for i in range(pointer_start, pointer_end):
        if grumpy[i]:
            current_grumpy_in_window += customers[i]
        else:
            result += customers[i]
    max_grumpy_in_window = current_grumpy_in_window

    while pointer_end < len(grumpy):
        if grumpy[pointer_end]:
            current_grumpy_in_window += customers[pointer_end]
        else:
            result += customers[pointer_end]

        if grumpy[pointer_start]:
            current_grumpy_in_window -= customers[pointer_start]

        max_grumpy_in_window = max(max_grumpy_in_window, current_grumpy_in_window)

        pointer_end += 1
        pointer_start += 1

    result += max_grumpy_in_window
    return result


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    pointer_a = 0
    pointer_b = 0
    max_consecutive = 0
    while pointer_b < len(nums):
        if nums[pointer_b] == 0:
            pointer_b += 1
            pointer_a = pointer_b
        else:
            max_consecutive = max(max_consecutive, pointer_b - pointer_a + 1)
            pointer_b += 1
    return max_consecutive


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    pointer_1 = 0
    pointer_2 = 0
    result = []
    while pointer_1 < len(nums1) and pointer_2 < len(nums2):
        if nums1[pointer_1] == nums2[pointer_2]:
            result.append(nums1[pointer_1])
            pointer_1 += 1
            pointer_2 += 1
        elif nums1[pointer_1] < nums2[pointer_2]:
            pointer_1 += 1
        else:
            pointer_2 += 1
    return result


def sortArray(nums: List[int]) -> List[int]:
    def merge_sort(nums):
        if len(nums) > 1:
            mid_point = len(nums) // 2

            left = nums[:mid_point]
            right = nums[mid_point:]

            merge_sort(left)
            merge_sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

    merge_sort(nums)
    return nums


def majorityElement(nums: List[int]) -> int:
    pointer_a, pointer_b = 0, 0
    while pointer_b < len(nums):
        if nums[pointer_b] < nums[pointer_a]:
            nums[pointer_b], nums[pointer_a] = nums[pointer_a], nums[pointer_b]
            pointer_a += 1
        else:
            pointer_b += 1
    return nums[len(nums) // 2]


def gameOfLife(board: List[List[int]]) -> None:
    def count_neighbors(x, y):
        directions = [[1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1], [0, 1], [0, -1]]

        count = 0
        for x_direction, y_direction in directions:
            x_position, y_position = x + x_direction, y + y_direction
            if 0 <= x_position < len(board) and 0 <= y_position < len(board[0]):
                if board[x_position][y_position] > 0:
                    count += 1
        return count

    for x, row in enumerate(board):
        for y, value in enumerate(row):
            neighbor_count = count_neighbors(x, y)
            if value == 0:
                if neighbor_count == 3:
                    board[x][y] = -1
            else:
                if neighbor_count > 3 or neighbor_count < 2:
                    board[x][y] = 2

    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == 2:
                board[x][y] = 0
            if value == -1:
                board[x][y] = 1


def moveZeroes(nums: List[int]) -> None:
    nonzero_pointer = 0
    zero_pointer = 0
    while zero_pointer < len(nums):
        if nums[zero_pointer] != 0:
            nums[zero_pointer], nums[nonzero_pointer] = nums[nonzero_pointer], nums[zero_pointer]
            nonzero_pointer += 1
        zero_pointer += 1


def containsDuplicate(nums: List[int]) -> bool:
    return len(nums) == len(set(nums))


def reorderLogFiles(logs: List[str]) -> List[str]:
    letter_logs = []
    digit_logs = []
    for log in logs:
        if log.split(' ')[1].isnumeric():
            digit_logs.append(log)
        else:
            letter_logs.append(log)

    letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letter_logs + digit_logs


def sortColors(nums: List[int]) -> None:
    pointer_zero = 0
    pointer_one = 0
    pointer_two = 0

    while pointer_two < len(nums):
        if nums[pointer_two] != 2:
            nums[pointer_two], nums[pointer_one] = nums[pointer_one], nums[pointer_two]
            pointer_one += 1
        pointer_two += 1

    pointer_end, pointer_one = pointer_one, 0

    while pointer_one < pointer_end:
        if nums[pointer_one] != 1:
            nums[pointer_one], nums[pointer_zero] = nums[pointer_zero], nums[pointer_one]
            pointer_zero += 1
        pointer_one += 1


def maxProfit(prices: List[int]) -> int:
    result = [0 for _ in range(len(prices))]
    min_so_far = prices[0]
    for i in range(1, len(prices)):
        result[i] = max(result[i - 1], prices[i] - min_so_far)
        min_so_far = min(min_so_far, prices[i])
    return result[-1]


def numIslands(grid: List[List[str]]) -> int:
    def yield_valid_directions(x, y):
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for x_direction, y_direction in directions:
            x_position = x + x_direction
            y_position = y + y_direction
            if 0 <= x_position < len(grid) and 0 <= y_position < len(grid[0]):
                if grid[x_position][y_position] == "1":
                    yield x_position, y_position

    def traverse(x, y):
        grid[x][y] = 0
        for new_x, new_y in yield_valid_directions(x, y):
            traverse(new_x, new_y)

    num_islands = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == "1":
                num_islands += 1
                traverse(x, y)
    return num_islands


def orangesRotting(grid: List[List[int]]) -> int:
    queue = collections.deque([])
    number_of_fresh_oranges = 0

    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == 2:
                queue.append([0, (x, y)])
            elif value == 1:
                number_of_fresh_oranges += 1

    minute = 0

    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while queue:
        minute, (x, y) = collections.deque.popleft(queue)
        for x_direction, y_direction in directions:
            x_position = x + x_direction
            y_position = y + y_direction
            if 0 <= x_position < len(grid) and 0 <= y_position < len(grid[0]):
                if grid[x_position][y_position] == 1:
                    grid[x_position][y_position] = 2
                    number_of_fresh_oranges -= 1
                    queue.append([minute + 1, (x_position, y_position)])

    if number_of_fresh_oranges != 0:
        return -1

    return minute


def removeElement(nums: List[int], val: int) -> int:
    pointer_end = 0
    pointer_start = 0
    while pointer_end < len(nums):
        if nums[pointer_end] != val:
            nums[pointer_end], nums[pointer_start], = nums[pointer_start], nums[pointer_end]
            pointer_start += 1
        pointer_end += 1
    return pointer_start


def findJudge(n: int, trust: List[List[int]]) -> int:
    not_visited = {i for i in range(1, n + 1)}
    visited = set()
    for origin, destination in trust:
        visited.add(destination)
        not_visited.remove(origin)
    if len(visited) > 1 or len(not_visited) != 1:
        return -1
    return list(visited)[0]


def maxSubArray(nums: List[int]) -> int:
    result = [0 for _ in range(len(nums))]
    maximum = float('-inf')
    for index, num in enumerate(nums):
        if index == 0:
            result[index] = num
        else:
            result[index] = max(result[index - 1] + num, num)
        maximum = max(maximum, result[index])
    return maximum


def expressiveWords(s: str, words: List[str]) -> int:
    pass


def rob(nums: List[int]) -> int:
    result = [0 for _ in range(len(nums))]
    for i, num in enumerate(nums):
        if i == 0 or i == 1:
            result[i] = num
        else:
            result[i] = result[i - 2] + num
    return max(result[-1], result[-2])


def merge_2(intervals: List[List[int]]) -> List[List[int]]:
    sorted(intervals, key=lambda x: x[0])
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append(intervals[i])
    return result


def maximalSquare(matrix: List[List[str]]) -> int:
    maximal = 0
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            matrix[x][y] = int(matrix[x][y])
            if x != 0 and y != 0:
                matrix[x][y] = min(matrix[x - 1][y - 1], matrix[x - 1][y], matrix[x][y - 1]) + matrix[x][y]
            maximal = max(maximal, matrix[x][y])
    return maximal ** 2


def plusOne(digits: List[int]) -> List[int]:
    digits[-1] += 1
    index = len(digits) - 1
    while digits[index] == 10 and index != 0:
        digits[index] = 0
        index -= 1
        digits[index] += 1
    if digits[0] == 10:
        digits[0] = 1
        digits.append(0)
    return digits


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    def get_adjacent(x, y):
        directions = [[-1, 1], [1, 0], [-1, -1], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1]]
        adjacent_cells = []
        for x_direction, y_direction in directions:
            x_position, y_position = x + x_direction, y + y_direction
            if 0 <= x_position < len(grid) and 0 <= y_position < len(grid[0]):
                if grid[x_position][y_position] == 0:
                    adjacent_cells.append([x_position, y_position])
        return adjacent_cells

    queue = collections.deque([[1, (0, 0)]])

    while queue:
        distance, (x_position, y_position) = queue.popleft()
        if x_position == len(grid) - 1 and y_position == len(grid[0]) - 1:
            return distance

        if grid[x_position][y_position] == 0:
            grid[x_position][y_position] = 1
            for x_adjacent, y_adjacent in get_adjacent(x_position, y_position):
                queue.append([distance + 1, (x_adjacent, y_adjacent)])

    return -1


def exist(board: List[List[str]], word: str) -> bool:
    def get_directions(x, y, letter):
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        valid_directions = []
        for x_direction, y_direction in directions:
            x_position, y_position = x + x_direction, y + y_direction
            if 0 <= x_position < len(board) and 0 <= y_position < len(board[0]):
                if board[x_position][y_position] == letter:
                    valid_directions.append([x_position, y_position])
        return valid_directions

    def traverse_board(x, y, remaining_word):
        if not remaining_word:
            return True
        board[x][y], temp = None, board[x][y]
        for x_position, y_position in get_directions(x, y, remaining_word[0]):
            if traverse_board(x_position, y_position, remaining_word[1:]):
                return True
        board[x][y] = temp
        return False

    for x, row in enumerate(board):
        for y, letter in enumerate(row):
            if letter == word[0]:
                if traverse_board(x, y, word[1:]):
                    return True
    return False


def canJump(nums: List[int]) -> bool:
    result = [0 for _ in range(len(nums))]
    for i in range(len(nums)):
        for j in range(1, nums[i] + 1):
            if 0 <= i + j < len(nums):
                result[i + j] += 1
    return result[-1] != 0
