import unittest
import TakeTwo.Algorithms.Solutions as algorithms


class SolutionsTest(unittest.TestCase):
    def test_birdirecitonal_bfs(self):
        edges = [[0, 1], [1, 5], [1, 4], [1, 2], [2, 3], [3, 6], [6, 7]]
        start = 0
        end = 7
        result = 5
        self.assertEqual(result, algorithms.bidirectional_bfs(edges, start, end))
        edges = [[0, 1], [1, 5], [1, 4], [1, 2], [2, 3], [3, 6], [6, 7]]
        start = 0
        end = 6
        result = 4
        self.assertEqual(result, algorithms.bidirectional_bfs(edges, start, end))
        edges = [[0, 1], [1, 5], [1, 4], [1, 2], [2, 3], [3, 6]]
        start = 0
        end = 7
        result = -1
        self.assertEqual(result, algorithms.bidirectional_bfs(edges, start, end))

    def test_binary_search(self):
        target = 20
        input = [1, 3, 5, 8, 11, 20]
        result = 5
        self.assertEqual(result, algorithms.binary_search(input, target))
        target = 1
        input = [1, 3, 5, 8, 11, 20]
        result = 0
        self.assertEqual(result, algorithms.binary_search(input, target))
        target = 11
        input = [1, 3, 5, 8, 11, 20]
        result = 4
        self.assertEqual(result, algorithms.binary_search(input, target))
        target = -11
        input = [1, 3, 5, 8, 11, 20]
        result = -1
        self.assertEqual(result, algorithms.binary_search(input, target))
        target = 15
        input = [1, 3, 5, 8, 11, 20]
        result = -1
        self.assertEqual(result, algorithms.binary_search(input, target))

    def test_merge_sort(self):
        input = [10, -11, 4, 5, 3, 3, 1]
        result = [-11, 1, 3, 3, 4, 5, 10]
        self.assertListEqual(result, algorithms.merge_sort(input))
