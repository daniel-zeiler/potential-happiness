import collections
import heapq
import math
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
    min_difference = min(abs(value - inorder[i + 1]) for i, value in enumerate(inorder[:-1]))
    return min_difference


def trimBST(root: Optional[Node], low: int, high: int) -> Optional[Node]:
    def traverse(node):
        if node:
            if node.value < low:
                if node.right:
                    return traverse(node.right)
            elif node.value > high:
                if node.left:
                    return traverse(node.left)
            else:
                node.right = traverse(node.right)
                node.left = traverse(node.left)
                return node

    return traverse(root)


def constructMaximumBinaryTree(nums: List[int]) -> Optional[Node]:
    def get_max_index(numbers):
        max_index = -1
        max_number = float('-inf')
        for i, number in enumerate(numbers):
            if number > max_number:
                max_number, max_index = number, i
        return max_index

    def build(nums_remaining):
        if nums_remaining:
            index = get_max_index(nums_remaining)
            new_node = Node(nums_remaining[index])
            new_node.left = build(nums_remaining[:index])
            new_node.right = build(nums_remaining[index + 1:])
            return new_node

    return build(nums)


def averageOfLevels(root: Optional[Node]) -> List[float]:
    levels = []
    queue = collections.deque([[root, 0]])

    while queue:
        node, level = queue.popleft()
        if len(levels) == level:
            levels.append([node.value])
        else:
            levels[level].append(node.value)
        if node.left:
            queue.append([node.left, level + 1])
        if node.right:
            queue.append([node.right, level + 1])

    return [sum(x) / len(x) for x in levels]


def mergeTrees(root1: Optional[Node], root2: Optional[Node]) -> Optional[Node]:
    def merge(node1, node2):
        if not node1 and not node2:
            return None
        elif not node1 and node2:
            return node2
        elif node1 and not node2:
            return node1
        else:
            node1.value += node2.value
            node1.left = merge(node1.left, node2.left)
            node1.right = merge(node1.right, node2.right)
            return node1

    return merge(root1, root2)


def tree2str(root: Optional[Node]) -> str:
    def builder(node):
        result = ""
        if node:
            result += str(node.value)
            if not node.left and node.right:
                result += "()(" + builder(node.right) + ")"
            elif node.left and not node.right:
                result += "(" + builder(node.left) + ")"
            elif node.left and node.right:
                result += "(" + builder(node.left) + ")(" + builder(node.right) + ")"
        return result

    return builder(root)


def diameterOfBinaryTree(root: Optional[Node]) -> int:
    max_diameter = 0

    def traverse(node):
        nonlocal max_diameter
        if not node:
            return 0
        left_traverse = traverse(node.left)
        right_traverse = traverse(node.right)
        max_diameter = max(max_diameter, left_traverse + right_traverse, left_traverse, right_traverse)
        return max(left_traverse, right_traverse) + 1

    traverse(root)
    return max_diameter


def convertBST(root: Optional[Node]) -> Optional[Node]:
    def traverse(node, sum_so_far):
        if node:
            right_sum = traverse(node.right, sum_so_far)
            node.value += right_sum
            left_sum = traverse(node.left, node.value)
            return left_sum
        return sum_so_far

    traverse(root, 0)
    return root


def getMinimumDifference(root: Optional[Node]) -> int:
    def traverse(node, minimum, maximum):
        if node:
            return min(
                abs(node.value - minimum),
                abs(node.value - maximum),
                traverse(node.left, min(minimum, node.value), max(maximum, node.value)),
                traverse(node.right, min(minimum, node.value), max(maximum, node.value))
            )
        return float('inf')

    return traverse(root, float('inf'), float('-inf'))


def sumOfLeftLeaves(root: Optional[Node]) -> int:
    def traverse(node):
        result = 0
        if node:
            if node.left and not node.left.left and not node.left.right:
                result += node.left.value
            result += traverse(node.left)
            result += traverse(node.right)
        return result

    return traverse(root)


def binaryTreePaths(root: Optional[Node]) -> List[str]:
    result = []

    def traverse(node, path_so_far):
        if node:
            if not path_so_far:
                path_so_far = str(node.value)
            else:
                path_so_far += '->' + str(node.value)

            if not node.left and not node.right:
                result.append(path_so_far)
            else:
                traverse(node.left, path_so_far)
                traverse(node.right, path_so_far)

    traverse(root, "")
    return result


def lowestCommonAncestor(root: 'Node', p: 'Node', q: 'Node') -> 'Node':
    def traverse(node):
        if node:
            if node == p or node == q:
                return node
            left = traverse(node.left)
            right = traverse(node.right)
            if left and right:
                return node
            return left or right
        return None

    return traverse(root)


def invertTree(root: Optional[Node]) -> Optional[Node]:
    def traverse(node):
        if node:
            node.left, node.right = traverse(node.right), traverse(node.left)
            return node

    return traverse(root)


def rightSideView(root: Optional[Node]) -> List[int]:
    if not root:
        return []
    levels = []
    queue = collections.deque([[root, 0]])
    while queue:
        node, level = queue.popleft()
        if len(levels) == level:
            levels.append(node.value)
        else:
            levels[level] = node.value
        if node.left:
            queue.append([node.left, level + 1])
        if node.right:
            queue.append([node.right, level + 1])
    return levels


def connect(root: 'Node') -> 'Node':
    levels = []
    if not root:
        return root
    queue = collections.deque([[root, 0]])
    while queue:
        node, level = queue.popleft()

        if len(levels) == level:
            levels.append(node)
        else:
            levels[level].next = node
            levels[level] = node

        if node.left:
            queue.append([node.left, level + 1])

        if node.right:
            queue.append([node.right, level + 1])

    return root


def connect2(root: 'Node') -> 'Node':
    pass


def hasPathSum(root: Optional[Node], targetSum: int) -> bool:
    def traverse(node, sum_so_far):
        if node:
            if node.left is None and node.right is None and sum_so_far + node.value == targetSum:
                return True
            if sum_so_far > targetSum:
                return False
            return traverse(node.left, sum_so_far + node.value) or traverse(node.right, sum_so_far + node.value)
        return False

    return traverse(root, 0)


def minDepth(root: Optional[Node]) -> int:
    def traverse(node):
        if node:
            if not node.left and not node.right:
                return 1
            left_path = traverse(node.left)
            right_path = traverse(node.right)
            return min(left_path, right_path) + 1
        return float('inf')

    return traverse(root)


def isBalanced(root: Optional[Node]) -> bool:
    def traverse(node):
        if not node:
            return True, 1
        left_balanced, left_level = traverse(node.left)
        right_balanced, right_level = traverse(node.right)
        if not left_balanced or not right_balanced or abs(left_level - right_level) > 1:
            return False, 0
        return True, max(right_level, left_level) + 1

    balanced, levels = traverse(root)
    return balanced


def maxDepth2(root: Optional[Node]) -> int:
    def traverse(node):
        if node:
            if not node.left and not node.right:
                return 1
            return max(traverse(node.left), traverse(node.right)) + 1
        return 0

    return traverse(root)


def zigzagLevelOrder(root: Optional[Node]) -> List[List[int]]:
    if not root:
        return []
    queue = collections.deque([[root, 0]])
    levels = []
    while queue:
        node, level = queue.popleft()
        if len(levels) == level:
            levels.append(collections.deque([node.value]))
        elif level % 2 == 0:
            levels[level].append(node.value)
        else:
            levels[level].appendleft(node.value)

        if node.left:
            queue.append([node.left, level + 1])
        if node.right:
            queue.append([node.right, level + 1])

    return [list(x) for x in levels]


def isSymmetric(root: Optional[Node]) -> bool:
    def traverse(node, other_node):
        if not node and not other_node:
            return True
        if node and not other_node or not node and other_node or node.value != other_node.value:
            return False
        return traverse(node.left, other_node.right) and traverse(node.right, other_node.left)

    return traverse(root, root)


def isSameTree(p: Optional[Node], q: Optional[Node]) -> bool:
    def traverse(node_a, node_b):
        if not node_a and not node_b:
            return True
        if node_a and not node_b or not node_a and node_b or node_a.value != node_b.value:
            return False
        return traverse(node_a.left, node_b.left) and traverse(node_a.right, node_b.right)

    return traverse(p, q)


def isValidBST(root: Optional[Node]) -> bool:
    def traverse(node):
        if not node:
            return True
        if node.left and node.left.val >= node.val:
            return False
        if node.right and node.right.val <= node.val:
            return False
        return traverse(node.left) and traverse(node.right)

    return traverse(root)


def pathSum(root: Optional[Node], targetSum: int) -> List[List[int]]:
    result = []

    def traverse(node, current_path, sum_remaining):
        if node:
            sum_remaining -= node.value
            if node.left is None and node.right is None and not sum_remaining:
                result.append(current_path + [node.value])
            if sum_remaining > 0:
                traverse(node.left, current_path + [node.value], sum_remaining)
                traverse(node.right, current_path + [node.value], sum_remaining)

    traverse(root, [], targetSum)
    return result
