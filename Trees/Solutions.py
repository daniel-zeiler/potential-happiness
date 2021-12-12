import collections
from typing import List, Optional

import binarytree
from binarytree import Node


def count_good_nodes_in_binary_tree(root: Node):
    def passdown(max_so_far, node):
        good_nodes = 0
        if node:
            if node.value >= max_so_far:
                good_nodes += 1
            max_so_far = max(max_so_far, node.value)
            good_nodes += (passdown(max_so_far, node.left) + passdown(max_so_far, node.right))
        return good_nodes

    return passdown(float('-inf'), root)


def time_needed_inform_all_employees(n, head_id, manager, inform_time):
    relationship_map = collections.defaultdict(list)
    for index, manager_index in enumerate(manager):
        relationship_map[manager_index].append(index)

    def find_max_time(index):
        max_inform_time = 0
        for subordinate in relationship_map[index]:
            max_inform_time = max(find_max_time(subordinate), max_inform_time)
        return max_inform_time + inform_time[index]

    return find_max_time(head_id)


def delete_leaves_given_value(root: binarytree.Node, target: int):
    if root:
        root.left = delete_leaves_given_value(root.left, target)
        root.right = delete_leaves_given_value(root.right, target)
        if root.value == target and root.left is None and root.right is None:
            return None
        return root


def validate_binary_nodes(n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    node_set = set(val for val in range(0, n))
    queue = collections.deque([0])
    while queue:
        node = queue.popleft()
        if node not in node_set:
            return False
        node_set.remove(node)
        if leftChild[node] != -1:
            queue.append(leftChild[node])
        if rightChild[node] != -1:
            queue.append(rightChild[node])
    return len(node_set) == 0


def deepest_leaves_sum(root: Optional[Node]) -> int:
    def traverse(node, level):
        if node:
            if not node.left and not node.right:
                return level, node.value
            elif not node.left:
                return traverse(node.left, level + 1)
            elif not node.right:
                traverse(node.right, level + 1)
            else:
                left_deepest_level, sum_left = traverse(node.left, level + 1)
                right_deepest_level, sum_right = traverse(node.right, level + 1)

                if left_deepest_level == right_deepest_level:
                    return left_deepest_level, sum_left + sum_right
                elif left_deepest_level > right_deepest_level:
                    return left_deepest_level, sum_left
                else:
                    return right_deepest_level, sum_right

    return traverse(root, 0)


def sum_even_grandparents(root):
    def traverse(node, parent, grandparent):
        value = 0
        if node:
            if grandparent:
                value += node.value
            value += traverse(node.left, node.value % 2 == 0, parent)
            value += traverse(node.right, node.value % 2 == 0, parent)
        return value

    return traverse(root, False, False)


def lca_deepest_leaves(root: Optional[Node]) -> Optional[Node]:
    def traverse(node, level):
        if node:
            if not node.left and not node.right:
                return node, level
            left_lca, left_level = traverse(node.left, level + 1)
            right_lca, right_level = traverse(node.right, level + 1)

            if left_lca and not right_lca:
                return left_lca, left_level
            if right_lca and not left_lca:
                return right_lca, right_level
            if left_level == right_level:
                return node, left_level
            elif left_level > right_level:
                return left_lca, left_level
            else:
                return right_lca, right_level
        else:
            return None, None

    return traverse(root, 0)[0]


def max_level_sum(root: Optional[Node]) -> int:
    levels = []
    queue = collections.deque([[root, 1]])

    current_max_level = 0
    current_max = float('-inf')

    while queue:
        node, level = queue.popleft()
        if level > len(levels):
            levels.append(node.value)
        else:
            levels[level - 1] += node.value

        if node.left:
            queue.append([node.left, level + 1])
        if node.right:
            queue.append([node.right, level + 1])

    for i, level in enumerate(levels):
        if level > current_max:
            current_max = level
            current_max_level = i + 1

    return current_max_level


def max_ancestor_diff(root: Optional[Node]) -> int:
    def traverse(root, maximum, minimum):
        values = [abs(root.val - maximum), abs(root.val - minimum)]
        new_max = max(maximum, root.val)
        new_min = min(minimum, root.val)
        if root.left:
            values.append(traverse(root.left, new_max, new_min))
        if root.right:
            values.append(traverse(root.right, new_max, new_min))
        return max(values)

    return traverse(root, root.val, root.val)


def is_cousins(root: Optional[Node], x: int, y: int) -> bool:
    def traverse(root, level):
        if root:
            if root.left and root.left.val in [x, y] and root.right and root.right.val in [x, y]:
                return False, level

            if root.val in [x, y]:
                return True, level

            left_val, left_level = traverse(root.left, level + 1)
            right_val, right_level = traverse(root.right, level + 1)

            if left_val and right_val:
                if left_level == right_level:
                    return True, right_level
                return False, right_level

            if left_val:
                return left_val, left_level

            return right_val, right_level
        return False, level

    return traverse(root, 0)[0]


def is_unival_tree(root: Optional[Node]) -> bool:
    def traverse(root, val):
        if root:
            if root.val != val:
                return False
            return traverse(root.left, val) and traverse(root.right, val)
        return True

    return traverse(root, root.val)


def flip_equiv(root1: Optional[Node], root2: Optional[Node]) -> bool:
    def traverse(root1, root2):
        if (not root1 and root2) or (root1 and not root2):
            return False
        elif not root1 and not root2:
            return True
        elif root1.val != root2.val:
            return False
        else:
            return (traverse(root1.left, root2.left) and traverse(root1.right, root2.right)) or (
                    traverse(root1.left, root2.right) and traverse(root1.right, root2.left))

    return traverse(root1, root2)


def range_sum_bst(root: Optional[Node], low: int, high: int) -> int:
    sum = 0
    if root:
        sum += range_sum_bst(root.left, low, high)
        sum += range_sum_bst(root.right, low, high)
        if low <= root.val <= high:
            sum += root.val
    return sum


def leaf_similar(root1: Optional[Node], root2: Optional[Node]) -> bool:
    def get_leaf_sequence(root):
        sequence = []
        if root:
            if root.left is None and root.right is None:
                sequence.append(root.val)
            sequence.extend(get_leaf_sequence(root.left))
            sequence.extend(get_leaf_sequence(root.right))
        return sequence

    leaf_sequence_one = get_leaf_sequence(root1)
    leaf_sequence_two = get_leaf_sequence(root2)
    for leaf_one, leaf_two in zip(leaf_sequence_one, leaf_sequence_two):
        if leaf_one != leaf_two:
            return False
    return True


def distance_k(root: Node, target: Node, k: int) -> List[int]:
    result = []

    def traverse(root) -> (bool, int):
        if root:
            if root.val == target.val:
                pass_down(root.left, k - 1)
                pass_down(root.right, k - 1)
                return True, k - 1
            else:
                on_left, distance_left = traverse(root.left)
                on_right, distance_right = traverse(root.right)
                if on_left and distance_left == 0 or on_right and distance_right == 0:
                    result.append(root.val)
                elif on_left:
                    pass_down(root.right, distance_left - 1)
                    return on_left, distance_left - 1
                elif on_right:
                    pass_down(root.left, distance_right - 1)
                    return on_right, distance_right - 1
        return False, -1

    def pass_down(root, k):
        if root:
            if k == 0:
                result.append(root.val)
            else:
                pass_down(root.left, k - 1)
                pass_down(root.right, k - 1)

    traverse(root)
    return result
