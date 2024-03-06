import unittest
import TakeTwo.BackTracking.Solutions2 as backtracking

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
        grid = [
            [1, 0, 7],
            [2, 0, 6],
            [3, 4, 5],
            [0, 3, 0],
            [9, 0, 20]
        ]
        output = 28
        self.assertEqual(backtracking.get_maximum_gold(grid), output)
        grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
        output = 24
        self.assertEqual(backtracking.get_maximum_gold(grid), output)

    def test_number_tile_possibilities(self):
        tiles = "AAB"
        output = 8
        self.assertEqual(output, backtracking.num_tile_possibilities(tiles))
        tiles = "AAABBC"
        output = 188
        self.assertEqual(output, backtracking.num_tile_possibilities(tiles))

    def test_all_paths_source_to_target(self):
        graph = [[1, 2], [3], [3], []]
        output = [[0, 1, 3], [0, 2, 3]]
        self.assertListEqual(output, backtracking.all_paths_source_to_target(graph))
        graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
        output = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
        self.assertListEqual(output, backtracking.all_paths_source_to_target(graph))
        graph = [[1], []]
        output = [[0, 1]]
        self.assertListEqual(output, backtracking.all_paths_source_to_target(graph))
        graph = [[1, 2, 3], [2], [3], []]
        output = [[0, 1, 2, 3], [0, 2, 3], [0, 3]]
        self.assertListEqual(output, backtracking.all_paths_source_to_target(graph))
        graph = [[1, 3], [2], [3], []]
        output = [[0, 1, 2, 3], [0, 3]]
        self.assertListEqual(output, backtracking.all_paths_source_to_target(graph))

    def test_letter_case_permutations(self):
        s = "a1b2"
        output = ["a1b2", "a1B2", "A1b2", "A1B2"]
        self.assertCountEqual(output, backtracking.letter_case_permutations(s))
        s = "3z4"
        output = ["3z4", "3Z4"]
        self.assertCountEqual(output, backtracking.letter_case_permutations(s))
        s = "12345"
        output = ["12345"]
        self.assertCountEqual(output, backtracking.letter_case_permutations(s))
        s = "0"
        output = ["0"]
        self.assertCountEqual(output, backtracking.letter_case_permutations(s))

    def test_subsets(self):
        nums = [1, 2, 3]
        output = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertCountEqual(output, backtracking.subsets(nums))
        nums = [0]
        output = [[], [0]]
        self.assertCountEqual(output, backtracking.subsets(nums))

    def test_combination_iterator(self):
        combination_iterator = backtracking_two.CombinationIterator("abc", 2)
        self.assertEqual("ab", combination_iterator.next())
        self.assertEqual(True, combination_iterator.hasNext())
        self.assertEqual("ac", combination_iterator.next())
        self.assertEqual(True, combination_iterator.hasNext())
        self.assertEqual("bc", combination_iterator.next())
        self.assertEqual(False, combination_iterator.hasNext())

    def test_combination_sum(self):
        candidates = [2, 3, 6, 7]
        target = 7
        output = [[2, 2, 3], [7]]
        self.assertListEqual(output, backtracking.combination_sum(candidates, target))

    def test_find_words(self):
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"]
        ]
        words = ["oath", "pea", "eat", "rain"]
        output = ["eat", "oath"]
        self.assertCountEqual(output, backtracking.find_Words(board, words))
        board = [["a", "b"], ["c", "d"]]
        words = ["abcb"]
        output = []
        self.assertCountEqual(output, backtracking.find_Words(board, words))

    def test_combination_sum_three(self):
        k = 3
        n = 9
        output = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        self.assertListEqual(output, backtracking.combination_sum_3(k, n))
        k = 3
        n = 7
        output = [[1, 2, 4]]
        self.assertListEqual(output, backtracking.combination_sum_3(k, n))

    def test_combine(self):
        n = 4
        k = 2
        output = [
            [2, 4],
            [3, 4],
            [2, 3],
            [1, 2],
            [1, 3],
            [1, 4],
        ]
        self.assertCountEqual(output, backtracking.combine(n, k))
        n = 1
        k = 1
        output = [
            [1]
        ]
        self.assertCountEqual(output, backtracking.combine(n, k))

    def test_beautiful_arrangments(self):
        n = 2
        output = 2
        self.assertEqual(output, backtracking.countArrangement(n))
        n = 7
        output = 41
        self.assertEqual(output, backtracking.countArrangement(n))


if __name__ == '__main__':
    unittest.main()
