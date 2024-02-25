import heapq
from typing import List


def two_sum(nums, target) -> List[int]:
    visited_dictionary = {}
    for i, num in enumerate(nums):
        if target - num in visited_dictionary:
            return [visited_dictionary[target - num], i]
        visited_dictionary[num] = i
    return []


def max_profit(prices: List[int]) -> int:
    prev_min = float('-inf')
    maximum_profit = 0
    for price in prices:
        if prev_min == float('-inf'):
            prev_min = price
        else:
            maximum_profit, prev_min = max(maximum_profit, price - prev_min), min(prev_min, price)
    return maximum_profit


def contains_duplicates(nums: List[int]) -> bool:
    nums.sort()
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


def max_sub_array(nums: List[int]) -> int:
    curr_max = float('-inf')
    temp_array = [num for num in nums]
    for i, num in enumerate(nums):
        if i == 0:
            pass
        elif num + temp_array[i - 1] > num:
            temp_array[i] = temp_array[i - 1] + num
        curr_max = max(curr_max, temp_array[i])
    return curr_max


def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    def two_sum(nums, target) -> List[List[int]]:
        num_set = set()
        result = []
        for i, num in enumerate(nums):
            if not result or num != result[-1][-1]:
                if target - num in num_set:
                    result.append([num, num - target])
            num_set.add(num)
        return result

    for i, num in enumerate(nums):
        if not i or nums[i - 1] != num:
            temp_result = two_sum(nums[i + 1:], -num)
            for temp in temp_result:
                result.append([num] + temp)
    return result


from collections import defaultdict


def lengthOfLongestSubstring(s: str) -> int:
    letter_dict = defaultdict(int)
    pointer_a, pointer_b = 0, 0
    length_of_longest = 0
    while pointer_b < len(s):
        while s[pointer_b] in letter_dict:
            del letter_dict[s[pointer_a]]
            pointer_a += 1
        letter_dict[s[pointer_b]] += 1
        pointer_b += 1
        length_of_longest = max(length_of_longest, pointer_b - pointer_a)
    return length_of_longest


def isAnagram(s: str, t: str) -> bool:
    s_counter = defaultdict(int)
    t_counter = defaultdict(int)
    for character in s:
        s_counter[character] += 1
    for character in t:
        t_counter[character] += 1
    if len(s_counter.keys()) != len(t_counter.keys()):
        return False
    for key in s_counter.keys():
        if key not in t_counter:
            return False
        if s_counter[key] != t_counter[key]:
            return False
    return True


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = defaultdict(list)
    for word in strs:
        hash_char = 0
        for character in word:
            hash_char += hash(character)
        result[hash_char].append(word)
    return list(result.values())


def isPalindrome(s: str) -> bool:
    pointer_start, pointer_end = 0, len(s) - 1
    while pointer_start <= pointer_end:
        if not s[pointer_start].isalpha():
            pointer_start += 1
        elif not s[pointer_end].isalpha():
            pointer_end -= 1
        elif s[pointer_start].lower() != s[pointer_end].lower():
            return False
        else:
            pointer_start += 1
            pointer_end -= 1
    return True


def isValid(s: str) -> bool:
    open_square, open_curly, open_paren = 0, 0, 0
    for character in s:
        if character == "(":
            open_paren += 1
        if character == ")":
            if not open_paren:
                return False
            open_paren -= 1
        if character == "[":
            open_square += 1
        if character == "]":
            if not open_square:
                return False
            open_square -= 1
        if character == "{":
            open_curly += 1
        if character == "}":
            if not open_curly:
                return False
            open_curly -= 1
    return not open_curly and not open_square and not open_paren


def setZeroes(matrix: List[List[int]]) -> None:
    row_zeros = set()
    column_zeros = set()
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if value == 0:
                row_zeros.add(x)
                column_zeros.add(y)

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if x in row_zeros or y in column_zeros:
                matrix[x][y] = 0


def exist(board: List[List[str]], word: str) -> bool:
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def traverse(x, y, word_remaining):
        board[x][y], tmp = None, board[x][y]
        if not word_remaining:
            return True
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(board) and 0 <= y_target < len(board[0]):
                if word_remaining[0] == board[x_target][y_target] and traverse(x_target, y_target, word_remaining[1:]):
                    return True
        board[x][y] = tmp
        return False

    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if word[0] == value and traverse(x, y, word[1:]):
                return True
    return False


def climbStairs(n: int) -> int:
    result = [1 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if i in [1, 2]:
            result[i] = i
        else:
            result[i] = result[i - 1] + result[i - 2]
    return result[-1]


def coin_change(coins, amount):
    result = [float('inf') for _ in range(amount + 1)]
    result[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            result[x] = min(result[x], result[x - coin] + 1)
    if result[-1] == float('inf'):
        return -1
    return result[-1]


def lengthOfLIS(nums: List[int]) -> int:
    result = [1 for _ in range(len(nums))]
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                result[i] = max(result[i], result[j] + 1)
    return max(result)


def longestCommonSubsequence(text1: str, text2: str) -> int:
    result = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
    for x in range(1, len(text1) + 1):
        for y in range(1, len(text2) + 1):
            if text1[x - 1] == text2[y - 1]:
                result[x][y] = result[x - 1][y - 1] + 1
            else:
                result[x][y] = max(result[x - 1][y], result[x][y - 1])
    return result[-1][-1]


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    result = []

    def helper_function(candidates_remaining, target_remaining, combo_so_far):
        if target_remaining == 0:
            return result.append(combo_so_far)
        else:
            for i, candidate in enumerate(candidates_remaining):
                if target_remaining - candidate >= 0:
                    helper_function(candidates_remaining[i:], target_remaining - candidate, combo_so_far + [candidate])
        return result

    return helper_function(candidates, target, [])


def rob(nums: List[int]) -> int:
    if len(nums) <= 2:
        return max(nums)
    result = [num for num in nums]
    for i, number in enumerate(nums):
        if i in [0, 1]:
            result[i] = number
        elif i == 2:
            result[i] += result[i - 2]
        else:
            result[i] += max(result[i - 2], result[i - 3])
    return max(result[-1], result[-2])


def uniquePaths(m: int, n: int) -> int:
    result = [[1 for _ in range(m)] for _ in range(n)]
    for x in range(len(result)):
        for y in range(len(result[x])):
            if x != 0 and y != 0:
                result[x][y] = result[x - 1][y] + result[x][y - 1]
    return result[-1][-1]


from typing import Optional
from binarytree import Node


def maxDepth(root: Optional[Node]) -> int:
    def traverse(node):
        if not node:
            return 0
        return max(traverse(node.left), traverse(node.right)) + 1

    return traverse(root)


from collections import deque


def levelOrder(root: Optional[Node]) -> List[List[int]]:
    ordering = []
    queue = deque([(0, root)])
    while queue:
        level, node = queue.popleft()
        if len(ordering) == level:
            ordering.append([node.value])
        else:
            ordering[level].append(node.value)
        if node.left:
            queue.append((level + 1, node.left))
        if node.right:
            queue.append((level + 1, node.right))
    return ordering


def isSubtree(root: Optional[Node], subRoot: Optional[Node]) -> bool:
    def traverse(node):
        if node:
            if node.value == subRoot.value and compare(node, subRoot):
                return True
            return traverse(node.left) or traverse(node.right)
        return False

    def compare(node1, node2):
        if (node1 and not node2) or (node2 and not node1):
            return False
        if not node1 and not node2:
            return True
        if node1.val != node2.val:
            return False
        return compare(node1.left, node2.left) and compare(node1.right, node2.right)

    return traverse(root)


def lowestCommonAncestor(root: 'Node', p: 'Node', q: 'Node') -> 'Node':
    def traverse(node, level):
        if node:
            if node.value in [p.value, q.value]:
                return node, level
            left_node, left_level = traverse(node.left, level + 1)
            right_node, right_level = traverse(node.right, level + 1)
            if left_node and right_node:
                return node, level
            return left_node or right_node, min(left_level, right_level)
        return None, float('inf')

    return traverse(root, 1)[0]


class TrieNode:
    def __init__(self):
        self.word = None
        self.children = defaultdict(TrieNode)


class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        def insert_helper(node, word_remaining):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    node.children[word_remaining[0]] = TrieNode()
                insert_helper(node.children[word_remaining[0]], word_remaining[1:])

        insert_helper(self.head, word)

    def search(self, word: str) -> bool:
        def search_helper(node, word_remaining):
            if not word_remaining:
                return node.word == word
            if word_remaining[0] in node.children:
                return search_helper(node.children[word_remaining[0]], word_remaining[1:])
            return False

        return search_helper(self.head, word)

    def startsWith(self, prefix: str) -> bool:

        def find_any(node):
            return True if node.word else any(find_any(child) for child in node.children.values())

        def starts_with_helper(node, prefix_remaining):
            if not prefix_remaining:
                return find_any(node)
            if prefix_remaining[0] in node.children:
                return starts_with_helper(node.children[prefix_remaining[0]], prefix_remaining[1:])
            return False

        return starts_with_helper(self.head, prefix)


class WordDictionaryTrieNode:
    def __init__(self):
        self.word = None
        self.children = defaultdict(WordDictionaryTrieNode)


class WordDictionary:

    def __init__(self):
        self.head = WordDictionaryTrieNode()

    def addWord(self, word: str) -> None:
        def add_word_helper(node, word_remaining):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    node.children[word_remaining[0]] = WordDictionaryTrieNode()
                add_word_helper(node.children[word_remaining[0]], word_remaining[1:])

        add_word_helper(self.head, word)

    def search(self, word: str) -> bool:
        def search_helper(node, word_remaining):
            if not word_remaining:
                return node.word is not None
            if word_remaining[0] == ".":
                return any(search_helper(child, word_remaining[1:]) for child in node.children.values())
            elif word_remaining[0] in node.children:
                return search_helper(node.children[word_remaining[0]], word_remaining[1:])
            return False

        return search_helper(self.head, word)


class FindWordsTrieNode:
    def __init__(self):
        self.word = None
        self.children = defaultdict(FindWordsTrieNode)


class FindWordsTrie:
    def __init__(self, board: List[List[str]]):
        self.board = board
        self.head = FindWordsTrieNode()
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def add_word(self, word):
        def add_word_helper(node, word_remaining):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    node.children[word_remaining[0]] = FindWordsTrieNode()
                add_word_helper(node.children[word_remaining[0]], word_remaining[1:])

        add_word_helper(self.head, word)

    def traverse(self, x, y) -> List[str]:
        def traverse_helper(node, x, y) -> List[str]:
            result = []
            temp = self.board[x][y]
            if node.word is not None:
                result.append(node.word)
                node.word = None
            for x_direction, y_direction in self.directions:
                x_target, y_target = x + x_direction, y + y_direction
                if 0 <= x_target < len(self.board) and 0 <= y_target < len(self.board[0]):
                    value = self.board[x_target][y_target]
                    if value in node.children:
                        result.extend(traverse_helper(node.children[value], x_target, y_target))
            self.board[x][y] = temp
            return result

        value = self.board[x][y]
        return traverse_helper(self.head.children[value], x, y)


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    find_words_trie = FindWordsTrie(board)
    for word in words:
        find_words_trie.add_word(word)

    result = []

    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value in find_words_trie.head.children:
                detected_words = find_words_trie.traverse(x, y)
                result.extend(detected_words)

    return result


class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    def traverse(node, previous):
        node.next, tmp = previous, node.next
        if tmp is None:
            return node
        return traverse(tmp, node)

    return traverse(head, None)


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    def merge(node1, node2):
        if not node1 or not node2:
            return node1 or node2
        if node1.value < node2.value:
            node1.next = merge(node1.next, node2)
            return node1
        else:
            node2.next = merge(node2.next, node1)
            return node2

    return merge(list1, list2)


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    queue = []
    if not lists:
        return None

    for node in lists:
        heapq.heappush(queue, (node.value, node))
    node_pointer = ListNode()
    tmp_head = node_pointer

    while queue:
        _, node = heapq.heappop(queue)
        node_pointer.next, node_pointer = node, node
        if node.next:
            heapq.heappush(queue, (node.next.value, node.next))

    return tmp_head.next


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    def build_graph_and_degree():
        in_degree = {i: 0 for i in range(numCourses)}
        graph = defaultdict(list)
        for after, before in prerequisites:
            in_degree[after] += 1
            graph[before].append(after)
        return graph, in_degree

    graph, in_degree = build_graph_and_degree()
    queue = deque([])
    visited = set()
    for node, degree in in_degree.items():
        if degree == 0:
            queue.append(node)

    while queue:
        node = queue.popleft()
        visited.add(node)
        for adjacent in graph[node]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                queue.append(adjacent)

    return len(visited) == numCourses


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    result = []
    for interval in intervals:
        if result and interval[0] <= result[-1][1]:
            result[-1][1] = max(interval[1], result[-1][1])
        else:
            result.append(interval)
    return result


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[1][0] <= intervals[i - 1][1]:
            return False
    return True


def minMeetingRooms(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[0])
    meeting_rooms = []
    for interval in intervals:
        for meeting_room in meeting_rooms:
            if interval[0] >= meeting_room[-1][1]:
                meeting_room.append(interval)
                break
        else:
            meeting_rooms.append([interval])
    return len(meeting_rooms)
