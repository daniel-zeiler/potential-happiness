import collections
from typing import List


def fib(n: int) -> int:
    result = collections.deque([])
    for i in range(n + 1):
        if i == 0:
            result.append(0)
        elif i == 1:
            result.append(1)
        else:
            result.append(result.popleft() + result[0])
    return result.pop()


def climbStairs(n: int) -> int:
    result = [0 for _ in range(n)]
    for i in range(n):
        if i == 0:
            result[i] = 1
        elif i == 1:
            result[i] = 2
        else:
            result[i] = result[i - 1] + result[i - 2]
    return result[-1]


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
    if len(nums) == 1:
        return nums[0]
    if not nums:
        return 0
    result = [0 for _ in range(len(nums))]
    for i, num in enumerate(nums):
        if i == 0 or i == 1:
            result[i] = num
        elif i == 2:
            result[i] = result[0] + num
        else:
            result[i] = max(result[i - 3], result[i - 2]) + num
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
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)


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


def jump(nums: List[int]) -> int:
    result = [float('inf') for _ in range(len(nums))]
    for i, num in enumerate(nums):
        if i == 0:
            for j in range(num):
                result[i + j + 1] = 1
            result[0] = 1
        else:
            if result[i] == float('inf'):
                return -1
            for j in range(num):
                if i + j + 1 < len(nums):
                    result[i + j + 1] = min(result[i + j + 1], result[i] + 1)
    return result[-1]


def maxSubarraySumCircular(nums: List[int]) -> int:
    result = [0 for _ in range(len(nums))]
    for i, num in enumerate(nums):
        if i == 0:
            result[i] = num
        else:
            result[i] = max(num, result[i - 1] + num)


def maxProduct(nums: List[int]) -> int:
    result = [0 for _ in range(len(nums))]
    max_product = float('-inf')
    for i, num in enumerate(nums):
        if i:
            result[i] = max(num, result[i - 1] * num)
        else:
            result[i] = num
        max_product = max(max_product, result[i])
    return max_product


def getMaxLen(nums: List[int]) -> int:
    result = [0 for _ in range(len(nums))]
    last_negative = -1
    max_len = 0
    for i, num in enumerate(nums):
        if num == 0:
            result[i] = 0
            last_negative = -1
        elif num < 0:
            if last_negative == -1:
                result[i] = 0
            else:
                result[i] = result[last_negative - 1] + 2
            last_negative = i
        else:
            result[i] = result[i - 1] + 1
        max_len = max(max_len, result[i])
    return max_len


def wordBreak(s: str, wordDict: List[str]) -> bool:
    words = set(wordDict)
    result = [False for _ in range(len(s))]
    pointer_a = 0

    while pointer_a < len(s):
        for pointer_b in range(pointer_a, len(s)):
            if s[pointer_a:pointer_b + 1] in words:
                result[pointer_b] = True

        pointer_a += 1

        while pointer_a < len(s) and not result[pointer_a - 1]:
            pointer_a += 1

    return result[-1]


def maxProfitTwo(prices: List[int]) -> int:
    result = [[0 for _ in range(len(prices) + 1)] for _ in range(len(prices) + 1)]
    for x in range(len(prices)):
        for y in range(len(prices)):
            if x == 0 and y == 0:
                result[x][y] = 0
            elif x == 0 or y == 1:
                result[x][y] = 1
            else:
                result[x][y] = result[x - 1][y - 2] + max(0, prices[x - 1] - prices[y - 1])
    print(result)


def max_score(tasks, time_given, minimum_score):
    result = [[0 for _ in range(time_given + 1)] for _ in range(len(tasks) + 1)]
    max_score_in_table = 0
    max_time_for_score = 0
    for x in range(1, len(tasks) + 1):
        for y in range(1, time_given + 1):
            time_for_task = tasks[x - 1][0]
            score_for_task = tasks[x - 1][1]
            current_time = y
            if current_time < time_for_task:
                result[x][y] = result[x - 1][y]
            else:
                result[x][y] = max(result[x - 1][y], result[x][y - 1],
                                   score_for_task + result[x - 1][y - time_for_task])
            if result[x][y] > max_score_in_table:
                max_score_in_table = result[x][y]
                max_time_for_score = y
    return max_time_for_score
