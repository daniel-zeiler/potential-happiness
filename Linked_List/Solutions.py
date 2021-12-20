import collections
from typing import Optional


class ListNode:
    def __init__(self, val=0, key=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry_over = False
    head = l1
    while l1 and l2:
        l1.val += l2.val
        if carry_over:
            l1.val += 1
            carry_over = False
        if l1.val >= 10:
            l1.val = l1.val % 10
            carry_over = True
        l1 = l1.next
        l2 = l2.next

    if l2:
        l1.next = l2

    while carry_over and l1:
        if l1.val:
            l1.val += 1
        if l1.val >= 10:
            l1.val = l1.val % 10
            carry_over = True
        else:
            carry_over = False
        if carry_over and l1.next is None:
            l1.next = ListNode(1)
            carry_over = False
        l1 = l1.next

    return head


"""
Set up dummy head before our head node.
Attach dummy head to head node.
Create a cursor variable pointing to our dummy head.

increased head node to nth location in the list

iterate cursor and head node in parellel until the head reaches the end of the list.

The cursor is now n away from the end of the list.

Set the cursors next value past the one we're deleting.

Return the original head of our list.

"""


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy_head = ListNode(None)
    dummy_head.next = head
    cursor = dummy_head

    for _ in range(n - 1):
        head = head.next

    while head and head.next:
        cursor = cursor.next
        head = head.next

    cursor.next = cursor.next.next
    return dummy_head.next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = ListNode(None)
    dummy_head.next = list1
    pointer = dummy_head
    while list1 and list2:
        if list2.val < list1.val:
            pointer.next = list2
            list2 = list2.next
        else:
            pointer.next = list1
            list1 = list1.next
        pointer = pointer.next

    if list1:
        pointer.next = list1
    if list2:
        pointer.next = list2

    return dummy_head.next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = ListNode(None)
    dummy_head.next = head
    pointer_begin = dummy_head
    while head:
        if pointer_begin.val == head.val:
            pointer_begin.next = head.next
        else:
            pointer_begin = pointer_begin.next
        head = head.next
    return dummy_head.next


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    pass


class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.key_map = collections.defaultdict(ListNode)
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove_from_tail(self):
        res = self.tail.prev
        self.remove_node(res)
        return res

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        else:
            node = self.key_map[key]
            self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            node = self.key_map[key]
            self.move_to_head(node)
            node.val = value
        else:
            node = ListNode(key=key, val=value)
            self.key_map[key] = node
            if len(self.key_map) > self.capacity:
                del self.key_map[self.tail.prev.key]
                self.remove_from_tail()

            self.add_node(node)
