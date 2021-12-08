import binarytree
import unittest
import Trees.Solutions as trees


class CustomAssertion:
    def assert_compare_trees(self, node_1: binarytree.Node, node_2: binarytree.Node):
        if node_1 and node_2:
            if node_1.value == node_2.value:
                self.assert_compare_trees(node_1.left, node_2.left)
                self.assert_compare_trees(node_1.right, node_2.right)
            else:
                raise AssertionError('Trees are not Equal')
        elif node_1 and not node_2 or node_2 and not node_1:
            raise AssertionError('Trees are not Equal')


class SolutionsTest(unittest.TestCase, CustomAssertion):

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

    def test_delete_leaves_given_value(self):
        root = binarytree.build2([1, 2, 3, 2, None, 2, 4])
        target = 2
        output = binarytree.build2([1, None, 3, None, 4])
        self.assert_compare_trees(trees.delete_leaves_given_value(root, target), output)
        root = binarytree.build2([1, 3, 3, 3, 2])
        target = 3
        output = binarytree.build2([1, 3, None, None, 2])
        self.assert_compare_trees(trees.delete_leaves_given_value(root, target), output)
        root = binarytree.build2([1, 1, 1])
        target = 1
        output = binarytree.build2([])
        self.assert_compare_trees(trees.delete_leaves_given_value(root, target), output)
        root = binarytree.build2([1, 2, 3])
        target = 1
        output = binarytree.build([1, 2, 3])
        self.assert_compare_trees(trees.delete_leaves_given_value(root, target), output)

    def test_validate_binary_nodes(self):
        n = 4
        leftChild = [1, -1, 3, -1]
        rightChild = [2, -1, -1, -1]
        output = True
        self.assertEqual(trees.validate_binary_nodes(n, leftChild, rightChild), output)
        n = 4
        leftChild = [1, -1, 3, -1]
        rightChild = [2, 3, -1, -1]
        output = False
        self.assertEqual(trees.validate_binary_nodes(n, leftChild, rightChild), output)
        n = 2
        leftChild = [1, 0]
        rightChild = [-1, -1]
        output = False
        self.assertEqual(trees.validate_binary_nodes(n, leftChild, rightChild), output)
        n = 6
        leftChild = [1, -1, -1, 4, -1, -1]
        rightChild = [2, -1, -1, 5, -1, -1]
        output = False
        self.assertEqual(trees.validate_binary_nodes(n, leftChild, rightChild), output)

    # def test_deepest_leaves_sum(self):
    #     self.assertEqual(
    #         trees.deepest_leaves_sum(binarytree.build2([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])), 15)
    #     self.assertEqual(
    #         trees.deepest_leaves_sum(binarytree.build2([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])), 19)

    def test_sum_even_grandparents(self):
        root = binarytree.build2([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])
        self.assertEqual(trees.sum_even_grandparents(root), 18)

    def test_lca_deepest_leaves(self):
        input = binarytree.build2([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        output = binarytree.build2([2, 7, 4])
        self.assert_compare_trees(trees.lca_deepest_leaves(input), output)
        input = binarytree.build2([1])
        output = binarytree.build2([1])
        self.assert_compare_trees(trees.lca_deepest_leaves(input), output)
        input = binarytree.build2([0, 1, 3, None, 2])
        output = binarytree.build2([2])
        self.assert_compare_trees(trees.lca_deepest_leaves(input), output)

    def test_max_level_sum(self):
        root = binarytree.build2([1, 7, 0, 7, -8, None, None])
        output = 2
        self.assertEqual(trees.max_level_sum(root), output)
        root = binarytree.build2([989, None, 10250, 98693, -89388, None, None, None, -32127])
        output = 2
        self.assertEqual(trees.max_level_sum(root), output)


if __name__ == '__main__':
    unittest.main()
