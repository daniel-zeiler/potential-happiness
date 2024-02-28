from typing import List

"""
2 arrays of integers
for any integer in arry1 we'll call the closest int from array2.  
it's sensor and the difference between the 2 integers can be called the sensor distance.  
Return the largest sensor distance.
"""


def find_largest_sensor_distance(array1: List[int], array2: List[int]) -> int:
    array2.sort()

    def binary_search_closest(array: List[int], low: int, high: int, target: int) -> int:
        if target <= array[low]:
            return array[low]
        if target >= array[high]:
            return array[high]
        center = (low + high) // 2
        if target == array[center]:
            return array[center]
        if array[center - 1] < target < array[center]:
            return array[center] if abs(target - array[center]) > abs(target - array[center - 1]) else array[center - 1]
        if array[center] > target > array[center + 1]:
            return array[center] if abs(target - array[center]) > abs(target - array[center + 1]) else array[center + 1]

        if target < array[center]:
            return binary_search_closest(array, low, center - 1, target)
        return binary_search_closest(array, center + 1, high, target)

    return max([abs(binary_search_closest(array2, 0, len(array2) - 1, value) - value) for value in array1])


array1 = [1, 2, 3, 4, 5, 99]
array2 = [3, 6, 7, 11, 12, 144]
# print(find_largest_sensor_distance(array1, array2))

"""
Calculator 1
1 + 2 - 5
"""

from typing import Any


def calculator_one(input_string: str) -> int:
    input_string = input_string.replace(" ", "")
    pointer = 0
    number = 0
    sign = "+"
    stack = []

    def update(sign, number):
        if sign == "+":
            stack.append(number)
        elif sign == "-":
            stack.append(-number)

    while pointer < len(input_string):
        character = input_string[pointer]
        if character.isdigit():
            number = number * 10 + int(character)
        elif character in ["+", "-"]:
            update(sign, number)
            number = 0
            sign = character
        pointer += 1
    update(sign, number)
    return sum(stack)


"""
Calculator 2
1 + (2 - 5) 
"""


def calculator_two(input_string: str) -> {int, int}:
    input_string = input_string.replace(" ", "")
    pointer = 0
    stack = []
    sign = "+"
    number = 0

    def process_number(sign, number):
        if sign == "+":
            stack.append(number)
        elif sign == "-":
            stack.append(-number)

    while pointer < len(input_string):
        character = input_string[pointer]
        if character.isdigit():
            number = number * 10 + int(character)
        elif character in ["+", "-"]:
            process_number(sign, number)
            sign = character
            number = 0
        elif character == "(":
            number, end_index = calculator_two(input_string[pointer + 1:])
            pointer += end_index
        elif character == ")":
            process_number(sign, number)
            return sum(stack), pointer
        pointer += 1
    process_number(sign, number)
    return sum(stack), pointer


"""
Calculator 3
1 + 2 / 5
"""


def calculator_three(input_string: str) -> int:
    pointer, sign, number, stack = 0, "+", 0, []
    input_string = input_string.replace(" ", "")

    def process_number(sign, number):
        if sign == "+":
            stack.append(number)
        elif sign == "-":
            stack.append(-number)
        elif sign == "/":
            stack.append(stack.pop() / number)
        else:
            stack.append(stack.pop() * number)

    while pointer < len(input_string):
        character = input_string[pointer]
        if character.isdigit():
            number = 10 * number + int(character)
        elif character in ["+", "/", "-", "*"]:
            process_number(sign, number)
            number, sign = 0, character
        pointer += 1

    process_number(sign, number)
    return sum(stack)


"""
Calculator 4
2 + 1 / (2 / 5) + 4
"""


def calculator_four(input_string: str) -> {int, int}:
    pointer, sign, number, stack = 0, "+", 0, []
    input_string = input_string.replace(" ", "")

    def process_number(sign, number):
        if sign == "+":
            stack.append(number)
        elif sign == "-":
            stack.append(-number)
        elif sign == "*":
            stack.append(stack.pop() * number)
        elif sign == "/":
            stack.append(stack.pop() / number)

    while pointer < len(input_string):
        character = input_string[pointer]
        if character.isdigit():
            number = 10 * number + int(character)
        elif character in ["+", "/", "-", "*"]:
            process_number(sign, number)
            sign, number = character, 0
        elif character == "(":
            number, index = calculator_four(input_string[pointer + 1:])
            pointer += index + 1
        elif character == ")":
            process_number(sign, number)
            return sum(stack), pointer
        pointer += 1
    process_number(sign, number)
    return sum(stack), pointer


print(calculator_four("2 + 1 / (2 / 5) + 4"))

"""
Group of sensors with time interval, sensor information comes in at random 
process(sensor_id:str,time_start:int,time_end:int)
total_time()
"""


class Sensor:
    def __init__(self):
        self.intervals = []

    def process(self, sensor_id, time_start, time_end):

        def insert_interval(intervals, start, end):
            for i, interval in enumerate(intervals):
                if i == 0:
                    if end < interval[0]:
                        return [start, end] + intervals
                else:
                    pass
            return [start, end] + intervals

        def is_intersecting(interval, start, end):
            if interval[1] > start and interval[0] < end:
                return True
            return False

        non_intersecting_intervals = []
        for interval in self.intervals:
            if is_intersecting(interval, time_start, time_end):
                start = min(interval[0], time_start)
                end = max(interval[1], time_end)
            else:
                non_intersecting_intervals.append(interval)
        self.intervals = insert_interval(non_intersecting_intervals, start, end)

    def total_time(self):
        pass
