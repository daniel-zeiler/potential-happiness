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
