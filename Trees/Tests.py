import unittest
import TreeNode
from collections import deque
import Solutions

#    1
#   /  \
#   2   3
#  /  \ /
# 4   5 6
preorder_list = [1, 2, 4, None, None, 5, None, None, 3, 6, None, None, None]
tree_node_preorder = TreeNode.build_tree_preorder_list(deque(preorder_list))

inorder_traversal = [4, 2, 5, 1, 6, 3]
preorder_traversal = [1, 2, 4, 5, 3, 6]
postorder_traversal = [4, 5, 2, 6, 3, 1]


class TreeNodeTest(unittest.TestCase):
    def test_build_tree_preorder_list(self):
        self.assertListEqual(TreeNode.preorder_traversal(tree_node_preorder), preorder_traversal)

    def test_build_tree_postorder_list(self):
        self.assertListEqual(TreeNode.postorder_traversal(tree_node_preorder), postorder_traversal)

    def test_build_tree_inorder_list(self):
        self.assertListEqual(TreeNode.inorder_traversal(tree_node_preorder), inorder_traversal)


class SolutionsTest(unittest.TestCase):
    def test_lowest_common_ancestor(self):
        self.assertEqual(Solutions.lowest_common_ancestors(tree_node_preorder, 5, 4), 2)
        self.assertEqual(Solutions.lowest_common_ancestors(tree_node_preorder, 4, 6), 1)
        self.assertEqual(Solutions.lowest_common_ancestors(tree_node_preorder, 1, 4), 1)


if __name__ == '__main__':
    unittest.main()
