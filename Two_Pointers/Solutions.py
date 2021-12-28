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


def removeDuplicates(nums: List[int]) -> int:
    write_pointer = 0
    read_pointer = 0
    while read_pointer < len(nums):
        if read_pointer > 0:
            if nums[read_pointer] != nums[read_pointer - 1]:
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1
        else:
            write_pointer += 1
        read_pointer += 1
    return write_pointer


def removeElement(nums: List[int], val: int) -> int:
    write_pointer = 0
    for i, num in enumerate(nums):
        if num != val:
            nums[write_pointer] = num
            write_pointer += 1
    return write_pointer


def sortColors(nums: List[int]) -> None:
    write_pointer = 0
    for index, num in enumerate(nums):
        if num == 0:
            nums[index], nums[write_pointer] = nums[write_pointer], nums[index]
            write_pointer += 1

    write_pointer_two = 0
    for index, num in enumerate(nums[write_pointer:]):
        if num == 1:
            nums[write_pointer + index], nums[write_pointer_two + write_pointer] = nums[
                                                                                       write_pointer + write_pointer_two], \
                                                                                   nums[write_pointer + index]
            write_pointer_two += 1


def isPalindrome(s: str) -> bool:
    start_pointer = 0
    end_pointer = len(s) - 1
    while start_pointer <= end_pointer:
        if not s[start_pointer].isalpha():
            start_pointer += 1
        elif not s[end_pointer].isalpha():
            end_pointer -= 1
        elif s[start_pointer].lower() != s[end_pointer].lower():
            return False
        else:
            start_pointer += 1
            end_pointer -= 1
    return True


def moveZeroes(nums: List[int]) -> None:
    write_pointer = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[i], nums[write_pointer] = nums[write_pointer], nums[i]
            write_pointer += 1


def reverseString(s: List[str]) -> None:
    start_pointer = 0
    end_pointer = len(s) - 1
    while start_pointer <= end_pointer:
        s[start_pointer], s[end_pointer] = s[end_pointer], s[start_pointer]
        start_pointer += 1
        end_pointer -= 1


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    pass
