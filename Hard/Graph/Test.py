import unittest
from typing import List

import Hard.Graph.Solution as graph


class SolutionsTest(unittest.TestCase):

    def test_find_islands(self):
        m = 3
        n = 3
        positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
        output = [1, 1, 2, 3]
        self.assertEqual(output, graph.numIslands2(m, n, positions))
        m = 1
        n = 1
        positions = [[0, 0]]
        output = [1]
        self.assertEqual(output, graph.numIslands2(m, n, positions))

        m = 3
        n = 3
        positions = [[0, 0], [0, 1], [1, 2], [1, 2]]
        output = [1, 1, 2, 2]
        self.assertEqual(output, graph.numIslands2(m, n, positions))

        m = 3
        n = 3
        positions = [[0, 1], [1, 2], [2, 1], [1, 0], [0, 2], [0, 0], [1, 1]]
        output = [1, 2, 3, 4, 3, 2, 1]
        self.assertEqual(output, graph.numIslands2(m, n, positions))


if __name__ == '__main__':
    unittest.main()
