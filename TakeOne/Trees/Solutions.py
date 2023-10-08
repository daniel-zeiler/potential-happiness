import collections
import heapq
from typing import List, Optional, Any

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


def pruneTree(root: Optional[Node]) -> Optional[Node]:
    def traverse(root):
        if root:
            root.left = traverse(root.left)
            root.right = traverse(root.right)
            if root.left is None and root.right is None and root.val == 0:
                return None
            return root

    return traverse(root)


def minDiffInBST(root: Optional[Node]) -> int:
    def fn(node, lo, hi):
        if not node:
            return hi - lo
        left = fn(node.left, lo, node.val)
        right = fn(node.right, node.val, hi)
        return min(left, right)

    return fn(root, float('-inf'), float('inf'))


def insertIntoBST(root: Optional[Node], val: int) -> Optional[Node]:
    def insert(root):
        if root:
            if val > root.val:
                root.right = insert(root.right)
            else:
                root.left = insert(root.left)
        else:
            root = Node(val)
        return root

    return insert(root)


def searchBST(root: Optional[Node], val: int) -> Optional[Node]:
    def search(root):
        if root:
            if root.val == val:
                return root
            elif val > root.val:
                return search(root.right)
            else:
                return search(root.left)

    return search(root)


def findSecondMinimumValue(root: Optional[Node]) -> int:
    queue = collections.deque([[0, root]])
    min_vals = set()
    current_level = 0
    while queue:
        level, node = queue.popleft()
        min_vals.add(node.val)
        if level != current_level:
            if len(min_vals) > 2:
                return heapq.nsmallest(2, list(min_vals))[1]
            current_level = level
        if node.left:
            queue.append([level + 1, node.left])
        if node.right:
            queue.append([level + 1, node.right])

    if len(min_vals) > 2:
        return heapq.nsmallest(2, list(min_vals))[1]

    return -1


def trimBST(root: Optional[Node], low: int, high: int) -> Optional[Node]:
    def trim(root):
        if root:
            root.left = trim(root.left)
            root.right = trim(root.right)
            if root.val > high or root.val < low:
                return root.left or root.right
            return root

    return trim(root)


def constructMaximumBinaryTree(nums: List[int]) -> Optional[Node]:
    def build(nums):
        if nums:
            max_index = get_max_index(nums)
            node = Node(nums[max_index])
            node.left = build(nums[:max_index])
            node.right = build(nums[max_index + 1:])
            return node

    def get_max_index(nums):
        max_index = 0
        maximum = float('-inf')
        for i, number in enumerate(nums):
            if number > maximum:
                maximum = number
                max_index = i
        return max_index

    return build(nums)


def findTarget(root: Optional[Node], k: int) -> bool:
    compliments = set()

    def traverse(root):
        if root:
            if root.val in compliments:
                return True
            compliments.add(k - root.val)
            return traverse(root.left) or traverse(root.right)
        return False

    return traverse(root)


def averageOfLevels(root: Optional[Node]) -> List[float]:
    queue = collections.deque([[0, root]])
    levels = []
    while queue:
        level, node = queue.popleft()

        if level == len(levels):
            levels.append([node.val])
        else:
            levels[level].append(node.val)

        if node.left:
            queue.append([level + 1, node.left])
        if node.right:
            queue.append([level + 1, node.right])

    return [sum(x) / len(x) for x in levels]


def mergeTrees(root_a: Optional[Node], root_b: Optional[Node]) -> Optional[Node]:
    if root_a and root_b:
        root_a.val += root_b.val
        root_a.left = mergeTrees(root_a.left, root_b.left)
        root_a.right = mergeTrees(root_a.right, root_b.right)
    return root_a or root_b


def tree2str(root: Optional[Node]) -> str:
    result = str(root.val)
    if root.left and root.right:
        result += '(' + tree2str(root.left) + ')' + '(' + tree2str(root.right) + ')'
    elif root.left:
        result += '(' + tree2str(root.left) + ')'
    elif root.right:
        result += '()(' + tree2str(root.right) + ')'
    return result


def diameterOfBinaryTree(root: Optional[Node]) -> int:
    result = 0

    def traverse(root):
        nonlocal result
        if root:
            left_length = traverse(root.left)
            right_length = traverse(root.right)
            result = max(result, left_length + right_length)
            return max(left_length, right_length) + 1
        return 0

    traverse(root)
    return result


def convertBST(root: Optional[Node]) -> Optional[Node]:
    maximum_value = 0

    def traverse(root):
        nonlocal maximum_value
        if root:
            traverse(root.right)
            root.val += maximum_value
            maximum_value = root.val
            traverse(root.left)

    traverse(root)
    return root


def getMinimumDifference(root: Optional[Node]) -> int:
    def get_inorder(root):
        result = []
        if root:
            result.extend(get_inorder(root.left))
            result.append(root.val)
            result.extend(get_inorder(root.right))
        return result

    inorder = get_inorder(root)
    return min([inorder[i] - inorder[i - 1] for i in range(1, len(inorder))])


class Codec:

    def serialize(self, root: Node) -> str:

        def traverse(node):
            result = ''
            if node:
                result += str(node.val) + ','
                result += traverse(node.left)
                result += traverse(node.right)
            else:
                result += 'None,'
            return result

        return traverse(root)

    def deserialize(self, data: str) -> Node:
        values = collections.deque(data.split(','))

        def traverse():
            if values:
                if values[0] == 'None':
                    values.popleft()
                    return None
                else:
                    root = Node(int(values.popleft()))
                    root.left = traverse()
                    root.right = traverse()
                    return root

        return traverse()


def sumOfLeftLeaves(root: Optional[Node]) -> int:
    def traverse(root, left_side):
        if root:
            if not root.left and not root.right and left_side:
                return root.val
            return traverse(root.left, True) + traverse(root.right, False)
        return 0

    return traverse(root, False)


def binaryTreePaths(root: Optional[Node]) -> List[str]:
    def traverse(root, path):
        result = []
        if root:
            path += str(root.val)
            if root.left:
                result.extend(traverse(root.left, path + '->'))
            if root.right:
                result.extend(traverse(root.right, path + '->'))
            if not root.left and not root.right:
                result.append(path)
        return result

    return traverse(root, '')


def lowestCommonAncestor(root: 'Node', p: 'Node', q: 'Node') -> 'Node':
    if root:
        if root == p or root == q:
            return root
        left_discovered = lowestCommonAncestor(root.left, p, q)
        right_discovered = lowestCommonAncestor(root.right, p, q)
        if left_discovered and right_discovered:
            return root
        else:
            return left_discovered or right_discovered


def invertTree(root: Optional[Node]) -> Optional[Node]:
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


def rightSideView(root: Optional[Node]) -> List[int]:
    if not root:
        return []
    queue = collections.deque([[0, root]])
    result = []
    while queue:
        level, node = queue.popleft()
        if level == len(result):
            result.append(node.val)
        else:
            result[level] = node.val

        if node.left:
            queue.append([level + 1, node.left])
        if node.right:
            queue.append([level + 1, node.right])

    return result


def preorderTraversal(root: Optional[Node]) -> List[int]:
    result = []
    if root:
        result.append(root.val)
        result.extend(preorderTraversal(root.left))
        result.extend(preorderTraversal(root.right))
    return result


class ConnectNode:
    def __init__(self, val: Any, left: "ConnectNode" = None, right: "ConnectNode" = None, next: "ConnectNode" = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: ConnectNode) -> ConnectNode:
    traversal = []
    queue = collections.deque([[0, root]])

    while queue:
        level, node = collections.deque.popleft(queue)

        if len(traversal) == level:
            traversal.append(node)
        else:
            traversal[level].next = node
            traversal[level] = node

        if node.left:
            queue.append([level + 1, node.left])
        if node.right:
            queue.append([level + 1, node.right])

    return root


def hasPathSum(root: Optional[Node], targetSum: int) -> bool:
    if root:
        if not root.left and not root.right and targetSum - root.val == 0:
            return True
        if targetSum < 0:
            return False
        return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)
    return False


def minDepth(root: Optional[Node]) -> int:
    def traverse(level, node):
        if node:
            if not node.left and not node.right:
                return level
            return min(traverse(level + 1, node.left), traverse(level + 1, node.right))
        return float('inf')

    return traverse(1, root)


def isBalanced(root: Optional[Node]) -> bool:
    is_balance = True

    def traverse(level, node):
        if node:
            left_level = traverse(level + 1, node.left)
            right_level = traverse(level + 1, node.right)
            if abs(left_level - right_level) > 1:
                nonlocal is_balance
                is_balance = False
            return max(left_level, right_level)
        return level

    traverse(1, root)
    return is_balance


def levelOrderBottom(root: Optional[Node]) -> List[List[int]]:
    if root:
        level_order = collections.deque([])
        queue = collections.deque([[0, root]])

        while queue:
            level, node = collections.deque.popleft(queue)
            if level == len(level_order):
                collections.deque.appendleft(level_order, [node.val])
            else:
                level_order[0].append(node.val)

            if node.left:
                queue.append([level + 1, node.left])
            if node.right:
                queue.append([level + 1, node.right])

        return [list(x) for x in list(level_order)]
    else:
        return []


def maxDepth2(root: Optional[Node]) -> int:
    def traverse(level, node):
        if not node:
            return level - 1
        return max(traverse(level + 1, node.left), traverse(level + 1, node.right))

    return traverse(1, root)


def zigzagLevelOrder(root: Optional[Node]) -> List[List[int]]:
    if not root:
        return []
    traversal = []
    queue = collections.deque([[0, root]])

    while queue:
        level, node = collections.deque.popleft(queue)
        if level == len(traversal):
            traversal.append(collections.deque([node.val]))
        else:
            if level % 2:
                collections.deque.appendleft(traversal[level], node.val)
            else:
                traversal[level].append(node.val)

        if node.left:
            queue.append([level + 1, node.left])
        if node.right:
            queue.append([level + 1, node.right])

    return [list(x) for x in list(traversal)]


def isSymmetric(root: Optional[Node]) -> bool:
    def traverse(node_a, node_b):
        if not node_a and not node_b:
            return True
        elif not node_a or not node_b:
            return False
        if node_a.val != node_b.val:
            return False
        return traverse(node_a.left, node_b.right) and traverse(node_a.right, node_b.left)

    return traverse(root, root)


def isSameTree(p: Optional[Node], q: Optional[Node]) -> bool:
    if not p and not q:
        return True
    elif not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


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


def inorderTraversal(root: Optional[Node]) -> List[int]:
    result = []
    if root:
        result.extend(inorderTraversal(root.left))
        result.append(root.val)
        result.extend(inorderTraversal(root.right))
    return result


def pathSum(root: Optional[Node], targetSum: int) -> List[List[int]]:
    result = []

    def traverse(node, path_so_far, target_remaining):
        if node:
            if not node.left and not node.right and target_remaining - node.val == 0:
                result.append(path_so_far + [node.val])
            else:
                traverse(node.left, path_so_far + [node.val], target_remaining - node.val)
                traverse(node.right, path_so_far + [node.val], target_remaining - node.val)

    traverse(root, [], targetSum)
    return result


def sumRootToLeaf(root: Optional[Node]) -> int:
    result = 0

    def traverse(node, value_so_far):
        if node:
            if not node.left and not node.right:
                nonlocal result
                result += int(value_so_far + str(node.val), 2)
            else:
                traverse(node.left, value_so_far + str(node.val))
                traverse(node.right, value_so_far + str(node.val))

    traverse(root, '')
    return result


def countUnivalSubtrees(root: Optional[Node]) -> int:
    result = 0

    def traverse(node):
        nonlocal result
        is_univalued = True
        if node:
            if node.left is not None:
                is_univalued = traverse(node.left) and node.left.val == node.val and is_univalued
            if node.right is not None:
                is_univalued = traverse(node.right) and node.right.val == node.val and is_univalued
            if is_univalued:
                result += 1
        return is_univalued

    traverse(root)
    return result


input = binarytree.build2([5, 1, 5, 5, 5, None, 5])
