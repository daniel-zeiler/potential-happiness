import unittest
import Two_Pointers.Solutions as two_pointer
import Linked_List.Tests as linked_list


class SolutionsTest(unittest.TestCase, linked_list.CustomAssertion):
    def test_max_area(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        output = 49
        self.assertEqual(output, two_pointer.maxArea(height))
        height = [1, 1]
        output = 1
        self.assertEqual(output, two_pointer.maxArea(height))
        height = [4, 3, 2, 1, 4]
        output = 16
        self.assertEqual(output, two_pointer.maxArea(height))
        height = [1, 2, 1]
        output = 2
        self.assertEqual(output, two_pointer.maxArea(height))

    def test_remove_nth_from_end(self):
        input = linked_list.list_builder([1, 2, 3, 4, 5])
        n = 2
        output = linked_list.list_builder([1, 2, 3, 5])
        self.assert_compare_lists(output, two_pointer.removeNthFromEnd(input, n))
        input = linked_list.list_builder([1, 2])
        n = 1
        output = linked_list.list_builder([1])
        self.assert_compare_lists(output, two_pointer.removeNthFromEnd(input, n))
        input = linked_list.list_builder([1])
        n = 1
        output = linked_list.list_builder([])
        self.assert_compare_lists(output, two_pointer.removeNthFromEnd(input, n))


if __name__ == '__main__':
    unittest.main()
