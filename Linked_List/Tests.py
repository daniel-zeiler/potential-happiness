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
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


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

    def test_remove_nth_from_end(self):
        head = list_builder([1, 2, 3, 4, 5])
        n = 2
        output = list_builder([1, 2, 3, 5])
        self.assert_compare_lists(linked_list.remove_nth_from_end(head, n), output)
        head = list_builder([1])
        n = 1
        output = list_builder([])
        self.assert_compare_lists(linked_list.remove_nth_from_end(head, n), output)
        head = list_builder([1, 2])
        n = 1
        output = list_builder([1])
        self.assert_compare_lists(linked_list.remove_nth_from_end(head, n), output)

    def test_merge_two_lists(self):
        list1 = list_builder([1, 2, 4])
        list2 = list_builder([1, 3, 4])
        output = list_builder([1, 1, 2, 3, 4, 4])
        self.assert_compare_lists(linked_list.merge_two_lists(list1, list2), output)
        list1 = list_builder([])
        list2 = list_builder([])
        output = list_builder([])
        self.assert_compare_lists(linked_list.merge_two_lists(list1, list2), output)
        list1 = list_builder([])
        list2 = list_builder([0])
        output = list_builder([0])
        self.assert_compare_lists(linked_list.merge_two_lists(list1, list2), output)

    def test_delete_duplicates(self):
        head = list_builder([1, 1, 2])
        output = list_builder([1, 2])
        self.assert_compare_lists(linked_list.delete_duplicates(head), output)
        head = list_builder([1, 1, 2, 3, 3])
        output = list_builder([1, 2, 3])
        self.assert_compare_lists(linked_list.delete_duplicates(head), output)

    def test_LRU_cache(self):
        lru_cache = linked_list.LRUCache(2)
        lru_cache.put(1, 1)
        lru_cache.put(2, 2)
        self.assertEqual(1, lru_cache.get(1))
        lru_cache.put(3, 3)
        self.assertEqual(-1, lru_cache.get(2))
        lru_cache.put(4, 4)
        self.assertEqual(-1, lru_cache.get(1))
        self.assertEqual(3, lru_cache.get(3))
        self.assertEqual(4, lru_cache.get(4))


if __name__ == '__main__':
    unittest.main()
