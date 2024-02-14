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
        input = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        output = 16
        self.assertEqual(output, grid.islandPerimeter(input))
        input = [[1]]
        output = 4
        self.assertEqual(output, grid.islandPerimeter(input))
        input = [[1, 0]]
        output = 4
        self.assertEqual(output, grid.islandPerimeter(input))

    def test_max_area(self):
        input = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                 [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
        output = 6
        self.assertEqual(output, grid.maxAreaOfIsland(input))
        input = [[0, 0, 0, 0, 0, 0, 0, 0]]
        output = 0
        self.assertEqual(output, grid.maxAreaOfIsland(input))

    def test_update_board(self):
        board = [
            ["E", "E", "E", "E", "E"],
            ["E", "E", "M", "E", "E"],
            ["E", "E", "E", "E", "E"],
            ["E", "E", "E", "E", "E"]
        ]
        output = [
            ["B", "1", "E", "1", "B"],
            ["B", "1", "M", "1", "B"],
            ["B", "1", "1", "1", "B"],
            ["B", "B", "B", "B", "B"]
        ]
        click = [3, 0]
        self.assertListEqual(output, grid.updateBoard(board, click))
        board = [
            ["B", "1", "E", "1", "B"],
            ["B", "1", "M", "1", "B"],
            ["B", "1", "1", "1", "B"],
            ["B", "B", "B", "B", "B"]
        ]
        click = [1, 2]
        output = [
            ["B", "1", "E", "1", "B"],
            ["B", "1", "X", "1", "B"],
            ["B", "1", "1", "1", "B"],
            ["B", "B", "B", "B", "B"]
        ]
        self.assertListEqual(output, grid.updateBoard(board, click))

    def test_maxGold(self):
        grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
        output = 24
        self.assertEqual(output, grid_two.getMaximumGold(grid))
        grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
        output = 28
        self.assertEqual(output, grid_two.getMaximumGold(grid))

    def test_enclaves(self):
        input = [
            [0, 0, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
        output = 3
        self.assertEqual(output, grid.numEnclaves(input))
        input = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        output = 0
        self.assertEqual(output, grid.numEnclaves(input))

    def test_min_path_sum(self):
        input = [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
        output = 7
        self.assertEqual(output, grid.minPathSum(input))
        input = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        output = 12
        self.assertEqual(output, grid.minPathSum(input))

    def test_floodFill(self):
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1
        sc = 1
        newColor = 2
        output = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        self.assertListEqual(output, grid.floodFill(image, sr, sc, newColor))
        image = [[0, 0, 0], [0, 0, 0]]
        sr = 0
        sc = 0
        newColor = 2
        output = [[2, 2, 2], [2, 2, 2]]
        self.assertListEqual(output, grid.floodFill(image, sr, sc, newColor))

    def test_num_islands(self):
        input = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        output = 1
        self.assertEqual(output, grid.numIslands(input))
        input = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        output = 3
        self.assertEqual(output, grid.numIslands(input))

    def test_rotten_oranges(self):
        input = [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]
        output = 4
        self.assertEqual(output, grid.orangesRotting(input))
        input = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        output = -1
        self.assertEqual(output, grid.orangesRotting(input))
        input = [[0, 2]]
        output = 0
        self.assertEqual(output, grid.orangesRotting(input))

    def test_fall_and_crush(self):
        input = [['#', '.', '#', '#', '*'],
                 ['#', '.', '.', '#', '#'],
                 ['.', '#', '.', '#', '.'],
                 ['.', '.', '#', '.', '#'],
                 ['#', '*', '.', '.', '.'],
                 ['.', '.', '*', '#', '.']]
        output = [['.', '.', '.', '.', '*'],
                  ['.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.'],
                  ['.', '.', '.', '.', '.'],
                  ['.', '.', '.', '#', '#'],
                  ['#', '.', '#', '#', '#']]
        self.assertListEqual(output, array_problems_three.fallAndCrush2(input))

    def test_pacific_atlantic(self):
        heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
        output = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        self.assertCountEqual(output, array_problems.pacificAtlantic(heights))
        heights = [[2, 1], [1, 2]]
        output = [[0, 0], [0, 1], [1, 0], [1, 1]]
        self.assertCountEqual(output, array_problems.pacificAtlantic(heights))

    def test_maximal_square(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
        output = 4
        self.assertEqual(output, grid.maximalSquare(matrix))
        matrix = [
            ["0", "1"],
            ["1", "0"]
        ]
        output = 1
        self.assertEqual(output, grid.maximalSquare(matrix))
        matrix = [
            ["0"]
        ]
        output = 0
        self.assertEqual(output, grid.maximalSquare(matrix))

    def test_shortest_path_binary_matrix(self):
        grid = [
            [0, 1],
            [1, 0]
        ]
        output = 2
        self.assertEqual(output, array_problems_four.shortestPathBinaryMatrix(grid))
        grid = [
            [0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]
        ]
        output = 4
        self.assertEqual(output, array_problems_four.shortestPathBinaryMatrix(grid))
        grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
        output = -1
        self.assertEqual(output, array_problems_four.shortestPathBinaryMatrix(grid))

    def test_exists(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        output = True
        self.assertEqual(output, array_problems.exist(board, word))
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "SEE"
        output = True
        self.assertEqual(output, array_problems.exist(board, word))
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        output = False
        self.assertEqual(output, array_problems.exist(board, word))
