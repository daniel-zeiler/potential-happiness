from typing import List, Optional

from Linked_List.Problems import ListNode

"""
Here i'll maintain two pointers.  One pointing to the end, the other the beginning.  I'll iteratively calculate the
area of this range.  Area = min(x1,x2) * (x2-x1+1).  I'll then increment or decrement the pointers based upon
which one has a lower value as we're trying to maximize the area.
"""


def maxArea(height: List[int]) -> int:
    pointer_a = 0
    pointer_b = len(height) - 1
    max_area = 0
    while pointer_a < pointer_b:
        area = min(height[pointer_b], height[pointer_a]) * (pointer_b - pointer_a)
        max_area = max(area, max_area)
        if height[pointer_b] < height[pointer_a]:
            pointer_b -= 1
        else:
            pointer_a += 1

    return max_area


"""
Here i'll create a dummy head for ease of operations.  I'll create two pointer and increment the second by n.  I'll then 
increment them both in parallel until I reach ther end with the second.  I'll then skip the next pointer on the first
pointer.  I'll return dummy head next.
"""


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy_head = ListNode(None)
    dummy_head.next = head
    pointer_a = dummy_head
    pointer_b = dummy_head

    for i in range(n + 1):
        pointer_b = pointer_b.next

    while pointer_b:
        pointer_a = pointer_a.next
        pointer_b = pointer_b.next
    pointer_a.next = pointer_a.next.next

    return dummy_head.next


"""
Here i'll maintain a write pointer and a read pointer.  I'll iterate throughout the nums array and if it's not a dupe
then i'll write to the head.  I'll continue until I each the end.  I'll return the write pointer index.
"""


def removeDuplicates(nums: List[int]) -> int:
    write_pointer = 1
    for read_pointer, num in enumerate(nums):
        if read_pointer and num != nums[read_pointer - 1]:
            nums[write_pointer] = num
            write_pointer += 1
    return write_pointer


"""
Here I will maintain a write pointer and a read pointer, I'll iterate and when I encounter a val that doesn't match
i'll write to head.  Else i'll skip it.  I'll return the write pointer index.
"""


def removeElement(nums: List[int], val: int) -> int:
    write_pointer = 0
    for read_pointer, num in enumerate(nums):
        if num != val:
            nums[write_pointer] = num
            write_pointer += 1
    return write_pointer
