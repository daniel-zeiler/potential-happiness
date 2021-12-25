from typing import List, Optional

from Linked_List.Problems import ListNode


def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    sum_so_far = sum(arr[:k])

    result = 0

    if sum_so_far / k >= threshold:
        result += 1

    pointer_a, pointer_b = 0, k

    while pointer_b < len(arr):
        sum_so_far += -arr[pointer_a] + arr[pointer_b]
        if sum_so_far / k >= threshold:
            result += 1
        pointer_a += 1
        pointer_b += 1
    return result


def maxArea(height: List[int]) -> int:
    max_area = 0
    pointer_a = 0
    pointer_b = len(height) - 1

    while pointer_a != pointer_b:
        area = min(height[pointer_b], height[pointer_a]) * (pointer_b - pointer_a)
        max_area = max(area, max_area)

        if height[pointer_b] < height[pointer_a]:
            pointer_b -= 1
        else:
            pointer_a += 1

    return max_area


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy_head = ListNode()
    dummy_head.next = head

    slow_pointer, fast_pointer = dummy_head, dummy_head

    for _ in range(n):
        fast_pointer = fast_pointer.next

    while fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

    slow_pointer.next = slow_pointer.next.next

    return dummy_head.next
