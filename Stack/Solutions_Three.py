from collections import deque
from typing import List


def maxDepth(s: str) -> int:
    max_depth = 0
    curr_depth = 0
    for character in s:
        if character == '(':
            curr_depth += 1
        elif character == ')':
            curr_depth -= 1
        max_depth = max(curr_depth, max_depth)
    return max_depth


def removeOuterParentheses(s: str) -> str:
    open = 0
    result = ''
    for character in s:
        if character == '(':
            if open != 0:
                result += character
            open += 1
        else:
            open -= 1
            if open != 0:
                result += character
    return result


def removeDuplicates(s: str) -> str:
    stack = []
    for character in s:
        if not stack:
            stack.append(character)
        elif character == stack[-1]:
            stack.pop()
        else:
            stack.append(character)
    return ''.join(stack)


def calPoints(ops: List[str]) -> int:
    total_points = 0
    prev_rounds = []
    for operation in ops:
        if operation == 'C':
            total_points -= prev_rounds.pop()
        elif operation == 'D':
            prev_rounds.append(prev_rounds[-1] * 2)
            total_points += prev_rounds[-1]
        elif operation == '+':
            prev_rounds.append(prev_rounds[-1] + prev_rounds[-2])
            total_points += prev_rounds[-1]
        else:
            prev_rounds.append(int(operation))
            total_points += prev_rounds[-1]
    return total_points


def makeGood(s: str) -> str:
    stack = []
    for character in s:
        if not stack or not (character.lower() == stack[-1] and character != stack[-1]):
            stack.append(character)
        else:
            stack.pop()
    return ''.join(stack)


def backspaceCompare(s: str, t: str) -> bool:
    s_stack = []
    t_stack = []
    for char in s:
        if char == '#':
            if s_stack:
                s_stack.pop()
        else:
            s_stack.append(char)
    for char in t:
        if char == '#':
            if t_stack:
                t_stack.pop()
        else:
            t_stack.append(char)
    return s_stack == t_stack


def isValid(s: str) -> bool:
    paren = 0
    curly = 0
    bracket = 0
    for character in s:
        if character == '{':
            curly += 1
        elif character == '}':
            if not curly:
                return False
            curly -= 1
        elif character == '(':
            paren += 1
        elif character == ')':
            if not paren:
                return False
            paren -= 1
        elif character == '[':
            bracket += 1
        elif character == ']':
            if not bracket:
                return False
            bracket -= 1
    return paren == curly == bracket == 0


def minAddToMakeValid(s: str) -> int:
    invalid = 0
    open = 0
    for character in s:
        if character == '(':
            open += 1
        elif open == 0:
            invalid += 1
        else:
            open -= 1
    return open + invalid


def reverseParentheses(s: str) -> str:
    def recursive_reverse(pointer):
        result = ''
        while pointer < len(s):
            character = s[pointer]
            if character != '(' and character != ')':
                result += character
                pointer += 1
            elif character == '(':
                pointer, temp_result = recursive_reverse(pointer + 1)
                pointer += 1
                result += temp_result
            elif character == ')':
                return pointer, result[::-1]
        return pointer, result

    pointer, result = recursive_reverse(0)
    return result


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    stack = []
    pushed = deque(pushed)
    popped = deque(popped)
    while pushed and popped:
        if not stack or not stack[-1] == popped[0]:
            stack.append(pushed.popleft())
        else:
            stack.pop()
            popped.popleft()
    while pushed:
        stack.append(pushed.popleft())
    while popped and popped[0] == stack[-1]:
        popped.popleft()
        stack.pop()
    return not stack


def minRemoveToMakeValid(s: str) -> str:
    result = ''
    invalid_indices = []
    open_paren = []
    for index, character in enumerate(s):
        if character == '(':
            open_paren.append(index)
        if character == ')':
            if not open_paren:
                invalid_indices.append(index)
            else:
                open_paren.pop()

    invalid_indices = set(invalid_indices + open_paren)
    for index, character in enumerate(s):
        if index not in invalid_indices:
            result += character

    return result


def is_valid_abc(s: str) -> bool:
    result_stack = []
    for character in s:
        if len(result_stack) >= 2 and character == 'c' and result_stack[-1] == 'b' and result_stack[-2] == 'a':
            result_stack.pop()
            result_stack.pop()
        else:
            result_stack.append(character)
    return not result_stack


def remove_duplicate_value(s: str, k: int) -> str:
    result_stack = []

    for character in s:
        if not result_stack or not character == result_stack[-1][0]:
            result_stack.append([character, 1])
        else:
            result_stack.append([character, result_stack[-1][1] + 1])

        if result_stack[-1][1] == k:
            for _ in range(k):
                result_stack.pop()

    result = ''
    for char, dupe in result_stack:
        result += char

    return result
