from typing import List


def largest_parameter(input):
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    largest_param = 0

    def traverse(x, y) -> int:
        input[x][y] = -1
        result = 0
        on_parameter = False
        for direction_x, direction_y in directions:
            x_direction, y_direction = x + direction_x, y + direction_y

            if 0 <= x_direction < len(input) and 0 <= y_direction < len(input[0]):
                if input[x_direction][y_direction] == 1:
                    result += traverse(x_direction, y_direction)
                elif input[x_direction][y_direction] == 0:
                    on_parameter = True
            else:
                on_parameter = True

        if on_parameter:
            result += 1
        return result

    for x in range(len(input)):
        for y in range(len(input[x])):
            if input[x][y] == 1:
                largest_param = max(largest_param, traverse(x, y))

    return largest_param


def maxIncreaseKeepingSkyline(grid: List[List[int]]) -> int:
    x_rows, y_columns = [0 for _ in range(len(grid))], [0 for _ in range(len(grid[0]))]

    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            x_rows[x], y_columns[y] = max(x_rows[x], val), max(y_columns[y], val)

    max_increase = 0
    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            max_increase += min(x_rows[x] - val, y_columns[y] - val)

    return max_increase


def countSquares(matrix: List[List[int]]) -> int:
    squares = 0
    for x, row in enumerate(matrix):
        for y, val in enumerate(row):
            if val == 1 and x != 0 and y != 0:
                matrix[x][y] = min(matrix[x - 1][y], matrix[x][y - 1], matrix[x - 1][y - 1]) + 1
            squares += matrix[x][y]
    return squares


def countBattleships(board: List[List[str]]) -> int:
    directions, result = [[-1, 0], [1, 0], [0, -1], [0, 1]], 0

    def traverse(x, y):
        board[x][y] = "."
        for x_direction, y_direction in directions:
            x_position, y_position = x + x_direction, y + y_direction
            if 0 <= x_position < len(board) and 0 <= y_position < len(board[0]) and board[x_position][
                y_position] == "X":
                traverse(x_position, y_position)

    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == "X":
                result += 1
                traverse(x, y)
    return result


def islandPerimeter(grid: List[List[int]]) -> int:
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def traverse(x: int, y: int) -> int:
        perimeter_size = 0
        grid[x][y] = -1
        for x_direction, y_direction in directions:
            x_position, y_position = x + x_direction, y + y_direction
            if 0 <= x_position < len(grid) and 0 <= y_position < len(grid[0]):
                if grid[x_position][y_position] == 1:
                    perimeter_size += traverse(x_position, y_position)
                elif grid[x_position][y_position] == 0:
                    perimeter_size += 1
            else:
                perimeter_size += 1
        return perimeter_size

    result = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == 1:
                result += traverse(x, y)
    return result


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def find_area(x: int, y: int) -> int:
        result = 1
        grid[x][y] = 0
        for x_direction, y_direction in directions:
            x_position, y_position = x + x_direction, y + y_direction
            if 0 <= x_position < len(grid) and 0 <= y_position < len(grid[0]) and grid[x_position][y_position]:
                result += find_area(x_position, y_position)
        return result

    max_area = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == 1:
                max_area = max(max_area, find_area(x, y))
    return max_area


def updateBoard(board: List[List[str]], click: List[int]) -> List[List[str]]:
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    if board[click[0]][click[1]] == 'M':
        board[click[0]][click[1]] = 'X'
        return board

    def count_adjacent_mines(x: int, y: int) -> int:
        result = 0
        for x_direction, y_direction in directions:
            x_position, y_position = x + x_direction, y + y_direction
            if 0 <= x_position < len(board) and 0 <= y_position < len(board[0]):
                if board[x_position][y_position] == 'M':
                    result += 1
        return result

    def update_function(x: int, y: int):
        number_of_adjacent_mines = count_adjacent_mines(x, y)
        if not number_of_adjacent_mines:
            board[x][y] = 'B'
            for x_direction, y_direction in directions:
                x_position, y_position = x + x_direction, y + y_direction
                if 0 <= x_position < len(board) and 0 <= y_position < len(board[0]) \
                        and board[x_position][y_position] == 'E':
                    update_function(x_position, y_position)
        else:
            board[x][y] = str(number_of_adjacent_mines)

    update_function(click[0], click[1])

    return board
