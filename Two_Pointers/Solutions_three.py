import math
from typing import List, Optional
from Linked_List.Problems import ListNode


def maxArea(height: List[int]) -> int:
    pointer_a = 0
    pointer_b = len(height) - 1
    max_area = 0
    while pointer_a != pointer_b:
        height_a = height[pointer_a]
        height_b = height[pointer_b]
        max_area = max(max_area, min(height_b, height_a) * (pointer_b - pointer_a))
        if height_a < height_b:
            pointer_a += 1
        elif height_a > height_b:
            pointer_b -= 1
        elif height[pointer_a + 1] > height[pointer_b - 1]:
            pointer_a += 1
        else:
            pointer_b -= 1
    return max_area


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    temp_head = ListNode()
    temp_head.next = head
    cursor = temp_head

    for i in range(n):
        head = head.next

    while head:
        cursor = cursor.next
        head = head.next
    cursor.next = cursor.next.next
    return temp_head.next


def removeDuplicates(nums: List[int]) -> int:
    write_pointer = 0
    for read_pointer, number in enumerate(nums):
        if not read_pointer:
            write_pointer += 1
        if read_pointer:
            if number != nums[write_pointer - 1]:
                nums[write_pointer] = number
                write_pointer += 1
    return write_pointer


def removeElement(nums: List[int], val: int) -> int:
    write_pointer = 0
    for read_pointer, number in enumerate(nums):
        if number != val:
            nums[write_pointer] = number
            write_pointer += 1
    return write_pointer


def sortColors(nums: List[int]) -> None:
    zero_pointer = 0
    for read_pointer, number in enumerate(nums):
        if number == 0:
            nums[read_pointer], nums[zero_pointer] = nums[zero_pointer], nums[read_pointer]
            zero_pointer += 1
    one_pointer = zero_pointer
    for read_pointer, number in enumerate(nums):
        read_pointer += zero_pointer - 1
        if number == 1:
            nums[read_pointer], nums[one_pointer] = nums[one_pointer], nums[read_pointer]
            one_pointer += 1


def isPalindrome(s: str) -> bool:
    pointer_a, pointer_b = 0, len(s) - 1
    while pointer_a < pointer_b:
        if s[pointer_a].isalpha() and s[pointer_b].isalpha():
            if s[pointer_a].lower() != s[pointer_b].lower():
                return False
            pointer_a += 1
            pointer_b -= 1
        elif s[pointer_a].isalpha():
            pointer_b -= 1
        elif s[pointer_b].isalpha():
            pointer_a += 1
        else:
            pointer_b -= 1
            pointer_a += 1
    return True


def moveZeroes(nums: List[int]) -> None:
    write_pointer = 0
    for read_pointer, number in enumerate(nums):
        if number != 0:
            nums[write_pointer], nums[read_pointer] = nums[read_pointer], nums[write_pointer]
            write_pointer += 1


def reverseString(s: List[str]) -> None:
    end_pointer = len(s) - 1
    start_pointer = 0
    while start_pointer < end_pointer:
        s[end_pointer], s[start_pointer] = s[start_pointer], s[end_pointer]
        start_pointer += 1
        end_pointer -= 1


def isSubsequence(s: str, t: str) -> bool:
    s_pointer = 0
    for character in t:
        if character == s[s_pointer]:
            s_pointer += 1
            if s_pointer >= len(s):
                return True
    return False


def reverseWords(s: str) -> str:
    result = ""
    stack = []
    for character in s:
        stack.append(character)
        if stack[-1] == " ":
            stack.pop()
            while stack:
                result += stack.pop()
            result += " "
    while stack:
        result += stack.pop()
    return result


def validPalindrome(s: str) -> bool:
    pointer_a = 0
    pointer_b = len(s) - 1
    while pointer_a < pointer_b:
        if s[pointer_a] != s[pointer_b]:
            mid_point = math.floor(pointer_b - pointer_a / 2)
            print(s[pointer_a + 1:mid_point:-1])
            print(s[mid_point:pointer_b+1])
            print("<><><><")
            print(s[pointer_a:mid_point:-1])
            print(s[mid_point:pointer_b])
            return s[pointer_a + 1:mid_point:-1] == s[mid_point:pointer_b+1] or s[pointer_a:mid_point:-1] == s[mid_point:pointer_b]
        pointer_a+=1
        pointer_b-=1
    return True