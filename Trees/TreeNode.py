from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_tree_postorder_list(traversal: deque[int]):
    def build():
        if traversal:
            left = build()
            right = build()
            value = traversal.popleft()
            if value:
                node = TreeNode(value, left, right)
                return node

    root = build()
    return root


def build_tree_inorder_list(traversal: deque[int]):
    def build():
        if traversal:
            left = build()
            value = traversal.popleft()
            right = build()
            if value:
                node = TreeNode(value, left, right)
                return node

    root = build()
    return root


def build_tree_preorder_list(traversal: deque[int]):
    def build():
        if traversal:
            value = traversal.popleft()
            if value:
                node = TreeNode(value, build(), build())
                return node

    root = build()
    return root


def inorder_traversal(root: TreeNode) -> list[int]:
    traversal = []
    if root:
        traversal.extend(inorder_traversal(root.left))
        traversal.append(root.value)
        traversal.extend(inorder_traversal(root.right))
    return traversal


def postorder_traversal(root: TreeNode) -> list[int]:
    traversal = []
    if root:
        traversal.extend(postorder_traversal(root.left))
        traversal.extend(postorder_traversal(root.right))
        traversal.append(root.value)
    return traversal


def preorder_traversal(root: TreeNode) -> list[int]:
    traversal = []
    if root:
        traversal.append(root.value)
        traversal.extend(preorder_traversal(root.left))
        traversal.extend(preorder_traversal(root.right))
    return traversal
