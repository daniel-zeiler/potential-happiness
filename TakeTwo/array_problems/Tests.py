import unittest
import TakeTwo.array_problems.Solutions as array_problems


class SolutionsTest(unittest.TestCase):
    def test_merge(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        output = [[1, 6], [8, 10], [15, 18]]
        self.assertListEqual(output, array_problems.merge(intervals))
        intervals = [[1, 4], [4, 5]]
        output = [[1, 5]]
        self.assertListEqual(output, array_problems.merge(intervals))

    def test_custom_stack(self):
        custom_stack = array_problems.CustomStack(3)
        custom_stack.push(1)
        custom_stack.push(2)
        self.assertEqual(2, custom_stack.pop())
        custom_stack.push(2)
        custom_stack.push(3)
        custom_stack.push(4)
        custom_stack.increment(5, 100)
        custom_stack.increment(2, 100)
        self.assertEqual(103, custom_stack.pop())
        self.assertEqual(202, custom_stack.pop())
        self.assertEqual(201, custom_stack.pop())
        self.assertEqual(-1, custom_stack.pop())

    def test_largest_parameter(self):
        input = [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [0, 1, 0, 1, 1]]
        output = 7
        self.assertEqual(output, array_problems.largest_parameter(input))
        input = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 1, 1, 1, 0],
                 [0, 1, 0, 1, 1, 1, 0],
                 [0, 0, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        output = 9
        self.assertEqual(output, array_problems.largest_parameter(input))

    def test_max_increase_keep_city_skyline(self):
        grid = [
            [3, 0, 8, 4],
            [2, 4, 5, 7],
            [9, 2, 6, 3],
            [0, 3, 1, 0]
        ]
        output = 35
        self.assertEqual(output, array_problems.maxIncreaseKeepingSkyline(grid))
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        output = 0
        self.assertEqual(output, array_problems.maxIncreaseKeepingSkyline(grid))

    def test_array_pair_sum(self):
        nums = [6, 2, 6, 5, 1, 2]
        output = 9
        self.assertEqual(output, array_problems.arrayPairSum(nums))
        nums = [1, 4, 3, 2]
        output = 4
        self.assertEqual(output, array_problems.arrayPairSum(nums))

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

    def test_subsets(self):
        nums = [1, 2, 3]
        output = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertCountEqual(output, array_problems.subsets(nums))
        nums = [0]
        output = [[], [0]]
        self.assertCountEqual(output, array_problems.subsets(nums))

    def test_cal_points(self):
        ops = ["5", "2", "C", "D", "+"]
        output = 30
        self.assertEqual(output, array_problems.cal_points(ops))
        ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
        output = 27
        self.assertEqual(output, array_problems.cal_points(ops))

    def test_island_perimeter(self):
        grid = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        output = 16
        self.assertEqual(output, array_problems.islandPerimeter(grid))
        grid = [[1]]
        output = 4
        self.assertEqual(output, array_problems.islandPerimeter(grid))
        grid = [[1, 0]]
        output = 4
        self.assertEqual(output, array_problems.islandPerimeter(grid))

    def test_max_area_of_island(self):
        grid = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        ]
        output = 6
        self.assertEqual(output, array_problems.maxAreaOfIsland(grid))
        grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
        output = 0
        self.assertEqual(output, array_problems.maxAreaOfIsland(grid))

    def test_relative_sort(self):
        arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
        arr2 = [2, 1, 4, 3, 9, 6]
        output = [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
        self.assertListEqual(output, array_problems.relative_sort_array(arr1, arr2))

    def test_intersection(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        output = [2]
        self.assertCountEqual(output, array_problems.intersection(nums1, nums2))
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        output = [9, 4]
        self.assertCountEqual(output, array_problems.intersection(nums1, nums2))

    def test_minimal_fall_path(self):
        matrix = [
            [2, 1, 3],
            [6, 5, 4],
            [7, 8, 9]
        ]
        output = 13
        self.assertEqual(output, array_problems.min_falling_path_sum(matrix))
        matrix = [
            [-19, 57],
            [-40, -5]
        ]
        output = -59
        self.assertEqual(output, array_problems.min_falling_path_sum(matrix))

    def test_kClosest(self):
        points = [[1, 3], [-2, 2]]
        k = 1
        output = [[-2, 2]]
        self.assertCountEqual(output, array_problems.kClosest(points, k))
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 2
        output = [[3, 3], [-2, 4]]
        self.assertCountEqual(output, array_problems.kClosest(points, k))

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
        self.assertEqual(output, array_problems.validate_stack_sequence(pushed, popped))
        pushed = [1, 2, 3, 4, 5]
        popped = [4, 3, 5, 1, 2]
        output = False
        self.assertEqual(output, array_problems.validate_stack_sequence(pushed, popped))

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
        self.assertEqual(output, array_problems.last_stone_weight(input))

    def test_can_reach(self):
        arr = [4, 2, 3, 0, 3, 1, 2]
        start = 0
        output = True
        self.assertEqual(output, array_problems.can_reach(arr, start))
        arr = [3, 0, 2, 1, 2]
        start = 2
        output = False
        self.assertEqual(output, array_problems.can_reach(arr, start))

    def test_longest_ones(self):
        nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        k = 3
        output = 10
        self.assertEqual(output, array_problems.longest_ones(nums, k))
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2
        output = 6
        self.assertEqual(output, array_problems.longest_ones(nums, k))

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

    def test_is_monitonic(self):
        nums = [1, 2, 2, 3]
        output = True
        self.assertEqual(output, array_problems.isMonotonic(nums))
        nums = [6, 5, 4, 4]
        output = True
        self.assertEqual(output, array_problems.isMonotonic(nums))
        nums = [1, 3, 2]
        output = False
        self.assertEqual(output, array_problems.isMonotonic(nums))

    def test_flood_fill(self):
        image = [
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1]
        ]
        sr = 1
        sc = 1
        newColor = 2
        output = [
            [2, 2, 2],
            [2, 2, 0],
            [2, 0, 1]
        ]
        self.assertListEqual(output, array_problems.floodFill(image, sr, sc, newColor))
        image = [
            [0, 0, 0],
            [0, 0, 0]
        ]
        sr = 0
        sc = 0
        newColor = 2
        output = [
            [2, 2, 2],
            [2, 2, 2]
        ]
        self.assertListEqual(output, array_problems.floodFill(image, sr, sc, newColor))

    def test_circular_queue(self):
        my_circular_queue = array_problems.MyCircularDeque(3)
        self.assertEqual(True, my_circular_queue.insertLast(1))
        self.assertEqual(True, my_circular_queue.insertLast(2))
        self.assertEqual(True, my_circular_queue.insertFront(3))
        self.assertEqual(False, my_circular_queue.insertFront(4))
        self.assertEqual(2, my_circular_queue.getRear())
        self.assertEqual(True, my_circular_queue.isFull())
        self.assertEqual(True, my_circular_queue.deleteLast())
        self.assertEqual(True, my_circular_queue.insertFront(4))
        self.assertEqual(4, my_circular_queue.getFront())

    def test_min_cost_climbing_stairs(self):
        cost = [10, 15, 20]
        output = 15
        self.assertEqual(output, array_problems.min_cost_climbing_stairs(cost))
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        output = 6
        self.assertEqual(output, array_problems.min_cost_climbing_stairs(cost))

    def test_max_satisfied(self):
        customers = [1, 0, 1, 2, 1, 1, 7, 5]
        grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
        minutes = 3
        output = 16
        self.assertEqual(output, array_problems.max_satisfied(customers, grumpy, minutes))

    def test_max_consecutive(self):
        nums = [1, 1, 0, 1, 1, 1]
        output = 3
        self.assertEqual(output, array_problems.findMaxConsecutiveOnes(nums))
        nums = [1, 0, 1, 1, 0, 1]
        output = 2
        self.assertEqual(output, array_problems.findMaxConsecutiveOnes(nums))

    def test_intersects(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        output = [2, 2]
        self.assertEqual(output, array_problems.intersect(nums1, nums2))
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        output = [4, 9]
        self.assertEqual(output, array_problems.intersect(nums1, nums2))

    def test_max_area(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        output = 49
        self.assertEqual(output, array_problems.maxArea(height))
        height = [1, 1]
        output = 1
        self.assertEqual(output, array_problems.maxArea(height))

    def test_sort_array(self):
        nums = [5, 2, 3, 1]
        output = [1, 2, 3, 5]
        self.assertListEqual(output, array_problems.sortArray(nums))
        nums = [5, 1, 1, 2, 0, 0]
        output = [0, 0, 1, 1, 2, 5]
        self.assertListEqual(output, array_problems.sortArray(nums))

    def test_majority_elements(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        output = 2
        self.assertEqual(output, array_problems.majorityElement(nums))
        nums = [3, 2, 3]
        output = 3
        self.assertEqual(output, array_problems.majorityElement(nums))

    def test_game_of_life(self):
        board = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]
        output = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        array_problems.gameOfLife(board)
        self.assertListEqual(output, board)
        board = [
            [1, 1],
            [1, 0]
        ]
        output = [[1, 1], [1, 1]]
        array_problems.gameOfLife(board)
        self.assertListEqual(output, board)

    def test_move_zeroes(self):
        nums = [0, 1, 0, 3, 12]
        array_problems.moveZeroes(nums)
        output = [1, 3, 12, 0, 0]
        self.assertListEqual(output, nums)
        nums = [1, 3, 5, 0, 2, 0]
        array_problems.moveZeroes(nums)
        output = [1, 3, 5, 2, 0, 0]
        self.assertListEqual(output, nums)

    def test_reorder_log_files(self):
        logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
        output = ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
        self.assertListEqual(output, array_problems.reorderLogFiles(logs))
        logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
        output = ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
        self.assertListEqual(output, array_problems.reorderLogFiles(logs))

    def test_sort_colors(self):
        nums = [2, 0, 2, 1, 1, 0]
        output = [0, 0, 1, 1, 2, 2]
        array_problems.sortColors(nums)
        self.assertListEqual(output, nums)

    def test_max_profits(self):
        prices = [7, 1, 5, 3, 6, 4]
        output = 5
        self.assertEqual(output, array_problems.maxProfit(prices))
        prices = [7, 6, 4, 3, 1]
        output = 0
        self.assertEqual(output, array_problems.maxProfit(prices))

    def test_number_of_islands(self):
        input = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        output = 1
        self.assertEqual(output, array_problems.numIslands(input))
        input = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        output = 3
        self.assertEqual(output, array_problems.numIslands(input))

    def test_rotting_oranges(self):
        grid = [
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]
        output = 4
        self.assertEqual(output, array_problems.orangesRotting(grid))
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        output = -1
        self.assertEqual(output, array_problems.orangesRotting(grid))
        grid = [[0, 2]]
        output = 0
        self.assertEqual(output, array_problems.orangesRotting(grid))

    def test_remove_elements(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        output = 5
        self.assertEqual(output, array_problems.removeElement(nums, val))
        nums = [3, 2, 2, 3]
        val = 3
        output = 2
        self.assertEqual(output, array_problems.removeElement(nums, val))

    def test_find_judge(self):
        n = 2
        trust = [[1, 2]]
        output = 2
        self.assertEqual(output, array_problems.findJudge(n, trust))
        n = 3
        trust = [[1, 3], [2, 3]]
        output = 3
        self.assertEqual(output, array_problems.findJudge(n, trust))
        n = 3
        trust = [[1, 3], [2, 3], [3, 1]]
        output = -1
        self.assertEqual(output, array_problems.findJudge(n, trust))

    def test_max_sub_array(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        output = 6
        self.assertEqual(output, array_problems.maxSubArray(nums))
        nums = [1]
        output = 1
        self.assertEqual(output, array_problems.maxSubArray(nums))
        nums = [5, 4, -1, 7, 8]
        output = 23
        self.assertEqual(output, array_problems.maxSubArray(nums))

    def test_length_of_list(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        output = 4
        self.assertEqual(output, array_problems.lengthOfLIS(nums))
        nums = [0, 1, 0, 3, 2, 3]
        output = 4
        self.assertEqual(output, array_problems.lengthOfLIS(nums))
        nums = [7, 7, 7, 7, 7, 7, 7]
        output = 1
        self.assertEqual(output, array_problems.lengthOfLIS(nums))

    def test_expressive_words(self):
        # s = "heeellooo"
        # words = ["hello", "hi", "helo"]
        # output = 1
        # self.assertEqual(output, array_problems.expressiveWords(s, words))
        # s = "zzzzzyyyyy"
        # words = ["zzyy", "zy", "zyy"]
        # output = 3
        # self.assertEqual(output, array_problems.expressiveWords(s, words))
        pass

    def test_rob(self):
        nums = [1, 2, 3, 1]
        output = 4
        self.assertEqual(output, array_problems.rob(nums))
        nums = [2, 7, 9, 3, 1]
        output = 12
        self.assertEqual(output, array_problems.rob(nums))

    def test_merge2(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        output = [[1, 6], [8, 10], [15, 18]]
        self.assertListEqual(output, array_problems.merge_2(intervals))
        intervals = [[1, 4], [4, 5]]
        output = [[1, 5]]
        self.assertListEqual(output, array_problems.merge_2(intervals))

    def test_maximal_square(self):
        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
        output = 4
        self.assertEqual(output, array_problems.maximalSquare(matrix))
        matrix = [
            ["0", "1"],
            ["1", "0"]
        ]
        output = 1
        self.assertEqual(output, array_problems.maximalSquare(matrix))
        matrix = [
            ["0"]
        ]
        output = 0
        self.assertEqual(output, array_problems.maximalSquare(matrix))

    def test_plus_one(self):
        digits = [4, 3, 2, 1]
        output = [4, 3, 2, 2]
        self.assertListEqual(output, array_problems.plusOne(digits))
        digits = [0]
        output = [1]
        self.assertListEqual(output, array_problems.plusOne(digits))
        digits = [9]
        output = [1, 0]
        self.assertListEqual(output, array_problems.plusOne(digits))

    def test_shortest_path_binary_matrix(self):
        grid = [
            [0, 1],
            [1, 0]
        ]
        output = 2
        self.assertEqual(output, array_problems.shortestPathBinaryMatrix(grid))
        grid = [
            [0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]
        ]
        output = 4
        self.assertEqual(output, array_problems.shortestPathBinaryMatrix(grid))
        grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
        output = -1
        self.assertEqual(output, array_problems.shortestPathBinaryMatrix(grid))

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

    def test_can_jump(self):
        nums = [2, 3, 1, 1, 4]
        output = True
        self.assertEqual(output, array_problems.canJump(nums))
        nums = [3, 2, 1, 0, 4]
        output = False
        self.assertEqual(output, array_problems.canJump(nums))

    def test_first_and_last_k(self):
        nums = [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6]
        k = 1
        self.assertListEqual([0, 4], array_problems.first_and_last_of_k(nums, k))
        nums = [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 11]
        k = 10
        array_problems.first_and_last_of_k(nums, k)
        self.assertListEqual([-1, -1], array_problems.first_and_last_of_k(nums, k))
        nums = [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6]
        k = 3
        self.assertListEqual([7, 7], array_problems.first_and_last_of_k(nums, k))

    def test_toeplitze_matrix(self):
        matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
        output = True
        self.assertEqual(output, array_problems.isToeplitzMatrix(matrix))
        matrix = [[1, 2], [2, 2]]
        output = False
        self.assertEqual(output, array_problems.isToeplitzMatrix(matrix))

    def test_is_alien_sorted(self):
        words = ["hello", "leetcode"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        output = True
        self.assertEqual(output, array_problems.isAlienSorted(words, order))
        words = ["word", "world", "row"]
        order = "worldabcefghijkmnpqstuvxyz"
        output = False
        self.assertEqual(output, array_problems.isAlienSorted(words, order))
        words = ["apple", "app"]
        order = "abcdefghijklmnopqrstuvwxyz"
        output = False
        self.assertEqual(output, array_problems.isAlienSorted(words, order))

    def test_plus_one_large_number(self):
        input = [
            [9, 9, 9, 9],
            [1, 1],
            [9, 4, 5, 6],
            [9, 0, 0, 0],
            [9, 9, 9, 9]
        ]
        output = [3, 8, 4, 6, 5]
        self.assertListEqual(output, array_problems.plus_one_large_number(input))

    def test_can_attend_meetings(self):
        input = [[0, 30], [5, 10], [15, 20]]
        output = False
        self.assertEqual(output, array_problems.canAttendMeetings(input))
        input = [[7, 10], [2, 4]]
        output = True
        self.assertEqual(output, array_problems.canAttendMeetings(input))

    def test_num_meeting_rooms(self):
        input = [[0, 30], [5, 10], [15, 20]]
        output = 2
        self.assertEqual(output, array_problems.numberMeetingRooms(input))

    def test_meeting_room_conflicts(self):
        calendar = [[1, 3], [4, 6], [6, 8], [9, 11], [6, 9], [1, 3], [4, 10]]
        rooms = 3
        queries = [[1, 9], [2, 6], [7, 9], [3, 5], [3, 9], [2, 4], [7, 10], [5, 9], [3, 10], [9, 10]]
        output = [False, True, False, True, False, True, False, False, False, True]
        self.assertListEqual(output, array_problems.meeting_room_conflicts(calendar, rooms, queries))

    def test_pacific_atlantic(self):
        heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
        output = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        self.assertCountEqual(output, array_problems.pacificAtlantic(heights))
        heights = [[2, 1], [1, 2]]
        output = [[0, 0], [0, 1], [1, 0], [1, 1]]
        self.assertCountEqual(output, array_problems.pacificAtlantic(heights))

    def test_pick_random_weight(self):
        pick_weight_random = array_problems.PickWeightedRandom([1, 3, 7, 1])
        print(pick_weight_random.pickIndex())
        print(pick_weight_random.pickIndex())
        print(pick_weight_random.pickIndex())
        print(pick_weight_random.pickIndex())
        print(pick_weight_random.pickIndex())
        print(pick_weight_random.pickIndex())
        print(pick_weight_random.pickIndex())
        print(pick_weight_random.pickIndex())
        print(pick_weight_random.pickIndex())
        print(pick_weight_random.pickIndex())
        print(pick_weight_random.pickIndex())

    def test_full_justify(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth = 16
        output = [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]
        self.assertListEqual(output, array_problems.fullJustify(words, maxWidth))
        words = ["What", "must", "be", "acknowledgment", "shall", "be"]
        maxWidth = 16
        output = [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
        self.assertListEqual(output, array_problems.fullJustify(words, maxWidth))

    def test_exclusive_time(self):
        n = 2
        logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
        output = [3, 4]
        self.assertListEqual(output, array_problems.exclusiveTime(n, logs))

    def test_rotate_matrix(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        output = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        array_problems.rotate(matrix)
        self.assertListEqual(output, matrix)

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
        self.assertListEqual(output, array_problems.fallAndCrush2(input))

    def test_number_of_markers_on_road(self):
        coordinates = [[4, 7], [-1, 5], [3, 6]]
        output = 9
        self.assertEqual(output, array_problems.number_of_markers_on_road(coordinates))

    def test_shortest_bridge(self):
        grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
        output = 2
        self.assertEqual(output, array_problems.shortestBridge(grid))
        grid = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
        output = 1
        self.assertEqual(output, array_problems.shortestBridge(grid))
        grid = [
            [1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ]
        output = 3
        self.assertEqual(output, array_problems.shortestBridge(grid))
        grid = [
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        output = 1
        self.assertEqual(output, array_problems.shortestBridge(grid))


if __name__ == '__main__':
    unittest.main()
