import collections
import heapq
from typing import List, Optional, Any

import binarytree
from binarytree import Node


def count_good_nodes_in_binary_tree(root):
    def traverse(node, maximum):
        count = 0
        if node:
            if node.value >= maximum:
                count += 1
            count += traverse(node.left, max(maximum, node.value)) + traverse(node.right, max(maximum, node.value))
        return count

    return traverse(root, float('-inf'))


def time_needed_inform_all_employees(n, head_id, manager, inform_time):
    queue = collections.deque([[0, head_id]])
    max_time = 0
    graph = collections.defaultdict(list)
    for i, m in enumerate(manager):
        graph[m].append(i)

    while queue:
        time, employee_index = queue.popleft()
        max_time = max(max_time, time)
        for subordinate_id in graph[employee_index]:
            queue.append([time + inform_time[employee_index], subordinate_id])

    return max_time


def delete_leaves_given_value(root, target):
    def traverse(node):
        if node:
            node.left, node.right = traverse(node.left), traverse(node.right)
            if not node.left and not node.right and node.value == target:
                return None
            return node

    return traverse(root)


def deepest_leaves_sum(root: Optional[Node]) -> int:
    def traverse(node, level):
        if node:
            if node.left is None and node.right is None:
                return node.value, level
            left_sum, left_level = traverse(node.left, level + 1)
            right_sum, right_level = traverse(node.right, level + 1)
            if left_level == right_level:
                return left_sum + right_sum, right_level
            elif left_level < right_level:
                return right_sum, right_level
            else:
                return left_sum, left_level
        return 0, float('-inf')

    sum, deepest_level = traverse(root, 0)
    return sum


def sumEvenGrandparent(root: Node) -> int:
    def traverse(node, parent, grandparent):
        sum = 0
        if node:
            if grandparent % 2 == 0:
                sum += node.value
            sum += traverse(node.left, node.value, parent)
            sum += traverse(node.right, node.value, parent)
        return sum

    return traverse(root, 1, 1)


def lca_deepest_leaves(root: Optional[Node]) -> Optional[Node]:
    def traverse(node, level):
        if node:
            if node.left is None and node.right is None:
                return node, level
            left_node, left_level = traverse(node.left, level + 1)
            right_node, right_level = traverse(node.right, level + 1)
            if left_level == right_level:
                return node, right_level
            elif left_level > right_level:
                return left_node, left_level
            else:
                return right_node, right_level
        return None, float('-inf')

    lca, lca_level = traverse(root, 0)
    return lca


def del_nodes(root: Node, to_delete: List[int]) -> List[Node]:
    nodes = [root]

    def traverse(node):
        if node:
            if node.value in to_delete:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
                return None
            else:
                node.left = traverse(node.left)
                node.right = traverse(node.right)
        return node

    for node in nodes:
        traverse(node)
    return nodes


def max_level_sum(root: Optional[Node]) -> int:
    level_ordering = []
    queue = collections.deque([[root, 1]])

    while queue:
        node, level = queue.popleft()
        if level - 1 == len(level_ordering):
            level_ordering.append(node.value)
        else:
            level_ordering[level - 1] += node.value

        if node.left:
            queue.append([node.left, level + 1])
        if node.right:
            queue.append([node.right, level + 1])

    result_index = -1
    min_sum = float('-inf')
    for i, value in enumerate(level_ordering):
        if value > min_sum:
            result_index = i + 1
            min_sum = value
    return result_index


def max_ancestor_diff(root: Optional[Node]) -> int:
    def traverse(node, min_ancestor, max_ancestor):
        if node:
            left_max = traverse(node.left, min(min_ancestor, node.value), max(max_ancestor, node.value))
            right_max = traverse(node.right, min(min_ancestor, node.value), max(max_ancestor, node.value))
            return max(left_max, right_max, max(abs(node.value - min_ancestor), abs(node.value - max_ancestor)))
        return 0

    return traverse(root, root.value, root.value)


def is_cousins(root: Optional[Node], x: int, y: int) -> bool:
    def traverse(node, level):
        if node:
            if node.left and node.right:
                if (node.left.value == x and node.right.value == y) or (node.left.value == y and node.right.value == y):
                    return None

            if node.value == x or node.value == y:
                return level

            left_level = traverse(node.left, level + 1)
            right_level = traverse(node.right, level + 1)

            if left_level and right_level and left_level != right_level:
                return None

            return left_level or right_level

    return traverse(root, 0) is not None


def verticalTraversal(root: Optional[Node]) -> List[List[int]]:
    left_half = []
    right_half = []

    def traverse(node, column):
        if node:
            if column >= 0:
                if len(right_half) == column:
                    right_half.append([node.value])
                else:
                    right_half[column].append(node.value)
            else:
                if -len(left_half) - 1 == column:
                    left_half.append([node.value])
                else:
                    left_half[-(column - 1)].append(node.value)
            traverse(node.left, column - 1)
            traverse(node.right, column + 1)

    traverse(root, 0)
    combined = left_half[::-1] + right_half
    return combined


def is_unival_tree(root: Optional[Node]) -> bool:
    def traverse(node, value):
        if node:
            if node.value == value:
                return traverse(node.left, value) and traverse(node.right, value)
            return False
        return True

    if not root:
        return False

    return traverse(root, root.value)


def flip_equiv(root1: Optional[Node], root2: Optional[Node]) -> bool:
    def traverse(node_1, node_2):
        if not node_1 and node_2 or node_1 and not node_2:
            return False
        elif not node_1 and not node_2:
            return True
        elif node_1.value != node_2.value:
            return False
        return traverse(node_1.left, node_2.left) and traverse(node_2.right, node_2.right) or \
               traverse(node_1.left, node_2.right) and traverse(node_1.right, node_2.left)

    return traverse(root1, root2)


def range_sum_bst(root: Optional[Node], low: int, high: int) -> int:
    def traverse(node):
        sum = 0
        if node:
            if low <= node.value <= high:
                sum += node.value
            sum += traverse(node.left) + traverse(node.right)
        return sum

    return traverse(root)


def increasingBST(root: Node) -> Node:
    def traverse(node):
        inorder = []
        if node:
            inorder.extend(traverse(node.left))
            inorder.append(node)
            inorder.extend(traverse(node.right))
        return inorder

    inorder = traverse(root)

    for i, node in enumerate(inorder):
        node.left = None
        if i == len(inorder) - 1:
            node.left = None
        else:
            node.right = inorder[i + 1]

    return inorder[0]


def leaf_similar(root1: Optional[Node], root2: Optional[Node]) -> bool:
    def traverse(node):
        sequence = []
        if node:
            if not node.left and not node.right:
                sequence.append(node.value)
            sequence.extend(traverse(node.left))
            sequence.extend(traverse(node.right))
        return sequence

    leaf_sequence_one = traverse(root1)
    leaf_sequence_two = traverse(root2)

    if len(leaf_sequence_two) != len(leaf_sequence_one):
        return False

    for node_one, node_two in zip(leaf_sequence_one, leaf_sequence_two):
        if node_one != node_two:
            return False
    return True


def distance_k(root: Node, target: Node, k: int) -> List[int]:
    result = []

    def traverse_down(node, distance):
        if node:
            if distance == 0:
                result.append(node.value)
            traverse_down(node.left, distance - 1)
            traverse_down(node.right, distance - 1)

    def traverse(node):
        if node:
            if node.value == target.value:
                traverse_down(node.left, k - 1)
                traverse_down(node.right, k - 1)
                return k - 1
            else:
                left_distance = traverse(node.left)
                right_distance = traverse(node.right)
                if left_distance != -1:
                    traverse_down(node.right, left_distance - 1)
                    return left_distance - 1
                if right_distance != -1:
                    traverse_down(node.left, right_distance - 1)
                    return right_distance - 1
        return -1

    traverse(root)
    return result


def pruneTree(root: Optional[Node]) -> Optional[Node]:
    def traverse(node):
        if node:
            left = traverse(node.left)
            if not left:
                node.left = None
            right = traverse(node.right)
            if not right:
                node.right = None
            if not left and not right and node.value != 1:
                return False
            return True
        return False

    traverse(root)
    return root


def minDiffInBST(root: Optional[Node]) -> int:
    def traverse(node):
        inorder = []
        if node:
            inorder.extend(traverse(node.left))
            inorder.append(node.value)
            inorder.extend(traverse(node.right))
        return inorder

    inorder = traverse(root)
    min_difference = min(abs(value - inorder[i+1]) for i, value in enumerate(inorder[:-1]))
    return min_difference
