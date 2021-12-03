import binarytree
import unittest
import Trees.Solutions as trees


class SolutionsTest(unittest.TestCase):

    def test_count_good_nodes_in_binary_tree(self):
        input = binarytree.build([3, 1, 4, 3, None, 1, 5])
        output = 4
        self.assertEqual(trees.count_good_nodes_in_binary_tree(input), output)
        input = binarytree.build([3, 3, None, 4, 2])
        output = 3
        self.assertEqual(trees.count_good_nodes_in_binary_tree(input), output)
        input = binarytree.build([1])
        output = 1
        self.assertEqual(trees.count_good_nodes_in_binary_tree(input), output)

    def test_time_needed_inform_all_employees(self):
        n = 1
        headID = 0
        manager = [-1]
        informTime = [0]
        output = 0
        self.assertEqual(trees.time_needed_inform_all_employees(n, headID, manager, informTime), output)
        n = 6
        headID = 2
        manager = [2, 2, -1, 2, 2, 2]
        informTime = [0, 0, 1, 0, 0, 0]
        output = 1
        self.assertEqual(trees.time_needed_inform_all_employees(n, headID, manager, informTime), output)
        n = 7
        headID = 6
        manager = [1, 2, 3, 4, 5, 6, -1]
        informTime = [0, 6, 5, 4, 3, 2, 1]
        output = 21
        self.assertEqual(trees.time_needed_inform_all_employees(n, headID, manager, informTime), output)
        n = 15
        headID = 0
        manager = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
        informTime = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        output = 3
        self.assertEqual(trees.time_needed_inform_all_employees(n, headID, manager, informTime), output)
        n = 4
        headID = 2
        manager = [3, 3, -1, 2]
        informTime = [0, 0, 162, 914]
        output = 1076
        self.assertEqual(trees.time_needed_inform_all_employees(n, headID, manager, informTime), output)


if __name__ == '__main__':
    unittest.main()
