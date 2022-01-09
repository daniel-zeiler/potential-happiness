import collections
from typing import Optional, List
from binarytree import Node


def count_good_nodes_in_binary_tree(root):
    def traverse(node, max_so_far):
        result = 0
        if node:
            if node.value >= max_so_far:
                result += 1
            result += traverse(node.left, max(max_so_far, node.value))
            result += traverse(node.right, max(max_so_far, node.value))
        return result

    return traverse(root, float('-inf'))


def time_needed_inform_all_employees(n, head_id, manager, inform_time):
    def get_graph():
        graph = collections.defaultdict(list)
        for i, origin in enumerate(manager):
            graph[origin].append([i, inform_time[origin]])
        return graph

    graph = get_graph()

    queue = collections.deque([[head_id, 0]])
    max_time = 0

    while queue:
        employee_id, time = queue.popleft()
        max_time = max(time, max_time)
        for adjacent, time_to in graph[employee_id]:
            queue.append([adjacent, time + time_to])

    return max_time


def delete_leaves_given_value(root, target):
    if root:
        root.left = delete_leaves_given_value(root.left, target)
        root.right = delete_leaves_given_value(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root


def validate_binary_nodes(n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    in_degree_set = {n for n in range(n)}

    for left, right in zip(leftChild, rightChild):
        if left != -1 and left in in_degree_set:
            in_degree_set.remove(left)
        if right != -1 and right in in_degree_set:
            in_degree_set.remove(right)

    if not in_degree_set or len(in_degree_set) != 1:
        return False

    visited = set()

    def traverse(node_id):
        if node_id in visited:
            return False
        visited.add(node_id)
        if leftChild[node_id] != -1 and not traverse(leftChild[node_id]):
            return False
        if rightChild[node_id] != -1 and not traverse(rightChild[node_id]):
            return False
        return True

    return traverse(list(in_degree_set)[0])


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


def sum_even_grandparents(root: Node) -> int:
    def traverse(node, parent, grandparent):
        result = 0
        if node:
            if grandparent % 2 == 0:
                result += node.value
            result += traverse(node.left, node.value, parent)
            result += traverse(node.right, node.value, parent)
        return result

    return traverse(root, 1, 1)


def lca_deepest_leaves(root: Optional[Node]) -> Optional[Node]:
    def traverse(node, level):
        if not node:
            return None, level

        left_node, left_level = traverse(node.left, level + 1)
        right_node, right_level = traverse(node.right, level + 1)

        if not left_node and not right_node or left_level == right_level:
            return node, left_level
        elif left_level < right_level:
            return right_node, right_level
        else:
            return left_node, left_level

    return traverse(root, 0)[0]


def del_nodes(root: Node, to_delete: List[int]) -> List[Node]:
    queue = collections.deque([root])
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

    result = []
    while queue:
        node = queue.popleft()
        pruned_node = traverse(node)
        if pruned_node:
            result.append(pruned_node)

    return result


def max_level_sum(root: Optional[Node]) -> int:
    max_level_sum = float('-inf')
    max_level = 0
    curr_sum = 0
    curr_level = 0
    queue = collections.deque([[root, 1]])
    while queue:
        node, level = queue.popleft()
        if level != curr_level:
            if max_level_sum < curr_sum:
                max_level_sum = curr_sum
                max_level = curr_level
            curr_sum = 0
            curr_level = level

        curr_sum += node.value

        if node.left:
            queue.append([node.left, level + 1])
        if node.right:
            queue.append([node.right, level + 1])

    if max_level_sum < curr_sum:
        max_level = curr_level
    return max_level


def bstToGst(root: Node) -> Node:
    add_value = 0

    def traverse(root):
        if root:
            nonlocal add_value
            traverse(root.right)
            root.value = root.value + add_value
            add_value = root.value
            traverse(root.left)

    traverse(root)
    return root


def max_ancestor_diff(root: Optional[Node]) -> int:
    def traverse(node, low, high):
        if node:
            left = traverse(node.left, min(low, node.value), max(high, node.value))
            right = traverse(node.right, min(low, node.value), max(high, node.value))
            return max(abs(node.value - low), abs(node.value - high), left, right)
        return 0

    return traverse(root, root.value, root.value)


def bstFromPreorder(preorder: List[int]) -> Optional[Node]:
    def next_greater_index(a_list):
        head_value = a_list[0]
        greater_index = len(a_list)
        for i, value in enumerate(a_list):
            if i and value > head_value:
                return i
        return greater_index

    def traverse(a_list):
        if not a_list:
            return
        node = Node(a_list[0])
        greater_index = next_greater_index(a_list)
        node.right = traverse(a_list[greater_index:])
        node.left = traverse(a_list[1:greater_index])
        return node

    return traverse(preorder)


def is_cousins(root: Optional[Node], x: int, y: int) -> bool:
    def traverse(node, level):
        if node:
            if node.left and node.left.value == x and node.right and node.right.value == y:
                return None
            if node.value == x or node.value == y:
                return level
            left = traverse(node.left, level + 1)
            right = traverse(node.right, level + 1)
            if left and right:
                if left != right:
                    return None
            if left:
                return left
            if right:
                return right

    return traverse(root, 0) is not None


def verticalTraversal(root: Optional[Node]) -> List[List[int]]:
    positive = []
    negative = []

    def add_value(list, index, value):
        if len(list) == index:
            list.append([value])
        else:
            list[index].append(value)

    def traverse(node, column_number):
        if node:
            if column_number >= 0:
                add_value(positive, column_number, node.value)
            else:
                add_value(negative, abs(column_number) - 1, node.value)
            traverse(node.left, column_number - 1)
            traverse(node.right, column_number + 1)

    traverse(root, 0)
    return negative[::-1] + positive


def is_unival_tree(root: Optional[Node]) -> bool:
    def traverse(node, value):
        if node:
            if node.value != value:
                return False
            else:
                return traverse(node.left, node.value) and traverse(node.right, node.value)
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


def increasingBST(root: Node) -> Node:
    def inorder_traversal(node):
        result = []
        if node:
            result.extend(inorder_traversal(node.left))
            result.append(node.value)
            result.extend(inorder_traversal(node.right))
        return result

    inorder = collections.deque(inorder_traversal(root))

    def buildBST():
        if inorder:
            node = Node(inorder.popleft())
            node.right = buildBST()
            return node

    return buildBST()


def leaf_similar(root1: Optional[Node], root2: Optional[Node]) -> bool:
    def get_leaf_sequence(node):
        result = []
        if node:
            result.extend(get_leaf_sequence(node.left))
            if not node.left and not node.right:
                result.append(node.value)
            result.extend(get_leaf_sequence(node.right))
        return result

    for i, j in zip(get_leaf_sequence(root1), get_leaf_sequence(root2)):
        if i != j:
            return False
    return True


def distance_k(root: Node, target: Node, k: int) -> List[int]:
    result = []

    def pass_down(node, remaining):
        if node:
            if not remaining:
                result.append(node.value)
            else:
                pass_down(node.left, remaining - 1)
                pass_down(node.right, remaining - 1)

    def traverse(node):
        if node:
            if node.value == target.value:
                pass_down(node.left, k - 1)
                pass_down(node.right, k - 1)
                return k - 1

            left_distance = traverse(node.left)
            right_distance = traverse(node.right)

            if left_distance != float('inf') or right_distance != float('inf'):
                if left_distance == 0 or right_distance == 0:
                    result.append(node.value)
                    return float('inf')
                if left_distance != float('inf'):
                    pass_down(node.right, min(left_distance, right_distance) - 1)
                else:
                    pass_down(node.left, min(left_distance, right_distance) - 1)
                return min(left_distance, right_distance) - 1
        return float('inf')

    traverse(root)
    return result


def pruneTree(root: Optional[Node]) -> Optional[Node]:
    def traverse(node):
        if node:
            node.left = traverse(node.left)
            node.right = traverse(node.right)
            if not node.left and not node.right and node.val == 0:
                return None
        return node

    return traverse(root)


def minDiffInBST(root: Optional[Node]) -> int:
    def traverse(node, low, high):
        if node:
            left = traverse(node.left, low, node.value)
            right = traverse(node.right, node.value, high)
            return min(left, right, abs(high - node.val), abs(low - node.val))
        return float('inf')

    return traverse(root, float('inf'), float('inf'))


def insertIntoBST(root: Optional[Node], val: int) -> Optional[Node]:
    def traverse(node):
        if not node:
            return Node(val)
        elif val > node.value:
            node.right = traverse(node.right)
        else:
            node.left = traverse(node.left)
        return node

    return traverse(root)
