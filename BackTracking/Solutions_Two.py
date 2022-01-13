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
    result = []

    def backtracking_function(digits, combination):
        if not digits:
            result.append(combination)
        else:
            for value in map[digits[0]]:
                backtracking_function(digits[1:], combination + value)

    backtracking_function(digits, '')
    return result


def generate_parentheses(n: int) -> List[str]:
    result = []

    def backtracking_function(open, close, result_so_far):
        if open == close == 0:
            result.append(result_so_far)
        else:
            if open:
                backtracking_function(open - 1, close, result_so_far + '(')
            if open < close:
                backtracking_function(open, close - 1, result_so_far + ')')

    backtracking_function(n, n, '')
    return result


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    def permute_function(numbers, permutation):
        if not numbers:
            result.append(permutation)
        for i, number in enumerate(numbers):
            permute_function(numbers[:i] + numbers[i + 1:], permutation + [number])

    permute_function(nums, [])
    return result


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def subset_function(numbers, subset):
        result.append(subset)
        if numbers:
            for i, number in enumerate(numbers):
                subset_function(numbers[i + 1:], subset + [number])

    subset_function(nums, [])
    return result


def exist(board: List[List[str]], word: str) -> bool:
    def get_directions(x, y, character):
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for x_direction, y_direction in directions:
            x_target = x + x_direction
            y_target = y + y_direction
            if 0 <= x_target < len(board) and 0 <= y_target < len(board[0]):
                if board[x_target][y_target] == character:
                    yield x_target, y_target

    def traverse(x, y, word_remaining):
        if not word_remaining:
            return True

        temp, board[x][y] = board[x][y], None

        for x_direction, y_direction in get_directions(x, y, word_remaining[0]):
            if traverse(x_direction, y_direction, word_remaining[1:]):
                return True

        board[x][y] = temp

    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == word[0]:
                if traverse(x, y, word[1:]):
                    return True
    return False


def letter_case_permutations(s: str) -> List[str]:
    result = []

    def permute_function(s_remaining, word_so_far):
        if not s_remaining:
            result.append(word_so_far)
        else:
            if s_remaining[0].isalpha():
                permute_function(s_remaining[1:], word_so_far + s_remaining[0].upper())
            permute_function(s_remaining[1:], word_so_far + s_remaining[0])

    permute_function(s, '')
    return result


def all_paths_source_to_target(graph: List[List[int]]) -> List[List[int]]:
    def get_graph(edges):
        graph = collections.defaultdict(list)
        for origin, destinations in enumerate(edges):
            graph[origin] = destinations
        return graph

    graph = get_graph(graph)
    result = []

    def traverse(node_index: int, visited: set, path: List[int]):
        if node_index == len(graph) - 1:
            result.append(path)
        for adjacent in graph[node_index]:
            if adjacent not in visited:
                visited.add(adjacent)
                traverse(adjacent, visited, path + [adjacent])
                visited.remove(adjacent)

    traverse(0, {0}, [0])
    return result


def num_tile_possibilities(tiles: str) -> int:
    tiles = sorted(list(tiles))

    def traverse(tiles_remaining):
        result = 1
        for i, tile in enumerate(tiles_remaining):
            if i and tiles_remaining[i - 1] == tile:
                continue
            result += traverse(tiles_remaining[:i] + tiles_remaining[i + 1:])
        return result

    result = 0
    for i, tile in enumerate(tiles):
        if i and tiles[i - 1] == tile:
            continue
        result += traverse(tiles[:i] + tiles[i + 1:])
    return result


class CombinationIterator:

    def __init__(self, characters: str, combination_length: int):
        self.characters = sorted(characters)
        self.combination_length = combination_length
        self.pointer_a = 0
        self.pointer_b = 1
        self.combo = None

    def next(self) -> str:
        if not self.combo:
            self.combo = self.characters[self.pointer_a] + self.characters[self.pointer_b]
            return self.combo
        if self.pointer_b == len(self.characters) - 1:
            self.pointer_a += 1
            self.pointer_b = self.pointer_a + 1
        else:
            self.pointer_b += 1
        self.combo = self.characters[self.pointer_a] + self.characters[self.pointer_b]
        return self.combo

    def hasNext(self) -> bool:
        return self.combo != self.characters[-2] + self.characters[-1]


def get_maximum_gold(grid: List[List[int]]) -> int:
    def get_directions(x, y):
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for x_direction, y_direction in directions:
            x_target = x + x_direction
            y_target = y + y_direction
            if 0 <= x_target < len(grid) and 0 <= y_target < len(grid[0]):
                if grid[x_target][y_target] != 0:
                    yield x_target, y_target

    def traverse(x, y):
        temp, grid[x][y] = grid[x][y], 0
        result = temp
        max_direction = 0
        for x_direction, y_direction in get_directions(x, y):
            max_direction = max(max_direction, traverse(x_direction, y_direction))
        result += max_direction
        grid[x][y] = temp
        return result

    result = 0
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            result = max(traverse(x, y), result)
    return result


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def combo_sum_function(candidates_remaining, target_remaining, combo):
        if target_remaining == 0:
            result.append(combo)
        elif target_remaining > 0 and candidates_remaining:
            for i, candidate in enumerate(candidates_remaining):
                if i == 0:
                    combo_sum_function(candidates_remaining, target_remaining - candidate, combo + [candidate])
                else:
                    combo_sum_function(candidates_remaining[i + 1:], target_remaining - candidate, combo + [candidate])

    combo_sum_function(candidates, target, [])
    return result


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    def yield_valid_directions(x, y, character):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for x_direction, y_direction in directions:
            x_target = x + x_direction
            y_target = y + y_direction
            if 0 <= x_target < len(board) and 0 <= y_target < len(board[0]):
                if board[x_target][y_target] == character:
                    yield x_target, y_target

    def traverse(x, y, word_remaining):
        if not word_remaining:
            return True
        temp, board[x][y] = board[x][y], None
        for x_direction, y_direction in yield_valid_directions(x, y, word_remaining[0]):
            if traverse(x_direction, y_direction, word_remaining[1:]):
                board[x][y] = temp
                return True
        board[x][y] = temp
        return False

    result = []
    for x, row in enumerate(board):
        for y, value in enumerate(row):
            for word in words:
                if value == word[0]:
                    if traverse(x, y, word[1:]):
                        result.append(word)
    return result


def combinationSum3(k: int, n: int) -> List[List[int]]:
    values = [i for i in range(1, min(n - 2, 10))]
    result = []

    def combo_sum_function(values_remaining, target_remaining, combo_so_far):
        if target_remaining == 0 and len(combo_so_far) == k:
            result.append(combo_so_far)
        elif combo_so_far == k or target_remaining < 0:
            return
        else:
            for i, value in enumerate(values_remaining):
                combo_sum_function(values_remaining[i + 1:], target_remaining - value, combo_so_far + [value])

    combo_sum_function(values, n, [])
    return result


def combine(n: int, k: int) -> List[List[int]]:
    result = []
    values = [i for i in range(1, n + 1)]

    def combine_function(values_remaining, values_so_far):
        if len(values_so_far) == k:
            result.append(values_so_far)
        else:
            for i, value in enumerate(values_remaining):
                combine_function(values_remaining[i + 1:], values_so_far + [value])

    combine_function(values, [])
    return result
