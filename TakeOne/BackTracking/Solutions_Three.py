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

    def letter_combinations_backtracking(digits_remaining, combination):
        result = []
        if not digits_remaining:
            result.append(combination)
        else:
            for value in map[digits_remaining[0]]:
                result.extend(letter_combinations_backtracking(digits_remaining[1:], combination + value))
        return result

    return letter_combinations_backtracking(digits, '')


def generate_parentheses(n: int) -> List[str]:
    def generate_parentheses_backtracking(open, close, generated_parens):
        result = []
        if open == 0 and close == 0:
            result.append(generated_parens)
        elif close == open:
            result.extend(generate_parentheses_backtracking(open - 1, close, generated_parens + '('))
        else:
            if open != 0:
                result.extend(generate_parentheses_backtracking(open - 1, close, generated_parens + '('))
            result.extend(generate_parentheses_backtracking(open, close - 1, generated_parens + ')'))
        return result

    return generate_parentheses_backtracking(n, n, '')


def permute(nums: List[int]) -> List[List[int]]:
    def permute_backtracking(nums_remaining, permutation):
        result = []
        if not nums_remaining:
            result.append(permutation)
        else:
            for i, number in enumerate(nums_remaining):
                result.extend(permute_backtracking(nums_remaining[:i] + nums_remaining[i + 1:], permutation + [number]))
        return result

    result = []
    for i, number in enumerate(nums):
        result.extend(permute_backtracking(nums[:i] + nums[i + 1:], [number]))
    return result


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def subsets_backtracking(nums_remaining, subset):
        result.append(subset)
        if nums_remaining:
            for i, number in enumerate(nums_remaining):
                subsets_backtracking(nums_remaining[i + 1:], subset + [number])

    subsets_backtracking(nums, [])
    return result


def exist(board: List[List[str]], word: str) -> bool:
    def yield_valid_directions(x, y, target_character):
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(board) and 0 <= y_target < len(board[0]):
                if board[x_target][y_target] == target_character:
                    yield x_target, y_target

    def exist_backtracking(x, y, word_remaining):
        if not word_remaining:
            return True
        board[x][y], temp = None, board[x][y]
        for x_direction,y_direction in yield_valid_directions(x, y, word_remaining[0]):
            if exist_backtracking(x_direction, y_direction, word_remaining[1:]):
                return True
        board[x][y] = temp
        return False

    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == word[0]:
                if exist_backtracking(x, y, word[1:]):
                    return True
    return False
