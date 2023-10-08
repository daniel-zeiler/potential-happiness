import collections
from typing import Optional, List

from binarytree import Node


def count_good_nodes_in_binary_tree(root):
    def count_recursive(node, greatest_so_far):
        result = 0
        if node:
            if node.value >= greatest_so_far:
                result += 1
            result += count_recursive(node.left, max(greatest_so_far, node.value))
            result += count_recursive(node.right, max(greatest_so_far, node.value))
        return result

    return count_recursive(root, root.value)


def time_needed_inform_all_employees(n, head_id, manager, inform_time):
    def get_graph():
        graph = collections.defaultdict(list)
        for destination, origin in enumerate(manager):
            graph[origin].append(destination)
        return graph

    graph = get_graph()
    visited = {head_id}
    queue = collections.deque([[0, head_id]])
    time = 0
    while queue:
        time, node_id = queue.popleft()
        for adjacent in graph[node_id]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append([time + inform_time[node_id], adjacent])
    return time


def delete_leaves_given_value(root, target):
    def traverse(node):
        if node:
            node.left = traverse(node.left)
            node.right = traverse(node.right)
            if node.value == target and not node.left and not node.right:
                return None
        return node

    return traverse(root)


def deepest_leaves_sum(root: Optional[Node]) -> int:
    def traverse(node, level):
        if not node:
            return -1, -1
        left_level, left_sum = traverse(node.left, level + 1)
        right_level, right_sum = traverse(node.right, level + 1)
        if left_sum == -1 and right_sum == -1:
            return level, node.value
        elif left_level == right_level:
            return left_level, right_sum + left_sum
        elif left_level < right_level:
            return right_level, right_sum
        else:
            return left_level, left_sum

    return traverse(root, 0)[1]


def sumEvenGrandparent(root: Node) -> int:
    def traverse(node, parent, grandparent):
        sum = 0
        if node:
            if grandparent:
                sum += node.value
            even = (node.value % 2) == 0
            sum += traverse(node.left, even, parent)
            sum += traverse(node.right, even, parent)
        return sum

    return traverse(root, False, False)


def lca_deepest_leaves(root: Optional[Node]) -> Optional[Node]:
    def traverse(node, level):
        if not node:
            return -1, None
        left_level, left_node = traverse(node.left, level + 1)
        right_level, right_node = traverse(node.right, level + 1)
        if left_level == -1 and right_level == -1:
            return level, node
        if left_level == right_level:
            return left_level, node
        elif left_level > right_level:
            return left_level, left_node
        return right_level, right_node

    return traverse(root, 0)[1]


def del_nodes(root: Node, to_delete: List[int]) -> List[Node]:
    queue = [root]
    result = []
    to_delete = set(to_delete)

    def traverse(node):
        if node:
            if node.val in to_delete:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                return None
            node.left = traverse(node.left)
            node.right = traverse(node.right)
        return node

    for node in queue:
        head = traverse(node)
        if head:
            result.append(head)
    return result


def max_level_sum(root: Optional[Node]) -> int:
    level_ordering = []
    queue = collections.deque([[0, root]])

    while queue:
        level, node = queue.popleft()
        if level == len(level_ordering):
            level_ordering.append(node.value)
        else:
            level_ordering[level] += node.value
        if node.left:
            queue.append([level + 1, node.left])
        if node.right:
            queue.append([level + 1, node.right])
    max_index = 0
    max_sum = 0
    for i, a_sum in enumerate(level_ordering):
        if a_sum > max_sum:
            max_index = i
            max_sum = a_sum

    return max_index + 1


def bstToGst(root: Node) -> Node:
    greater_sum = 0

    def traverse(node):
        if node:
            nonlocal greater_sum
            traverse(node.right)
            node.value += greater_sum
            greater_sum = node.value
            traverse(node.left)
        return node

    return traverse(root)


def max_ancestor_diff(root: Optional[Node]) -> int:
    def traverse(node, low, high):
        if node:
            diff = max(abs(node.value - low), abs(node.value - high))
            low = min(low, node.value)
            high = max(high, node.value)
            return max(diff, traverse(node.left, low, high), traverse(node.right, low, high))
        return 0

    return traverse(root, root.value, root.value)


def is_cousins(root: Optional[Node], x: int, y: int) -> bool:
    def traverse(node, level):
        if node:
            if node.left and node.right:
                if (node.left.value == x or node.left.value == y) and (node.right.value == x or node.right.value == y):
                    return None

            if node.value == x or node.value == y:
                return level

            left = traverse(node.left, level + 1)
            right = traverse(node.right, level + 1)

            if left and right and left != right:
                return None

            return left or right

    return traverse(root, 0) is not None


def verticalTraversal(root: Optional[Node]) -> List[List[int]]:
    negative = []
    positive = []

    def traverse(node, position):
        if node:
            if position >= 0:
                if len(positive) == position:
                    positive.append([node.value])
                else:
                    positive[position].append(node.value)
            elif len(negative) == abs(position) - 1:
                negative.append([node.value])
            else:
                negative[abs(position) - 1].append(node.value)
            traverse(node.left, position - 1)
            traverse(node.right, position + 1)

    traverse(root, 0)
    return negative[::-1] + positive


def is_unival_tree(root: Optional[Node]) -> bool:
    def traverse(node, a_value):
        if node:
            if node.value != a_value:
                return False
            return traverse(node.left, a_value) and traverse(node.right, a_value)
        return True

    return traverse(root, root.value)


def range_sum_bst(root: Optional[Node], low: int, high: int) -> int:
    def traverse(node):
        result = 0
        if node:
            if low <= node.value <= high:
                result += node.value
            result += traverse(node.left)
            result += traverse(node.right)
        return result

    return traverse(root)


def leaf_similar(root1: Optional[Node], root2: Optional[Node]) -> bool:
    def get_leaf_sequence(node):
        result = []
        if node:
            result.extend(get_leaf_sequence(node.left))
            if node.left is None and node.right is None:
                result.append(node.value)
            result.extend(get_leaf_sequence(node.right))
        return result

    for node1, node2 in zip(get_leaf_sequence(root1), get_leaf_sequence(root2)):
        if node1 != node2:
            return False
    return True


def distance_k(root: Node, target: Node, k: int) -> List[int]:
    result = []

    def traverse(node):
        if node:
            if node.value == target.value:
                pass_down(node.left, 1)
                pass_down(node.right, 1)
                return 1
            left_distance = traverse(node.left)
            right_distance = traverse(node.right)
            if left_distance != float('inf'):
                if left_distance == k:
                    result.append(node.value)
                    return float('inf')
                else:
                    pass_down(node.right, left_distance + 1)
                    return left_distance + 1
            if right_distance != float('inf'):
                if right_distance == k:
                    result.append(node.value)
                    return float('inf')
                else:
                    pass_down(node.left, right_distance + 1)
                    return right_distance + 1
        return float('inf')

    def pass_down(node, distance):
        if node:
            if distance == k:
                result.append(node.value)
            else:
                pass_down(node.left, distance + 1)
                pass_down(node.right, distance + 1)

    traverse(root)
    return result


def pruneTree(root: Optional[Node]) -> Optional[Node]:
    def traverse(node):
        if node:
            node.left = traverse(node.left)
            node.right = traverse(node.right)
            if not node.left and not node.right and node.value == 0:
                return None
        return node

    return traverse(root)


def minDiffInBST(root: Optional[Node]) -> int:
    def inorder(node):
        result = []
        if node:
            result.extend(inorder(node.left))
            result.append(node.value)
            result.extend(inorder(node.right))
        return result

    min_difference = float('inf')
    inorder_traversal = inorder(root)
    for i, value in enumerate(inorder_traversal):
        if i:
            min_difference = min(min_difference, value - inorder_traversal[i - 1])

    return min_difference


def trimBST(root: Optional[Node], low: int, high: int) -> Optional[Node]:
    def traverse(node):
        if node:
            node.left = traverse(node.left)
            node.right = traverse(node.right)
            if node.value < low or node.value > high:
                return node.left or node.right
        return node

    return traverse(root)


def constructMaximumBinaryTree(nums: List[int]) -> Optional[Node]:
    def get_max_index(nums_remaining):
        max_index = 0
        max_value = float('-inf')
        for i, value in enumerate(nums_remaining):
            if value > max_value:
                max_index = i
                max_value = max(max_value, value)
        return max_index

    def traverse(nums_remaining):
        if nums_remaining:
            max_index = get_max_index(nums_remaining)
            node = Node(nums_remaining[max_index])
            node.left = traverse(nums_remaining[:max_index])
            node.right = traverse(nums_remaining[max_index + 1:])
            return node

    return traverse(nums)


def averageOfLevels(root: Optional[Node]) -> List[float]:
    levels = []
    queue = collections.deque([[0, root]])

    while queue:
        level, node = queue.popleft()
        if level == len(levels):
            levels.append([node.value])
        else:
            levels[level].append(node.value)
        if node.left:
            queue.append([level + 1, node.left])
        if node.right:
            queue.append([level + 1, node.right])

    for i, values in enumerate(levels):
        levels[i] = sum(values) / len(values)
    return levels


def mergeTrees(root1: Optional[Node], root2: Optional[Node]) -> Optional[Node]:
    def traverse(node1, node2):
        if node1 or node2:
            if node1 and node2:
                node1.value += node2.value
                node1.left = traverse(node1.left, node2.left)
                node1.right = traverse(node1.right, node2.right)
        return node1 or node2

    return traverse(root1, root2)


def tree2str(root: Optional[Node]) -> str:
    def traverse(node):
        result = ''
        if node:
            result = str(node.value)
            if node.left:
                result += '(' + traverse(node.left) + ')'
                if node.right:
                    result += '(' + traverse(node.right) + ')'
            elif node.right:
                result += '()(' + traverse(node.right) + ')'
        return result

    return traverse(root)


def diameterOfBinaryTree(root: Optional[Node]) -> int:
    result = 0

    def traverse(node):
        if node:
            left = traverse(node.left)
            right = traverse(node.right)
            nonlocal result
            result = max(result, left + right + 1)
            return max(left, right) + 1
        return 0

    traverse(root)
    return result - 1


# Definition for a binary tree node.
# class Node:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import json


class Codec:

    def serialize(self, root: Node) -> str:
        def traverse(node):
            result = []
            if node:
                result.append(node.value)
                result.extend(traverse(node.left))
                result.extend(traverse(node.right))
                return result
            return [None]

        return json.dumps({'values': traverse(root)})

    def deserialize(self, data: str) -> Node:
        """Decodes your encoded data to tree.
        """
        queue = collections.deque(json.loads(data)['values'])

        def traverse():
            if queue:
                if queue[0] is None:
                    return queue.popleft()
                node = Node(queue.popleft())
                node.left = traverse()
                node.right = traverse()
                return node

        return traverse()


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

    return traverse(root)


def invertTree(root: Optional[Node]) -> Optional[Node]:
    def traverse(node):
        if node:
            node.left, node.right = traverse(node.right), traverse(node.left)
        return node

    return traverse(root)


def rightSideView(root: Optional[Node]) -> List[int]:
    levels = []
    queue = collections.deque([[0, root]])
    if not root:
        return levels
    while queue:
        level, node = queue.popleft()
        if level == len(levels):
            levels.append(node.value)
        else:
            levels[level] = node.value
        if node.left:
            queue.append([level + 1, node.left])
        if node.right:
            queue.append([level + 1, node.right])
    return levels


def isSymmetric(root: Optional[Node]) -> bool:
    def traverse(left_node, right_node):
        if left_node and right_node:
            if left_node.value != right_node.value:
                return False
            return traverse(left_node.left, right_node.right) and traverse(left_node.right, right_node.left)

        if not left_node and not right_node:
            return True
        return False

    return traverse(root, root)
