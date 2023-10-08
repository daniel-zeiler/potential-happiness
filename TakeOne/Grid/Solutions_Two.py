import collections
from typing import List


def largest_parameter(input):
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def traverse(x, y):
        input[x][y] = -1
        parameter = 0
        on_parameter = False
        for x_direction, y_direction in directions:
            new_x = x + x_direction
            new_y = y + y_direction
            if 0 <= new_x < len(input) and 0 <= new_y < len(input[0]):
                if input[new_x][new_y] == 0:
                    on_parameter = True
                elif input[new_x][new_y] == 1:
                    parameter += traverse(new_x, new_y)
            else:
                on_parameter = True
        if on_parameter:
            parameter += 1
        return parameter

    max_parameter = 0

    for x, row in enumerate(input):
        for y, value in enumerate(row):
            if value == 1:
                max_parameter = max(max_parameter, traverse(x, y))
    return max_parameter


def maxIncreaseKeepingSkyline(grid: List[List[int]]) -> int:
    max_x_list = [float('-inf') for _ in range(len(grid))]
    max_y_list = [float('-inf') for _ in range(len(grid[0]))]
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            max_x_list[x] = max(max_x_list[x], value)
            max_y_list[y] = max(max_y_list[y], value)

    max_increase = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            max_increase += min(max_x_list[x] - value, max_y_list[y] - value)
    return max_increase


def countSquares(matrix: List[List[int]]) -> int:
    num_squares = 0
    temp_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if (x == 0 or y == 0) and value == 1:
                temp_matrix[x][y] = 1
            elif value == 1:
                temp_matrix[x][y] = min(temp_matrix[x - 1][y], temp_matrix[x][y - 1], temp_matrix[x - 1][y - 1]) + 1
            num_squares += temp_matrix[x][y]
    return num_squares


def countBattleships(board: List[List[str]]) -> int:
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def traverse(x, y):
        board[x][y] = "."
        for x_direction, y_direction in directions:
            new_x = x + x_direction
            new_y = y + y_direction
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == "X":
                traverse(new_x, new_y)

    number_of_ships = 0
    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == 'X':
                traverse(x, y)
                number_of_ships += 1
    return number_of_ships


def islandPerimeter(grid: List[List[int]]) -> int:
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def traverse(x, y):
        parameter = 0
        grid[x][y] = -1
        for x_direction, y_direction in directions:
            new_x = x + x_direction
            new_y = y + y_direction
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                if grid[new_x][new_y] == 1:
                    parameter += traverse(new_x, new_y)
                elif grid[new_x][new_y] == 0:
                    parameter += 1
            else:
                parameter += 1
        return parameter

    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == 1:
                return traverse(x, y)


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def traverse(x, y):
        area = 1
        grid[x][y] = 0
        for x_direction, y_direction in directions:
            new_x = x + x_direction
            new_y = y + y_direction
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                area += traverse(new_x, new_y)
        return area

    max_area = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == 1:
                max_area = max(max_area, traverse(x, y))
    return max_area


def getMaximumGold(grid: List[List[int]]) -> int:
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def traverse(x, y):
        temp, gold, grid[x][y], max_path = grid[x][y], grid[x][y], 0, 0
        for x_direction, y_direction in directions:
            new_x = x + x_direction
            new_y = y + y_direction
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != 0:
                max_path = max(max_path, traverse(new_x, new_y))
        grid[x][y] = temp
        return gold + max_path

    max_gold = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value != 0:
                max_gold = max(max_gold, traverse(x, y))
    return max_gold


def numEnclaves(grid: List[List[int]]) -> int:
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def traverse(x, y):
        grid[x][y] = 0
        enclaves = 1
        is_enclave = True
        for x_direction, y_direction in directions:
            new_x = x + x_direction
            new_y = y + y_direction
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                if grid[new_x][new_y] == 1:
                    is_enclave_traverse, enclaves_traverse = traverse(new_x, new_y)
                    enclaves += enclaves_traverse
                    if not is_enclave_traverse:
                        is_enclave = False
            else:
                is_enclave = False
        return is_enclave, enclaves

    result = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == 1:
                is_enclave, enclaves = traverse(x, y)
                if is_enclave:
                    result += enclaves
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
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def traverse(x, y, old_color):
        image[x][y] = newColor
        for x_direction, y_direction in directions:
            new_x, new_y = x + x_direction, y + y_direction
            if 0 <= new_x < len(image) and 0 <= new_y < len(image[0]) and image[new_x][new_y] == old_color:
                traverse(new_x, new_y, old_color)

    old_color = image[sr][sc]

    if old_color == newColor:
        return image
    traverse(sr, sc, old_color)
    return image


def numIslands(grid: List[List[str]]) -> int:
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def traverse(x, y):
        grid[x][y] = "0"
        for x_direction, y_direction in directions:
            new_x, new_y = x + x_direction, y + y_direction
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == "1":
                traverse(new_x, new_y)

    num_island = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == "1":
                num_island += 1
                traverse(x, y)
    return num_island


def orangesRotting(grid: List[List[int]]) -> int:
    rotten_queue = collections.deque()
    num_fresh = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == 2:
                rotten_queue.append([0, x, y])
            elif value == 1:
                num_fresh += 1

    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    time_it_takes = 0
    while rotten_queue:
        time_it_takes, x, y = rotten_queue.popleft()
        for x_direction, y_direction in directions:
            new_x, new_y = x + x_direction, y + y_direction
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                grid[new_x][new_y] = 2
                rotten_queue.append([time_it_takes + 1, new_x, new_y])
                num_fresh -= 1

    if num_fresh > 0:
        return -1
    return time_it_takes
