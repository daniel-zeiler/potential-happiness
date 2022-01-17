import unittest
from typing import List

import Hard.Heap.Solution as heap_problems
from Hard.Heap.Problems import Interval


class CustomAssertion:
    def assert_compare_Intervals(self, int_one: List[Interval], int_two: List[Interval]):
        for interval_one, interval_two in zip(int_one, int_two):
            if interval_one.start != interval_two.start or interval_one.end != interval_two.end:
                raise AssertionError('Intervals not equal')
        return True


class SolutionsTest(unittest.TestCase, CustomAssertion):

    def test_employee_free_time(self):
        schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
        input = [[Interval(*x) for x in y] for y in schedule]
        output = [Interval(*x) for x in [[3, 4]]]
        self.assert_compare_Intervals(output, heap_problems.employeeFreeTime(input))

        schedule = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
        input = [[Interval(*x) for x in y] for y in schedule]
        output = [Interval(*x) for x in [[5, 6], [7, 9]]]
        self.assert_compare_Intervals(output, heap_problems.employeeFreeTime(input))

        schedule = [[[7, 24], [29, 33], [45, 57], [66, 69], [94, 99]],
                    [[6, 24], [43, 49], [56, 59], [61, 75], [80, 81]],
                    [[5, 16], [18, 26], [33, 36], [39, 57], [65, 74]],
                    [[9, 16], [27, 35], [40, 55], [68, 71], [78, 81]],
                    [[0, 25], [29, 31], [40, 47], [57, 87], [91, 94]]]
        input = [[Interval(*x) for x in y] for y in schedule]
        output = [Interval(*x) for x in [[26, 27], [36, 39], [87, 91]]]
        self.assert_compare_Intervals(output, heap_problems.employeeFreeTime(input))


if __name__ == '__main__':
    unittest.main()
