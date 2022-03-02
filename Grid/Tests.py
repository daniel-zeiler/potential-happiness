import Grid.Solutions as grid

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
