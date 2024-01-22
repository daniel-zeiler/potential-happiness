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


def removeDuplicates(nums: List[int]) -> int:
    read_pointer, write_pointer = 1, 0
    while read_pointer < len(nums):
        if nums[read_pointer] != nums[write_pointer]:
            write_pointer += 1
            nums[write_pointer] = nums[read_pointer]
        read_pointer += 1
    return write_pointer + 1


def removeElement(nums: List[int], val: int) -> int:
    read_pointer, write_pointer = 0, 0
    while read_pointer < len(nums):
        number = nums[read_pointer]
        if number != val:
            nums[write_pointer] = number
            write_pointer += 1
        read_pointer += 1
    return write_pointer


def sortColors(nums: List[int]) -> None:
    write_pointer, read_pointer = 0, 0
    while read_pointer < len(nums):
        if nums[read_pointer] == 0:
            nums[write_pointer], nums[read_pointer] = nums[read_pointer], nums[write_pointer]
            write_pointer += 1
        read_pointer += 1

    read_pointer = write_pointer
    while read_pointer < len(nums):
        if nums[read_pointer] == 1:
            nums[write_pointer], nums[read_pointer] = nums[read_pointer], nums[write_pointer]
            write_pointer += 1
        read_pointer += 1


def isPalindrome(s: str) -> bool:
    start_pointer, end_pointer = 0, len(s) - 1
    while start_pointer < end_pointer:
        if s[start_pointer] != s[end_pointer]:
            return False
        start_pointer += 1
        end_pointer -= 1
    return True
