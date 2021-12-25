import binarytree
import unittest
import Trees.Solutions as trees
from binarytree import Node


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
    #         trees.deepest_leaves_sum(binarytree.build2([1, 2, 3, 4, 5, None, 6, 7, None, None,
    #         None, None, 8])), 15)
    #     self.assertEqual(
    #         trees.deepest_leaves_sum(binarytree.build2([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None,
    #         None, None, 5])), 19)

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

    def test_max_ancestor_diff(self):
        root = binarytree.build2([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])
        output = 7
        self.assertEqual(trees.max_ancestor_diff(root), output)
        root = binarytree.build2([1, None, 2, None, 0, 3])
        output = 3
        self.assertEqual(trees.max_ancestor_diff(root), output)

    def test_is_cousins(self):
        root = binarytree.build2([1, 2, 3, 4])
        x = 4
        y = 3
        output = False
        self.assertEqual(trees.is_cousins(root, x, y), output)
        root = binarytree.build2([1, 2, 3, None, 4, None, 5])
        x = 5
        y = 4
        output = True
        self.assertEqual(trees.is_cousins(root, x, y), output)
        root = binarytree.build2([1, 2, 3, None, 4])
        x = 2
        y = 3
        output = False
        self.assertEqual(trees.is_cousins(root, x, y), output)

    def test_unival_tree(self):
        root = binarytree.build2([1, 1, 1, 1, 1, None, 1])
        output = True
        self.assertEqual(trees.is_unival_tree(root), output)
        root = binarytree.build2([2, 2, 2, 5, 2])
        output = False
        self.assertEqual(trees.is_unival_tree(root), output)

    def test_flip_equiv(self):
        root1 = binarytree.build2([1, 2, 3, 4, 5, 6, None, None, None, 7, 8])
        root2 = binarytree.build2([1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7])
        output = True
        self.assertEqual(trees.flip_equiv(root1, root2), output)
        root1 = binarytree.build2([])
        root2 = binarytree.build2([])
        output = True
        self.assertEqual(trees.flip_equiv(root1, root2), output)
        root1 = binarytree.build2([])
        root2 = binarytree.build2([1])
        output = False
        self.assertEqual(trees.flip_equiv(root1, root2), output)
        root1 = binarytree.build2([0, None, 1])
        root2 = binarytree.build2([])
        output = False
        self.assertEqual(trees.flip_equiv(root1, root2), output)
        root1 = binarytree.build2([0, None, 1])
        root2 = binarytree.build2([0, 1])
        output = True
        self.assertEqual(trees.flip_equiv(root1, root2), output)

    def test_range_sum_bst(self):
        root = binarytree.build2([10, 5, 15, 3, 7, None, 18])
        low = 7
        high = 15
        output = 32
        self.assertEqual(output, trees.range_sum_bst(root, low, high))
        root = binarytree.build2([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        low = 6
        high = 10
        output = 23
        self.assertEqual(output, trees.range_sum_bst(root, low, high))

    def test_leaf_similar(self):
        root1 = binarytree.build2([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
        root2 = binarytree.build2([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
        output = True
        self.assertEqual(output, trees.leaf_similar(root1, root2))
        root1 = binarytree.build2([1])
        root2 = binarytree.build2([1])
        output = True
        self.assertEqual(output, trees.leaf_similar(root1, root2))
        root1 = binarytree.build2([1])
        root2 = binarytree.build2([2])
        output = False
        self.assertEqual(output, trees.leaf_similar(root1, root2))
        root1 = binarytree.build2([1, 2])
        root2 = binarytree.build2([2, 2])
        output = True
        self.assertEqual(output, trees.leaf_similar(root1, root2))
        root1 = binarytree.build2([1, 2, 3])
        root2 = binarytree.build2([1, 3, 2])
        output = False
        self.assertEqual(output, trees.leaf_similar(root1, root2))

    def test_distance_k(self):
        root = binarytree.build2([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        target = Node(5)
        k = 2
        output = [7, 4, 1]
        self.assertListEqual(output, trees.distance_k(root, target, k))
        root = binarytree.build2([1])
        target = Node(1)
        k = 3
        output = []
        self.assertListEqual(output, trees.distance_k(root, target, k))

    def test_prune_tree(self):
        root = binarytree.build2([1, None, 0, 0, 1])
        output = binarytree.build2([1, None, 0, None, 1])
        self.assert_compare_trees(output, trees.pruneTree(root))
        root = binarytree.build2([1, 0, 1, 0, 0, 0, 1])
        output = binarytree.build2([1, None, 1, None, 1])
        self.assert_compare_trees(output, trees.pruneTree(root))
        root = binarytree.build2([1, 1, 0, 1, 1, 0, 1, 0])
        output = binarytree.build2([1, 1, 0, 1, 1, None, 1])
        self.assert_compare_trees(output, trees.pruneTree(root))

    def test_min_diff_bst(self):
        root = binarytree.build2([4, 2, 6, 1, 3])
        output = 1
        self.assertEqual(output, trees.minDiffInBST(root))
        root = binarytree.build2([1, 0, 48, None, None, 12, 49])
        output = 1
        self.assertEqual(output, trees.minDiffInBST(root))

    def test_insert_into_bst(self):
        root = binarytree.build2([4, 2, 7, 1, 3])
        val = 5
        output = binarytree.build2([4, 2, 7, 1, 3, 5])
        self.assert_compare_trees(output, trees.insertIntoBST(root, val))
        root = binarytree.build2([40, 20, 60, 10, 30, 50, 70])
        val = 25
        output = binarytree.build2([40, 20, 60, 10, 30, 50, 70, None, None, 25])
        self.assert_compare_trees(output, trees.insertIntoBST(root, val))
        root = binarytree.build2([4, 2, 7, 1, 3, None, None, None, None, None, None])
        val = 5
        output = binarytree.build2([4, 2, 7, 1, 3, 5])
        self.assert_compare_trees(output, trees.insertIntoBST(root, val))

    def test_search_bst(self):
        root = binarytree.build2([4, 2, 7, 1, 3])
        val = 2
        output = binarytree.build2([2, 1, 3])
        self.assert_compare_trees(output, trees.searchBST(root, val))
        root = binarytree.build2([4, 2, 7, 1, 3])
        val = 5
        output = binarytree.build2([])
        self.assert_compare_trees(output, trees.searchBST(root, val))

    def test_second_minimum_value(self):
        root = binarytree.build2([2, 2, 5, None, None, 5, 7])
        output = 5
        self.assertEqual(output, trees.findSecondMinimumValue(root))
        root = binarytree.build2([2, 2, 2])
        output = -1
        self.assertEqual(output, trees.findSecondMinimumValue(root))

    def test_trim_binary_search_tree(self):
        root = binarytree.build2([1, 0, 2])
        low = 1
        high = 2
        output = binarytree.build2([1, None, 2])
        self.assert_compare_trees(output, trees.trimBST(root, low, high))
        root = binarytree.build2([3, 0, 4, None, 2, None, None, 1])
        low = 1
        high = 3
        output = binarytree.build2([3, 2, None, 1])
        self.assert_compare_trees(output, trees.trimBST(root, low, high))
        root = binarytree.build2([1])
        low = 1
        high = 2
        output = binarytree.build2([1])
        self.assert_compare_trees(output, trees.trimBST(root, low, high))
        root = binarytree.build2([1, None, 2])
        low = 1
        high = 3
        output = binarytree.build2([1, None, 2])
        self.assert_compare_trees(output, trees.trimBST(root, low, high))
        root = binarytree.build2([1, None, 2])
        low = 2
        high = 4
        output = binarytree.build2([2])
        self.assert_compare_trees(output, trees.trimBST(root, low, high))

    def test_construct_maximum_binary_tree(self):
        nums = [3, 2, 1, 6, 0, 5]
        output = binarytree.build2([6, 3, 5, None, 2, 0, None, None, 1])
        self.assert_compare_trees(output, trees.constructMaximumBinaryTree(nums))
        nums = [3, 2, 1]
        output = binarytree.build2([3, None, 2, None, 1])
        self.assert_compare_trees(output, trees.constructMaximumBinaryTree(nums))

    def test_find_target(self):
        root = binarytree.build2([5, 3, 6, 2, 4, None, 7])
        k = 9
        output = True
        self.assertEqual(output, trees.findTarget(root, k))
        root = binarytree.build2([5, 3, 6, 2, 4, None, 7])
        k = 28
        output = False
        self.assertEqual(output, trees.findTarget(root, k))
        root = binarytree.build2([2, 1, 3])
        k = 4
        output = True
        self.assertEqual(output, trees.findTarget(root, k))
        root = binarytree.build2([2, 1, 3])
        k = 1
        output = False
        self.assertEqual(output, trees.findTarget(root, k))
        root = binarytree.build2([2, 1, 3])
        k = 3
        output = True
        self.assertEqual(output, trees.findTarget(root, k))

    def test_average_levels(self):
        root = binarytree.build2([3, 9, 20, None, None, 15, 7])
        output = [3, 14.5, 11]
        self.assertEqual(output, trees.averageOfLevels(root))
        root = binarytree.build2([3, 9, 20, 15, 7])
        output = [3, 14.5, 11]
        self.assertEqual(output, trees.averageOfLevels(root))

    def test_merge_trees(self):
        root1 = binarytree.build2([1, 3, 2, 5])
        root2 = binarytree.build2([2, 1, 3, None, 4, None, 7])
        output = binarytree.build2([3, 4, 5, 5, 4, None, 7])
        self.assert_compare_trees(output, trees.mergeTrees(root1, root2))
        root1 = binarytree.build2([1])
        root2 = binarytree.build2([1, 2])
        output = binarytree.build2([2, 2])
        self.assert_compare_trees(output, trees.mergeTrees(root1, root2))

    def test_tree_to_str(self):
        input = binarytree.build2([1, 2, 3, 4])
        output = "1(2(4))(3)"
        self.assertEqual(output, trees.tree2str(input))
        input = binarytree.build2([1, 2, 3, None, 4])
        output = "1(2()(4))(3)"
        self.assertEqual(output, trees.tree2str(input))

    def test_diameter_of_binary_tree(self):
        root = binarytree.build2([1, 2, 3, 4, 5])
        output = 3
        self.assertEqual(output, trees.diameterOfBinaryTree(root))
        root = binarytree.build2([1, 2])
        output = 1
        self.assertEqual(output, trees.diameterOfBinaryTree(root))

    def test_convert_bst(self):
        root = binarytree.build2([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
        output = binarytree.build2([30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8])
        self.assert_compare_trees(output, trees.convertBST(root))
        root = binarytree.build2([0, None, 1])
        output = binarytree.build2([1, None, 1])
        self.assert_compare_trees(output, trees.convertBST(root))
        root = binarytree.build2([1, 0, 2])
        output = binarytree.build2([3, 3, 2])
        self.assert_compare_trees(output, trees.convertBST(root))
        root = binarytree.build2([3, 2, 4, 1])
        output = binarytree.build2([7, 9, 4, 10])
        self.assert_compare_trees(output, trees.convertBST(root))

    def test_get_minimum_difference(self):
        root = binarytree.build2([4, 2, 6, 1, 3])
        output = 1
        self.assertEqual(output, trees.getMinimumDifference(root))
        root = binarytree.build2([1, 0, 48, None, None, 12, 49])
        output = 1
        self.assertEqual(output, trees.getMinimumDifference(root))

    def test_searialize_desearlize(self):
        root = binarytree.build2([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
        output = binarytree.build2([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
        codec = trees.Codec()
        self.assert_compare_trees(output, codec.deserialize(codec.serialize(root)))

    def test_sum_of_left_leaves(self):
        root = binarytree.build2([3, 9, 20, None, None, 15, 7])
        output = 24
        self.assertEqual(output, trees.sumOfLeftLeaves(root))
        root = binarytree.build2([1])
        output = 0
        self.assertEqual(output, trees.sumOfLeftLeaves(root))

    def test_binary_tree_paths(self):
        root = binarytree.build2([1, 2, 3, None, 5])
        output = ["1->2->5", "1->3"]
        self.assertListEqual(output, trees.binaryTreePaths(root))
        root = binarytree.build2([1])
        output = ["1"]
        self.assertListEqual(output, trees.binaryTreePaths(root))

    def test_lowest_common_ancestor(self):
        root = binarytree.build2([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = root.left
        q = root.right
        output = root
        self.assert_compare_trees(output, trees.lowestCommonAncestor(root, p, q))
        root = binarytree.build2([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = root.left
        q = root.left.right.right
        output = root.left
        self.assert_compare_trees(output, trees.lowestCommonAncestor(root, p, q))
        root = binarytree.build2([1, 2])
        p = root
        q = root.left
        output = root
        self.assert_compare_trees(output, trees.lowestCommonAncestor(root, p, q))

    def test_invert_tree(self):
        root = binarytree.build2([4, 2, 7, 1, 3, 6, 9])
        output = binarytree.build2([4, 7, 2, 9, 6, 3, 1])
        self.assert_compare_trees(output, trees.invertTree(root))

    def test_right_side_view(self):
        root = binarytree.build2([1, 2, 3, None, 5, None, 4])
        output = [1, 3, 4]
        self.assertListEqual(output, trees.rightSideView(root))
        root = binarytree.build2([1,None,3])
        output = [1, 3]
        self.assertListEqual(output, trees.rightSideView(root))
        root = binarytree.build2([])
        output = []
        self.assertListEqual(output, trees.rightSideView(root))


if __name__ == '__main__':
    unittest.main()
