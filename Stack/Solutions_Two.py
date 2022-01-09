import collections
from typing import List


def maxDepth(s: str) -> int:
    stack = []
    max_depth = 0
    for character in s:
        if character == '(':
            stack.append(character)
        elif character == ')':
            stack.pop()
        max_depth = max(max_depth, len(stack))
    return max_depth


def removeOuterParentheses(s: str) -> str:
    stack = []
    result = ''
    for i, character in enumerate(s):
        if character == '(':
            stack.append(i)
        else:
            if len(stack) == 1:
                result += s[stack[0] + 1:i]
            stack.pop()
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
    stack = []
    total_points = 0
    for operation in ops:
        if operation == 'C':
            total_points -= stack.pop()
        else:
            if operation == '+':
                stack.append(stack[-1] + stack[-2])
            elif operation == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(operation))
            total_points += stack[-1]
    return total_points


def makeGood(s: str) -> str:
    stack = []
    for character in s:
        if not stack:
            stack.append(character)
        elif stack[-1] == character.lower() and stack[-1] != character:
            stack.pop()
        else:
            stack.append(character)
    return ''.join(stack)


def backspaceCompare(s: str, t: str) -> bool:
    s_list = []
    t_list = []
    for character in s:
        if character == '#':
            if s_list:
                s_list.pop()
        else:
            s_list.append(character)
    for character in t:
        if character == '#':
            if t_list:
                t_list.pop()
        else:
            t_list.append(character)

    return s_list == t_list


def isValid(s: str) -> bool:
    curly = 0
    square = 0
    bracket = 0
    for character in s:
        if character == ')':
            bracket -= 1
        elif character == '(':
            bracket += 1
        elif character == ']':
            square -= 1
        elif character == '[':
            square += 1
        elif character == '}':
            curly -= 1
        else:
            curly += 1
        if curly | square | bracket == -1:
            return False
    return curly == square == bracket == 0


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
    return min_add + stack


def reverseParentheses(s: str) -> str:
    s = list(s)
    stack = []
    result_list = []
    for index, character in enumerate(s):
        if character == ')':
            while stack[-1] != '(':
                result_list.append(stack.pop())
            stack.pop()
            stack.extend(result_list)
            result_list = []
        else:
            stack.append(character)
    return ''.join(stack)


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    stack = []
    pushed = collections.deque(pushed)
    popped = collections.deque(popped)

    while pushed:
        if not stack or stack[-1] != popped[0]:
            stack.append(pushed.popleft())
        else:
            popped.popleft()
            stack.pop()

    while popped and stack[-1] == popped[0]:
        stack.pop()
        popped.popleft()

    return len(pushed) == len(popped) == 0


def minRemoveToMakeValid(s: str) -> str:
    stack = []
    remove_set = set()

    for index, character in enumerate(s):
        if character == ')':
            if not stack:
                remove_set.add(index)
            else:
                stack.pop()
        elif character == '(':
            stack.append(index)

    remove_set.update(stack)
    result = ''

    for index, character in enumerate(s):
        if index not in remove_set:
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
    stack = []
    for character in s:
        stack.append(character)
        if len(stack) >= k:
            if set(stack[-k:]) == set(character):
                for _ in range(k):
                    stack.pop()
    return ''.join(stack)


def decodeString(s: str) -> str:
    stack = []
    for character in s:
        stack.append(character)
        if stack[-1] == ']':
            stack.pop()
            decode = ''
            while stack[-1] != '[':
                decode = stack.pop() + decode
            stack.pop()
            decode = int(stack.pop()) * decode
            stack.extend(list(decode))
    return ''.join(stack)
