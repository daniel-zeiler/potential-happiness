import collections
from typing import List


def maxSubArray(nums: List[int]) -> int:
    result = [float('-inf') for _ in range(len(nums))]
    max_sub_array = float('-inf')

    for i, num in enumerate(nums):
        if i == 0:
            result[i] = num
        else:
            result[i] = max(num, result[i - 1] + num)
        max_sub_array = max(max_sub_array, result[i])

    return max_sub_array


def canJump(nums: List[int]) -> bool:
    result = [0 for _ in range(len(nums))]
    for i, num in enumerate(nums):
        for j in range(1, num + 1):
            if 0 <= i + j < len(nums):
                result[i + j] = result[i + j] + 1
    return result[-1] != 0


def uniquePaths(m: int, n: int) -> int:
    result = [[0 for _ in range(m)] for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if x == 0 and y == 0:
                result[x][y] = 1
            elif x == 0 or y == 0:
                result[x][y] = 1
            else:
                result[x][y] = result[x - 1][y] + result[x][y - 1]
    return result[-1][-1]


def minPathSum(grid: List[List[int]]) -> int:
    result = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if x == 0 and y == 0:
                result[x][y] = grid[x][y]
            elif x == 0:
                result[x][y] = result[x][y - 1] + grid[x][y]
            elif y == 0:
                result[x][y] = result[x - 1][y] + grid[x][y]
            else:
                result[x][y] = min(result[x - 1][y], result[x][y - 1]) + grid[x][y]
    return result[-1][-1]


def maxProfit(prices: List[int]) -> int:
    lowest_so_far = float('inf')
    result = [0 for _ in range(len(prices))]
    for i, price in enumerate(prices):
        lowest_so_far = min(price, lowest_so_far)
        if i != 0:
            if price <= lowest_so_far:
                lowest_so_far = price
            else:
                result[i] = max(result[i - 1], price - lowest_so_far)
    return result[-1]


def rob(nums: List[int]) -> int:
    result = [0 for _ in range(len(nums))]
    for i, num in enumerate(nums):
        if i == 0 or i == 1:
            result[i] = num
        else:
            result[i] = result[i - 2] + num
    return max(result[-1], result[-2])


def maximalSquare(matrix: List[List[str]]) -> int:
    maximal_area = 0
    result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if x == 0 or y == 0:
                result[x][y] = int(value)
            else:
                if int(value) == 0:
                    result[x][y] = 0
                else:
                    result[x][y] = min(result[x - 1][y], result[x - 1][y - 1], result[x][y - 1]) + int(value)
            area = result[x][y] * result[x][y]
            maximal_area = max(maximal_area, area)
    return maximal_area


def lengthOfLIS(nums: List[int]) -> int:
    result = [1 for _ in range(len(nums))]
    for i, num in enumerate(nums):
        if i:
            if num > nums[i - 1]:
                result[i] += result[i - 1]
            else:
                result[i] = result[i - 1]
    return result[-1]


def isSubsequence(s: str, t: str) -> bool:
    result = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
    for s_index in range(1, len(s) + 1):
        for t_index in range(1, len(t) + 1):
            t_val = t[t_index - 1]
            s_val = s[s_index - 1]
            if s_val == t_val:
                result[t_index][s_index] = result[t_index - 1][s_index - 1] + 1
            else:
                result[t_index][s_index] = max(result[t_index - 1][s_index], result[t_index][s_index])

            if result[t_index][s_index] == min(len(s), len(t)):
                return True
    return False


def minCostClimbingStairs(cost: List[int]) -> int:
    result = [0 for _ in range(len(cost))]
    for i, value in enumerate(cost):
        if i == 0 or i == 1:
            result[i] = value
        else:
            result[i] = value + min(result[i - 1], result[i - 2])
    return min(result[-1], result[-2])


def minFallingPathSum(matrix: List[List[int]]) -> int:
    result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if x == 0:
                result[x][y] = value
            elif y == 0:
                result[x][y] = min(result[x - 1][y], result[x - 1][y + 1]) + value
            elif y == len(matrix) - 1:
                result[x][y] = min(result[x - 1][y], result[x - 1][y - 1]) + value
            else:
                result[x][y] = min(result[x - 1][y], result[x - 1][y - 1], result[x - 1][y + 1]) + value
    return min(result[-1])


def tribonacci(n: int) -> int:
    result = collections.deque([])
    for i in range(n + 1):
        if i == 0:
            collections.deque.append(result, 0)
        elif i == 1 or i == 2:
            collections.deque.append(result, 1)
        else:
            collections.deque.append(result, collections.deque.popleft(result) + result[0] + result[1])
    return result[-1]


def longestCommonSubsequence(text1: str, text2: str) -> int:
    result = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
    longest_common_subsequence = 0
    for x in range(len(text2) + 1):
        for y in range(len(text1) + 1):
            if x == 0 or y == 0:
                result[x][y] = 0
            else:
                text_1_char = text1[y - 1]
                text_2_char = text2[x - 1]
                if text_1_char == text_2_char:
                    result[x][y] = result[x - 1][y - 1] + 1
                    longest_common_subsequence = max(longest_common_subsequence, result[x][y])
                else:
                    result[x][y] = max(result[x - 1][y], result[x][y - 1])
    return longest_common_subsequence


def countSquares(matrix: List[List[int]]) -> int:
    result = 0
    squares = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if x == 0 or y == 0:
                squares[x][y] = matrix[x][y]
            elif matrix[x][y]:
                squares[x][y] = min(squares[x - 1][y - 1], squares[x - 1][y], squares[x][y - 1]) + 1
            else:
                squares[x][y] = 0
            result += squares[x][y]
    return result
