from typing import List, Optional
from TakeTwo.LinkedList.Tests import ListNode


def max_area(height: List[int]) -> int:
    pointer_a = 0
    pointer_b = len(height) - 1
    max_area = 0
    while pointer_a < pointer_b:
        a_height = height[pointer_a]
        b_height = height[pointer_b]
        area = min(a_height, b_height) * (pointer_b - pointer_a)
        max_area = max(area, max_area)
        if a_height < b_height:
            pointer_a += 1
        else:
            pointer_b -= 1
    return max_area


# TODO FIX THIS AFTER DOING LINKED LISTS
def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    temp_head = ListNode(0, head)
    pointer_a = head
    for _ in range(n):
        pointer_a = pointer_a.next
    while pointer_a:
        head = head.next
        pointer_a = pointer_a.next

    head.next = head.next.next
    return temp_head.next
