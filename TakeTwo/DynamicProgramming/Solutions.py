def fib(n: int) -> int:
    memo = [0 for _ in range(n + 1)]
    for i in range(n + 1):
        if i in [0, 1]:
            memo[i] = i
        else:
            memo[i] = memo[i - 1] + memo[i - 2]
    return memo[-1]


from typing import List


def maxSubArray(nums: List[int]) -> int:
    memo = [num for num in nums]
    for i in range(1, len(nums)):
        memo[i] = max(memo[i], memo[i - 1] + memo[i])
    return max(memo)


def canJump(nums: List[int]) -> bool:
    memo = [False for _ in range(len(nums))]
    memo[0] = True
    for i in range(len(nums)):
        if not memo[i]:
            return False
        distance = nums[i]
        for j in range(i, i + distance + 1):
            if j < len(nums):
                memo[j] = True
    return True


def uniquePaths(m: int, n: int) -> int:
    memo = [[0 for _ in range(n)] for _ in range(m)]
    for x, row in enumerate(memo):
        for y, value in enumerate(row):
            memo[x][y] = 1 if (x == 0 or y == 0) else memo[x][y - 1] + memo[x - 1][y]
    return memo[-1][-1]


def minPathSum(grid: List[List[int]]) -> int:
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if x == 0 and y == 0:
                continue
            if x == 0:
                grid[x][y] += grid[x][y - 1]
            elif y == 0:
                grid[x][y] += grid[x - 1][y]
            else:
                grid[x][y] += min(grid[x - 1][y], grid[x][y - 1])
    return grid[-1][-1]


def climbStairs(n: int) -> int:
    memo = [0 for _ in range(n)]
    for i in range(n):
        memo[i] = i + 1 if i in [0, 1] else memo[i - 1] + memo[i - 2]
    return memo[-1]


def maxProfit(prices: List[int]) -> int:
    memo = [0 for _ in range(len(prices))]
    lowest = prices[0]
    for i, price in enumerate(prices):
        memo[i] = price - lowest
        lowest = price if price < lowest else lowest
    return max(memo)


def rob(nums: List[int]) -> int:
    for i, num in enumerate(nums):
        if i in [0, 1]:
            nums[i] = num
        elif i == 2:
            nums[i] += nums[i - 2]
        else:
            nums[i] += max(nums[i - 2], nums[i - 3])
    return max(nums[-1], nums[-2])


import math


def maximalSquare(matrix: List[List[str]]) -> int:
    largest = 0
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            matrix[x][y] = int(matrix[x][y])
            if x != 0 and y != 0 and matrix[x][y]:
                matrix[x][y] += min(matrix[x - 1][y], matrix[x][y - 1], matrix[x - 1][y - 1])
            largest = max(largest, matrix[x][y])
    return int(math.pow(largest, 2))


def lengthOfLIS(nums: List[int]) -> int:
    memo = [1 for _ in nums]
    for i, number in enumerate(nums):
        for j in range(i):
            if nums[j] < number:
                memo[i] = max(memo[i], memo[j] + 1)
    return max(memo)


def isSubsequence(s: str, t: str) -> bool:
    for character in t:
        if s and s[0] == character:
            s = s[1:]
    return not s


def minCostClimbingStairs(cost: List[int]) -> int:
    if len(cost) == 0:
        return 0
    if len(cost) == 1:
        return cost[0]

    for i, a_coast in enumerate(cost):
        if i not in [0, 1]:
            cost[i] += min(cost[i - 1], cost[i - 2])

    return min(cost[-1], cost[-2])


def minFallingPathSum(matrix: List[List[int]]) -> int:
    for x in range(1, len(matrix)):
        for y in range(len(matrix[0])):
            if y == 0:
                matrix[x][y] += min(matrix[x - 1][y], matrix[x - 1][y + 1])
            elif y == len(matrix[0]) - 1:
                matrix[x][y] += min(matrix[x - 1][y], matrix[x - 1][y - 1])
            else:
                matrix[x][y] += min(matrix[x - 1][y - 1], matrix[x - 1][y], matrix[x - 1][y + 1])
    return min(matrix[-1])


def tribonacci(n: int) -> int:
    memo = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3] if i > 2 else 1
    return memo[-1]


def longestCommonSubsequence(text1: str, text2: str) -> int:
    memo = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
    for x in range(1, len(text1) + 1):
        for y in range(1, len(text2) + 1):
            memo[x][y] = memo[x - 1][y - 1] + 1 if text1[x - 1] == text2[y - 1] else max(memo[x][y - 1], memo[x - 1][y])
    return memo[-1][-1]


def countSquares(matrix: List[List[int]]) -> int:
    result = 0
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if 0 not in [x, y] and value:
                matrix[x][y] = min(matrix[x - 1][y], matrix[x - 1][y - 1], matrix[x][y - 1]) + 1
            result += matrix[x][y]
    return result


def deleteAndEarn(nums: List[int]) -> int:
    memo = [[0 for _ in range(len(nums) + 1)] for _ in range(len(nums) + 1)]
    result = 0
    for x in range(1, len(nums) + 1):
        visited_set = set()
        for y in range(x, len(nums) + 1):
            if nums[y - 1] not in visited_set:
                memo[x][y] = memo[x][y - 1] + nums[y - 1]
                visited_set = visited_set | {memo[x][y] - 1, memo[x][y] + 1}
            else:
                memo[x][y] = memo[x][y - 1]
        result = max(result, memo[x][-1])
    return result


def maxProduct(nums: List[int]) -> int:
    min_so_far = [num for num in nums]
    max_so_far = [num for num in nums]
    max_product = 0
    for i in range(1, len(nums)):
        num = nums[i]
        if num != 0:
            min_so_far[i] = min(num, num * min_so_far[i - 1])
            max_so_far[i] = max(num, num * min_so_far[i - 1], num * max_so_far[i - 1])
        max_product = max(max_product, max_so_far[i])
    return max_product


def getMaxLen(nums: List[int]) -> int:
    tmp = [0 for _ in range(len(nums))]
    max_len = 0
    for i in range(len(nums)):
        num = nums[i]
        if i == 0:
            if num > 0:
                tmp[i] = 1
            elif num < 0:
                tmp[i] = -1
        else:
            if num < 0:
                if tmp[i - 1] < 0:
                    tmp[i] = abs(tmp[i - 1]) + 1
                else:
                    tmp[i] = -abs(tmp[i - 1] + 1)
            elif num > 0:
                tmp[i] = abs(tmp[i - 1]) + 1
        max_len = max(max_len, tmp[i])
    return max_len
