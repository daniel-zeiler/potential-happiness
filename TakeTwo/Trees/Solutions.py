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
    pass
