import collections
import math
from typing import List


def maxDepth(s: str) -> int:
    stack = []
    max_depth = 0
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
        max_depth = max(max_depth, len(stack))
    return max_depth


def removeOuterParentheses(s: str) -> str:
    stack = []
    open_p = 0
    close_p = 0
    result = ''
    for char in s:
        if char == '(':
            open_p += 1
        else:
            close_p += 1
        stack.append(char)
        if open_p == close_p:
            result += ''.join(stack[1:-1])
            stack = []
            open_p, close_p = 0, 0
    return result


def removeDuplicates(s: str) -> str:
    stack = []
    for char in s:
        stack.append(char)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    return ''.join(stack)


def calPoints(ops: List[str]) -> int:
    score = 0
    previous_scores = []
    for operation in ops:
        if operation == '+':
            previous_scores.append(previous_scores[-2] + previous_scores[-1])
            score += previous_scores[-1]
        elif operation == 'D':
            previous_scores.append(previous_scores[-1] * 2)
            score += previous_scores[-1]
        elif operation == 'C':
            score -= previous_scores[-1]
            previous_scores.pop()
        else:
            previous_scores.append(int(operation))
            score += previous_scores[-1]
    return score


def makeGood(s: str) -> str:
    stack = []
    for character in s:
        stack.append(character)
        while len(stack) > 1 and stack[-1].lower() == stack[-2].lower() and stack[-1] != stack[-2]:
            stack.pop()
            stack.pop()
    return ''.join(stack)


class MyQueue:

    def __init__(self):
        self.origin_stack = []
        self.reverse_stack = []

    def push(self, x: int) -> None:
        self.origin_stack.append(x)

    def pop(self) -> int:
        if not self.empty():
            while self.origin_stack:
                self.reverse_stack.append(self.origin_stack.pop())
            result = self.reverse_stack.pop()
            while self.reverse_stack:
                self.origin_stack.append(self.reverse_stack.pop())
            return result

    def peek(self) -> int:
        if not self.empty():
            return self.origin_stack[0]

    def empty(self) -> bool:
        return len(self.origin_stack) == 0


class MinStack:

    def __init__(self):
        self.value_stack = []
        self.minimum_value_stack = []

    def push(self, val: int) -> None:
        if not self.minimum_value_stack or val <= self.minimum_value_stack[-1]:
            self.minimum_value_stack.append(val)
        self.value_stack.append(val)

    def pop(self) -> None:
        if not self.is_empty():
            if self.value_stack[-1] == self.minimum_value_stack[-1]:
                self.minimum_value_stack.pop()
            self.value_stack.pop()

    def top(self) -> int:
        if not self.is_empty():
            return self.value_stack[-1]

    def is_empty(self) -> bool:
        return len(self.value_stack) == 0

    def getMin(self) -> int:
        if not self.is_empty():
            return self.minimum_value_stack[-1]


def backspaceCompare(s: str, t: str) -> bool:
    def process_string(characters):
        stack = []
        for character in characters:
            if character == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(character)
        return ''.join(stack)

    return process_string(s) == process_string(t)


def isValid(s: str) -> bool:
    square = 0
    curved = 0
    squiggly = 0
    for character in s:
        if character == '[':
            square += 1
        elif character == ']':
            square -= 1
        elif character == '(':
            curved += 1
        elif character == ')':
            curved -= 1
        elif character == '{':
            squiggly += 1
        elif character == '}':
            squiggly -= 1
    return square == curved == squiggly == 0


def minAddToMakeValid(s: str) -> int:
    stack = []
    for character in s:
        stack.append(character)
        while len(stack) > 1 and stack[-1] == ')' and stack[-2] == '(':
            stack.pop()
            stack.pop()
    return len(stack)


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) != self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for index in range(0, min(len(self.stack), k)):
            self.stack[index] += val


def reverseParentheses(s: str) -> str:
    stack = []
    reverse_list = []
    for char in s:
        if char == ')':
            while stack[-1] != '(':
                reverse_list.append(stack.pop())
            stack.pop()
            stack += reverse_list
            reverse_list = []
        else:
            stack.append(char)
    return ''.join(stack)


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    pushed_index = 0
    popped_index = 0
    stack = []
    while pushed_index < len(pushed) and popped_index < len(popped):
        if not stack or stack[-1] != popped[popped_index]:
            stack.append(pushed[pushed_index])
            pushed_index += 1
        else:
            stack.pop()
            popped_index += 1

    while popped_index < len(popped):
        if stack[-1] == popped[popped_index]:
            stack.pop()
            popped_index += 1
        else:
            return False

    return not stack


def minRemoveToMakeValid(s: str) -> str:
    invalid_close_index = []
    invalid_open_index = []
    for index, character in enumerate(s):
        if character == ')':
            if not invalid_open_index:
                invalid_close_index.append(index)
            else:
                invalid_open_index.pop()
        elif character == '(':
            invalid_open_index.append(index)

    result = ''
    for index, character in enumerate(s):
        if index not in invalid_close_index and index not in invalid_open_index:
            result += character
    return result


def is_valid_abc(s: str) -> bool:
    stack = []
    for character in s:
        stack.append(character)
        while len(stack) >= 3 and stack[-3] + stack[-2] + stack[-1] == 'abc':
            stack.pop()
            stack.pop()
            stack.pop()
    return not stack


def remove_duplicate_value(s: str, k: int) -> str:
    def check_stack(stack: List[str]) -> bool:
        if len(stack) >= k:
            for i in range(1, k):
                if stack[-1] != stack[-1 - i]:
                    return False
            return True

    stack = []
    for character in s:
        stack.append(character)
        if check_stack(stack):
            for i in range(k):
                stack.pop()
    return ''.join(stack)


def decodeString(s: str) -> str:
    def process_stack(stack):
        for i in range(len(stack) - 1, -1, -1):
            if stack[i].isnumeric():
                return stack[:i] + (''.join(stack[i + 1:]) * int(stack[i])).split()

    character_stack = []
    for character in s:
        if character != '[' and character != ']':
            character_stack.append(character)
        elif character == ']':
            character_stack = process_stack(character_stack)
    return ''.join(character_stack)


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            denominator = stack.pop()
            numerator = stack.pop()
            stack.append(math.trunc(numerator / denominator))
        elif token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            stack.append(stack.pop() - stack.pop())
        else:
            stack.append(int(token))
    return stack[-1]


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = []
    output = [0 for _ in range(len(temperatures))]
    for i, temp in enumerate(temperatures):
        if not stack:
            stack.append(i)
        else:
            if temp <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temp:
                    index = stack.pop()
                    output[index] = i - index
                stack.append(i)
    return output


def finalPrices(prices: List[int]) -> List[int]:
    stack = []
    output = [price for price in prices]
    for i, price in enumerate(prices):
        if not stack:
            stack.append(i)
        elif price > prices[stack[-1]]:
            stack.append(i)
        else:
            while stack and price <= prices[stack[-1]]:
                index = stack.pop()
                output[index] = prices[index] - price
            stack.append(i)
    return output


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    temp_dict = collections.defaultdict(int)
    stack = []

    for i, num in enumerate(nums2):
        if not stack or num < nums2[stack[-1]]:
            stack.append(i)
        else:
            while stack and num > nums2[stack[-1]]:
                index = stack.pop()
                temp_dict[nums2[index]] = num
            stack.append(i)

    for i, num in enumerate(nums1):
        if num in temp_dict:
            nums1[i] = temp_dict[num]
        else:
            nums1[i] = -1

    return nums1
