"""
2 arrays of integers
for any integer in arry1 we'll call the closest int from array2.
it's sensor and the difference between the 2 integers can be called the sensor distance.
Return the largest sensor distance.

"""
from typing import List


def find_furthest_sensor_distance(sensor_one: List[int], sensor_two: List[int]):
    sensor_one.sort()

    # use binary search to find the value closest to our target O(logn) operation
    def binary_search(target: int) -> int:
        low, high = 0, len(sensor_one) - 1
        while low <= high:
            mid = (high + low) // 2
            if sensor_one[mid] == target:
                return target
            if sensor_one[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        # if low and high are inside the list, compare the two values
        if low < len(sensor_one) and high >= 0:
            if abs(target - sensor_one[low]) < abs(target - sensor_one[high]):
                return sensor_one[low]
            return sensor_one[high]

        # return the value inside the list
        return sensor_one[low] if low == 0 else sensor_one[high]

    # for reach element in sensor_two find the closest element in sensor_one
    # O (m * logn)
    result = 0
    for sensor in sensor_two:
        closest = binary_search(sensor)
        result = max(result, abs(closest - sensor))
    return result


list_one = [-10, 2, 3, 40]
list_two = [-11, 2, 5, 100]
print(find_furthest_sensor_distance(list_one, list_two))

"""
Calculate "1 + 1 - 5"

Calculate "1 * 2 - 5"

Calculate (1 + (2 - 5))

Calculate (1 * (2 - 5))
"""


def calculate_one(input_string: str):
    def process_operation(curr_int, op, result):
        if op == "+":
            result.append(curr_int)
        elif op == "-":
            result.append(-curr_int)
        elif op == "*":
            result.append(result.pop() * curr_int)
        elif op == "/":
            result.append(result.pop() / curr_int)

    def calculator_helper(input_string) -> (int, int):
        input_string = input_string.replace(" ", "")
        result, operation, current_integer, index = [], "+", 0, 0
        while index < len(input_string):
            character = input_string[index]
            if character in ["+", "-", "/", "*"]:
                process_operation(current_integer, operation, result)
                operation, current_integer = character, 0
            elif character == "(":
                current_integer, processed_index = calculator_helper(input_string[index + 1:])
                index += processed_index
            elif character == ")":
                process_operation(current_integer, operation, result)
                return sum(result), index
            elif not current_integer:
                current_integer = int(character)
            else:
                current_integer = (current_integer * 10) + int(character)
            index += 1

        process_operation(current_integer, operation, result)
        return sum(result), index

    return calculator_helper(input_string)[0]


input = "1 + 1 - 5"
print(calculate_one(input))
input = "1 / 2 - 5"
print(calculate_one(input))
input = "(1 - (2 * 5))"
print(calculate_one(input))

"""
Given a list of words and a searchWord, for each prefix of searchWord find the first three lexicographically matching
 words with the prefix.
"""

words = ["s", "sea", "sear", "pasta", "frenchfries", "seeeee"]
searchWord = "searchWord"
from collections import defaultdict


class SearchWordTrieNode:
    def __init__(self):
        self.children = defaultdict(SearchWordTrieNode)
        self.word = None


class SearchWordTrie:
    def __init__(self, words):
        self.head = SearchWordTrieNode()
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        def add_word_helper(node, word_remaining):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    node.children[word_remaining[0]] = SearchWordTrieNode()
                add_word_helper(node.children[word_remaining[0]], word_remaining[1:])

        add_word_helper(self.head, word)

    def find_matches(self, target_word):
        def find_matches_helper(node, target_word_remaining):
            result = []
            if node.word is not None:
                result.append(node.word)
            if target_word_remaining and target_word_remaining[0] in node.children:
                result.extend(find_matches_helper(node.children[target_word_remaining[0]], target_word_remaining[1:]))
            return result

        return find_matches_helper(self.head, target_word)


search_word_trie = SearchWordTrie(words)
print(search_word_trie.find_matches(searchWord))

"""
Given a list of connections (edges), if you remove one edge at a time would it create a disjoint graph.
"""
from collections import deque


def find_weakly_connected_components(edges: List[List[int]]) -> List[bool]:
    graph, nodes = defaultdict(set), set()

    def build_graph():
        for origin, destination in edges:
            graph[origin].add(destination)
            graph[destination].add(origin)
            nodes.add(origin)
            nodes.add(destination)

    build_graph()
    number_of_nodes = len(nodes)

    def validate_removed_edge(node_a: int) -> bool:
        visited, queue = set(), deque([node_a])
        while queue:
            node = queue.popleft()
            visited.add(node)
            for adjacent in graph[node]:
                if adjacent not in visited:
                    queue.append(adjacent)
        return len(visited) != number_of_nodes

    result = []
    for origin, destination in edges:
        graph[origin].remove(destination)
        graph[destination].remove(origin)
        result.append(validate_removed_edge(origin))
        graph[origin].add(destination)
        graph[destination].add(origin)
    return result


edges = [[0, 1], [1, 2], [2, 3], [3, 0], [3, 1], [4, 2]]
print(find_weakly_connected_components(edges))
