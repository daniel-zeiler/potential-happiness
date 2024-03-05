def maxDepth(s: str) -> int:
    depth, max_depth = 0, 0
    for character in s:
        if character == '(':
            depth += 1
        elif character == ')':
            depth -= 1
        max_depth = max(depth, max_depth)
    return max_depth


def removeOuterParentheses(s: str) -> str:
    stack, result, open, close = [], "", 0, 0
    for i, character in enumerate(s):
        stack.append(i)
        if character == "(":
            open += 1
        if character == ")":
            close += 1
        if open == close:
            result += s[stack[1]:stack[-1]]
            stack = []
    return result


def removeDuplicates(s: str) -> str:
    stack = []
    for character in s:
        stack.append(character)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop(), stack.pop()

    return "".join(stack)


from typing import List


def calPoints(ops: List[str]) -> int:
    stack = []

    def process_operation(operation):
        if operation == "C":
            stack.pop()
        elif operation == "D":
            stack.append(stack[-1] * 2)
        else:
            stack.append(stack[-1] + stack[-2])

    for operation in ops:
        if operation in ["+", "C", "D"]:
            process_operation(operation)
        else:
            stack.append(int(operation))
    return sum(stack)


def makeGood(s: str) -> str:
    stack = []
    for character in s:
        stack.append(character)
        if len(stack) > 1 and stack[-1].lower() == stack[-2].lower() and stack[-1] != stack[-2]:
            stack.pop()
            stack.pop()
    return "".join(stack)


def backspaceCompare(s: str, t: str) -> bool:
    def process_input(input_string: str) -> str:
        stack = []
        for character in input_string:
            if character == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(character)
        return "".join(stack)

    return process_input(s) == process_input(t)


def isValid(s: str) -> bool:
    square, curly, paren = 0, 0, 0
    for character in s:
        if character == "(":
            paren += 1
        if character == "[":
            square += 1
        if character == "{":
            curly += 1
        if character == ")":
            if not paren:
                return False
            paren -= 1
        if character == "]":
            if not square:
                return False
            square -= 1
        if character == "}":
            if not curly:
                return False
            curly -= 1
    return not square and not curly and not paren


def minAddToMakeValid(s: str) -> int:
    add_to_make_valid, stack = 0, []
    for character in s:
        if character == "(":
            stack.append(character)
        elif character == ")":
            if not stack:
                add_to_make_valid += 1
            else:
                stack.pop()
    return add_to_make_valid + len(stack)


def reverseParentheses(s: str) -> str:
    s = [character for character in s]
    stack, result = [], ""
    for index, character in enumerate(s):
        if character == "(":
            stack.append(index)
        elif character == ")":
            s[stack[-1]:index + 1] = s[stack[-1]:index + 1][::-1]
            stack.pop()
        elif not stack:
            result += character

    return "".join(list(filter(lambda x: x not in [")", "("], s)))
