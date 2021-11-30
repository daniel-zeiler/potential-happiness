import TreeNode

"""
Return the lowest common ancestor of two given values in the tree.
"""


def lowest_common_ancestors(root: TreeNode, value_one: any, value_two: any) -> any:
    if root:
        if root.value == value_one or root.value == value_two:
            return root.value
        left_lca = lowest_common_ancestors(root.left, value_one, value_two)
        right_lca = lowest_common_ancestors(root.right, value_one, value_two)
        if left_lca and right_lca:
            return root.value
        return left_lca or right_lca
