"""
Fibonacci numbers
F(0) = 0
F(1) = 1
F(n) = F(n-1) + f(N-2)

"""


def recursive(n):
    if n <= 1:
        return n
    return recursive(n - 1) + recursive(n - 2)


def memoization(n):
    memo = [None for _ in range(n + 1)]

    def traverse(n):
        if memo[n]:
            return memo[n]
        else:
            if n <= 1:
                memo[n] = n
                return n
            memo[n] = traverse(n - 1) + traverse(n - 2)
            return memo[n]

    return traverse(n)


def dynamic_programming(n):
    result = []
    for i in range(n + 1):
        if i == 0:
            result.append(0)
        elif i == 1:
            result.append(1)
        else:
            result.append(result[-2] + result[-1])
    return result.pop()


"""
Zero / One
0    / 1
Knapsack problem.
Coins,= [1,2,3] -> target = 5

Is it possible to ever sum up to this target?
Zero one means that the coins are a fixed quantity when trying to get to target.
How can we use dynamic programming to cut down on all possible combinations?
combination work is O(2^n)...
How does dynamic programming speed this up?

5 [1,2,3]   -> 4 [2,3]
            -> 3 [1,3]
            -> 2 [1,2]

Target ranges [0,5]

Dimensions are coins and target range.

    5   4   3   2   1   0
1                       T
2                       T
3                       T

We will go bottom up here starting at r[3][1].  
The answers are dependent upon diagonal.


1   1   1   1   1   1   1
1
1
1
1
"""


def target_sum(nums, target):
    def backtracking_function(numbers_remaining, sum_so_far):
        result = 0
        if not numbers_remaining:
            if sum_so_far == 0:
                result += 1
        else:
            result += backtracking_function(numbers_remaining[1:], sum_so_far + numbers_remaining[0])
            result += backtracking_function(numbers_remaining[1:], sum_so_far - numbers_remaining[0])
        return result

    return backtracking_function(nums, target)


def target_sum_memoization(nums, target):
    dp = {}

    def backtracking_function(index, sum_so_far):
        if index == len(nums):
            return 1 if sum_so_far == target else 0
        if (index, sum_so_far) in dp:
            return dp[(index, sum_so_far)]
        dp[(index, sum_so_far)] = backtracking_function(index + 1, sum_so_far + nums[index]) + \
                                  backtracking_function(index + 1, sum_so_far - nums[index])
        return dp[(index, sum_so_far)]

    return backtracking_function(0, 0)


def target_sum_dynamic_programming():
    pass


nums = [2, 1, 1, 1, 2]
target = 3
print(target_sum_memoization(nums, target))


def partition_equal_subset_sum(nums):
    target = sum(nums) / 2

    def backtracking_function(index, sum_so_far):
        if index == len(nums):
            if sum_so_far == target:
                return True
            return False
        return backtracking_function(index + 1, sum_so_far + nums[index]) \
               or backtracking_function(index + 1, sum_so_far)

    return backtracking_function(0, 0)


def partition_equal_subsets_memoization(nums):
    memo = {}
    target = sum(nums) / 2

    def backtracking_function(index, sum_so_far):
        if index == len(nums):
            if sum_so_far == target:
                return True
            return False
        if (index, sum_so_far) in memo:
            return memo[(index, sum_so_far)]
        memo[(index, sum_so_far)] = backtracking_function(index + 1, sum_so_far + nums[index]) \
                                    or backtracking_function(index + 1, sum_so_far)
        return memo[(index, sum_so_far)]

    return backtracking_function(0, 0)


nums = [1, 5, 11, 5]
print(partition_equal_subsets_memoization(nums))
nums_2 = [1, 2, 3, 5]
print(partition_equal_subsets_memoization(nums_2))

"""
Unbounded Knapsack

The difference means that you can repeat coin selections from the above problem.
The goal between these problems is still the same.
Dimensions are coins and target range.

    5   4   3   2   1   0
1                       T   
2                       T
3                       T

We will go bottom up here starting at r[3][1].  The answers are 
dependent upon both the diagonal as well as the right side as
we can reuse coins at each different iteration.

"""

"""
Longest Common Sub Sequence

Here we have a string "abc" a subsequence is "ac".  Noncontiguous same ordering.
we decide if we include or do not include, maintain ordering.
This is kind of like the knapsack problem where you compare characters
multidimensionally.

    "   a   b   c
"   0   0   0   0
a   0   1   1   1
c   0   1   1   2
e   0   1   1   2

if n[x] = l[y] ans[x][y] = ans[x-1][y-1] + 1
else ans[x][y] = max(ans[x-1][y],ans[x][y-1])

"""

"""
Palindromes

suppose we're given a sting like 'racecar'. Lets count all the palindromes in
this entire string.
"""


def uniquePaths(m: int, n: int) -> int:
    result = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if x == 0 and y == 0:
                result[x][y] = 0
            if x == 0 or y == 0:
                result[x][y] = 1
            else:
                result[x][y] = result[x - 1][y] + result[x][y - 1]
    print(result)
    return result[-1][-1]


uniquePaths(3, 7)
