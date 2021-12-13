import collections
from typing import List


def letter_combinations(digits: str) -> List[str]:
    map = {
        '1': ['@'],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        '0': [' ']
    }
    output = []

    def backtrack_helper(digits, combination_so_far):
        if not digits:
            output.append(combination_so_far)
        else:
            for character in map[digits[0]]:
                backtrack_helper(digits[1:], combination_so_far + character)

    backtrack_helper(digits, '')
    return output


def generate_parentheses(n: int) -> List[str]:
    result = []

    def backtracking_function(open, close, result_so_far):
        if open == 0 and close == 0:
            result.append(result_so_far)
        elif open == close:
            backtracking_function(open - 1, close, result_so_far + '(')
        elif open == 0:
            backtracking_function(open, close - 1, result_so_far + ')')
        else:
            backtracking_function(open - 1, close, result_so_far + '(')
            backtracking_function(open, close - 1, result_so_far + ')')

    backtracking_function(n, n, '')
    return result


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    def backtracking_function(input_nums, result_so_far):
        if not input_nums:
            result.append(result_so_far)
        else:
            for index, number in enumerate(input_nums):
                backtracking_function(input_nums[:index] + input_nums[index + 1:], result_so_far + [number])

    backtracking_function(nums, [])

    return result


def exist(board: List[List[str]], word: str) -> bool:
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def get_valid_directions(x, y):
        for x_direction, y_direction in directions:
            new_x = x + x_direction
            new_y = y + y_direction
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                yield new_x, new_y

    def backtracking_function(x, y, word):
        if not word:
            return True
        old_char, board[x][y] = board[x][y], None

        for valid_x, valid_y in get_valid_directions(x, y):
            if board[valid_x][valid_y] == word[0]:
                if backtracking_function(valid_x, valid_y, word[1:]):
                    return True

        board[x][y] = old_char

    for x, row in enumerate(board):
        for y, char in enumerate(row):
            if char == word[0]:
                if backtracking_function(x, y, word[1:]):
                    return True
    return False


def get_maximum_gold(grid: List[List[int]]) -> int:
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    maximum_gold = 0

    def get_valid_directions(x, y):
        for x_direction, y_direction in directions:
            new_x = x + x_direction
            new_y = y + y_direction
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != 0:
                yield x + x_direction, y + y_direction

    def determine_maximum(x, y):
        gold_at_position, max_gold_on_path, grid[x][y] = grid[x][y], 0, 0
        for valid_x, valid_y in get_valid_directions(x, y):
            max_gold_on_path = max(determine_maximum(valid_x, valid_y), max_gold_on_path)
        grid[x][y] = gold_at_position
        return gold_at_position + max_gold_on_path

    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value != 0:
                maximum_gold = max(determine_maximum(x, y), maximum_gold)

    return maximum_gold


def num_tile_possibilities(tiles: str) -> int:
    tiles = sorted(tiles)

    def backtracking_function(tiles, temp):
        count = 0
        if temp:
            count += 1
        for i, tile in enumerate(tiles):
            if i and tiles[i - 1] == tiles[i]:
                continue
            count += backtracking_function(tiles[:i] + tiles[i + 1:], temp + tile)
        return count

    return backtracking_function(tiles, '')


def all_paths_source_to_target(graph: List[List[int]]) -> List[List[int]]:
    result = []

    def traverse(location, path_so_far):
        if location == len(graph) - 1:
            result.append(path_so_far)
        else:
            for adjacent in graph[location]:
                if adjacent not in path_so_far:
                    traverse(adjacent, path_so_far + [adjacent])

    traverse(0, [0])
    return result


def letter_case_permutations(s: str) -> List[str]:
    numbers = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}

    def permute(remaining, so_far):
        result = []
        if not remaining:
            return [so_far]
        if remaining[0] not in numbers:
            result.extend(permute(remaining[1:], so_far + remaining[0].lower()))
            result.extend(permute(remaining[1:], so_far + remaining[0].upper()))
        else:
            result.extend(permute(remaining[1:], so_far + remaining[0]))
        return result

    return permute(s, '')


def subsets(nums: List[int]) -> List[List[int]]:
    pass
