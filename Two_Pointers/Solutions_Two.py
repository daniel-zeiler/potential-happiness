import collections
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


def sortColors(nums: List[int]) -> None:
    zero_pointer = 0
    for read_pointer, num in enumerate(nums):
        if num == 0:
            nums[zero_pointer], nums[read_pointer] = nums[read_pointer], nums[zero_pointer]
            zero_pointer += 1
    one_pointer = zero_pointer
    for read_pointer in range(one_pointer, len(nums)):
        num = nums[read_pointer]
        if num == 1:
            nums[one_pointer], nums[read_pointer] = nums[read_pointer], nums[one_pointer]
            one_pointer += 1


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))


def isSubsequence(s: str, t: str) -> bool:
    result = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]

    for x in range(len(t) + 1):
        for y in range(len(s) + 1):
            if x == 0 or y == 0:
                continue
            char_s = s[y - 1]
            char_t = t[x - 1]
            if char_s == char_t:
                result[x][y] = result[x - 1][y - 1] + 1
            else:
                result[x][y] = max(result[x - 1][y], result[x][y - 1])
    return result[-1][-1] == len(s)


def reverseWords(s):
    s = list(s)
    pointer_a = 0
    for i, value in enumerate(s):
        if value == ' ':
            s[pointer_a:i] = s[pointer_a:i][::-1]
            pointer_a = i + 1
    s[pointer_a:len(s)] = s[pointer_a:len(s)][::-1]
    return ''.join(s)


def partitionLabels(s: str) -> List[int]:
    partitions = collections.defaultdict(list)
    for index, character in enumerate(s):
        if character not in partitions:
            partitions[character] = [index, index]
        else:
            partitions[character][1] = index
    partitions = sorted(list(partitions.values()), key=lambda x: x[0])

    merged = []

    for partition in partitions:
        if not merged:
            merged.append(partition)
        elif merged[-1][1] > partition[0]:
            merged[-1][1] = max(merged[-1][1], partition[1])
        else:
            merged.append(partition)

    return [x[1] - x[0] + 1 for x in merged]
