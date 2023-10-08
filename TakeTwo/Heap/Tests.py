import unittest
import TakeOne.Heap.Solutions as heap_problems


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

    def test_number_of_cabs(self):
        n = 10
        cabTravelTime = [1, 3, 5, 7, 8]
        output = 7
        self.assertEqual(output, heap_problems.number_of_cabs(n, cabTravelTime))
        n = 3
        cabTravelTime = [3, 4, 8]
        output = 6
        self.assertEqual(output, heap_problems.number_of_cabs(n, cabTravelTime))


if __name__ == '__main__':
    unittest.main()
