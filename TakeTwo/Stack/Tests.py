import unittest
import TakeOne.Stack.Solutions as stack
import TakeOne.Stack.Solutions_Three as stack_three
import TakeOne.Stack.Solutions_Four as stack_four


class SolutionsTest(unittest.TestCase):
    def test_max_depth(self):
        s = "(1+(2*3)+((8)/4))+1"
        output = 3
        self.assertEqual(output, stack_four.maxDepth(s))
        s = "(1)+((2))+(((3)))"
        output = 3
        self.assertEqual(output, stack_four.maxDepth(s))
        s = "1+(2*3)/(2-1)"
        output = 1
        self.assertEqual(output, stack_four.maxDepth(s))
        s = "1"
        output = 0
        self.assertEqual(output, stack_four.maxDepth(s))

    def test_remove_outer_parentheses(self):
        s = "(()())(())"
        output = "()()()"
        self.assertEqual(output, stack_four.removeOuterParentheses(s))
        s = "(()())(())(()(()))"
        output = "()()()()(())"
        self.assertEqual(output, stack_four.removeOuterParentheses(s))
        s = "()()"
        output = ""
        self.assertEqual(output, stack_four.removeOuterParentheses(s))

    def test_remove_duplicates(self):
        s = "abbaca"
        output = "ca"
        self.assertEqual(output, stack_four.removeDuplicates(s))
        s = "azxxzy"
        output = "ay"
        self.assertEqual(output, stack_four.removeDuplicates(s))

    def test_cal_points(self):
        ops = ["5", "2", "C", "D", "+"]
        output = 30
        self.assertEqual(output, stack_three.calPoints(ops))
        ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
        output = 27
        self.assertEqual(output, stack_three.calPoints(ops))
        ops = ["1"]
        output = 1
        self.assertEqual(output, stack_three.calPoints(ops))

    def test_make_good(self):
        s = "leEeetcode"
        output = "leetcode"
        self.assertEqual(output, stack_four.makeGood(s))
        s = "abBAcC"
        output = ""
        self.assertEqual(output, stack_four.makeGood(s))
        s = "s"
        output = "s"
        self.assertEqual(output, stack_four.makeGood(s))

    def test_my_queue(self):
        my_queue = stack.MyQueue()
        my_queue.push(1)
        my_queue.push(2)
        self.assertEqual(1, my_queue.peek())
        self.assertEqual(1, my_queue.pop())
        self.assertEqual(False, my_queue.empty())

    def test_min_stack(self):
        min_stack = stack.MinStack()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        self.assertEqual(-3, min_stack.getMin())
        min_stack.pop()
        self.assertEqual(0, min_stack.top())
        self.assertEqual(-2, min_stack.getMin())

    def test_backspace_compare(self):
        s = "ab#c"
        t = "ad#c"
        output = True
        self.assertEqual(output, stack_four.backspaceCompare(s, t))
        s = "ab##"
        t = "c#d#"
        output = True
        self.assertEqual(output, stack_four.backspaceCompare(s, t))
        s = "a##c"
        t = "#a#c"
        output = True
        self.assertEqual(output, stack_four.backspaceCompare(s, t))
        s = "a#c"
        t = "b"
        output = False
        self.assertEqual(output, stack_four.backspaceCompare(s, t))

    def test_validate_brackets(self):
        s = "()"
        output = True
        self.assertEqual(output, stack_four.isValid(s))
        s = "()[]{}"
        output = True
        self.assertEqual(output, stack_four.isValid(s))
        s = "(]"
        output = False
        self.assertEqual(output, stack_four.isValid(s))

    def test_min_add_to_make_valid(self):
        s = "())"
        output = 1
        self.assertEqual(output, stack_four.minAddToMakeValid(s))
        s = "((("
        output = 3
        self.assertEqual(output, stack_four.minAddToMakeValid(s))
        s = "()"
        output = 0
        self.assertEqual(output, stack_four.minAddToMakeValid(s))
        s = "()))(("
        output = 4
        self.assertEqual(output, stack_four.minAddToMakeValid(s))

    def test_custom_stack(self):
        custom_stack = stack.CustomStack(3)
        custom_stack.push(1)
        custom_stack.push(2)
        self.assertEqual(2, custom_stack.pop())
        custom_stack.push(2)
        custom_stack.push(3)
        custom_stack.push(4)
        custom_stack.increment(5, 100)
        custom_stack.increment(2, 100)
        self.assertEqual(103, custom_stack.pop())
        self.assertEqual(202, custom_stack.pop())
        self.assertEqual(201, custom_stack.pop())
        self.assertEqual(-1, custom_stack.pop())

    def test_reverse_parentheses(self):
        s = "(abcd)"
        output = "dcba"
        self.assertEqual(output, stack_four.reverseParentheses(s))
        s = "(u(love)i)"
        output = "iloveu"
        self.assertEqual(output, stack_four.reverseParentheses(s))
        s = "(ed(et(oc))el)"
        output = "leetcode"
        self.assertEqual(output, stack_four.reverseParentheses(s))
        s = "a(bcdefghijkl(mno)p)q"
        output = "apmnolkjihgfedcbq"
        self.assertEqual(output, stack_four.reverseParentheses(s))

    def test_validate_stack_sequence(self):
        pushed = [1, 2, 3, 4, 5]
        popped = [4, 5, 3, 2, 1]
        output = True
        self.assertEqual(output, stack_three.validateStackSequences(pushed, popped))
        pushed = [1, 2, 3, 4, 5]
        popped = [4, 3, 5, 1, 2]
        output = False
        self.assertEqual(output, stack_three.validateStackSequences(pushed, popped))

    def test_min_remove_make_valid(self):
        s = "lee(t(c)o)de)"
        output = "lee(t(c)o)de"
        self.assertEqual(output, stack_four.minRemoveToMakeValid(s))
        s = "a)b(c)d"
        output = "ab(c)d"
        self.assertEqual(output, stack_four.minRemoveToMakeValid(s))
        s = "))(("
        output = ""
        self.assertEqual(output, stack_four.minRemoveToMakeValid(s))
        s = "(a(b(c)d)"
        output = "a(b(c)d)"
        self.assertEqual(output, stack_four.minRemoveToMakeValid(s))

    def test_is_valid_abc(self):
        s = "aabcbc"
        output = True
        self.assertEqual(output, stack_four.is_valid_abc(s))
        s = "abcabcababcc"
        output = True
        self.assertEqual(output, stack_four.is_valid_abc(s))
        s = "abccba"
        output = False
        self.assertEqual(output, stack_four.is_valid_abc(s))
        s = "cababc"
        output = False
        self.assertEqual(output, stack_four.is_valid_abc(s))

    def test_remove_duplicate_value(self):
        s = "abcd"
        k = 2
        output = "abcd"
        self.assertEqual(output, stack_four.remove_duplicate_value(s, k))
        s = "deeedbbcccbdaa"
        k = 3
        output = "aa"
        self.assertEqual(output, stack_four.remove_duplicate_value(s, k))
        s = "pbbcggttciiippooaais"
        k = 2
        output = "ps"
        self.assertEqual(output, stack_four.remove_duplicate_value(s, k))

    def test_decode_string(self):
        s = "3[a]2[bc]"
        output = "aaabcbc"
        self.assertEqual(output, stack_four.decodeString(s))
        s = "3[a2[c]]"
        output = "accaccacc"
        self.assertEqual(output, stack_four.decodeString(s))
        s = "2[abc]3[cd]ef"
        output = "abcabccdcdcdef"
        self.assertEqual(output, stack_four.decodeString(s))
        s = "abc3[cd]xyz"
        output = "abccdcdcdxyz"
        self.assertEqual(output, stack_four.decodeString(s))
        s = "100[lol]"
        self.assertEqual(100 * 'lol', stack_four.decodeString(s))

    def test_eval_rpn(self):
        tokens = ["2", "1", "+", "3", "*"]
        output = 9
        self.assertEqual(output, stack_four.evalRPN(tokens))
        tokens = ["4", "13", "5", "/", "+"]
        output = 6
        self.assertEqual(output, stack_four.evalRPN(tokens))
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        output = 22
        self.assertEqual(output, stack_four.evalRPN(tokens))

    def test_prices(self):
        prices = [8, 4, 6, 2, 3]
        output = [4, 2, 4, 2, 3]
        self.assertListEqual(output, stack_four.finalPrices(prices))
        prices = [1, 2, 3, 4, 5]
        output = [1, 2, 3, 4, 5]
        self.assertListEqual(output, stack_four.finalPrices(prices))
        prices = [10, 1, 1, 6]
        output = [9, 0, 1, 6]
        self.assertListEqual(output, stack_four.finalPrices(prices))

    def test_next_greater(self):
        nums1 = [4, 1, 2]
        nums2 = [1, 3, 4, 2]
        output = [-1, 3, -1]
        self.assertListEqual(output, stack_three.nextGreaterElement(nums1, nums2))
        nums1 = [2, 4]
        nums2 = [1, 2, 3, 4]
        output = [3, -1]
        self.assertListEqual(output, stack_three.nextGreaterElement(nums1, nums2))

    def test_daily_temperature(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        output = [1, 1, 4, 2, 1, 1, 0, 0]
        self.assertListEqual(output, stack_three.dailyTemperatures(temperatures))
        temperatures = [30, 40, 50, 60]
        output = [1, 1, 1, 0]
        self.assertListEqual(output, stack_three.dailyTemperatures(temperatures))
        temperatures = [30, 60, 90]
        output = [1, 1, 0]
        self.assertListEqual(output, stack_three.dailyTemperatures(temperatures))

    def test_next_greater_circular(self):
        nums = [1, 2, 1]
        output = [2, -1, 2]
        self.assertListEqual(output, stack_three.nextGreaterElements(nums))
        nums = [1, 2, 3, 4, 3]
        output = [2, 3, 4, -1, 4]
        self.assertListEqual(output, stack_three.nextGreaterElements(nums))

    def test_find_unsorted_subarry(self):
        nums = [2, 6, 4, 8, 10, 9, 15]
        output = 5
        self.assertEqual(output, stack_three.findUnsortedSubarray(nums))
        nums = [1, 2, 3, 4]
        output = 0
        self.assertEqual(output, stack_three.findUnsortedSubarray(nums))


if __name__ == '__main__':
    unittest.main()
