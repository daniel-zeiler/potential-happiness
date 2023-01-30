import math
from typing import List


def maxDepth(s: str) -> int:
    depth = 0
    max_depth = 0
    for character in s:
        if character == '(':
            depth += 1
        elif character == ')':
            depth -= 1
        max_depth = max(max_depth, depth)
    return max_depth


def removeOuterParentheses(s: str) -> str:
    result = ""
    stack = []
    for i, character in enumerate(s):
        if character == '(':
            stack.append(i)
        elif character == ')':
            index = stack.pop()
            if len(stack) == 0:
                result += s[index + 1:i]
    return result


def removeDuplicates(s: str) -> str:
    stack = []
    for character in s:
        if not stack:
            stack.append(character)
        elif stack[-1] == character:
            stack.pop()
        else:
            stack.append(character)
    return ''.join(stack)


def makeGood(s: str) -> str:
    stack = []
    for character in s:
        if not stack:
            stack.append(character)
        elif (stack[-1].lower() == character or stack[-1] == character.lower()) and stack[-1] != character:
            stack.pop()
        else:
            stack.append(character)
    return ''.join(stack)


def backspaceCompare(s: str, t: str) -> bool:
    def backspace_string(input_string):
        result = []
        for character in input_string:
            if character == '#':
                if result:
                    result.pop()
            else:
                result.append(character)
        return ''.join(result)

    return backspace_string(s) == backspace_string(t)


def isValid(s: str) -> bool:
    curly = 0
    square = 0
    paren = 0
    for character in s:
        if character == '(':
            paren += 1
        elif character == ')':
            if not paren:
                return False
            paren -= 1
        elif character == '{':
            curly += 1
        elif character == '}':
            if not curly:
                return False
            curly -= 1
        elif character == '[':
            square += 1
        else:
            if not square:
                return False
            square -= 1
    return not curly and not square and not paren


def minAddToMakeValid(s: str) -> int:
    min_add = 0
    stack = 0
    for character in s:
        if character == ')':
            if not stack:
                min_add += 1
            else:
                stack -= 1
        else:
            stack += 1
    return stack + min_add


def reverseParentheses(s: str) -> str:
    stack = []
    temp_result = []
    for i, character in enumerate(s):
        if character != ')':
            stack.append(character)
        else:
            while stack[-1] != '(':
                temp_result.append(stack.pop())
            stack.pop()
            stack.extend(temp_result)
            temp_result = []
    return "".join(stack)


def minRemoveToMakeValid(s: str) -> str:
    invalid_indices = []
    stack = []
    result = ""
    for i, character in enumerate(s):
        if character == ')':
            if not stack:
                invalid_indices.append(i)
            else:
                stack.pop()
        elif character == '(':
            stack.append(i)

    invalid_indices = set(invalid_indices + stack)
    for i, character in enumerate(s):
        if i not in invalid_indices:
            result += character
    return result


def is_valid_abc(s: str) -> bool:
    stack = []
    for character in s:
        stack.append(character)
        if len(stack) >= 3:
            if stack[-3] + stack[-2] + stack[-1] == 'abc':
                stack = stack[:len(stack) - 3]
    return not stack


def remove_duplicate_value(s: str, k: int) -> str:
    stack = []
    for character in s:
        stack.append(character)
        if len(stack) >= k:
            if len(set(stack[-k:])) == 1:
                stack = stack[:len(stack) - k]
    return ''.join(stack)


def decodeString(s: str) -> str:
    stack = []
    for i, character in enumerate(s):
        stack.append(character)
        if stack[-1] == ']':
            stack.pop()
            decode = ""
            number = ""
            while stack[-1] != '[':
                decode += stack.pop()
            stack.pop()
            while stack and stack[-1].isnumeric():
                number += stack.pop()
            stack.extend(int(number[::-1]) * decode[::-1])
    return "".join(stack)


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token.strip('-').isnumeric():
            stack.append(int(token))
        elif token == "/":
            denom = stack.pop()
            num = stack.pop()
            stack.append(math.trunc(num / denom))
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "+":
            stack.append(stack.pop() + stack.pop())
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
    return stack[0]


def finalPrices(prices: List[int]) -> List[int]:
    stack = []
    result = [price for price in prices]
    for i, price in enumerate(prices):
        while stack and price <= prices[stack[-1]]:
            index = stack.pop()
            result[index] -= price
        stack.append(i)
    return result


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    pass
