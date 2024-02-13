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
        start_character = s[start_pointer]
        end_character = s[end_pointer]
        if start_character.isalpha() and end_character.isalpha():
            if start_character.lower() != end_character.lower():
                return False
            start_pointer += 1
            end_pointer -= 1
        elif not start_character.isalpha():
            start_pointer += 1
        else:
            end_pointer -= 1
    return True


def moveZeroes(nums: List[int]) -> None:
    read_pointer, write_pointer = 0, 0
    while read_pointer < len(nums):
        read_character = nums[read_pointer]
        if read_character != 0:
            nums[read_pointer], nums[write_pointer] = nums[write_pointer], nums[read_pointer]
            write_pointer += 1
        read_pointer += 1


def reverseString(s: List[str]) -> None:
    start_pointer, end_pointer = 0, len(s) - 1
    while start_pointer < end_pointer:
        s[start_pointer], s[end_pointer] = s[end_pointer], s[start_pointer]
        start_pointer += 1
        end_pointer -= 1


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1).intersection(set(nums2)))


def isSubsequence(s: str, t: str) -> bool:
    len_s = len(s)
    len_t = len(t)

    def is_subsequence(word_one, word_two) -> bool:
        pointer_one = 0
        for i, character in enumerate(word_two):
            if character == word_one[pointer_one]:
                pointer_one += 1
                if pointer_one == len(word_one):
                    return True
        return False

    if len_s < len_t:
        return is_subsequence(s, t)
    return is_subsequence(t, s)


def reverseWords(s: str) -> str:
    result = ""
    for word in s.split(" "):
        if result:
            result += " "
        result += word[::-1]
    return result


def validPalindrome(s: str) -> bool:
    pointer_a, pointer_b = 0, len(s) - 1

    def validate_palindrom_helper(index_one, index_two, skip_allowed):
        while index_one < index_two:
            if s[index_one] != s[index_two]:
                if not skip_allowed:
                    return False
                return validate_palindrom_helper(index_one + 1, index_two, False) or validate_palindrom_helper(
                    index_one, index_two - 1, False)
            index_one += 1
            index_two -= 1
        return True

    return validate_palindrom_helper(pointer_a, pointer_b, True)
