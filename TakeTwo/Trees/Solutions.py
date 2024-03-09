import collections
from typing import Optional, List
from binarytree import Node


def count_good_nodes_in_binary_tree(root: Node) -> int:
    def traverse(node, prev_max):
        value = 0
        if not node:
            return value
        if node.value >= prev_max:
            value += 1
        prev_max = max(prev_max, node.value)
        return value + traverse(node.left, prev_max) + traverse(node.right, prev_max)

    return traverse(root, float('-inf'))


def time_needed_inform_all_employees(n, head_id, manager, inform_time) -> int:
    def build_manager_graph() -> dict:
        manager_graph = collections.defaultdict(list)
        for i, m in enumerate(manager):
            manager_graph[m].append(i)
        return manager_graph

    max_time = 0
    queue = collections.deque([[head_id, 0]])
    manager_graph = build_manager_graph()
    while queue:
        employee_id, time = queue.popleft()
        max_time = max(time, max_time)
        for adjacent in manager_graph[employee_id]:
            queue.append([adjacent, time + inform_time[employee_id]])
    return max_time


def delete_leaves_given_value(root, target) -> Node:
    def traverse(node) -> Optional[Node]:
        if not node:
            return None
        node.left = traverse(node.left)
        node.right = traverse(node.right)
        if not node.left and not node.right and node.value == target:
            return None
        return node

    return traverse(root)


def validate_binary_nodes(n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    visited = {0}
    for i in range(n):
        left = leftChild[i]
        right = rightChild[i]

        if left in visited or right in visited:
            return False
        if left != -1:
            visited.add(left)
        if right != -1:
            visited.add(right)

    return len(visited) == n


def deepest_leaves_sum(root: Optional[Node]) -> int:
    def traverse(node, level) -> [int, int]:
        if not node:
            return 0, float('-inf')

        if not node.right and not node.left:
            return node.value, level

        left_sum, left_level = traverse(node.left, level + 1)
        right_sum, right_level = traverse(node.right, level + 1)

        if left_level == right_level:
            return left_sum + right_sum, right_level
        elif left_level < right_level:
            return right_sum, right_level
        return left_sum, left_level

    deepest_sum, level = traverse(root, 0)
    return deepest_sum


def sum_even_grandparents(root: Node) -> int:
    def traverse(node, parent, grandparent) -> int:
        value = 0

        if not node:
            return value
        if grandparent % 2 == 0:
            value += node.value

        return value + traverse(node.left, node.value, parent) + traverse(node.right, node.value, parent)

    return traverse(root, 1, 1)


def lca_deepest_leaves(root: Optional[Node]) -> Optional[Node]:
    def traverse(node, current_level) -> [Node, int]:
        if not node:
            return None, float('-inf')
        if not node.right and not node.left:
            return node, current_level

        left_node, left_level = traverse(node.left, current_level + 1)
        right_node, right_level = traverse(node.right, current_level + 1)

        if left_level == right_level:
            return node, right_level
        if left_level < right_level:
            return right_node, right_level
        return left_node, left_level

    lca, level = traverse(root, 0)
    return lca


def del_nodes(root: Node, to_delete: List[int]) -> List[Node]:
    node_queue = [root]
    to_delete = set(to_delete)

    def traverse_tree(node: Node) -> Optional[Node]:
        if node:
            if node.value in to_delete:
                node_queue.append(node.left)
                node_queue.append(node.right)
                return None
            node.left, node.right = traverse_tree(node.left), traverse_tree(node.right)
            return node

    for node in node_queue:
        traverse_tree(node)

    return list(filter(lambda x: x is not None, node_queue))


def max_level_sum(root: Optional[Node]) -> int:
    levels, queue = [], collections.deque([[0, root]])

    while queue:
        level, node = queue.popleft()
        if level == len(levels):
            levels.append(node.value)
        else:
            levels[level] += node.value

        if node.left:
            queue.append([level + 1, node.left])
        if node.right:
            queue.append([level + 1, node.right])

    max_level, max_sum = 0, float('-inf')
    for level, sum in enumerate(levels):
        if sum > max_sum:
            max_level = level + 1
            max_sum = sum

    return max_level


def bstToGst(root: Node) -> Node:
    sum_so_far = 0

    def traverse(node):
        nonlocal sum_so_far
        if node:
            traverse(node.right)
            sum_so_far += node.value
            node.value = sum_so_far
            traverse(node.left)

    traverse(root)
    return root


def max_ancestor_diff(root: Optional[Node]) -> int:
    def traverse(node, ancestor_min, ancestor_max):
        if node:
            return max(traverse(node.left, min(ancestor_min, node.value), max(ancestor_max, node.value)),
                       traverse(node.right, min(ancestor_min, node.value), max(ancestor_max, node.value)),
                       max(abs(node.value - ancestor_min), abs(node.value - ancestor_max)))
        return 0

    return traverse(root, root.value, root.value)


def bstFromPreorder(preorder: List[int]) -> Optional[Node]:
    def insert(node, value):
        # we reached a leaf position, create the node
        if not node:
            return Node(value)

        # if value is creater than current position, insert to the right
        # else insert to the left
        if value > node.value:
            node.right = insert(node.right, value)
        else:
            node.left = insert(node.left, value)

        # return the current node
        return node

    # create root of binary tree
    root = Node(preorder[0])
    # for each value iteratively insert into binary search tree
    for value in preorder[1:]:
        insert(root, value)

    return root


def is_cousins(root: Optional[Node], x: int, y: int) -> bool:
    def traverse(node, level):
        if node:
            # if the children of the current node are the two target nodes, return -1
            if (node.left and node.right) and (node.left.value in [x, y] and node.right.value in [x, y]):
                return -1

            # if the current node is a target node, return the level
            if node.value in [x, y]:
                return level

            # get levels from left and right, if they're not equal to one another, return -1, else return a valid value
            left_level, right_level = traverse(node.left, level + 1), traverse(node.right, level + 1)
            if left_level != -1 and right_level != -1 and left_level != right_level:
                return -1
            return left_level if left_level != -1 else right_level

        # return -1 to leaves
        return -1

    return traverse(root, 0) != -1


def verticalTraversal(root: Optional[Node]) -> List[List[int]]:
    negatives = []
    positives = []

    def traverse(node, vertical_level):
        if node:
            if vertical_level >= 0:
                if len(positives) == vertical_level:
                    positives.append([node.value])
                else:
                    positives[vertical_level].append(node.value)
            else:
                negative_level = abs(vertical_level + 1)
                if len(negatives) == negative_level:
                    negatives.append([node.value])
                else:
                    negatives[negative_level].append(node.value)
            traverse(node.left, vertical_level - 1)
            traverse(node.right, vertical_level + 1)

    traverse(root, 0)
    return negatives[::-1] + positives


def is_unival_tree(root: Optional[Node]) -> bool:
    def traverse(node, target):
        if node:
            return traverse(node.left, target) and traverse(node.right, target) if node.value == target else False
        return True

    return traverse(root, root.value)


def flip_equiv(root1: Optional[Node], root2: Optional[Node]) -> bool:
    def traverse(node1, node2):
        if not node1 and not node2:
            return True
        if (not node1 and node2 or node1 and not node2) or node1.value != node2.value:
            return False
        return (traverse(node1.left, node2.left) and traverse(node1.right, node2.right)) or (
                traverse(node1.left, node2.right) and traverse(node1.right, node2.left))

    return traverse(root1, root2)


def range_sum_bst(root: Optional[Node], low: int, high: int) -> int:
    def traverse(node):
        result = 0
        if node:
            if low <= node.value <= high:
                result += node.value
            result += traverse(node.left) + traverse(node.right)
        return result

    return traverse(root)


def increasingBST(root: Node) -> Node:
    def preorder(node):
        result = []
        if node:
            result.extend(preorder(node.left))
            result.append(node)
            result.extend(preorder(node.right))
        return result

    preorder_nodes = preorder(root)
    for i, node in enumerate(preorder_nodes):
        node.left, node.right = None, None
        if i > 0:
            preorder_nodes[i - 1].right = node
    return preorder_nodes[0]


def leaf_similar(root1: Optional[Node], root2: Optional[Node]) -> bool:
    def get_leaves(node):
        result = []
        if node:
            result.extend(get_leaves(node.left))
            if node.left is None and node.right is None:
                result.append(node.value)
            result.extend(get_leaves(node.right))
        return result

    return get_leaves(root1) == get_leaves(root2)


def distance_k(root: Node, target: Node, k: int) -> List[int]:
    result = []

    def traverse(node) -> int:
        if node:
            if node.value == target.value:
                traverse_down(node.left, k - 1)
                traverse_down(node.right, k - 1)
                return k - 1
            else:
                left_distance = traverse(node.left)
                right_distance = traverse(node.right)
                if left_distance == 0 or right_distance == 0:
                    result.append(node.value)
                    return -1
                else:
                    if left_distance != -1:
                        traverse_down(node.right, left_distance - 1)
                        return left_distance - 1
                    if right_distance != -1:
                        traverse_down(node.left, right_distance - 1)
                        return right_distance - 1
                return -1
        else:
            return -1

    def traverse_down(node, distance):
        if node:
            if distance == 0:
                result.append(node.value)
            else:
                traverse_down(node.left, distance - 1)
                traverse_down(node.right, distance - 1)

    traverse(root)
    return result


def pruneTree(root: Optional[Node]) -> Optional[Node]:
    def traverse(node):
        if node:
            left_side, right_side = traverse(node.left), traverse(node.right)
            if not left_side:
                node.left = None
            if not right_side:
                node.right = None
            return left_side or right_side or node.value == 1

    if not traverse(root):
        return None
    return root


def minDiffInBST(root: Optional[Node]) -> int:
    def traverse(node):
        result = []
        if node:
            result.extend(traverse(node.left) + [node.value] + traverse(node.right))
        return result

    sorted = traverse(root)
    return min([abs(sorted[i] - sorted[i - 1]) for i in range(1, len(sorted))])


def trimBST(root: Optional[Node], low: int, high: int) -> Optional[Node]:
    def traverse(node):
        if node:
            node.left, node.right = traverse(node.left), traverse(node.right)
            return node.left or node.right if (node.value > high or node.value < low) else node

    return traverse(root)


def constructMaximumBinaryTree(nums: List[int]) -> Optional[Node]:
    def traverse(values: List[int]) -> Optional[Node]:
        if values:
            max_index = get_max_index(values)
            node = Node(values[max_index])
            node.left, node.right = traverse(values[:max_index]), traverse(values[max_index + 1:])
            return node

    def get_max_index(values: List[int]) -> int:
        max_index, max_so_far = 0, float('-inf')
        for i, value in enumerate(values):
            if value > max_so_far:
                max_index, max_so_far = i, value
        return max_index

    return traverse(nums)


def averageOfLevels(root: Optional[Node]) -> List[float]:
    queue = collections.deque([[0, root]])
    result = []
    while queue:
        level, node = queue.popleft()
        result.append([node.value]) if len(result) == level else result[level].append(node.value)

        if node.left:
            queue.append([level + 1, node.left])
        if node.right:
            queue.append([level + 1, node.right])

    return [sum(numbers) / len(numbers) for numbers in result]


def mergeTrees(root1: Optional[Node], root2: Optional[Node]) -> Optional[Node]:
    def merge(node1: Optional[Node], node2: Optional[Node]) -> Optional[Node]:
        if not node1 or not node2:
            return node1 or node2
        node1.value += node2.value
        node1.left, node1.right = merge(node1.left, node2.left), merge(node1.right, node2.right)
        return node1

    return merge(root1, root2)


def tree2str(root: Optional[Node]) -> str:
    def traverse(node):
        result = ""
        if node:
            result += str(node.value)
            if node.right:
                result += "(" + traverse(node.left) + ")(" + traverse(node.right) + ")"
            elif node.left:
                result += "(" + traverse(node.left) + ")"
        return result

    return traverse(root)


def diameterOfBinaryTree(root: Optional[Node]) -> int:
    max_path = 0

    def traverse(node: Optional[Node]) -> int:
        nonlocal max_path
        if node:
            left_distance, right_distance = traverse(node.left), traverse(node.right)
            max_path = max(max_path, left_distance + right_distance)
            return max(left_distance, right_distance) + 1
        return 0

    traverse(root)
    return max_path


import json


class Codec:

    def serialize(self, root: Node) -> str:
        def traverse(node) -> List[any]:
            return [node.value] + traverse(node.left) + traverse(node.right) if node else [None]

        return json.dumps({"values": traverse(root)})

    def deserialize(self, data: str) -> Node:
        queue = collections.deque(json.loads(data)["values"])
        """Decodes your encoded data to tree.
        """

        def traverse():
            if not queue:
                return None
            if queue[0] is None:
                queue.popleft()
                return None
            node = Node(queue.popleft())
            node.left, node.right = traverse(), traverse()
            return node

        return traverse()


def sumOfLeftLeaves(root: Optional[Node]) -> int:
    def traverse(node, left):
        if node:
            return node.value if node.left is None and node.right is None and left else \
                traverse(node.left, True) + traverse(node.right, False)
        return 0

    return traverse(root, False)


def binaryTreePaths(root: Optional[Node]) -> List[str]:
    result = []

    def traverse(node, path_so_far):
        if node:
            path_so_far += str(node.value)
            if node.left is None and node.right is None:
                result.append(path_so_far)
            if node.left:
                traverse(node.left, path_so_far + "->")
            if node.right:
                traverse(node.right, path_so_far + "->")

    traverse(root, "")
    return result


def lowestCommonAncestor(root: 'Node', p: 'Node', q: 'Node') -> 'Node':
    def traverse(node: Optional[Node]) -> Optional[Node]:
        if node:
            if node.value in [p.value, q.value]:
                return node
            left, right = traverse(node.left), traverse(node.right)
            return node if left and right else left or right

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
    view = []
    queue = collections.deque([(0, root)])
    while queue:
        level, node = queue.popleft()
        if len(view) == level:
            view.append(node.value)
        else:
            view[level] = node.value
        if node.left:
            queue.append((level + 1, node.left))
        if node.right:
            queue.append((level + 1, node.right))
    return view


def preorderTraversal(root: Optional[Node]) -> List[int]:
    def traverse(node):
        return [node.value] + traverse(node.left) + traverse(node.right) if node else []

    return traverse(root)


def hasPathSum(root: Optional[Node], targetSum: int) -> bool:
    def traverse(n, sum):
        return traverse(n.left, sum + n.value) or traverse(n.right, sum + n.value) if n else sum == targetSum

    return traverse(root, 0) if root else False


def minDepth(root: Optional[Node]) -> int:
    def traverse(node):
        if node:
            return min(traverse(node.left), traverse(node.right)) + 1 if node.left or node.right else 1
        return float('inf')

    return traverse(root)


def isBalanced(root: Optional[Node]) -> bool:
    balanced = True

    def traverse(node):
        if node:
            left, right = traverse(node.left), traverse(node.right)
            if left and right and abs(left - right) > 1:
                nonlocal balanced
                balanced = False
            return max(left, right) + 1
        return 0

    traverse(root)
    return balanced


def levelOrderBottom(root: Optional[Node]) -> List[List[int]]:
    if not root:
        return []
    queue = collections.deque([(0, root)])
    ordering = []
    while queue:
        level, node = queue.popleft()
        if len(ordering) == level:
            ordering.append([node.value])
        else:
            ordering[level].append(node.value)
        if node.left:
            queue.append((level + 1, node.left))
        if node.right:
            queue.append((level + 1, node.right))

    return ordering[::-1]


def maxDepth2(root: Optional[Node]) -> int:
    if not root:
        return 0

    def traverse(node):
        if node:
            return max(traverse(node.left), traverse(node.right)) + 1 if node.left or node.right else 1
        return float('-inf')

    return traverse(root)


def zigzagLevelOrder(root: Optional[Node]) -> List[List[int]]:
    if not root:
        return []
    queue, ordering = collections.deque([(0, root)]), []

    while queue:
        level, node = queue.popleft()
        if len(ordering) == level:
            ordering.append([node.value])
        else:
            ordering[level].append(node.value)
        if node.left:
            queue.append((level + 1, node.left))
        if node.right:
            queue.append((level + 1, node.right))

    for i in range(len(ordering)):
        if i % 2 == 1:
            ordering[i] = ordering[i][::-1]

    return ordering


def isSymmetric(root: Optional[Node]) -> bool:
    def traverse(left, right):
        if not left or not right:
            return left == right
        return traverse(left.left, right.right) and traverse(left.right, right.left) and left.value == right.value

    return traverse(root, root)


def isSameTree(p_node: Optional[Node], q_node: Optional[Node]) -> bool:
    if not p_node or not q_node:
        return p_node == q_node
    return p_node.value == q_node.value and isSameTree(p_node.left, q_node.left) and isSameTree(p_node.right,
                                                                                                q_node.right)


def isValidBST(root: Optional[Node]) -> bool:
    def traverse(node, minimum, maximum):
        if node:
            if node.val <= minimum or node.val >= maximum:
                return False
            return traverse(node.left, minimum, node.value) and traverse(node.right, node.value, maximum)
        return True

    return traverse(root, float('-inf'), float('inf'))


def inorderTraversal(root: Optional[Node]) -> List[int]:
    return inorderTraversal(root.left) + [root.value] + inorderTraversal(root.right) if root else []


def pathSum(root: Optional[Node], targetSum: int) -> List[List[int]]:
    result = []

    def traverse(node, remaining, path):
        if node:
            if remaining - node.value > 0:
                traverse(node.left, remaining - node.value, path + [node.value])
                traverse(node.right, remaining - node.value, path + [node.value])
            elif remaining - node.value == 0:
                result.append(path + [node.value])

    traverse(root, targetSum, [])
    return result


def countUnivalSubtrees(root: Optional[Node]) -> int:
    result = 0

    def traverse(node):
        if node:
            nonlocal result
            left, right = True, True
            if node.left:
                left = traverse(node.left) and node.left.value == node.value
            if node.right:
                right = traverse(node.right) and node.right.value == node.value
            if left and right:
                result += 1
                return True
            else:
                return False
        return True

    traverse(root)
    return result
