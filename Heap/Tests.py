import unittest
import Heap.Solutions as heap_problems


class SolutionsTest(unittest.TestCase):
    def test_find_max_product(self):
        arr = [1, 2, 3, 4, 5]
        output = [-1, -1, 6, 24, 60]
        self.assertListEqual(output, heap_problems.findMaxProduct(arr))

    def test_median_finder(self):
        medianFinder = heap_problems.MedianFinder()
        medianFinder.addNum(1)
        self.assertEqual(1, medianFinder.findMedian())
        medianFinder.addNum(2)
        self.assertEqual(1.5, medianFinder.findMedian())
        medianFinder.addNum(3)
        self.assertEqual(2.0, medianFinder.findMedian())


if __name__ == '__main__':
    unittest.main()
