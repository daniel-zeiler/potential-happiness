import unittest
import array_problems.Solutions as array_problems


class SolutionsTest(unittest.TestCase):
  def test_merge(self):
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    output = [[1, 6], [8, 10], [15, 18]]
    self.assertListEqual(output, array_problems.merge(intervals))
    intervals = [[1, 4], [4, 5]]
    output = [[1, 5]]
    self.assertListEqual(output, array_problems.merge(intervals))

  def test_largest_parameter(self):
    input = [
      [1, 0, 1, 1, 1],
      [1, 0, 1, 1, 1],
      [0, 1, 0, 1, 1]]
    output = 7
    self.assertEqual(output, array_problems.largest_parameter(input))

  def test_sort_array_by_parity(self):
    input = [3, 1, 2, 4]
    output = [2, 4, 3, 1]
    self.assertEqual(output, array_problems.sortArrayByParity(input))

  def test_replace_elements(self):
    input = [17, 18, 5, 4, 6, 1]
    output = [18, 6, 6, 6, 1, -1]
    self.assertEqual(output, array_problems.replaceElements(input))

  def test_count_squares(self):
    input = [
      [0, 1, 1, 1],
      [1, 1, 1, 1],
      [0, 1, 1, 1]
    ]
    output = 15
    self.assertEqual(output, array_problems.countSquares(input))
    input = [
      [1, 0, 1],
      [1, 1, 0],
      [1, 1, 0]
    ]
    output = 7
    self.assertEqual(output, array_problems.countSquares(input))

  def test_count_battleships(self):
    board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
    output = 2
    self.assertEqual(output, array_problems.countBattleships(board))

  def test_interval_intersection(self):
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    output = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    self.assertListEqual(output, array_problems.intervalIntersection(firstList, secondList))

  def test_permute(self):
    nums = [1, 2, 3]
    output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    self.assertListEqual(output, array_problems.permute(nums))

  def test_minimal_fall_path(self):
    matrix = [
      [2, 1, 3],
      [6, 5, 4],
      [7, 8, 9]
    ]
    output = 13
    self.assertEqual(output, array_problems.minFallingPathSum(matrix))
    matrix = [
      [-19, 57],
      [-40, -5]
    ]
    output = -59
    self.assertEqual(output, array_problems.minFallingPathSum(matrix))

  def test_get_max_gold(self):
    input = [
      [1, 0, 7],
      [2, 0, 6],
      [3, 4, 5],
      [0, 3, 0],
      [9, 0, 20]
    ]
    output = 28
    self.assertEqual(output, array_problems.getMaximumGold(input))
    input = [
      [0, 6, 0],
      [5, 8, 7],
      [0, 9, 0]
    ]
    output = 24
    self.assertEqual(output, array_problems.getMaximumGold(input))

  def test_validate_stack_sequence(self):
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    output = True
    self.assertEqual(output, array_problems.validateStackSequences(pushed, popped))
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    output = False
    self.assertEqual(output, array_problems.validateStackSequences(pushed, popped))

  def test_update_board(self):
    board = [
      ["E", "E", "E", "E", "E"],
      ["E", "E", "M", "E", "E"],
      ["E", "E", "E", "E", "E"],
      ["E", "E", "E", "E", "E"]
    ]
    click = [3, 0]
    output = [
      ["B", "1", "E", "1", "B"],
      ["B", "1", "M", "1", "B"],
      ["B", "1", "1", "1", "B"],
      ["B", "B", "B", "B", "B"]
    ]
    self.assertEqual(output, array_problems.minesweeper(board, click))
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
    self.assertEqual(output, array_problems.minesweeper(board, click))

  def test_last_stones(self):
    input = [2, 7, 4, 1, 8, 1]
    output = 1
    self.assertEqual(output, array_problems.lastStoneWeight(input))

  def test_can_reach(self):
    arr = [4, 2, 3, 0, 3, 1, 2]
    start = 0
    output = True
    self.assertEqual(output, array_problems.canReach(arr, start))
    arr = [3, 0, 2, 1, 2]
    start = 2
    output = False
    self.assertEqual(output, array_problems.canReach(arr, start))

  def test_longest_ones(self):
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    output = 10
    self.assertEqual(output, array_problems.longestOnes(nums, k))
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    output = 6
    self.assertEqual(output, array_problems.longestOnes(nums, k))

  def test_num_enclaves(self):
    grid = [
      [0, 0, 0, 0],
      [1, 0, 1, 0],
      [0, 1, 1, 0],
      [0, 0, 0, 0]
    ]
    output = 3
    self.assertEqual(output, array_problems.numEnclaves(grid))

  def test_min_path_sum(self):
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    output = 7
    self.assertEqual(output, array_problems.minPathSum(grid))
    grid = [[1, 2, 3], [4, 5, 6]]
    output = 12
    self.assertEqual(output, array_problems.minPathSum(grid))
