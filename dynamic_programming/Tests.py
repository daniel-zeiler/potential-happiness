import unittest
import dynamic_programming.Solutions as dynamic_programming


class SolutionsTest(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
