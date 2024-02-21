"""
2 arrays of integers
for any integer in arry1 we'll call the closest int from array2.
it's sensor and the difference between the 2 integers can be called the sensor distance.
Return the largest sensor distance.
"""

input_1 = [1, 3, 5, 96]
input_2 = [3, 4, 5, 77]

from typing import List


def find_maximize_minimum_difference(array1: List[int], array2: List[int]) -> int:
    array2.sort()
    maximum_min_difference = 0
    if not input_2 or not input_1:
        return -1

    def binary_search(input_list: List[int], target: int) -> int:
        low, high = 0, len(input_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if input_list[mid] == target:
                return 0
            elif input_list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if low < len(input_list) and high >= 0:
            return min(abs(input_list[low] - target), abs(input_list[high] - target))
        elif low < len(input_list):
            return abs(input_list[low] - target)
        else:
            return abs(input_list[high] - target)

    for value in array1:
        maximum_min_difference = max(maximum_min_difference, binary_search(array2, value))
    return maximum_min_difference


print(find_maximize_minimum_difference(input_1, input_2))


def calculator(input_string: str) -> int:
    input_string = input_string.replace(" ", "")

    def update_stack(operation, number, stack):
        if operation == "+":
            stack.append(number)
        elif operation == "-":
            stack.append(-number)
        elif operation == "/":
            stack.append(stack.pop() / number)
        elif operation == "*":
            stack.append(stack.pop() * number)

    def calculator_helper(input_string: str, index: int) -> (int, int):
        stack, number, operation = [], 0, "+"

        while index < len(input_string):
            character = input_string[index]
            if character.isdigit():
                number = number * 10 + int(character)
            elif character in ["+", "-", "/", "*"]:
                update_stack(operation, number, stack)
                number = 0
                operation = character
            elif character == "(":
                number, next_index = calculator_helper(input_string, index + 1)
                index += next_index
            elif character == ")":
                update_stack(operation, number, stack)
                return sum(stack), index + 1
            index += 1
        update_stack(operation, number, stack)
        return sum(stack), index

    return calculator_helper(input_string, 0)[0]


input = " 1 / 2 + 5 - ((3 + 7) * 2)"
print(calculator(input))
