import unittest
import TakeTwo.DynamicProgramming.Solutions as dynamic_programming


class SolutionsTest(unittest.TestCase):

    def test_fib(self):
        n = 2
        output = 1
        self.assertEqual(output, dynamic_programming.fib(n))
        n = 3
        output = 2
        self.assertEqual(output, dynamic_programming.fib(n))
        n = 4
        output = 3
        self.assertEqual(output, dynamic_programming.fib(n))

    def test_max_subarray(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        output = 6
        self.assertEqual(output, dynamic_programming.maxSubArray(nums))
        nums = [5, 4, -1, 7, 8]
        output = 23
        self.assertEqual(output, dynamic_programming.maxSubArray(nums))

    def test_can_reach_end(self):
        nums = [2, 3, 1, 1, 4]
        output = True
        self.assertEqual(output, dynamic_programming.canJump(nums))
        nums = [3, 2, 1, 0, 4]
        output = False
        self.assertEqual(output, dynamic_programming.canJump(nums))

    def test_unique_paths(self):
        m = 3
        n = 7
        output = 28
        self.assertEqual(output, dynamic_programming.uniquePaths(m, n))
        m = 3
        n = 2
        output = 3
        self.assertEqual(output, dynamic_programming.uniquePaths(m, n))
        m = 7
        n = 3
        output = 28
        self.assertEqual(output, dynamic_programming.uniquePaths(m, n))
        m = 3
        n = 3
        output = 6
        self.assertEqual(output, dynamic_programming.uniquePaths(m, n))

    def test_min_path_sum(self):
        grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        output = 7
        self.assertEqual(output, dynamic_programming.minPathSum(grid))
        grid = [[1, 2, 3], [4, 5, 6]]
        output = 12
        self.assertEqual(output, dynamic_programming.minPathSum(grid))

    def test_climb_stairs(self):
        n = 2
        output = 2
        self.assertEqual(output, dynamic_programming.climbStairs(n))
        n = 3
        output = 3
        self.assertEqual(output, dynamic_programming.climbStairs(n))

    def test_max_profit(self):
        prices = [7, 1, 5, 3, 6, 4]
        output = 5
        self.assertEqual(output, dynamic_programming.maxProfit(prices))
        prices = [7, 6, 4, 3, 1]
        output = 0
        self.assertEqual(output, dynamic_programming.maxProfit(prices))

    def test_rob(self):
        nums = [1, 2, 3, 1]
        output = 4
        self.assertEqual(output, dynamic_programming.rob(nums))
        nums = [2, 7, 9, 3, 1]
        output = 12
        self.assertEqual(output, dynamic_programming.rob(nums))

    def test_maximal_area(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "1", "1", "1"]
        ]
        output = 9
        self.assertEqual(output, dynamic_programming.maximalSquare(matrix))
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
        output = 4
        self.assertEqual(output, dynamic_programming.maximalSquare(matrix))

    def test_longest_increasing_subsequence(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        output = 4
        self.assertEqual(output, dynamic_programming.lengthOfLIS(nums))
        nums = [0, 1, 0, 3, 2, 3]
        output = 4
        self.assertEqual(output, dynamic_programming.lengthOfLIS(nums))
        nums = [7, 7, 7, 7, 7, 7, 7]
        output = 1
        self.assertEqual(output, dynamic_programming.lengthOfLIS(nums))

    def test_is_subsequence(self):
        s = "abc"
        t = "ahbgdc"
        output = True
        self.assertEqual(output, dynamic_programming.isSubsequence(s, t))

        s = "axc"
        t = "ahbgdc"
        output = False
        self.assertEqual(output, dynamic_programming.isSubsequence(s, t))

    def test_min_cost_climbing_stiars(self):
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        output = 6
        self.assertEqual(output, dynamic_programming.minCostClimbingStairs(cost))
        cost = [10, 15, 20]
        output = 15
        self.assertEqual(output, dynamic_programming.minCostClimbingStairs(cost))

    def test_min_path_falling(self):
        matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
        output = 13
        self.assertEqual(output, dynamic_programming.minFallingPathSum(matrix))
        matrix = [[-19, 57], [-40, -5]]
        output = -59
        self.assertEqual(output, dynamic_programming.minFallingPathSum(matrix))

    def test_tribonacci(self):
        n = 4
        output = 4
        self.assertEqual(output, dynamic_programming.tribonacci(n))
        n = 25
        output = 1389537
        self.assertEqual(output, dynamic_programming.tribonacci(n))

    def test_longest_common_subsequence(self):
        text1 = "abcde"
        text2 = "ace"
        output = 3
        self.assertEqual(output, dynamic_programming.longestCommonSubsequence(text1, text2))
        text1 = "abc"
        text2 = "abc"
        output = 3
        self.assertEqual(output, dynamic_programming.longestCommonSubsequence(text1, text2))
        text1 = "abc"
        text2 = "def"
        output = 0
        self.assertEqual(output, dynamic_programming.longestCommonSubsequence(text1, text2))

    def test_count_squares(self):
        matrix = [
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 1, 1, 1]
        ]
        output = 15
        self.assertEqual(output, dynamic_programming.countSquares(matrix))
        matrix = [
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 0]
        ]
        output = 7
        self.assertEqual(output, dynamic_programming.countSquares(matrix))

    def test_jump(self):
        nums = [2, 3, 1, 1, 4]
        output = 2
        self.assertEqual(output, dynamic_programming.jump(nums))
        nums = [2, 3, 0, 1, 4]
        output = 2
        self.assertEqual(output, dynamic_programming.jump(nums))

    def test_max_circular_subarray(self):
        nums = [1, -2, 3, -2]
        output = 3
        self.assertEqual(output, dynamic_programming.maxSubarraySumCircular(nums))

    def test_max_product(self):
        nums = [2, 3, -2, 4]
        output = 6
        self.assertEqual(output, dynamic_programming.maxProduct(nums))
        nums = [-2, 0, -1]
        output = 0
        self.assertEqual(output, dynamic_programming.maxProduct(nums))

    def test_get_max_len(self):
        nums = [-1, -2, -3, 0, 1]
        output = 2
        self.assertEqual(output, dynamic_programming.getMaxLen(nums))
        nums = [0, 1, -2, -3, -4]
        output = 3
        self.assertEqual(output, dynamic_programming.getMaxLen(nums))
        nums = [1, -2, -3, 4]
        output = 4
        self.assertEqual(output, dynamic_programming.getMaxLen(nums))

    def test_word_break(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        output = True
        self.assertEqual(output, dynamic_programming.wordBreak(s, wordDict))
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        self.assertEqual(output, dynamic_programming.wordBreak(s, wordDict))
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        output = False
        self.assertEqual(output, dynamic_programming.wordBreak(s, wordDict))

    def test_max_score(self):
        input = [[1, 3],
                 [5, 10],
                 [3, 12]]
        t = 9
        k = 10
        output = 9
        self.assertEqual(output, dynamic_programming.max_score(input, t, k))
        input = [[12, 10],
                 [16, 10],
                 [20, 10],
                 [24, 10],
                 [8, 3]]
        t = 40
        k = 21
        output = 36
        self.assertEqual(output, dynamic_programming.max_score(input, t, k))


if __name__ == '__main__':
    unittest.main()
