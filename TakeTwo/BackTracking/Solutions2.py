from typing import List


def letter_combinations(digits: str) -> List[str]:
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["h", "i", "j"],
        "5": ["k", "l", "m"],
        "6": ["n", "o", "p"]
    }
    result = []

    def letter_combo_helper(digits_remaining: str, tmp_result: str):
        if not digits_remaining:
            result.append(tmp_result)
        for character in mapping[digits_remaining[0]]:
            letter_combo_helper(digits_remaining[1:], tmp_result + character)

    letter_combo_helper(digits, "")
    return result


def generate_parentheses(n: int) -> List[str]:
    result = []

    def generate_paren_helper(open_remaining, close_remaining, tmp_result):
        if not open_remaining and not close_remaining:
            result.append(tmp_result)
        elif open_remaining == close_remaining:
            generate_paren_helper(open_remaining - 1, close_remaining, tmp_result + "(")
        elif not open_remaining:
            generate_paren_helper(open_remaining, close_remaining - 1, tmp_result + ")")
        else:
            generate_paren_helper(open_remaining - 1, close_remaining, tmp_result + "(")
            generate_paren_helper(open_remaining, close_remaining - 1, tmp_result + ")")

    generate_paren_helper(n, n, "")
    return result


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    def permute_helper(nums_remaining, temp_result):
        if not nums_remaining:
            result.append(temp_result)
        for i, character in enumerate(nums_remaining):
            permute_helper(nums_remaining[:i] + nums_remaining[i + 1:], temp_result + [character])

    permute_helper(nums, [])
    return result


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def subsets_helper(nums_remaining, temp_result):
        result.append(temp_result)
        for i, character in enumerate(nums_remaining):
            subsets_helper(nums_remaining[i + 1:], temp_result + [character])

    subsets_helper(nums, [])
    return result


def exist(board: List[List[str]], word: str) -> bool:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def traverse_board(x, y, word_remaining) -> bool:
        if not word_remaining:
            return True
        board[x][y], tmp = None, board[x][y]
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(board) and 0 <= y_target < len(board[0]):
                if board[x_target][y_target] == word_remaining[0] and traverse_board(x_target, y_target,
                                                                                     word_remaining[1:]):
                    return True
        board[x][y] = tmp
        return False

    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == word[0]:
                if traverse_board(x, y, word[1:]):
                    return True
    return False


def letter_case_permutations(s: str) -> List[str]:
    result = []

    def letter_case_helper(letters_remaining, temp_result):
        if not letters_remaining:
            result.append(temp_result)
        else:
            if not letters_remaining[0].isnumeric():
                letter_case_helper(letters_remaining[1:], temp_result + letters_remaining[0].upper())
            letter_case_helper(letters_remaining[1:], temp_result + letters_remaining[0])

    letter_case_helper(s, "")
    return result


def all_paths_source_to_target(graph: List[List[int]]) -> List[List[int]]:
    result = []

    def traverse(current_position, path, visited):
        if current_position == len(graph) - 1:
            result.append(path)
        else:
            for adjacent in graph[current_position]:
                if adjacent not in visited:
                    traverse(adjacent, path + [adjacent], visited | {adjacent})

    traverse(0, [0], {0})
    return result


def num_tile_possibilities(tiles: str) -> int:
    def num_tiles_helper(tiles_remaining):
        result = 1
        for i, tile in enumerate(tiles_remaining):
            if not i or tile != tiles_remaining[i - 1]:
                result += num_tiles_helper(tiles_remaining[:i] + tiles_remaining[i + 1:])
        return result

    return num_tiles_helper(tiles) - 1


def get_maximum_gold(grid: List[List[int]]) -> int:
    max_available = 0
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def max_gold_helper(x, y):
        max_on_path, gold, tmp, grid[x][y] = 0, grid[x][y], grid[x][y], -1

        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]) and grid[x_target][y_target] not in (-1, 0):
                max_on_path = max(max_on_path, max_gold_helper(x_target, y_target))

        grid[x][y] = tmp
        return gold + max_on_path

    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            max_available = max(max_available, max_gold_helper(x, y))

    return max_available


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def combo_sum_helper(candidates, target_remaining, temp_result):
        if target_remaining == 0:
            result.append(temp_result)
        elif target_remaining > 0:
            for i, value in enumerate(candidates):
                combo_sum_helper(candidates[i:], target_remaining - value, temp_result + [value])

    combo_sum_helper(candidates, target, [])
    return result


def combination_sum_3(k: int, n: int) -> List[List[int]]:
    result = []

    def combination_helper(numbers_remaining, target_remaining, temp_result):
        if len(temp_result) < k and target_remaining > 0:
            for i, value in enumerate(numbers_remaining):
                combination_helper(numbers_remaining[i + 1:], target_remaining - value, temp_result + [value])

        if len(temp_result) == k and not target_remaining:
            result.append(temp_result)

    combination_helper(range(1, n + 1), n, [])
    return result


def combine(n: int, k: int) -> List[List[int]]:
    result = []

    def combine_helper(numbers_remaining, temp_result):
        if len(temp_result) == k:
            result.append(temp_result)
        elif len(temp_result) < k:
            for i, value in enumerate(numbers_remaining):
                combine_helper(numbers_remaining[i + 1:], temp_result + [value])

    combine_helper(range(1, n + 1), [])
    return result
