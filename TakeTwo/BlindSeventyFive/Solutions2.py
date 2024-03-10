from typing import List


def two_sum(nums, target) -> List[int]:
    num_dict = {}
    for i, num in enumerate(nums):
        if target - num in num_dict:
            return [num_dict[target - num], i]
        num_dict[num] = i
    return []


def max_profit(prices: List[int]) -> int:
    maximum_profit, min_so_far = 0, prices[0]
    for i, price in enumerate(prices):
        maximum_profit, min_so_far = max(maximum_profit, price - min_so_far), min(min_so_far, price)
    return maximum_profit


def contains_duplicates(nums: List[int]) -> bool:
    num_set = set(nums)
    return len(num_set) != len(nums)


def product_except_self(nums: List[int]) -> List[int]:
    result = [1 for _ in nums]
    result_forward = [num for num in nums]
    result_backwards = [num for num in nums]
    for i in range(1, len(nums)):
        result_forward[i] *= result_backwards[i - 1]
    for i in range(len(nums) - 2, -1, -1):
        result_backwards[i] *= result_backwards[i + 1]

    for i in range(len(nums)):
        if i == 0:
            result[i] = result_backwards[i + 1]
        elif i == len(nums) - 1:
            result[i] = result_forward[i - 1]
        else:
            result[i] = result_backwards[i + 1] * result_forward[i - 1]

    return result


def max_sub_array(nums: List[int]) -> int:
    if not nums:
        return 0
    max_num = nums[0]
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i - 1] + nums[i])
        max_num = max(max_num, nums[i])
    return max_num


def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    def two_sum(target, numbers):
        num_set = set()
        result = []
        for i, num in enumerate(numbers):
            if not result or num != result[-1][-1]:
                if target - num in num_set:
                    result.append([-target, num, num - target])
            num_set.add(num)
        return result

    for i, num in enumerate(nums):
        if not i or nums[i - 1] != num:
            result.extend(two_sum(-num, nums[i + 1:]))
    return result


def maxArea(height: List[int]) -> int:
    left_pointer, right_pointer = 0, len(height) - 1
    max_area = 0
    while left_pointer < right_pointer:
        left_height, right_height = height[left_pointer], height[right_pointer]
        max_area = max(max_area, min(left_height, right_height) * abs(left_pointer - right_pointer))
        if left_height < right_height:
            left_pointer += 1
        else:
            right_pointer -= 1
    return max_area


def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    letter_set = set()
    pointer_head = 0
    for i, character in enumerate(s):
        while character in letter_set:
            letter_set.remove(s[pointer_head])
            pointer_head += 1
        max_len = max(max_len, i - pointer_head + 1)
        letter_set.add(character)
    return max_len


from collections import defaultdict


def characterReplacement(s: str, k: int) -> int:
    max_count, pointer_a, pointer_b, result, in_window = 0, 0, 0, 0, defaultdict(int)
    while pointer_b < len(s):
        in_window[s[pointer_b]] += 1
        max_count = max(max_count, in_window[s[pointer_b]])
        if (pointer_b - pointer_a + 1) - max_count > k:
            in_window[s[pointer_a]] -= 1
            pointer_a += 1
        result = max(result, pointer_b - pointer_a + 1)
        pointer_b += 1
    return result


def minWindow(s: str, t: str) -> str:
    pointer_a = 0
    result = ""
    formed = 0
    t_dictionary, s_dictionary = defaultdict(int), defaultdict(int)
    for character in t:
        t_dictionary[character] += 1

    required_to_form = len(t_dictionary)

    for pointer_b in range(len(s)):
        character = s[pointer_b]
        s_dictionary[character] += 1
        if character in t_dictionary and s_dictionary[character] == t_dictionary[character]:
            formed += 1
        while pointer_a <= pointer_b and formed == required_to_form:
            if not result or len(result) > pointer_b - pointer_a + 1:
                result = s[pointer_a:pointer_b + 1]
            s_dictionary[s[pointer_a]] -= 1
            if s[pointer_a] in t_dictionary and s_dictionary[s[pointer_a]] < t_dictionary[s[pointer_a]]:
                formed -= 1
            pointer_a += 1
    return result


def isAnagram(s: str, t: str) -> bool:
    s_dict = defaultdict(int)
    t_dict = defaultdict(int)

    for character in s:
        s_dict[character] += 1
    for character in t:
        t_dict[character] += 1

    if len(s_dict) == len(t_dict):
        for character, value in s_dict.items():
            if character not in t_dict or value != t_dict[character]:
                return False
        return True
    return False


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hash_map = defaultdict(list)
    for word in strs:
        word_hash = 0
        for character in word:
            word_hash += hash(character)
        hash_map[word_hash].append(word)
    return list(hash_map.values())


def setZeroes(matrix: List[List[int]]) -> None:
    x_zero_set = set()
    y_zero_set = set()
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if value == 0:
                x_zero_set.add(x)
                y_zero_set.add(y)

    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if x in x_zero_set or y in y_zero_set:
                matrix[x][y] = 0


def exist(board: List[List[str]], word: str) -> bool:
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def traverse(x, y, word_remaining):
        if not word_remaining:
            return True

        temp, board[x][y] = board[x][y], None
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(board) and 0 <= y_target < len(board[0]) and board[x_target][y_target] == \
                    word_remaining[0]:
                if traverse(x_target, y_target, word_remaining[1:]):
                    return True

        board[x][y] = False
        return False

    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == word[0] and traverse(x, y, word[1:]):
                return True
    return False


def climbStairs(n: int) -> int:
    result = [1 for _ in range(n)]
    for i in range(1, n):
        if i == 1:
            result[i] += 1
        else:
            result[i] = result[i - 1] + result[i - 2]
    return result[-1]


def coin_change(coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0
    result = [-1 for _ in range(amount + 1)]
    coins.sort()
    for coin in coins:
        for i in range(coin, len(result)):
            if i % coin == 0:
                result[i] = i / coin
            elif result[i % coin] != -1:
                result[i] = (i // coin) + result[i % coin]
    return int(result[-1])


def lengthOfLIS(nums: List[int]) -> int:
    result = [1 for _ in range(len(nums))]
    for i in range(len(nums)):
        i_num = nums[i]
        for j in range(i):
            j_num = nums[j]
            if i_num > j_num:
                result[i] = max(result[i], result[j] + 1)
    return max(result)


def longestCommonSubsequence(text1: str, text2: str) -> int:
    result = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            i_character = text1[i - 1]
            j_caracter = text2[j - 1]
            if i_character == j_caracter:
                result[i][j] = result[i - 1][j - 1] + 1
            else:
                result[i][j] = max(result[i - 1][j], result[i][j - 1])
    return result[-1][-1]


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    candidates.sort()

    def traverse(candidates_remaining, target_remaining, temp_result):
        if not target_remaining:
            result.append(temp_result)
        for i, candidate in enumerate(candidates_remaining):
            if target_remaining - candidate >= 0:
                traverse(candidates_remaining[i:], target_remaining - candidate, temp_result + [candidate])
            else:
                break

    traverse(candidates, target, [])
    return result


from typing import Optional
from binarytree import Node


def maxDepth(root: Optional[Node]) -> int:
    return max(maxDepth(root.left), maxDepth(root.right)) + 1 if root else 0


def isSameTree(p: Optional[Node], q: Optional[Node]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.value == q.value and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def invertTree(root: Optional[Node]) -> Optional[Node]:
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


def maxPathSum(root: Optional[Node]) -> int:
    result = 0

    def traverse(node):
        if node:
            left, right = 0, 0
            if node.left:
                left = traverse(node.left)
            if node.right:
                right = traverse(node.right)
            nonlocal result
            result = max(result, left + right + node.value)
            return max(left, right) + node.value

    traverse(root)
    return result


from collections import deque


def levelOrder(root: Optional[Node]) -> List[List[int]]:
    result = []
    queue = deque([(0, root)])
    while queue:
        level, node = queue.popleft()
        if level == len(result):
            result.append([node.value])
        else:
            result[level].append(node.value)
        if node.left:
            queue.append((level + 1, node.left))
        if node.right:
            queue.append((level + 1, node.right))
    return result


import json


class TreeCodec:

    def serialize(self, root):
        inorder = []

        def traverse(node):
            if node:
                inorder.append(node.value)
                traverse(node.left)
                traverse(node.right)
            else:
                inorder.append(None)

        result = {"inorder": inorder}
        traverse(root)
        return json.dumps(result)

    def deserialize(self, data):
        input = json.loads(data)
        queue = deque(input["inorder"])

        def traverse():
            if queue[0] is None:
                queue.popleft()
                return None
            return Node(queue.popleft(), traverse(), traverse())

        return traverse()


def isSubtree(root: Optional[Node], subRoot: Optional[Node]) -> bool:
    def check_subtree(node, sub_node):
        if not node and not sub_node:
            return True
        if not node or not sub_node:
            return False
        return node.value == sub_node.value and check_subtree(node.left, sub_node.left) and check_subtree(node.right,
                                                                                                          sub_node.right)

    if root:
        if root.value == subRoot.value and check_subtree(root, subRoot):
            return True
        return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
    return False


from typing import Union


def isValidBST(root: Optional[Node]) -> bool:
    def traverse(node: Optional[Node], min: Union[int, float], max: Union[int, float]) -> bool:
        if node:
            if node.value <= min or node.value >= max:
                return False
            return traverse(node.left, min, node.value) and traverse(node.right, node.value, max)
        return True

    return traverse(root, float('-inf'), float('inf'))


def lowestCommonAncestor(root: 'Node', p: 'Node', q: 'Node') -> 'Node':
    def traverse(node: Node) -> Optional[Node]:
        if node:
            if node.value == p.value or node.value == q.value:
                return node
            left_node, right_node = traverse(node.left), traverse(node.right)
            if left_node and right_node:
                return node
            if left_node:
                return left_node
            return right_node

        return None

    return traverse(root)


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        def insert_helper(node, word_remaining):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    node.children[word_remaining[0]] = TrieNode()
                insert_helper(node.children[word_remaining[0]], word_remaining[1:])

        insert_helper(self.root, word)

    def search(self, word: str) -> bool:
        def search_helper(node, word_remaining):
            if not word_remaining:
                return node.word == word
            if word_remaining[0] not in node.children:
                return False
            return search_helper(node.children[word_remaining[0]], word_remaining[1:])

        return search_helper(self.root, word)

    def startsWith(self, prefix: str) -> bool:
        def traverse_to(node, prefix_remaining):
            if not prefix_remaining:
                return True
            if prefix_remaining[0] not in node.children:
                return False
            return traverse_to(node.children[prefix_remaining[0]], prefix_remaining[1:])

        return traverse_to(self.root, prefix)


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        def add_word_helper(node, word_remaining):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    node.children[word_remaining[0]] = TrieNode()
                add_word_helper(node.children[word_remaining[0]], word_remaining[1:])

        add_word_helper(self.root, word)

    def search(self, word: str) -> bool:
        def search_helper(node, word_remaining):
            if not word_remaining:
                return node.word is not None
            character = word_remaining[0]
            if character == ".":
                return any(search_helper(child, word_remaining[1:]) for child in node.children.values())
            elif word_remaining[0] in node.children:
                return search_helper(node.children[word_remaining[0]], word_remaining[1:])
            return False

        return search_helper(self.root, word)


class FindWordsTrie:
    def __init__(self):
        self.root = TrieNode()
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def insert(self, word):
        def insert_helper(node, word_remaining):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    node.children[word_remaining[0]] = TrieNode()
                insert_helper(node.children[word_remaining[0]], word_remaining[1:])

        insert_helper(self.root, word)

    def traverse(self, board):
        result = []

        def traverse_helper(x, y, node):
            if node.word is not None:
                result.append(node.word)
                node.word = None

            temp, board[x][y] = board[x][y], None
            for x_direction, y_direction in self.directions:
                x_target, y_target = x + x_direction, y + y_direction
                if 0 <= x_target < len(board) and 0 <= y_target < len(board[0]) and board[x_target][
                    y_target] in node.children:
                    traverse_helper(x_target, y_target, node.children[board[x_target][y_target]])

            board[x][y] = temp

        for x, row in enumerate(board):
            for y, value in enumerate(row):
                if value in self.root.children:
                    traverse_helper(x, y, self.root.children[board[x][y]])
        return result


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    trie = FindWordsTrie()
    for word in words:
        trie.insert(word)
    return trie.traverse(board)


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    def build_graph():
        for destination, origin in prerequisites:
            graph[origin].append(destination)
            if origin not in in_degree:
                in_degree[origin] = 0
            in_degree[destination] += 1

    build_graph()

    queue = deque([])
    visited = set()
    for key, value in in_degree.items():
        if value == 0:
            queue.append(key)
    while queue:
        node = queue.popleft()
        visited.add(node)
        for adjacent in graph[node]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                queue.append(adjacent)
    return len(visited) == numCourses
