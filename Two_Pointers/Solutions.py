import collections
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
    result = []
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    pointer_1 = 0
    pointer_2 = 0
    while pointer_1 < len(nums1) and pointer_2 < len(nums2):
        if nums1[pointer_1] == nums2[pointer_2]:
            if not result or result[-1] != nums1[pointer_1]:
                result.append(nums1[pointer_1])
        if nums1[pointer_1] <= nums2[pointer_2]:
            pointer_1 += 1
        else:
            pointer_2 += 1

    return result


def isSubsequence(s: str, t: str) -> bool:
    s_pointer = 0
    t_pointer = 0
    while t_pointer < len(t):
        if s[s_pointer] == t[t_pointer]:
            s_pointer += 1
        if s_pointer == len(s):
            return True
        t_pointer += 1
    return False


def reverseWords(s: str) -> str:
    s = list(s)
    word_pointer = 0
    for read_pointer, character in enumerate(s):
        if character == ' ':
            s[word_pointer:read_pointer] = s[word_pointer:read_pointer][::-1]
            word_pointer = read_pointer + 1
    s[word_pointer:len(s)] = s[word_pointer:len(s)][::-1]
    return ''.join(s)


def validPalindrome(s: str) -> bool:
    def check_palindrome(start_pointer, end_pointer):
        while start_pointer <= end_pointer:
            if s[start_pointer] != s[end_pointer]:
                return False
            start_pointer += 1
            end_pointer -= 1
        return True

    start_pointer = 0
    end_pointer = len(s) - 1
    while start_pointer <= end_pointer:
        if s[start_pointer] != s[end_pointer]:
            return check_palindrome(start_pointer + 1, end_pointer) or check_palindrome(start_pointer,
                                                                                        end_pointer - 1)
        start_pointer += 1
        end_pointer -= 1
    return True


def partitionLabels(s: str) -> List[int]:
    letter_map = collections.defaultdict(list)
    for index, letter in enumerate(s):
        if letter not in letter_map:
            letter_map[letter] = [index, index]
        else:
            letter_map[letter][1] = index

    label_ranges = sorted(letter_map.values(), key=lambda x: x[0])
    partitions = []

    for index, label_range in enumerate(label_ranges):
        if not partitions:
            partitions.append(label_range)
        else:
            if label_range[0] <= partitions[-1][1]:
                partitions[-1][1] = max(label_range[1], partitions[-1][-1])
            else:
                partitions.append(label_range)

    return [x[1] - x[0] + 1 for x in partitions]


def sortArrayByParity(nums: List[int]) -> List[int]:
    even_pointer = 0
    for read_pointer, num in enumerate(nums):
        if num % 2 == 0:
            nums[even_pointer], nums[read_pointer] = nums[read_pointer], nums[even_pointer]
            even_pointer += 1
    return nums


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    firstList.sort(key=lambda x: x[0])
    secondList.sort(key=lambda x: x[0])
    first_pointer = 0
    second_pointer = 0

    intersection = []

    while first_pointer < len(firstList) and second_pointer < len(secondList):

        if secondList[second_pointer][0] <= firstList[first_pointer][0] <= secondList[second_pointer][1]:
            intersection.append(
                [firstList[first_pointer][0], min(firstList[first_pointer][1], secondList[second_pointer][1])])
        if firstList[first_pointer][0] <= secondList[second_pointer][0] <= firstList[first_pointer][1]:
            intersection.append(
                [secondList[second_pointer][0], min(firstList[first_pointer][1], secondList[second_pointer][1])])
        if firstList[first_pointer][0] < secondList[second_pointer][0]:
            first_pointer += 1
        else:
            second_pointer += 1

    return intersection


def numOfSubarraysTwo(arr: List[int], k: int, threshold: int) -> int:
    result = 0
    if not arr or k > len(arr):
        return result

    sum_in_sub_array = sum(arr[:k])
    if sum_in_sub_array / k >= threshold:
        result += 1

    pointer_a, pointer_b = 0, k

    while pointer_b < len(arr):
        sum_in_sub_array += -arr[pointer_a] + arr[pointer_b]
        if sum_in_sub_array / k >= threshold:
            result += 1

        pointer_b += 1
        pointer_a += 1

    return result
