import unittest
import Heap.Solutions as heap_problems


class SolutionsTest(unittest.TestCase):
    def test_find_max_product(self):
        arr = [1, 2, 3, 4, 5]
        output = [-1, -1, 6, 24, 60]
        self.assertListEqual(output, heap_problems.findMaxProduct(arr))


if __name__ == '__main__':
    unittest.main()
