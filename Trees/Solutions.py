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
    pass
