from typing import List


def largest_parameter(input):
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def traverse(x, y):
        result = 0
        is_parameter = False
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(input) and 0 <= y_target < len(input[0]):
                if input[x_target][y_target] == 1:
                    input[x_target][y_target] = -1
                    result += traverse(x_target, y_target)
                elif input[x_target][y_target] == 0:
                    is_parameter = True
            else:
                is_parameter = True
        if is_parameter:
            result += 1
        return result

    parameter = 0
    for x, row in enumerate(input):
        for y, value in enumerate(row):
            if value == 1:
                input[x][y] = -1
                parameter = max(parameter, traverse(x, y))
    return parameter


def maxIncreaseKeepingSkyline(grid: List[List[int]]) -> int:
    pass
