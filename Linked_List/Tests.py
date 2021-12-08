import unittest
import Linked_List.Solutions as linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_builder(a_list: list) -> ListNode:
    head = None
    temp = None
    for element in a_list:
        a_list_node = ListNode(element)
        if not head:
            head = a_list_node
        else:
            temp.next = a_list_node
        temp = a_list_node
    return head


def print_list(head: ListNode):
    while head:
        print(head.val)
        head = head.next


class CustomAssertion:
    def assert_compare_lists(self, node_1: ListNode, node_2: ListNode):
        while node_1 or node_2:
            if not node_1 or not node_2 or node_1.val != node_2.val:
                raise AssertionError('lists are not equal')
            node_1 = node_1.next
            node_2 = node_2.next


class SolutionsTest(unittest.TestCase, CustomAssertion):
    def test_add_two_numbers(self):
        l1 = list_builder([2, 4, 3])
        l2 = list_builder([5, 6, 4])
        output = list_builder([7, 0, 8])
        self.assert_compare_lists(linked_list.add_two_numbers(l1, l2), output)
        l1 = list_builder([0])
        l2 = list_builder([0])
        output = list_builder([0])
        self.assert_compare_lists(linked_list.add_two_numbers(l1, l2), output)
        l1 = list_builder([9, 9, 9, 9, 9, 9, 9])
        l2 = list_builder([9, 9, 9, 9])
        output = list_builder([8, 9, 9, 9, 0, 0, 0, 1])
        self.assert_compare_lists(linked_list.add_two_numbers(l1, l2), output)
