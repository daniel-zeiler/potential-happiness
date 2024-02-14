from typing import List


def maxDepth(s: str) -> int:
    stack = []
    max_depth = 0
    for char in s:
        if char == '(':
            stack.append('(')
        elif char == ')':
            stack.pop()
        max_depth = max(max_depth, len(stack))
    return max_depth


def removeOuterParentheses(s: str) -> str:
    stack = []
    result = ""
    open = 0
    close = 0

    for i, character in enumerate(s):
        stack.append(character)
        if character == "(":
            open += 1
        else:
            close += 1
        if open == close:
            result += "".join(stack[1:-1])
            open, close, stack = 0, 0, []
    return result


def removeDuplicates(s: str) -> str:
    stack = []
    for character in s:
        if stack and stack[-1] == character:
            stack.pop()
        else:
            stack.append(character)
    return "".join(stack)


def calPoints(ops: List[str]) -> int:
    record = []
    for operation in ops:
        if operation.isnumeric() or operation[0] == "-":
            record.append(float(operation))
        elif operation == "+":
            record.append(record[-1] + record[-2])
        elif operation == "C":
            record.pop()
        else:
            record.append(record[-1] * 2)
    return sum(record)


def makeGood(s: str) -> str:
    stack = []
    for character in s:
        if stack and (stack[-1].lower() == character.lower() and stack[-1] != character):
            stack.pop()
        else:
            stack.append(character)
    return "".join(stack)


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((0, val))
        else:
            if val < self.stack[self.stack[-1][0]][1]:
                self.stack.append((len(self.stack), val))
            else:
                self.stack.append((self.stack[-1][0], val))

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()[1]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][1]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[self.stack[-1][0]][1]


def backspaceCompare(s: str, t: str) -> bool:
    def backspace_build(input: str) -> str:
        stack = []
        for character in input:
            if character == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(character)
        return "".join(stack)

    return backspace_build(s) == backspace_build(t)


def isValid(s: str) -> bool:
    stack = []
    for character in s:
        if character in ["(", "[", "{"]:
            stack.append(character)
        elif character == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif character == "}":
            if stack[-1] == "{":
                stack.pop()
            else:
                return False
        elif character == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                return False
        else:
            return False
    return not stack


def minAddToMakeValid(s: str) -> int:
    min_add = 0
    stack = []
    for character in s:
        if character == ")":
            if stack:
                stack.pop()
            else:
                min_add += 1
        else:
            stack.append(character)
    return len(stack) + min_add


def reverseParentheses(s: str) -> str:
    stack = []
    for i, character in enumerate(s):
        if character == "(":
            stack.append(i)
        elif character == ")":
            s = s[:stack[-1]] + s[stack[-1]:i + 1][::-1] + s[i + 1:]
            stack.pop()
    return s.replace("(", "").replace(")", "")


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    stack, push_pointer, pop_pointer = [], 0, 0

    while push_pointer < len(pushed) and pop_pointer < len(popped):
        if not stack or stack[-1] != popped[pop_pointer]:
            stack.append(pushed[push_pointer])
            push_pointer += 1
        else:
            stack.pop()
            pop_pointer += 1

    if push_pointer != len(pushed):
        return False

    while pop_pointer < len(popped):
        if not stack or stack[-1] != popped[pop_pointer]:
            return False
        stack.pop()
        pop_pointer += 1

    return not stack


def minRemoveToMakeValid(s: str) -> str:
    stack = []
    invalid_indices = []
    for i, character in enumerate(s):
        if character == "(":
            stack.append(i)
        elif character == ")":
            if not stack:
                invalid_indices.append(i)
            else:
                stack.pop()
    invalid_indices.extend(stack)

    return "".join([char for i, char in enumerate(s) if i not in invalid_indices])


def is_valid_abc(s: str) -> bool:
    stack = []
    for character in s:
        stack.append(character)
        if len(stack) >= 3 and stack[-3] + stack[-2] + stack[-1] == "abc":
            stack = stack[:-3]
    return not stack


def remove_duplicate_value(s: str, k: int) -> str:
    stack = []
    for character in s:
        stack.append(character)
        if len(stack) >= k and len(set(stack[-k:])) == 1:
            stack = stack[:-k]
    return "".join(stack)


def decodeString(s: str) -> str:
    stack = []
    for character in s:
        stack.append(character)
        if character == "]":
            temp_string = ""
            stack.pop()
            while stack and stack[-1] != "[":
                temp_string = stack.pop() + temp_string
            stack.pop()
            value = ""
            while stack and stack[-1].isnumeric():
                value = stack.pop() + value
            for character in [int(value) * temp_string]:
                stack.append(character)
    return "".join(stack)


import math


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token.isnumeric() or token[0] == "-":
            stack.append(int(token))
        elif token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "/":
            denom = stack.pop()
            num = stack.pop()
            stack.append(int(num / denom))
        else:
            stack.append(stack.pop() * stack.pop())
    return stack[0]


"""
Here I will maintain a stack of indicies of prices that haven't received a discount.
I'll then iterate through prices and attempt to pop from the stack if we would apply a discount. 
I'd then append that value to the stack.
This function is O(n) space and time complexity as we're iterating over the input space and 
the size of the stack would be equivalent to the input in the worst case.
"""


def finalPrices(prices: List[int]) -> List[int]:
    stack = []
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] >= price:
            prices[stack.pop()] -= price
        stack.append(i)
    return prices


"""
I'll create an index dictionary of values within nums1 such that they're initialized to -1
I'll then maintain a stack for all values in nums2 such that as I iterate through nums2 I'll pop off the index when I
identify the next largest value
"""


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    nums_dictionary = {x: -1 for x in nums1}
    stack = []
    for i, number_two in enumerate(nums2):
        while stack and nums2[stack[-1]] < number_two:
            value = nums2[stack.pop()]
            if value in nums_dictionary:
                nums_dictionary[value] = number_two
        stack.append(i)
    return [nums_dictionary[num] for num in nums1]


"""
I will initialize a list of length temperatures with 0s as default values.
I'll then maintain a stack of indices within temperatures that haven't seen a warmer day yet.
I'll iterate through the temperatures and attempt to pop off the stack where I detect we've reached a day with 
a higher temperature, i'll update the above list and append the new value to the stack.
"""


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    result = [0 for _ in range(len(temperatures))]
    stack = []
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)
    return result


class StockSpanner:

    def __init__(self):
        self.prices = []
        self.stack = []

    def next(self, price: int) -> int:
        index = len(self.prices)
        self.prices.append(price)
        if not self.stack:
            self.stack.append(index)
            return 1
        while self.stack and self.prices[self.stack[-1]] < price:
            self.stack.pop()
        result = index - self.stack[-1] if self.stack else index
        self.stack.append(index)
        return result
