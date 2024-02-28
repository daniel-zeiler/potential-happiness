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


def numEnclaves(grid: List[List[int]]) -> int:
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def traverse(x: int, y: int) -> int:
        size = 1
        on_edge = False
        grid[x][y] = -1
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]):
                if grid[x_target][y_target] == 1:
                    adjacent_size = traverse(x_target, y_target)
                    if not adjacent_size:
                        on_edge = True
                    size += adjacent_size
            else:
                on_edge = True
        if on_edge:
            return 0
        return size

    result = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == 1:
                result += traverse(x, y)
    return result


def minPathSum(grid: List[List[int]]) -> int:
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if x == 0 and y == 0:
                continue
            elif x == 0:
                grid[x][y] += grid[x][y - 1]
            elif y == 0:
                grid[x][y] += grid[x - 1][y]
            else:
                grid[x][y] += min(grid[x - 1][y], grid[x][y - 1])
    return grid[-1][-1]


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    source_color = image[sr][sc]
    if source_color == newColor:
        return image

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def traverse(x, y, source_color):
        image[x][y] = newColor
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(image) and 0 <= y_target < len(image[0]) and image[x_target][
                y_target] == source_color:
                traverse(x_target, y_target, source_color)

    traverse(sr, sc, source_color)
    return image


def numIslands(grid: List[List[str]]) -> int:
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def traverse(x, y):
        grid[x][y] = "0"
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]) and grid[x_target][y_target] == '1':
                traverse(x_target, y_target)

    result = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == '1':
                traverse(x, y)
                result += 1
    return result


from collections import deque


def orangesRotting(grid: List[List[int]]) -> int:
    time, num_oranges, queue, directions = 0, 0, deque([]), [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == 2:
                queue.append((time, x, y))
            elif value == 1:
                num_oranges += 1

    while queue:
        time, x, y = queue.popleft()
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]) and grid[x_target][y_target] == 1:
                num_oranges -= 1
                grid[x_target][y_target] = 2
                queue.append((time + 1, x_target, y_target))

    return time if not num_oranges else -1


def maximalSquare(matrix: List[List[str]]) -> int:
    max_square = 0

    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if x != 0 and y != 0 and matrix[x][y] == "1":
                matrix[x][y] = str(
                    int(matrix[x][y]) + min(int(matrix[x - 1][y]), int(matrix[x - 1][y - 1]), int(matrix[x][y - 1])))
            max_square = max(int(matrix[x][y]) ** 2, max_square)
    return max_square


import collections


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    directions = [[-1, -1], [-1, 0], [-1, 1], [1, 0], [0, 1], [0, -1], [1, -1], [1, 1]]
    if grid[0][0] == 1:
        return -1
    grid[0][0] = 1
    queue = collections.deque([(1, 0, 0)])
    while queue:
        distance, x, y = queue.popleft()
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            return distance
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]):
                if grid[x_target][y_target] == 0:
                    grid[x][y] = 1
                    queue.append((distance + 1, x_target, y_target))
    return -1


def getMaximumGold(grid: List[List[int]]) -> int:
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def traverse(x: int, y: int) -> int:
        result, temp, grid[x][y], max_path = grid[x][y], grid[x][y], 0, 0
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]) and grid[x_target][y_target]:
                max_path = max(max_path, traverse(x_target, y_target))
        grid[x][y] = temp
        return result + max_path

    max_val = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value != 0:
                max_val = max(max_val, traverse(x, y))
    return max_val


def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    queue = deque([])
    result = [[None for _ in range(len(mat[0]))] for _ in range(len(mat))]
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    for x, row in enumerate(mat):
        for y, value in enumerate(row):
            if value == 0:
                result[x][y] = 0
                queue.append((0, x, y))

    while queue:
        distance, x, y = queue.popleft()
        result[x][y] = distance
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(mat) and 0 <= y_target < len(mat[0]) and result[x_target][y_target] is None:
                result[x_target][y_target] = distance + 1
                queue.append((distance + 1, x_target, y_target))

    return result
