import unittest
import BackTracking.Solutions as backtracking


class SolutionsTest(unittest.TestCase):
    def test_letter_combinations(self):
        input_1 = "23"
        output_1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        input_2 = "2"
        output_2 = ["a", "b", "c"]
        self.assertCountEqual(backtracking.letter_combinations(input_1), output_1)
        self.assertCountEqual(backtracking.letter_combinations(input_2), output_2)

    def test_generate_parentheses(self):
        input = 3
        output = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        input_2 = 1
        output_2 = ["()"]
        self.assertCountEqual(backtracking.generate_parentheses(input), output)
        self.assertCountEqual(backtracking.generate_parentheses(input_2), output_2)

    def test_permute(self):
        input_1 = [1, 2, 3]
        output_1 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        input_2 = [0, 1]
        output_2 = [[0, 1], [1, 0]]
        input_3 = [1]
        output_3 = [[1]]
        self.assertCountEqual(backtracking.permute(input_1), output_1)
        self.assertCountEqual(backtracking.permute(input_2), output_2)
        self.assertCountEqual(backtracking.permute(input_3), output_3)

    def test_exists(self):
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]
        word = "SEE"
        output = True
        self.assertEqual(backtracking.exist(board, word), output)
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]
        word = "ABCCED"
        output = True
        self.assertEqual(backtracking.exist(board, word), output)
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]
        word = "ABCB"
        output = False
        self.assertEqual(backtracking.exist(board, word), output)

    def test_get_maximum_gold(self):
        grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
        output = 28
        self.assertEqual(backtracking.get_maximum_gold(grid), output)
        grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
        output = 24
        self.assertEqual(backtracking.get_maximum_gold(grid), output)


if __name__ == '__main__':
    unittest.main()
