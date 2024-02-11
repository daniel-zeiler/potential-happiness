import unittest
import TakeOne.Heap.Solutions as heap_problems

from TakeTwo.Heap.Problems import Interval


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

    def test_employee_free_time(self):
        schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
        input = [[Interval(*x) for x in y] for y in schedule]
        output = [Interval(*x) for x in [[3, 4]]]
        self.assert_compare_Intervals(output, heap_problems2.employeeFreeTime(input))

        schedule = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
        input = [[Interval(*x) for x in y] for y in schedule]
        output = [Interval(*x) for x in [[5, 6], [7, 9]]]
        self.assert_compare_Intervals(output, heap_problems2.employeeFreeTime(input))

        schedule = [[[7, 24], [29, 33], [45, 57], [66, 69], [94, 99]],
                    [[6, 24], [43, 49], [56, 59], [61, 75], [80, 81]],
                    [[5, 16], [18, 26], [33, 36], [39, 57], [65, 74]],
                    [[9, 16], [27, 35], [40, 55], [68, 71], [78, 81]],
                    [[0, 25], [29, 31], [40, 47], [57, 87], [91, 94]]]
        input = [[Interval(*x) for x in y] for y in schedule]
        output = [Interval(*x) for x in [[26, 27], [36, 39], [87, 91]]]
        self.assert_compare_Intervals(output, heap_problems2.employeeFreeTime(input))


if __name__ == '__main__':
    unittest.main()
