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

    def test_distance_bust(self):
        routes = [[1, 2, 7], [3, 6, 7]]
        source = 1
        target = 6
        self.assertEqual(2, graph.numBusesToDestination(routes, source, target))
        routes = [[1, 7], [3, 5]]
        source = 5
        target = 5
        output = 0
        self.assertEqual(output, graph.numBusesToDestination(routes, source, target))
        routes = [[2], [2, 8]]
        source = 8
        target = 2
        output = 1
        self.assertEqual(output, graph.numBusesToDestination(routes, source, target))
        routes = [[17, 19, 22, 25, 26, 49, 59], [2, 6, 30], [8, 15, 16, 26, 41, 49, 50, 55, 58, 59, 64],
                  [7, 11, 17, 21, 26, 31, 35, 43], [8, 11, 15, 29], [17, 19, 21, 23, 24, 26, 33, 43, 46, 47, 64],
                  [7, 11, 22, 32, 34, 45, 47, 48, 55, 63], [1, 7, 14, 26, 37, 40, 45, 49, 52, 58, 63], [13, 37, 43, 62],
                  [12, 40], [2, 4, 21, 24, 32, 39, 43, 44, 48, 50, 52, 56], [19, 21, 24, 30, 32, 35, 37, 56, 60],
                  [8, 10, 16, 18, 29, 33, 37, 42, 62, 63]]
        source = 17
        target = 60
        output = 2
        self.assertEqual(output, graph.numBusesToDestination(routes, source, target))


if __name__ == '__main__':
    unittest.main()
