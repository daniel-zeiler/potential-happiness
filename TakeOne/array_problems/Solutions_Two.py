import collections
import heapq
import math
from typing import List


"""
In this solution I will be sorting the intervals by their first element. This will
allow for an easy comparison between different intervals and allow for an iterative
solution to take place after sorting.  This is an O(nlogn) algorith due to sorting
and the space complexity is O(n).
"""


def merge(intervals: List[List[int]]) -> List[List[int]]:
  intervals.sort(key=lambda x: x[0])
  result = []
  for index, number in enumerate(intervals):
    if index == 0:
      result.append(number)
    elif number[0] <= result[-1][1]:
      result[-1][1] = max(result[-1][1], number[1])
    else:
      result.append(number)
  return result


"""
Here I will traverse the input grid until I reach land.  Then, I will perform depth
first search on that piece of land and counting the number of pieces of land That
aren't connected to other pieces of land four directionally, summing them up, and
returning that value.  This will be an O(n) algorithm time and space complexity 
due to the recursive nature of this function.
"""


def largest_parameter(input):
  result = 0

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

  for x, row in enumerate(input):
    for y, value in enumerate(row):
      if value == 1:
        result = max(traverse(x, y), result)
  return result


"""
Here i'll be iterate through the grid and find the maximal value for each x and y
value.  I think take the difference between minimas between those values for 
each position and aggregate those values into a result.  O(2n) time.  O(x+y) space
where is is the len of the x dimension and y is the len of the y dimension.
"""


def maxIncreaseKeepingSkyline(grid: List[List[int]]) -> int:
  max_x_axis = [float('-inf') for _ in range(len(grid))]
  max_y_axis = [float('-inf') for _ in range(len(grid[0]))]

  for x, row in enumerate(grid):
    for y, value in enumerate(row):
      max_x_axis[x] = max(max_x_axis[x], value)
      max_y_axis[y] = max(max_y_axis[y], value)

  result = 0

  for x, row in enumerate(grid):
    for y, value in enumerate(row):
      result += min(max_x_axis[x], max_y_axis[y]) - value

  return result


"""
For each number i'll cast it into an int and then find the remainder of / 2 operation.
That's the answer.
"""


def findNumbers(nums: List[int]) -> int:
  result = 0
  for num in nums:
    if len(str(num)) % 2 == 0:
      result += 1
  return result


def arrayPairSum(nums: List[int]) -> int:
  nums.sort()
  result = 0
  i = 1
  while i < len(nums):
    result += min(nums[i], nums[i - 1])
    i += 2
  return result


def sortArrayByParity(nums: List[int]) -> List[int]:
  write_pointer = 0
  for read_pointer, num in enumerate(nums):
    if num % 2 == 0:
      nums[write_pointer], nums[read_pointer] = nums[read_pointer], nums[write_pointer]
      write_pointer += 1
  return nums


def replaceElements(arr: List[int]) -> List[int]:
  result = [-1 for _ in range(len(arr))]
  max_so_far = float('-inf')
  for i in range(len(arr) - 1, -1, -1):
    if i != len(arr) - 1:
      result[i] = max_so_far
    max_so_far = max(max_so_far, arr[i])
  return result


"""
Here i'm going to iterate throughout the matrix and maintain a result matrix.
The values in the result matrix will reference other positions and take the form
of ans[x][y] = min(ans[x-1][y-1],ans[x-1][y],ans[x][y]) + matrix[x][y]. The final
result will be the maximal value of this result matrix.
"""


def countSquares(matrix: List[List[int]]) -> int:
  result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
  squares = 0
  for x, row in enumerate(matrix):
    for y, value in enumerate(row):
      if x == 0 or y == 0:
        result[x][y] = matrix[x][y]
      elif matrix[x][y]:
        result[x][y] = min(result[x - 1][y - 1], result[x][y - 1], result[x - 1][y]) + 1
      else:
        result[x][y] = 0
      squares += result[x][y]
  return squares


"""
Here i'm going to traverse throughout the board until I detect a battleship, i'll increment a 
result counter 
and dfs traverse through the length of the battleship marking as I go.  I'll then return the 
number of detects.
This will be O(n) time complexity and O(max(len(board)) space complexity due to the recursive 
nature of thee problem.
"""


def countBattleships(board: List[List[str]]) -> int:
  def yield_directions(x, y):
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    for x_direction, y_direction in directions:
      x_target = x + x_direction
      y_target = y + y_direction
      if 0 <= x_target < len(board) and 0 <= y_target < len(board[0]):
        if board[x_target][y_target] == 'X':
          yield x_target, y_target

  def traverse(x, y):
    board[x][y] = '.'
    for new_x, new_y in yield_directions(x, y):
      traverse(new_x, new_y)

  result = 0
  for x, row in enumerate(board):
    for y, value in enumerate(row):
      if value == 'X':
        result += 1
        traverse(x, y)
  return result


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[
  List[int]]:
  result = []
  pointer_a = 0
  pointer_b = 0
  while pointer_a < len(firstList) and pointer_b < len(secondList):

    if secondList[pointer_b][0] <= firstList[pointer_a][0] <= secondList[pointer_b][1]:
      result.append(
        [firstList[pointer_a][0], min(secondList[pointer_b][1], firstList[pointer_a][1])])
    elif firstList[pointer_a][0] <= secondList[pointer_b][0] <= firstList[pointer_a][1]:
      result.append(
        [secondList[pointer_b][0], min(firstList[pointer_a][1], secondList[pointer_b][1])])

    if firstList[pointer_a][0] < secondList[pointer_b][0]:
      pointer_a += 1
    else:
      pointer_b += 1

  return result


"""
This is a recursive problem where I recursively iterate on the remaining permutation space until 
I reach a final solution space.  I aggregate the solution space int oa result.
This is an O(n^2) algorithm in both time and space.
"""


def permute(nums: List[int]) -> List[List[int]]:
  result = []

  def helper_function(nums_remaining, result_so_far):
    if not nums_remaining:
      result.append(result_so_far)
    else:
      for i, num in enumerate(nums_remaining):
        helper_function(nums_remaining[:i] + nums_remaining[i + 1:], result_so_far + [num])

  helper_function(nums, [])
  return result


"""
Here I will traverse the nums space iteratively and build a results along the way.  These will be 
added to a result list
until the nums space is exhausted.  This is an O(n) algorithm in both time and space.
"""


def subsets(nums: List[int]) -> List[List[int]]:
  result = []

  def helper_function(nums_remaining, result_so_far):
    result.append(result_so_far)
    if nums_remaining:
      for i, num in enumerate(nums_remaining):
        helper_function(nums_remaining[i + 1:], result_so_far + [num])

  helper_function(nums, [])
  return result


"""
Here i'll maintain a stack that records the score.  Based upon the current operation
i'll push / pop from the stack and record total points.  This is an O(n) algorithm in both
space and time.
"""


def calPoints(ops: List[str]) -> int:
  stack = []
  result = 0
  for operation in ops:
    if operation == '+':
      stack.append(stack[-1] + stack[-2])
      result += stack[-1]
    elif operation == 'D':
      stack.append(stack[-1] * 2)
      result += stack[-1]
    elif operation == 'C':
      result -= stack.pop()
    else:
      stack.append(int(operation))
      result += stack[-1]

  return result


def islandPerimeter(grid: List[List[int]]) -> int:
  def get_directions(x, y):
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    perimeter_value = 0
    new_directions = []
    for x_direction, y_direction in directions:
      x_target = x + x_direction
      y_target = y + y_direction
      if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]):
        if grid[x_target][y_target] == 1:
          new_directions.append([x_target, y_target])
        elif grid[x_target][y_target] == 0:
          perimeter_value += 1
      else:
        perimeter_value += 1
    return perimeter_value, new_directions

  def traverse(x, y):
    result = 0
    if grid[x][y] == 1:
      grid[x][y] = -1
      perimeter_value, new_directions = get_directions(x, y)
      result += perimeter_value
      for x_direction, y_direction, in new_directions:
        result += traverse(x_direction, y_direction)
    return result

  for x, row in enumerate(grid):
    for y, value in enumerate(row):
      if value == 1:
        return traverse(x, y)


"""
In this problem I will traverse the grid until I reach land.  I'll then aggregate all adjacent 
land pieces in a dfs manner.
Then I'll return the total area of this aggregation.  I'll finally return the maximal value of 
these aggregations.
O(n) space and time complexity.
"""


def maxAreaOfIsland(grid: List[List[int]]) -> int:
  max_area = 0

  def yield_directions(x, y):
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for x_direction, y_direction in directions:
      target_x = x + x_direction
      target_y = y + y_direction
      if 0 <= target_x < len(grid) and 0 <= target_y < len(grid[0]) and grid[target_x][target_y]:
        yield target_x, target_y

  def traverse(x, y):
    area = 1
    grid[x][y] = 0
    for x_direction, y_direction in yield_directions(x, y):
      area += traverse(x_direction, y_direction)
    return area

  for x, row in enumerate(grid):
    for y, value in enumerate(row):
      if value == 1:
        max_area = max(max_area, traverse(x, y))

  return max_area


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
  nums1.sort()
  nums2.sort()
  pointer_a = 0
  pointer_b = 0
  result = []
  while pointer_a < len(nums1) and pointer_b < len(nums2):
    if nums1[pointer_a] == nums2[pointer_b]:
      result.append(nums1[pointer_a])
      pointer_b += 1
      pointer_a += 1
    elif nums1[pointer_a] < nums2[pointer_b]:
      pointer_a += 1
    else:
      pointer_b += 1
  return list(set(result))


"""
Here i'll maintain a result matrix of the same size.  
Each element in the result matrix will be ans[x][y] = min(ans[x-1][y-1],ans[x-1][y],ans[x-1][
y+1]) + matrix[x][y]
The result is the minimum value in the last row of the array.
"""


def minFallingPathSum(matrix: List[List[int]]) -> int:
  result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
  for x, row in enumerate(matrix):
    for y, value in enumerate(row):
      if x == 0:
        result[x][y] = value
      elif y == 0:
        result[x][y] = min(result[x - 1][y], result[x - 1][y + 1]) + value
      elif y == len(matrix[0]) - 1:
        result[x][y] = min(result[x - 1][y - 1], result[x - 1][y]) + value
      else:
        result[x][y] = min(result[x - 1][y - 1], result[x - 1][y], result[x - 1][y + 1]) + value

  return min(result[-1])


"""
Here i'll iteratively perform dfs from each location that has gold and return the max.
This will be an O(n^2) operation as it may be a differnet answer for each one and it can 
potentially 
traverse every node.
"""


def getMaximumGold(grid: List[List[int]]) -> int:
  max_gold = 0

  def get_directions(x, y):
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    for x_direction, y_direction in directions:
      x_target = x + x_direction
      y_target = y + y_direction
      if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]):
        if grid[x_target][y_target]:
          yield x_target, y_target

  def traverse(x, y):
    gold, grid[x][y], temp = grid[x][y], 0, grid[x][y]
    gold_along_path = 0
    for x_destination, y_destination in get_directions(x, y):
      gold_along_path = max(gold_along_path, traverse(x_destination, y_destination))
    grid[x][y] = temp
    return gold + gold_along_path

  for x, row in enumerate(grid):
    for y, value in enumerate(row):
      if value:
        max_gold = max(max_gold, traverse(x, y))
  return max_gold


"""
Here i'll have a stack and push to it when it's empty or the head of popped isnt equal.
return False if popped is not empty.
"""


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
  pushed = collections.deque(pushed)
  popped = collections.deque(popped)
  stack = []
  while pushed or popped:
    if not stack:
      stack.append(collections.deque.popleft(pushed))
    elif stack[-1] == popped[0]:
      stack.pop()
      collections.deque.popleft(popped)
    else:
      if not pushed:
        return False
      stack.append(collections.deque.popleft(pushed))
  return not popped and not pushed


def lastStoneWeight(stones: List[int]) -> int:
  heap = [-x for x in stones]
  heapq.heapify(heap)
  while len(heap) > 1:
    val_one = heapq.heappop(heap)
    val_two = heapq.heappop(heap)
    heapq.heappush(heap, -abs(val_one - val_two))
  return -heap[0]


"""
Here I will recursively traverse the array starting at 0, i'll go in either direction and 
maintain a 'visited' set.  If I haven't visited an area i'll continue traversing.
If I ever reach a 0 i'll return True, else return False.
O(n) algorithm.
"""


def canReach(arr: List[int], start: int) -> bool:
  visited_indexes = set()

  def traverse(index):
    visited_indexes.add(index)
    left_index = index - arr[index]
    right_index = index + arr[index]
    if 0 <= left_index and left_index not in visited_indexes:
      if traverse(left_index):
        return True
    if right_index < len(arr) and right_index not in visited_indexes:
      if traverse(right_index):
        return True
    return arr[index] == 0

  return traverse(start)


def sortArray(nums: List[int]) -> List[int]:
  def merge_util(nums):
    if len(nums) == 1:
      return nums

    mid_pointer = int(len(nums) / 2)
    left = merge_util(nums[:mid_pointer])
    right = merge_util(nums[mid_pointer:])
    result = []
    left_pointer = 0
    right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
      if left[left_pointer] < right[right_pointer]:
        result.append(left[left_pointer])
        left_pointer += 1
      else:
        result.append(right[right_pointer])
        right_pointer += 1

    if left_pointer != len(left):
      result.extend(left[left_pointer:])
    if right_pointer != len(right):
      result.extend(right[right_pointer:])

    return result

  return merge_util(nums)


def longestOnes(nums: List[int], k: int) -> int:
  pointer_start = 0
  pointer_end = 0
  flipped_values = 0
  longest = 0
  while pointer_end < len(nums):
    while flipped_values == k and nums[pointer_end] == 0:
      if nums[pointer_start] == 0:
        flipped_values -= 1
      pointer_start += 1
    if nums[pointer_end] == 0:
      flipped_values += 1
    longest = max(longest, pointer_end - pointer_start + 1)
    pointer_end += 1
  return longest


def findMaxConsecutiveOnes(nums: List[int]) -> int:
  pointer_a = 0
  pointer_b = 0
  max_ones = 0
  while pointer_b < len(nums):
    if nums[pointer_b] == 1:
      max_ones = max(max_ones, pointer_b - pointer_a + 1)
    else:
      pointer_a = pointer_b + 1
    pointer_b += 1
  return max_ones


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
  result = []
  nums1.sort()
  nums2.sort()
  nums_one_pointer = 0
  nums_two_pointer = 0
  while nums_one_pointer < len(nums1) and nums_two_pointer < len(nums2):
    if nums1[nums_one_pointer] == nums2[nums_two_pointer]:
      result.append(nums1[nums_one_pointer])
      nums_one_pointer += 1
      nums_two_pointer += 1
    elif nums1[nums_one_pointer] < nums2[nums_two_pointer]:
      nums_one_pointer += 1
    else:
      nums_two_pointer += 1

  return result


def sortColors(nums: List[int]) -> None:
  zero_pointer = 0

  for i, num in enumerate(nums):
    if num == 0:
      nums[zero_pointer], nums[i] = nums[i], nums[zero_pointer]
      zero_pointer += 1

  one_pointer = zero_pointer

  for i in range(zero_pointer, len(nums)):
    if nums[i] == 1:
      nums[one_pointer], nums[i] = nums[i], nums[one_pointer]
      one_pointer += 1


def maxProfit(prices: List[int]) -> int:
  min_so_far = float('inf')
  result = [0 for _ in range(len(prices))]
  for i, price in enumerate(prices):
    if i:
      result[i] = max(result[i - 1], price - min_so_far)
    min_so_far = min(min_so_far, price)
  return result[-1]


def numIslands(grid: List[List[str]]) -> int:
  def yield_directions(x, y):
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    for x_direction, y_direction in directions:
      x_target = x + x_direction
      y_target = y + y_direction
      if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]):
        if grid[x_target][y_target] == '1':
          yield x_target, y_target

  def traverse(x, y):
    grid[x][y] = '0'
    for x, y in yield_directions(x, y):
      traverse(x, y)

  result = 0
  for x, row in enumerate(grid):
    for y, value in enumerate(row):
      if value == '1':
        result += 1
        traverse(x, y)
  return result


def orangesRotting(grid: List[List[int]]) -> int:
  number_of_oranges = 0
  rotten_oranges = collections.deque([])
  for x, row in enumerate(grid):
    for y, value in enumerate(row):
      if value == 2:
        rotten_oranges.append([0, [x, y]])
      if value == 1:
        number_of_oranges += 1
  directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

  while rotten_oranges:
    time, [x, y] = rotten_oranges.popleft()

    if grid[x][y] == 1:
      number_of_oranges -= 1
      grid[x][y] = 2

    if number_of_oranges == 0:
      return time

    for x_direction, y_direction in directions:
      x_target = x + x_direction
      y_target = y + y_direction
      if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]):
        if grid[x_target][y_target] == 1:
          rotten_oranges.append([time + 1, [x_target, y_target]])

  return -1


def findJudge(n: int, trust: List[List[int]]) -> int:
  in_degree = set()
  out_degree = {i for i in range(n)}

  for origin, destination in trust:
    if origin in out_degree:
      out_degree.remove(origin)
    if destination not in in_degree:
      in_degree.add(destination)

  if len(in_degree) == 1 and list(in_degree)[0] not in out_degree:
    return list(in_degree)[0]

  return -1


def maxSubArray(nums: List[int]) -> int:
  result = [float('-inf') for _ in range(len(nums))]
  max_subarray = 0
  for i, num in enumerate(nums):
    if i == 0:
      result[i] = num
    else:
      result[i] = max(num, result[i - 1] + num)
    max_subarray = max(max_subarray, result[i])
  return max_subarray
