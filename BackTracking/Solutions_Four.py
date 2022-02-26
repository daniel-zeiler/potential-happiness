from typing import List


def letter_combinations(digits: str) -> List[str]:
    mapping = {
        '1': [],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def backtracking_function(digits_remaining, temp_result):
        result = []
        if not digits_remaining:
            result.append(temp_result)
        else:
            digit = digits_remaining[0]
            for mapped_letter in mapping[digit]:
                result.extend(backtracking_function(digits_remaining[1:], temp_result + mapped_letter))
        return result

    return backtracking_function(digits, '')


def generate_parentheses(n: int) -> List[str]:
    def backtracking_function(open_remaining, close_remaining, temp_result):
        result = []
        if open_remaining == 0 and close_remaining == 0:
            result.append(temp_result)
        else:
            if open_remaining == close_remaining:
                result.extend(backtracking_function(open_remaining - 1, close_remaining, temp_result + '('))
            else:
                if open_remaining != 0:
                    result.extend(backtracking_function(open_remaining - 1, close_remaining, temp_result + '('))
                result.extend(backtracking_function(open_remaining, close_remaining - 1, temp_result + ')'))
        return result

    return backtracking_function(n, n, '')


def permute(nums: List[int]) -> List[List[int]]:
    def backtracking_function(nums_remaining, temp_result):
        result = []
        if not nums_remaining:
            result.append(temp_result)
        for i, num in enumerate(nums_remaining):
            result.extend(backtracking_function(nums_remaining[:i] + nums_remaining[i + 1:], temp_result + [num]))
        return result

    return backtracking_function(nums, [])


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def backtracking_function(nums_remaining, temp_result):
        result.append(temp_result)
        for i, num in enumerate(nums_remaining):
            backtracking_function(nums_remaining[i + 1:], temp_result + [num])

    backtracking_function(nums, [])
    return result


def exist(board: List[List[str]], word: str) -> bool:
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def yield_valid_directions(x, y, letter):
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(board) and 0 <= y_target < len(board[0]):
                if board[x_target][y_target] == letter:
                    yield x_target, y_target

    def traverse(x, y, word_remaining):
        if not word_remaining:
            return True
        letter = word_remaining[0]
        for x_direction, y_direction in yield_valid_directions(x, y, letter):
            board[x_direction][y_direction], temp = None, board[x_direction][y_direction]
            if traverse(x_direction, y_direction, word_remaining[1:]):
                return True
            board[x_direction][y_direction] = temp
        return False

    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == word[0]:
                board[x][y], temp = None, board[x][y]
                if traverse(x, y, word[1:]):
                    return True
                board[x][y] = temp
    return False


def letter_case_permutations(s: str) -> List[str]:
    def backtracking_function(string_remaining, temp_result):
        result = []
        if not string_remaining:
            result.append(temp_result)
        else:
            letter = string_remaining[0]
            if letter.isalpha():
                result.extend(backtracking_function(string_remaining[1:], temp_result + letter.upper()))
            result.extend(backtracking_function(string_remaining[1:], temp_result + letter))
        return result

    return backtracking_function(s, '')


def all_paths_source_to_target(graph: List[List[int]]) -> List[List[int]]:
    source = 0
    target = len(graph) - 1

    def traverse(node_id, path, visited):
        result = []
        if node_id == target:
            result.append(path)
        else:
            for adjacent in graph[node_id]:
                if adjacent not in visited:
                    result.extend(traverse(adjacent, path + [adjacent], visited | {adjacent}))
        return result

    return traverse(source, [source], {source})


def num_tile_possibilities(tiles: str) -> int:
    def backtracking_function(tiles_remaining):
        result = 1
        if not tiles:
            return result
        for i, tile in enumerate(tiles_remaining):
            if i == 0 or tile != tiles_remaining[i - 1]:
                result += backtracking_function(tiles_remaining[:i] + tiles_remaining[i + 1:])
        return result

    return backtracking_function(tiles) - 1


def get_maximum_gold(grid: List[List[int]]) -> int:
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def yield_directions(x, y):
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]):
                if grid[x_target][y_target] != 0:
                    yield x_target, y_target

    def traverse(x, y):
        temp_result = 0
        grid[x][y], temp = 0, grid[x][y]
        for x_direction, y_direction in yield_directions(x, y):
            temp_result = max(temp_result, traverse(x_direction, y_direction))
        grid[x][y] = temp
        return temp_result + temp

    result = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value != 0:
                result = max(result, traverse(x, y))
    return result


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def backtracking_function(candidates_remaining, sum_so_far, values):
        result = []
        if sum_so_far == target:
            result.append(values)
        elif sum_so_far < target:
            for i, candidate in enumerate(candidates_remaining):
                result.extend(
                    backtracking_function(candidates_remaining[i:], sum_so_far + candidate, values + [candidate])
                )
        return result

    candidates.sort()
    return backtracking_function(candidates, 0, [])


def combinationSum3(k: int, n: int) -> List[List[int]]:
    def backtracking_function(candidates_remaining, sum_so_far, values):
        result = []
        if sum_so_far == n and len(values) == k:
            result.append(values)
        elif len(values) < k and sum_so_far < n:
            for i, candidate in enumerate(candidates_remaining):
                result.extend(
                    backtracking_function(candidates_remaining[i + 1:], sum_so_far + candidate, values + [candidate])
                )
        return result

    return backtracking_function([n for n in range(1, 10)], 0, [])


def combine(n: int, k: int) -> List[List[int]]:
    number_range = [n for n in range(1, n + 1)]

    def backtracking_function(numbers_remaining, numbers_so_far):
        result = []
        if len(numbers_so_far) == k:
            result.append(numbers_so_far)
        else:
            for i, value in enumerate(numbers_remaining):
                result.extend(backtracking_function(numbers_remaining[i + 1:], numbers_so_far + [value]))
        return result

    return backtracking_function(number_range, [])
