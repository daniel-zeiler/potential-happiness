import unittest

import TakeTwo.TwoPointer.Solutions as two_pointer
import TakeOne.Two_Pointers.Solutions_Two as two_pointer_two
import TakeOne.Two_Pointers.Solutions_three as two_pointer_three
import TakeTwo.LinkedList.Tests as linked_list


def print_list(head: linked_list.ListNode):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


class SolutionsTest(unittest.TestCase, linked_list.CustomAssertion):
    def test_max_area(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        output = 49
        self.assertEqual(output, two_pointer.max_area(height))
        height = [1, 1]
        output = 1
        self.assertEqual(output, two_pointer.max_area(height))
        height = [4, 3, 2, 1, 4]
        output = 16
        self.assertEqual(output, two_pointer.max_area(height))
        height = [1, 2, 1]
        output = 2
        self.assertEqual(output, two_pointer.max_area(height))

    def test_remove_nth_from_end(self):
        input = linked_list.list_builder([1, 2, 3, 4, 5])
        n = 2
        output = linked_list.list_builder([1, 2, 3, 5])
        linked_list.print_list(two_pointer.remove_nth_from_end(input, n))
        self.assert_compare_lists(output, two_pointer.remove_nth_from_end(input, n))
        input = linked_list.list_builder([1, 2])
        n = 1
        output = linked_list.list_builder([1])
        self.assert_compare_lists(output, two_pointer.remove_nth_from_end(input, n))
        input = linked_list.list_builder([1])
        n = 1
        output = linked_list.list_builder([])
        self.assert_compare_lists(output, two_pointer.remove_nth_from_end(input, n))

    def test_remove_duplicates(self):
        nums = [1, 1, 2]
        output = 2
        self.assertEqual(output, two_pointer_three.removeDuplicates(nums))
        self.assertListEqual([1, 2], nums[:2])
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        output = 5
        self.assertEqual(output, two_pointer_three.removeDuplicates(nums))
        self.assertListEqual([0, 1, 2, 3, 4], nums[:5])

    def test_remove_elements(self):
        nums = [3, 2, 2, 3]
        val = 3
        output = 2
        output_2 = [2, 2]
        self.assertEqual(output, two_pointer_three.removeElement(nums, val))
        self.assertCountEqual(output_2, nums[:2])
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        output = 5
        output_2 = [0, 1, 4, 0, 3]
        self.assertEqual(output, two_pointer_three.removeElement(nums, val))
        self.assertCountEqual(output_2, nums[:5])

    def test_sort_color(self):
        nums = [2, 0, 2, 1, 1, 0]
        output = [0, 0, 1, 1, 2, 2]
        two_pointer_three.sortColors(nums)
        self.assertListEqual(output, nums)
        nums = [2, 0, 1]
        output = [0, 1, 2]
        two_pointer_three.sortColors(nums)
        self.assertListEqual(output, nums)
        nums = [0]
        output = [0]
        two_pointer_three.sortColors(nums)
        self.assertListEqual(output, nums)
        nums = [1]
        output = [1]
        two_pointer_three.sortColors(nums)
        self.assertListEqual(output, nums)

    def test_is_palindrome(self):
        s = "A man, a plan, a canal: Panama"
        output = True
        self.assertEqual(output, two_pointer_three.isPalindrome(s))
        s = "race a car"
        output = False
        self.assertEqual(output, two_pointer_three.isPalindrome(s))
        s = " "
        output = True
        self.assertEqual(output, two_pointer_three.isPalindrome(s))

    def test_move_zeros(self):
        nums = [0, 1, 0, 3, 12]
        output = [1, 3, 12, 0, 0]
        two_pointer_three.moveZeroes(nums)
        self.assertListEqual(output, nums)

    def test_reverse_string(self):
        s = ["h", "e", "l", "l", "o"]
        output = ["o", "l", "l", "e", "h"]
        two_pointer_three.reverseString(s)
        self.assertListEqual(output, s)
        s = ["H", "a", "n", "n", "a", "h"]
        output = ["h", "a", "n", "n", "a", "H"]
        two_pointer_three.reverseString(s)
        self.assertListEqual(output, s)

    def test_intersection(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        output = [2]
        self.assertListEqual(output, two_pointer_two.intersection(nums1, nums2))
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        output = [4, 9]
        self.assertCountEqual(output, two_pointer_two.intersection(nums1, nums2))

    def test_is_subsequence(self):
        s = "abc"
        t = "ahbgdc"
        output = True
        self.assertEqual(output, two_pointer_three.isSubsequence(s, t))
        s = "axc"
        t = "ahbgdc"
        output = False
        self.assertEqual(output, two_pointer_three.isSubsequence(s, t))

    def test_reverse(self):
        s = "Let's take LeetCode contest"
        output = "s'teL ekat edoCteeL tsetnoc"
        self.assertEqual(output, two_pointer_three.reverseWords(s))
        s = "God Ding"
        output = "doG gniD"
        self.assertEqual(output, two_pointer_three.reverseWords(s))

    def test_valid_palindrome(self):
        s = "aba"
        self.assertEqual(True, two_pointer.validPalindrome(s))
        s = "abca"
        self.assertEqual(True, two_pointer.validPalindrome(s))
        s = "abc"
        self.assertEqual(False, two_pointer.validPalindrome(s))

    def test_partition_labels(self):
        s = "ababcbacadefegdehijhklij"
        output = [9, 7, 8]
        self.assertListEqual(output, two_pointer_two.partitionLabels(s))
        s = "eccbbbbdec"
        output = [10]
        self.assertListEqual(output, two_pointer_two.partitionLabels(s))

    def test_sort_array_by_parity(self):
        nums = [3, 1, 2, 4]
        output = [2, 4, 3, 1]
        self.assertListEqual(output, two_pointer.sortArrayByParity(nums))

    def test_interval_intersection(self):
        firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
        secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
        output = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
        self.assertListEqual(output, two_pointer.intervalIntersection(firstList, secondList))
        firstList = [[1, 3], [5, 9]]
        secondList = []
        output = []
        self.assertListEqual(output, two_pointer.intervalIntersection(firstList, secondList))
        firstList = []
        secondList = [[4, 8], [10, 12]]
        output = []
        self.assertListEqual(output, two_pointer.intervalIntersection(firstList, secondList))
        firstList = [[1, 7]]
        secondList = [[3, 10]]
        output = [[3, 7]]
        self.assertListEqual(output, two_pointer.intervalIntersection(firstList, secondList))

    def test_num_of_sub_arrays(self):
        arr = [2, 2, 2, 2, 5, 5, 5, 8]
        k = 3
        threshold = 4
        output = 3
        self.assertEqual(output, two_pointer.numOfSubarraysTwo(arr, k, threshold))
        self.assertEqual(output, two_pointer.numOfSubarrays(arr, k, threshold))

    def test_min_pair_sum(self):
        nums = [3, 5, 2, 3]
        output = 7
        self.assertEqual(output, two_pointer.minPairSum(nums))
        nums = [3, 5, 4, 2, 4, 6]
        output = 8
        self.assertEqual(output, two_pointer.minPairSum(nums))


if __name__ == '__main__':
    unittest.main()
