import TakeTwo.Grid.Solutions as grid

import unittest


class SolutionsTest(unittest.TestCase):
    def test_largest_parameter(self):
        input = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 1, 1, 0],
                 [0, 1, 0, 1, 1, 1, 0],
                 [0, 0, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        output = 9
        self.assertEqual(output, grid.largest_parameter(input))
        input = [[1, 0, 1, 1, 1],
                 [1, 0, 1, 1, 1],
                 [0, 1, 0, 1, 1]]
        output = 7
        self.assertEqual(output, grid.largest_parameter(input))

    def test_maxIncreaseKeepingSkyline(self):
        input = [
            [3, 0, 8, 4],
            [2, 4, 5, 7],
            [9, 2, 6, 3],
            [0, 3, 1, 0]
        ]
        output = 35
        self.assertEqual(output, grid.maxIncreaseKeepingSkyline(input))
        input = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        output = 0
        self.assertEqual(output, grid.maxIncreaseKeepingSkyline(input))

    def test_countSquares(self):
        matrix = [
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 1, 1, 1]
        ]
        output = 15
        self.assertEqual(output, grid.countSquares(matrix))
        matrix = [
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 0]
        ]
        output = 7
        self.assertEqual(output, grid.countSquares(matrix))

    def test_CountBattleships(self):
        matrix = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
        output = 2
        self.assertEqual(output, grid.countBattleships(matrix))
        matrix = [["."]]
        output = 0
        self.assertEqual(output, grid.countBattleships(matrix))

    def test_islandparameter(self):
        grid = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        output = 16
        self.assertEqual(output, grid_two.islandPerimeter(grid))
        grid = [[1]]
        output = 4
        self.assertEqual(output, grid_two.islandPerimeter(grid))
        grid = [[1, 0]]
        output = 4
        self.assertEqual(output, grid_two.islandPerimeter(grid))

    def test_max_area(self):
        grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
        output = 6
        self.assertEqual(output, grid_two.maxAreaOfIsland(grid))
        grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
        output = 0
        self.assertEqual(output, grid_two.maxAreaOfIsland(grid))

    def test_maxGold(self):
        grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
        output = 24
        self.assertEqual(output, grid_two.getMaximumGold(grid))
        grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
        output = 28
        self.assertEqual(output, grid_two.getMaximumGold(grid))

    def test_enclaves(self):
        grid = [
            [0, 0, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
        output = 3
        self.assertEqual(output, grid_two.numEnclaves(grid))
        grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        output = 0
        self.assertEqual(output, grid_two.numEnclaves(grid))

    def test_min_path_sum(self):
        grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        output = 7
        self.assertEqual(output, grid_two.minPathSum(grid))
        grid = [[1, 2, 3], [4, 5, 6]]
        output = 12
        self.assertEqual(output, grid_two.minPathSum(grid))

    def test_floodFill(self):
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1
        sc = 1
        newColor = 2
        output = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        self.assertListEqual(output, grid_two.floodFill(image, sr, sc, newColor))
        image = [[0, 0, 0], [0, 0, 0]]
        sr = 0
        sc = 0
        newColor = 2
        output = [[2, 2, 2], [2, 2, 2]]
        self.assertListEqual(output, grid_two.floodFill(image, sr, sc, newColor))

    def test_num_islands(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        output = 1
        self.assertEqual(output, grid_two.numIslands(grid))
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        output = 3
        self.assertEqual(output, grid_two.numIslands(grid))

    def test_rotten_oranges(self):
        grid = [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]
        output = 4
        self.assertEqual(output, grid_two.orangesRotting(grid))
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        output = -1
        self.assertEqual(output, grid_two.orangesRotting(grid))
        grid = [[0, 2]]
        output = 0
        self.assertEqual(output, grid_two.orangesRotting(grid))
