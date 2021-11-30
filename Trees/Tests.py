import unittest
from collections import deque
import Solutions

from binarytree import Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)


class SolutionsTest(unittest.TestCase):
    def test_lowest_common_ancestor(self):
        return


if __name__ == '__main__':
    unittest.main()
