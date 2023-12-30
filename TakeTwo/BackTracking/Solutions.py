from typing import List


def letter_combinations(digits: str) -> List[str]:
    result = []
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"]
    }

    def backtrack_function(letters_remaining, tmp):
        if not letters_remaining:
            result.append(tmp)
        else:
            for letter in mapping[letters_remaining[0]]:
                backtrack_function(letters_remaining[1:], tmp + letter)

    backtrack_function(digits, "")
    return result


def generate_parentheses(n: int) -> List[str]:
    result = []

    def backtrack_function(open_remaining, close_remaining, tmp):
        if not open_remaining and not close_remaining:
            result.append(tmp)
        elif not open_remaining:
            backtrack_function(open_remaining, close_remaining - 1, tmp + ")")
        elif open_remaining == close_remaining:
            backtrack_function(open_remaining - 1, close_remaining, tmp + "(")
        else:
            backtrack_function(open_remaining - 1, close_remaining, tmp + "(")
            backtrack_function(open_remaining, close_remaining - 1, tmp + ")")

    backtrack_function(n, n, "")
    return result


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    def permutation_helper(nums_remaining, tmp):
        if not nums_remaining:
            result.append(tmp)
        else:
            for i, num in enumerate(nums_remaining):
                permutation_helper(nums_remaining[:i] + nums_remaining[i + 1:], tmp + [num])

    permutation_helper(nums, [])
    return result


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def subset_function(nums_remaining, tmp):
        result.append(tmp)
        for i, num in enumerate(nums_remaining):
            subset_function(nums_remaining[i + 1:], tmp + [num])

    subset_function(nums, [])
    return result


def exist(board: List[List[str]], word: str) -> bool:
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def backtracking_function(x, y, word):
        if not word:
            return True
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(board) and 0 <= y_target < len(board[0]) and board[x_target][y_target] == word[0]:
                temp, board[x_target][y_target] = word[0], "-1"
                if backtracking_function(x_target, y_target, word[1:]):
                    return True
                board[x_target][y_target] = temp
        pass

    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == word[0]:
                board[x][y] = "-1"
                if backtracking_function(x, y, word[1:]):
                    return True
                board[x][y] = value
    return False


def letter_case_permutations(s: str) -> List[str]:
    result = []

    def backtracking_function(word_remaining, tmp):
        if not word_remaining:
            result.append(tmp)
        else:
            if word_remaining[0].isnumeric():
                backtracking_function(word_remaining[1:], tmp + word_remaining[0])
            else:
                backtracking_function(word_remaining[1:], tmp + word_remaining[0].lower())
                backtracking_function(word_remaining[1:], tmp + word_remaining[0].upper())

    backtracking_function(s, "")
    return result


def all_paths_source_to_target(graph: List[List[int]]) -> List[List[int]]:
    result = []

    def traverse(curr_node: int, visited: set):
        if curr_node == len(graph) - 1:
            result.append(list(visited))
        else:
            for adjacent in graph[curr_node]:
                if adjacent not in visited:
                    traverse(adjacent, visited.union({adjacent}))

    traverse(0, {0})
    return result


def num_tile_possibilities(tiles: str) -> int:
    def backtracking_function(tiles_remaining, tmp):
        result = 0
        if tmp:
            result = 1
        for i, tile in enumerate(tiles_remaining):
            if not i or tile != tiles_remaining[i - 1]:
                result += backtracking_function(tiles_remaining[:i] + tiles_remaining[i + 1:], tmp + tile)
        return result

    return backtracking_function(tiles, "")


def get_maximum_gold(grid: List[List[int]]) -> int:
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def traverse_mine(x: int, y: int) -> int:
        tmp, gold, grid[x][y], max_along_path = grid[x][y], grid[x][y], 0, 0
        for x_direction, y_direction in directions:
            x_position, y_position = x + x_direction, y + y_direction
            if 0 <= x_position < len(grid) and 0 <= y_position < len(grid[0]) and grid[x_position][y_position]:
                max_along_path = max(max_along_path, traverse_mine(x_position, y_position))
        grid[x][y] = tmp
        return gold + max_along_path

    max_gold = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value:
                max_gold = max(max_gold, traverse_mine(x, y))
    return max_gold


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def backtracking_function(candidates_remaining, target_remaining, tmp):
        if not target_remaining:
            result.append(tmp)
        if target_remaining > 0:
            for i, value in enumerate(candidates_remaining):
                backtracking_function(candidates_remaining[i:], target_remaining - value, tmp + [value])

    backtracking_function(candidates, target, [])
    return result
