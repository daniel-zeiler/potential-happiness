from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry_over = False
    head = None
    temp = False
    while l1 or l2:
        if l1 and l2:
            new_val = l1.val + l2.val
            if carry_over:
                new_val += 1
