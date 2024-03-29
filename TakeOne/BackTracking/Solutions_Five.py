import collections
from typing import List


def letter_combinations(digits: str) -> List[str]:
    combinations = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["h", "i", "j"]}

    def backtracking(digits_remaining, temp):
        result = []
        if not digits_remaining:
            result.append(temp)
        else:
            for comb in combinations[digits_remaining[0]]:
                result.extend(backtracking(digits_remaining[1:], temp + comb))
        return result

    return backtracking(digits, "")


def generate_parentheses(n: int) -> List[str]:
    def backtrack_function(open, close, temp):
        result = []
        if not open and not close:
            result.append(temp)
        elif open == close:
            result.extend(backtrack_function(open - 1, close, temp + "("))
        else:
            if open:
                result.extend(backtrack_function(open - 1, close, temp + "("))
            result.extend(backtrack_function(open, close - 1, temp + ")"))

        return result

    return backtrack_function(n, n, "")


def permute(nums: List[int]) -> List[List[int]]:
    def backtrack_function(nums_remaining, temp):
        result = []
        if not nums_remaining:
            result.append(temp)
        else:
            for i, number in enumerate(nums_remaining):
                result.extend(backtrack_function(nums_remaining[:i] + nums_remaining[i + 1:], [number] + temp))
        return result

    return backtrack_function(nums, [])


def subsets(nums: List[int]) -> List[List[int]]:
    def backtrack_subsets(nums_remaining, temp):
        result = []
        result.append(temp)
        for i, number in enumerate(nums_remaining):
            result.extend(backtrack_subsets(nums_remaining[i + 1:], temp + [number]))
        return result

    return backtrack_subsets(nums, [])


def exist(board: List[List[str]], word: str) -> bool:
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def traverse(x, y, word_remaining):
        if not word_remaining:
            return True
        board[x][y], tmp = "false", board[x][y]
        for x_direction, y_direction in directions:
            new_x, new_y = x + x_direction, y + y_direction
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == word_remaining[0]:
                if traverse(new_x, new_y, word_remaining[1:]):
                    return True
        board[x][y] = tmp
        return False

    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == word[0]:
                found = traverse(x, y, word[1:])
                if found:
                    return True
    return False


def letter_case_permutations(s: str) -> List[str]:
    def backtracking_function(letters_remaining, tmp):
        result = []
        if not letters_remaining:
            result.append(tmp)
        else:
            if letters_remaining[0].isalpha():
                result.extend(backtracking_function(letters_remaining[1:], tmp + letters_remaining[0].lower()))
                result.extend(backtracking_function(letters_remaining[1:], tmp + letters_remaining[0].upper()))
            else:
                result.extend(backtracking_function(letters_remaining[1:], tmp + letters_remaining[0]))
        return result

    return backtracking_function(s, "")


def all_paths_source_to_target(graph: List[List[int]]) -> List[List[int]]:
    def traverse(current_position, path):
        result = []
        if current_position == len(graph) - 1:
            result.append(path)
        for next_node in graph[current_position]:
            result.extend(traverse(next_node, path + [next_node]))
        return result

    return traverse(0, [0])


def num_tile_possibilities(tiles: str) -> int:
    def traverse(tiles_remaining):
        result = 1
        for i, tile in enumerate(tiles_remaining):
            if i == 0 or tile != tiles_remaining[i - 1]:
                result += traverse(tiles_remaining[:i] + tiles_remaining[i + 1:])
        return result

    return traverse(tiles) - 1


def get_maximum_gold(grid: List[List[int]]) -> int:
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def traverse(x, y) -> int:
        temp, grid[x][y] = grid[x][y], 0
        max_path = 0
        for x_direction, y_direction in directions:
            new_x, new_y = x_direction + x, y_direction + y
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != 0:
                max_path = max(traverse(new_x, new_y), max_path)
        grid[x][y] = temp
        return max_path + temp

    max_path = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value != 0:
                max_path = max(max_path, traverse(x, y))
    return max_path


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def traverse(candidates, target_remaining, combo):
        result = []
        if target_remaining == 0:
            result.append(combo)
        elif target_remaining > 0:
            for i, candid in enumerate(candidates):
                result.extend(traverse(candidates[i:], target_remaining - candid, combo + [candid]))
        return result

    candidates.sort()
    return traverse(candidates, target, [])


def combinationSum3(k: int, n: int) -> List[List[int]]:
    def traverse(nums_remaining, nums_so_far, remainder):
        result = []
        if remainder == 0 and len(nums_so_far) == k:
            result.append(nums_so_far)
        elif remainder > 0:
            for i, value in enumerate(nums_remaining):
                result.extend(
                    traverse(nums_remaining[i + 1:], nums_so_far + [value], remainder - value))
        return result

    r = [i for i in range(1, 9)]
    result = []
    for i, value in enumerate(r):
        result.extend(traverse(r[i + 1:], [value], n - value))
    return result


def combine(n: int, k: int) -> List[List[int]]:
    def traverse(nums_remaining, nums_so_far):
        result = []
        if len(nums_so_far) == k:
            result.append(nums_so_far)
        else:
            for i, value in enumerate(nums_remaining):
                result.extend(traverse(nums_remaining[i + 1:], nums_so_far + [value]))
        return result

    result = []
    r = [i for i in range(1, n + 1)]
    for i, value in enumerate(r):
        result.extend(traverse(r[i + 1:], [value]))
    return result
