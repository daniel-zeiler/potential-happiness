import binarytree as binarytree
import unittest
import BlindSeventyFive.Solutions as bsf
import BlindSeventyFive.SolutionsTwo as bsf2
import BlindSeventyFive.SolutionsThree as bsf3


class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None


ListNode.__lt__ = lambda self, other: self.value < other.value


def list_builder(a_list: list) -> ListNode:
    head = None
    temp = None
    for element in a_list:
        a_list_node = ListNode(element)
        if not head:
            head = a_list_node
        else:
            temp.next = a_list_node
        temp = a_list_node
    return head


def print_list(head: ListNode):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    print(result)


class CustomAssertion:
    def assert_compare_lists(self, node_1: ListNode, node_2: ListNode):
        while node_1 or node_2:
            if not node_1 or not node_2 or node_1.value != node_2.value:
                raise AssertionError('lists are not equal')
            node_1 = node_1.next
            node_2 = node_2.next

    def assert_compare_trees(self, node_1: binarytree.Node, node_2: binarytree.Node):
        if node_1 and node_2:
            if node_1.value == node_2.value:
                self.assert_compare_trees(node_1.left, node_2.left)
                self.assert_compare_trees(node_1.right, node_2.right)
            else:
                raise AssertionError('Trees are not Equal')
        elif node_1 and not node_2 or node_2 and not node_1:
            raise AssertionError('Trees are not Equal')


class SolutionsTest(unittest.TestCase, CustomAssertion):
    def test_two_sum(self):
        nums = [2, 7, 11, 15]
        target = 9
        output = [0, 1]
        self.assertListEqual(output, bsf3.twoSum(nums, target))
        nums = [3, 2, 4]
        target = 6
        output = [1, 2]
        self.assertListEqual(output, bsf3.twoSum(nums, target))
        nums = [3, 3]
        target = 6
        output = [0, 1]
        self.assertListEqual(output, bsf3.twoSum(nums, target))

    def test_max_profit(self):
        prices = [7, 1, 5, 3, 6, 4]
        output = 5
        self.assertEqual(output, bsf3.maxProfit(prices))
        prices = [7, 6, 4, 3, 1]
        output = 0
        self.assertEqual(output, bsf3.maxProfit(prices))

    def test_contains_duplicates(self):
        nums = [1, 2, 3, 1]
        output = True
        self.assertEqual(output, bsf3.containsDuplicate(nums))
        nums = [1, 2, 3, 4]
        output = False
        self.assertEqual(output, bsf3.containsDuplicate(nums))
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        output = True
        self.assertEqual(output, bsf3.containsDuplicate(nums))

    def test_product_except_self(self):
        nums = [1, 2, 3, 4]
        output = [24, 12, 8, 6]
        self.assertListEqual(output, bsf3.productExceptSelf(nums))
        nums = [-1, 1, 0, -3, 3]
        output = [0, 0, 9, 0, 0]
        self.assertListEqual(output, bsf3.productExceptSelf(nums))

    def test_max_sub_array(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        output = 6
        self.assertEqual(output, bsf3.maxSubArray(nums))
        nums = [5, 4, -1, 7, 8]
        output = 23
        self.assertEqual(output, bsf3.maxSubArray(nums))
        nums = [1]
        output = 1
        self.assertEqual(output, bsf3.maxSubArray(nums))

    def test_max_product_sub_array(self):
        nums = [2, 3, -2, 4]
        output = 6
        self.assertEqual(output, bsf3.maxProduct(nums))
        nums = [-2, 0, -1]
        output = 0
        self.assertEqual(output, bsf3.maxProduct(nums))
        nums = [-4, -3, -2]
        output = 12
        self.assertEqual(output, bsf3.maxProduct(nums))

    def test_find_min_rotated(self):
        nums = [3, 4, 5, 1, 2]
        output = 1
        self.assertEqual(output, bsf3.findMin(nums))
        nums = [4, 5, 6, 7, 0, 1, 2]
        output = 0
        self.assertEqual(output, bsf3.findMin(nums))
        nums = [11, 13, 15, 17]
        output = 11
        self.assertEqual(output, bsf3.findMin(nums))

    def test_search_rotated(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        output = 4
        self.assertEqual(output, bsf.search(nums, target))
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        output = -1
        self.assertEqual(output, bsf.search(nums, target))
        nums = [1]
        target = 0
        output = -1
        self.assertEqual(output, bsf.search(nums, target))

    def test_three_sum(self):
        nums = [-1, 0, 1, 2, -1, -4]
        output = [[-1, -1, 2], [-1, 0, 1]]
        self.assertCountEqual(output, bsf3.threeSum(nums))
        nums = [0, 0, 0, 0]
        output = [[0, 0, 0]]
        self.assertCountEqual(output, bsf3.threeSum(nums))

    def test_max_area(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        output = 49
        self.assertEqual(output, bsf2.maxArea(height))

    def test_length_of_longest_string(self):
        s = "abcabcbb"
        output = 3
        self.assertEqual(output, bsf3.lengthOfLongestSubstring(s))
        s = "bbbbb"
        output = 1
        self.assertEqual(output, bsf3.lengthOfLongestSubstring(s))
        s = "pwwkew"
        output = 3
        self.assertEqual(output, bsf3.lengthOfLongestSubstring(s))

    def test_character_replacement(self):
        s = "BAAAB"
        k = 2
        output = 5
        self.assertEqual(output, bsf3.characterReplacement(s, k))
        s = "ABAB"
        k = 2
        output = 4
        self.assertEqual(output, bsf3.characterReplacement(s, k))
        s = "AABABBA"
        k = 1
        output = 4
        self.assertEqual(output, bsf3.characterReplacement(s, k))

    def test_min_window(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        output = "BANC"
        self.assertEqual(output, bsf2.minWindow(s, t))
        s = "a"
        t = "a"
        output = "a"
        self.assertEqual(output, bsf2.minWindow(s, t))
        s = "a"
        t = "aa"
        output = ""
        self.assertEqual(output, bsf2.minWindow(s, t))

    def test_is_anagram(self):
        s = "anagram"
        t = "nagaram"
        output = True
        self.assertEqual(output, bsf2.isAnagram(s, t))
        s = "rat"
        t = "car"
        output = False
        self.assertEqual(output, bsf2.isAnagram(s, t))

    def test_group_anagrams(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        self.assertCountEqual(output, bsf2.group_anagrams(strs))

    def test_is_palindrome(self):
        s = "A man, a plan, a canal: Panama"
        output = True
        self.assertEqual(output, bsf2.isPalindrome(s))
        s = "race a car"
        output = False
        self.assertEqual(output, bsf2.isPalindrome(s))
        s = " "
        output = True
        self.assertEqual(output, bsf2.isPalindrome(s))

    def test_is_valid(self):
        s = "()"
        output = True
        self.assertEqual(output, bsf2.isValid(s))
        s = "()[]{}"
        output = True
        self.assertEqual(output, bsf2.isValid(s))
        s = "(]"
        output = False
        self.assertEqual(output, bsf2.isValid(s))

    def test_longest_palindrome(self):
        s = "babad"
        output = "bab"
        self.assertEqual(output, bsf2.longestPalindrome(s))
        s = "cbbd"
        output = "bb"
        self.assertEqual(output, bsf2.longestPalindrome(s))

    def test_count_substrings(self):
        s = "abc"
        output = 3
        self.assertEqual(output, bsf2.countSubstrings(s))
        s = "aaa"
        output = 6
        self.assertEqual(output, bsf2.countSubstrings(s))

    def test_set_zeros(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        output = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        bsf2.setZeroes(matrix)
        self.assertEqual(output, matrix)
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        output = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        bsf2.setZeroes(matrix)
        self.assertEqual(output, matrix)

    def test_spiral_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        output = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertListEqual(output, bsf2.spiralOrder(matrix))
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertListEqual(output, bsf2.spiralOrder(matrix))

    def test_exists(self):
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]]
        word = "ABCCED"
        self.assertEqual(True, bsf2.exist(board, word))
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "SEE"
        self.assertEqual(True, bsf2.exist(board, word))
        board = [["A", "B", "C", "E"], ["S", "F", "C", "  S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        self.assertEqual(False, bsf2.exist(board, word))

    def test_climb_stairs(self):
        n = 2
        output = 2
        self.assertEqual(output, bsf.climb_stairs_recursive(n))
        self.assertEqual(output, bsf.climb_stairs_memoization(n))
        self.assertEqual(output, bsf.climb_stairs_bottom_up(n))
        n = 3
        output = 3
        self.assertEqual(output, bsf.climb_stairs_recursive(n))
        self.assertEqual(output, bsf.climb_stairs_memoization(n))
        self.assertEqual(output, bsf.climb_stairs_bottom_up(n))

    def test_coin_change(self):
        coins = [1, 2, 5]
        amount = 11
        output = 3
        self.assertEqual(output, bsf.coin_change(coins, amount))
        self.assertEqual(output, bsf.coin_change_memoization(coins, amount))
        self.assertEqual(output, bsf.coin_change_iterative(coins, amount))
        coins = [2]
        amount = 3
        output = -1
        self.assertEqual(output, bsf.coin_change(coins, amount))
        self.assertEqual(output, bsf.coin_change_memoization(coins, amount))
        self.assertEqual(output, bsf.coin_change_iterative(coins, amount))
        coins = [1]
        amount = 0
        output = 0
        self.assertEqual(output, bsf.coin_change(coins, amount))
        self.assertEqual(output, bsf.coin_change_memoization(coins, amount))
        self.assertEqual(output, bsf.coin_change_iterative(coins, amount))

    def test_max_depth(self):
        input = binarytree.build2([3, 9, 20, None, None, 15, 7])
        output = 3
        self.assertEqual(output, bsf2.maxDepth(input))

    def test_same_tree(self):
        p = binarytree.build2([1, 2, 3])
        q = binarytree.build2([1, 2, 3])
        output = True
        self.assertEqual(output, bsf.same_tree(p, q))
        p = binarytree.build2([1, 2])
        q = binarytree.build2([1, None, 2])
        output = False
        self.assertEqual(output, bsf.same_tree(p, q))
        p = binarytree.build2([1, 2, 1])
        q = binarytree.build2([1, 1, 2])
        output = False
        self.assertEqual(output, bsf.same_tree(p, q))

    def test_invert_tree(self):
        root = binarytree.build2([4, 2, 7, 1, 3, 6, 9])
        output = binarytree.build2([4, 7, 2, 9, 6, 3, 1])
        bsf.invertTree(root)
        self.assert_compare_trees(root, output)

    def test_max_path_sum(self):
        root = binarytree.build2([1, 2, 3])
        output = 6
        self.assertEqual(output, bsf.maxPathSum(root))
        root = binarytree.build2([-10, 9, 20, None, None, 15, 7])
        output = 42
        self.assertEqual(output, bsf.maxPathSum(root))

    def test_level_order(self):
        root = binarytree.build2([3, 9, 20, None, None, 15, 7])
        output = [[3], [9, 20], [15, 7]]
        self.assertListEqual(output, bsf.levelOrder(root))

    def test_serialize_deserialize(self):
        root = binarytree.build2([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
        output = binarytree.build2([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
        codec = bsf.TreeCodec()
        self.assert_compare_trees(output, codec.deserialize(codec.serialize(root)))

    def test_subtree_of_tree(self):
        root = binarytree.build2([3, 4, 5, 1, 2])
        subRoot = binarytree.build2([4, 1, 2])
        output = True
        self.assertEqual(output, bsf.isSubtree(root, subRoot))
        root = binarytree.build2([3, 4, 5, 1, 2, None, None, None, None, 0])
        subRoot = binarytree.build2([4, 1, 2])
        output = False
        self.assertEqual(output, bsf.isSubtree(root, subRoot))

    def test_build_tree(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        output = binarytree.build2([3, 9, 20, None, None, 15, 7])
        self.assert_compare_trees(output, bsf.buildTree(preorder, inorder))
        preorder = [-1]
        inorder = [-1]
        output = binarytree.build2([-1])
        self.assert_compare_trees(output, bsf.buildTree(preorder, inorder))

    def test_is_valid_bst(self):
        root = binarytree.build2([5, 1, 4, None, None, 3, 6])
        output = False
        self.assertEqual(output, bsf.isValidBST(root))
        root = binarytree.build2([2, 1, 3])
        output = True
        self.assertEqual(output, bsf.isValidBST(root))
        root = binarytree.build2([2, 2, 2])
        output = False
        self.assertEqual(output, bsf.isValid(root))

    def test_kth_smallest(self):
        root = binarytree.build2([3, 1, 4, None, 2])
        k = 1
        output = 1
        self.assertEqual(output, bsf.kthSmallest(root, k))
        root = binarytree.build2([5, 3, 6, 2, 4, None, None, 1])
        k = 3
        output = 3
        self.assertEqual(output, bsf.kthSmallest(root, k))

    def test_lowest_common_ancestor(self):
        root = binarytree.build2([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = root.left
        q = root.right
        output = root
        self.assert_compare_trees(output, bsf.lowestCommonAncestor(root, p, q))
        root = binarytree.build2([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = root.left
        q = root.left.right.right
        output = root.left
        self.assert_compare_trees(output, bsf.lowestCommonAncestor(root, p, q))
        root = binarytree.build2([1, 2])
        p = root
        q = root.left
        output = root
        self.assert_compare_trees(output, bsf.lowestCommonAncestor(root, p, q))

    def test_trie(self):
        a_trie = bsf.Trie()
        a_trie.insert("apple")
        self.assertEqual(True, a_trie.search("apple"))
        self.assertEqual(False, a_trie.search("app"))
        self.assertEqual(True, a_trie.startsWith("app"))
        a_trie.insert("app")
        self.assertEqual(True, a_trie.search("app"))

    def test_word_dictionary(self):
        word_dictionary = bsf.WordDictionary()
        word_dictionary.addWord("bad")
        word_dictionary.addWord("dad")
        word_dictionary.addWord("mad")
        self.assertEqual(False, word_dictionary.search("pad"))
        self.assertEqual(True, word_dictionary.search("bad"))
        self.assertEqual(True, word_dictionary.search(".ad"))
        self.assertEqual(True, word_dictionary.search("b.."))

    def test_find_words(self):
        board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
        words = [
            "oath", "pea",
            "eat", "rain"]
        output = ["eat", "oath"]
        self.assertCountEqual(output, bsf.findWords(board, words))

    def test_reverse_list(self):
        head = list_builder([1, 2, 3, 4, 5])
        output = list_builder([5, 4, 3, 2, 1])
        self.assert_compare_lists(output, bsf.reverseList(head))
        head = list_builder([1, 2])
        output = list_builder([2, 1])
        self.assert_compare_lists(output, bsf.reverseList(head))
        head = list_builder([])
        output = list_builder([])
        self.assert_compare_lists(output, bsf.reverseList(head))

    def test_merge_two_lists(self):
        list1 = list_builder([1, 2, 4])
        list2 = list_builder([1, 3, 4])
        output = list_builder([1, 1, 2, 3, 4, 4])
        self.assert_compare_lists(bsf.mergeTwoLists(list1, list2), output)
        list1 = list_builder([])
        list2 = list_builder([])
        output = list_builder([])
        self.assert_compare_lists(bsf.mergeTwoLists(list1, list2), output)
        list1 = list_builder([])
        list2 = list_builder([0])
        output = list_builder([0])
        self.assert_compare_lists(bsf.mergeTwoLists(list1, list2), output)

    def test_merge_k_lists(self):
        lists = [list_builder([1, 4, 5]), list_builder([1, 3, 4]), list_builder([2, 6])]
        result = list_builder([1, 1, 2, 3, 4, 4, 5, 6])
        self.assert_compare_lists(result, bsf.mergeKLists(lists))

    def test_remove_nth_from_end(self):
        head = list_builder([1, 2, 3, 4, 5])
        n = 2
        output = list_builder([1, 2, 3, 5])
        self.assert_compare_lists(bsf.removeNthFromEnd(head, n), output)
        head = list_builder([1])
        n = 1
        output = list_builder([])
        self.assert_compare_lists(bsf.removeNthFromEnd(head, n), output)
        head = list_builder([1, 2])
        n = 1
        output = list_builder([1])
        self.assert_compare_lists(bsf.removeNthFromEnd(head, n), output)

    def test_reorder_list(self):
        head = list_builder([1, 2, 3, 4])
        output = list_builder([1, 4, 2, 3])
        bsf.reorderList(head)
        print_list(head)
        self.assert_compare_lists(output, head)

    def test_can_finish(self):
        number = 3
        prerequs = [[0, 1], [0, 2], [1, 2]]
        output = True
        self.assertEqual(output, bsf.canFinish(number, prerequs))

    def test_number_of_islands(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        output = 1
        self.assertEqual(output, bsf.numIslands(grid))
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        output = 3
        self.assertEqual(output, bsf.numIslands(grid))

    def test_merge_interval(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        output = [[1, 6], [8, 10], [15, 18]]
        self.assertListEqual(output, bsf3.merge(intervals))
        intervals = [[1, 4], [4, 5]]
        output = [[1, 5]]
        self.assertListEqual(output, bsf3.merge(intervals))

    def test_erase_overlap_interval(self):
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        output = 1
        self.assertEqual(output, bsf3.eraseOverlapIntervals(intervals))

    def test_can_attend_meetings(self):
        intervals = [[0, 30], [5, 10], [15, 20]]
        output = False
        self.assertEqual(output, bsf3.canAttendMeetings(intervals))
        intervals = [[7, 10], [2, 4]]
        output = True
        self.assertEqual(output, bsf3.canAttendMeetings(intervals))

    def test_min_meeting_rooms(self):
        intervals = [[0, 30], [5, 10], [15, 20]]
        output = 2
        self.assertEqual(output, bsf3.minMeetingRooms(intervals))
        intervals = [[7, 10], [2, 4]]
        output = 1
        self.assertEqual(output, bsf3.minMeetingRooms(intervals))

    def test_insert_interval(self):
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        output = [[1, 5], [6, 9]]
        self.assertListEqual(output, bsf3.insert(intervals, newInterval))
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        output = [[1, 2], [3, 10], [12, 16]]
        self.assertListEqual(output, bsf3.insert(intervals, newInterval))
