from typing import Optional
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    number_one = ""
    number_two = ""
    while l1:
        number_one += str(l1.val)
        l1 = l1.next
    while l2:
        number_two += str(l2.val)
        l2 = l2.next

    val = str(int(number_one[::-1]) + int(number_two[::-1]))[::-1]

    temp_head = ListNode(0, None)
    pointer = temp_head
    for value in val:
        pointer.next = ListNode(int(value), None)
        pointer = pointer.next
    return temp_head.next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    temp_head = ListNode(0, None)
    pointer = temp_head

    while list1 and list2:
        if list1.val < list2.val:
            pointer.next = list1
            list1 = list1.next
        else:
            pointer.next = list2
            list2 = list2.next
        pointer = pointer.next

    while list1:
        pointer.next = list1
        list1 = list1.next
        pointer = pointer.next

    while list2:
        pointer.next = list2
        list2 = list2.next
        pointer = pointer.next

    return temp_head.next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    temp_head = ListNode(0, head)
    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        head = head.next
    return temp_head.next


class CacheNode:
    def __init__(self, key=None, value=None, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

    def remove_from_current_position(self):
        self.prev.next, self.next.prev = self.next, self.prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_size = 0
        self.cache = collections.defaultdict(CacheNode)
        self.tail = CacheNode()
        self.head = CacheNode()
        self.tail.next, self.head.prev = self.head, self.tail

    def _add_to_head(self, cache_node: CacheNode):
        self.head.prev.next, self.head.prev, cache_node.prev, cache_node.next = cache_node, cache_node, self.head.prev, self.head

    def _remove_from_tail(self):
        del self.cache[self.tail.next.key]
        self.tail.next, self.tail.next.prev = self.tail.next.next, self.tail

    def get(self, key: int) -> int:
        if key in self.cache:
            cache_node = self.cache[key]
            cache_node.remove_from_current_position()
            self._add_to_head(cache_node)
            return cache_node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            cache_node = self.cache[key]
            cache_node.remove_from_current_position()
            self._add_to_head(cache_node)
            cache_node.value = value
        else:
            cache_node = CacheNode(key, value, None, None)
            self.cache[key] = cache_node
            if self.current_size == self.capacity:
                self._remove_from_tail()
            else:
                self.current_size += 1
            self._add_to_head(cache_node)

    def delete(self, key):
        if key in self.cache:
            cache_node = self.cache[key]
            cache_node.remove_from_current_position()
            del self.cache[key]
            self.current_size -= 1


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if not head:
        return None

    temp_head = ListNode()
    temp_head.next, pointer = head, temp_head

    while pointer and pointer.next:
        if pointer.next.val == val:
            pointer.next = pointer.next.next
        pointer = pointer.next
    return temp_head.next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    previous = None
    while head:
        head.next, head, previous = previous, head.next, head
    return previous


def deleteNode(head, value):
    temp_head = ListNode()
    temp_head.next, pointer = head, temp_head
    while pointer:
        if pointer.next and pointer.next.val == value:
            pointer.next = pointer.next.next
        pointer = pointer.next
    return temp_head.next


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    temp_head_odd, temp_head_even = ListNode(), ListNode()
    head_pointer_odd, head_pointer_even = temp_head_odd, temp_head_even
    while head:
        if head.val % 2 == 0:
            head_pointer_even.next = head
            head_pointer_even = head_pointer_even.next
        else:
            head_pointer_odd.next = head
            head_pointer_odd = head_pointer_odd.next
        head = head.next
    head_pointer_even.next, head_pointer_odd.next = None, temp_head_even.next
    return temp_head_odd.next


from typing import List


def numComponents(head: Optional[ListNode], nums: List[int]) -> int:
    nums = set(nums)

    def traverse(prev_a_component, node):
        result = 0
        if node:
            if node.val in nums and not prev_a_component:
                result += 1
            result += traverse(node.val in nums, node.next)
        return result

    return traverse(False, head)
