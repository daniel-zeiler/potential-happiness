import collections
import heapq
import json
from typing import List, Optional

from binarytree import Node


def twoSum(nums, target):
    compliment_set = collections.defaultdict(int)
    for i, number in enumerate(nums):
        compliment = target - number
        if compliment in compliment_set:
            return [compliment_set[compliment], i]
        compliment_set[number] = i
    return []


def maxProfit(prices: List[int]) -> int:
    min_so_far = prices[0]
    max_profit = 0
    for i, price in enumerate(prices):
        max_profit = max(max_profit, price - min_so_far)
        min_so_far = min(min_so_far, price)
    return max_profit


def containsDuplicate(nums: List[int]) -> bool:
    value_set = set()
    for num in nums:
        if num in value_set:
            return True
        value_set.add(num)
    return False


def productExceptSelf(nums: List[int]) -> List[int]:
    prefix = [0 for _ in range(len(nums))]
    postfix = [0 for _ in range(len(nums))]
    for i, num in enumerate(nums):
        if i == 0:
            prefix[i] = num
        else:
            prefix[i] = prefix[i - 1] * num

    for j in range(len(nums) - 1, -1, -1):
        num = nums[j]
        if j == len(nums) - 1:
            postfix[j] = num
        else:
            postfix[j] = postfix[j + 1] * num

    result = [0 for _ in range(len(nums))]
    for i in range(len(result)):
        if i == 0:
            result[i] = 1 * postfix[i + 1]
        elif i == len(result) - 1:
            result[i] = 1 * prefix[i - 1]
        else:
            result[i] = prefix[i - 1] * postfix[i + 1]

    return result


def maxSubArray(nums: List[int]) -> int:
    if not nums:
        return 0
    max_at_position = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]
        max_at_position = max(num, num + max_at_position)
        result = max(result, max_at_position)
    return result


def maxProduct(nums: List[int]) -> int:
    if not nums:
        return 0
    max_product_at_position = nums[0]
    min_product_at_position = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        max_product_at_position, min_product_at_position = max(num, num * max_product_at_position,
                                                               num * min_product_at_position), min(num,
                                                                                                   num * max_product_at_position,
                                                                                                   num * min_product_at_position)
        result = max(result, max_product_at_position)
    return result


def findMin(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    result = float('inf')
    while left <= right:
        if nums[left] < nums[right]:
            result = min(result, nums[left])
            break
        middle_index = (left + right) // 2
        result = min(result, nums[middle_index])
        if nums[middle_index] >= nums[left]:
            left = middle_index + 1
        else:
            right = middle_index - 1
    return result


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle_index = (left + right) // 2
        middle_value = nums[middle_index]
        if middle_value == target:
            return middle_index

        if nums[left] < nums[right]:
            if middle_value < target:
                left = middle_index + 1
            else:
                right = middle_index - 1
        elif middle_value >= nums[left]:
            left = middle_index + 1
        else:
            right = middle_index - 1

    return -1


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []

    def two_sum(numbers, target):
        compliment_set = set()
        i = 0

        while i < len(numbers):
            number = numbers[i]
            compliment = target - number
            if compliment in compliment_set:
                result.append([-target, compliment, number])
                while i != len(numbers) - 1 and number == numbers[i + 1]:
                    i += 1
            compliment_set.add(number)
            i += 1

    for i, num in enumerate(nums):
        if i == 0 or num != nums[i - 1]:
            two_sum(nums[i + 1:], -num)

    return result


def maxArea(height: List[int]) -> int:
    max_area = float('-inf')
    pointer_start = 0
    pointer_end = len(height) - 1

    while pointer_end > pointer_start:
        max_area = max(min(height[pointer_start], height[pointer_end]) * (pointer_end - pointer_start), max_area)
        if height[pointer_start] < height[pointer_end]:
            pointer_start += 1
        else:
            pointer_end -= 1
    return max_area


def lengthOfLongestSubstring(s: str) -> int:
    pointer_start = 0
    character_set = set()
    result = 0
    for pointer_end, character in enumerate(s):
        while character in character_set:
            character_set.remove(s[pointer_start])
            pointer_start += 1
        character_set.add(character)
        result = max(pointer_end - pointer_start + 1, result)
    return result


def characterReplacement(s: str, k: int) -> int:
    character_set = set(s)
    result = 0
    for character in character_set:
        pointer_start = 0
        flipped_chars = 0
        for pointer_end, read_character in enumerate(s):
            while flipped_chars == k and read_character != character:
                if s[pointer_start] != character:
                    flipped_chars -= 1
                pointer_start += 1

            if read_character != character:
                flipped_chars += 1
            result = max(result, pointer_end - pointer_start + 1)
    return result


def minWindow(s: str, t: str) -> str:
    start_pointer = 0
    valid = False
    t_character_set = collections.defaultdict(int)
    s_character_set = collections.defaultdict(int)
    result = ''
    min_window = float('inf')
    for character in t:
        t_character_set[character] += 1

    def check_valid():
        if len(t_character_set) == len(s_character_set):
            for key, value in s_character_set.items():
                if value < t_character_set[key]:
                    return False
            return True
        else:
            return False

    for end_pointer, character in enumerate(s):
        if character in t_character_set:
            s_character_set[character] += 1
        if check_valid():
            valid = True
        while valid:
            if end_pointer - start_pointer + 1 < min_window:
                result = s[start_pointer:end_pointer + 1]
                min_window = len(result)
            if s[start_pointer] in s_character_set:
                s_character_set[s[start_pointer]] -= 1
                if s_character_set[s[start_pointer]] == 0:
                    del s_character_set[s[start_pointer]]
                    valid = False
            start_pointer += 1

    return result


def isAnagram(s: str, t: str) -> bool:
    s_count_dict = collections.defaultdict(int)

    for character in s:
        s_count_dict[character] += 1

    for character in t:
        if character not in s_count_dict:
            return False
        s_count_dict[character] -= 1
        if s_count_dict[character] == 0:
            del s_count_dict[character]

    return not s_count_dict


def group_anagrams(strs):
    result = collections.defaultdict(list)

    for word in strs:
        temp = [0 for _ in range(26)]
        for letter in word:
            temp[ord(letter) - ord('a')] += 1
        result[tuple(temp)].append(word)

    return result.values()


def isPalindrome(s: str) -> bool:
    pointer_start = 0
    pointer_end = len(s) - 1

    while pointer_start < pointer_end:
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
    square = 0
    paren = 0
    curly = 0
    for character in s:
        if character == '}':
            if not curly:
                return False
            curly -= 1
        elif character == '{':
            curly += 1
        elif character == ']':
            if not square:
                return False
            square -= 1
        elif character == '[':
            square += 1
        elif character == ')':
            if not paren:
                return False
            paren -= 1
        elif character == '(':
            paren += 1
        else:
            return False

    return not square and not paren and not curly


def setZeroes(matrix: List[List[int]]) -> None:
    zeros_x = set()
    zeros_y = set()
    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if value == 0:
                zeros_x.add(x)
                zeros_y.add(y)

    for x, row in enumerate(matrix):
        for y, value in enumerate(row):
            if x in zeros_x or y in zeros_y:
                matrix[x][y] = 0


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction_pointer = 0
    result = []
    position = [0, 0]

    def get_next_position(x, y):
        nonlocal direction_pointer
        for i in range(len(directions)):
            x_direction, y_direction = directions[(i + direction_pointer) % len(directions)]
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(matrix) and 0 <= y_target < len(matrix[0]) and matrix[x_target][
                y_target] is not None:
                direction_pointer = (i + direction_pointer) % len(directions)
                return [x_target, y_target]
        return []

    while position:
        x, y = position
        result.append(matrix[x][y])
        matrix[x][y] = None
        position = get_next_position(x, y)
    return result


def exist(board: List[List[str]], word: str) -> bool:
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def yield_valid_direction(x, y, letter):
        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(board) and 0 <= y_target < len(board[0]):
                if board[x_target][y_target] == letter:
                    yield x_target, y_target

    def traverse(x, y, word_remaining):
        if len(word_remaining) == 1:
            return True
        board[x][y], temp = None, board[x][y]
        for x_direction, y_direction in yield_valid_direction(x, y, word_remaining[1]):
            if traverse(x_direction, y_direction, word_remaining[1:]):
                return True
        board[x][y] = temp
        return False

    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == word[0]:
                if traverse(x, y, word):
                    return True
    return False


def climb_stairs_recursive(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)


def climb_stairs_memoization(n):
    memo = {}

    def climb_stairs_recursive(n):
        if n == 1:
            memo[n] = 1
        elif n == 2:
            memo[n] = 2
        else:
            memo[n] = climb_stairs_memoization(n - 1) + climb_stairs_recursive(n - 2)
        return memo[n]

    return climb_stairs_recursive(n)


def climb_stairs_bottom_up(n):
    result = [0 for _ in range(0, n + 1)]
    for i in range(1, n + 1):
        if i == 1:
            result[i] = 1
        elif i == 2:
            result[i] = 2
        else:
            result[i] = result[i - 1] + result[i - 2]
    return result[-1]


"""
Base case of recursion is no amount remaining.
Return the number of coins as solution.
Else return min of iterative approach.
"""


def coin_change(coins: List[int], amount: int) -> int:
    def coin_change_recursive(coins, num_coins, amount_remaining):
        solution = float('inf')
        if amount_remaining == 0:
            return num_coins
        for coin in coins:
            if amount_remaining - coin >= 0:
                solution = min(coin_change_recursive(coins, num_coins + 1, amount_remaining - coin), solution)
        return solution

    result = coin_change_recursive(coins, 0, amount)
    if result == float('inf'):
        return -1
    return result


def coin_change_memoization(coins, amount):
    memo = {}

    def coin_change_recursive(number_of_coins, amount_remaining):
        if amount_remaining not in memo or memo[amount_remaining] > number_of_coins:
            memo[amount_remaining] = number_of_coins
            for coin in coins:
                if amount_remaining - coin >= 0:
                    coin_change_recursive(number_of_coins + 1, amount_remaining - coin)

    coin_change_recursive(0, amount)
    if 0 not in memo:
        return -1
    return memo[0]


def coin_change_iterative(coins, amount):
    result = [float('inf') for _ in range(amount + 1)]
    result[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            result[x] = min(result[x], result[x - coin] + 1)
    if amount == 0:
        return amount
    if result[-1] == float('inf'):
        return -1
    return int(result[-1])


def maxDepth(root: Optional[Node]) -> int:
    def traverse(node):
        if not node:
            return 0
        return max(traverse(node.left), traverse(node.right)) + 1

    return traverse(root)


def same_tree(p, q):
    if not p and not q:
        return True
    if (p and not q) or (q and not p) or p.val != q.val:
        return False
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)


def invertTree(root: Optional[Node]) -> Optional[Node]:
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


def maxPathSum(root: Optional[Node]) -> int:
    result = 0

    def traverse(node):
        if node:
            nonlocal result
            left = traverse(node.left)
            right = traverse(node.right)
            result = max(result, left + right + node.val, node.val, left + node.val, right + node.val)
            return max(left + node.val, right + node.val, node.val)
        return 0

    traverse(root)
    return result


def levelOrder(root):
    result = []
    queue = collections.deque([[0, root]])
    if not root:
        return result
    while queue:
        level, node = queue.popleft()
        if level == len(result):
            result.append([node.val])
        else:
            result[level].append(node.val)
        if node.left:
            queue.append([level + 1, node.left])
        if node.right:
            queue.append([level + 1, node.right])
    return result


class TreeCodec:

    def serialize(self, root):
        def traverse(node):
            result = []
            if node:
                result.append(node.val)
                result.extend(traverse(node.left))
                result.extend(traverse(node.right))
                return result
            return [None]

        return json.dumps({'traversal': traverse(root)})

    def deserialize(self, data):
        traversal = collections.deque(json.loads(data)['traversal'])

        def rebuild():
            if traversal[0] is None:
                return traversal.popleft()
            node = Node(traversal.popleft())
            node.left = rebuild()
            node.right = rebuild()
            return node

        return rebuild()


def isSubtree(root: Optional[Node], subRoot: Optional[Node]) -> bool:
    def is_same(node_a, node_b):
        if (node_b and not node_a) or (node_a and not node_b):
            return False
        if node_b and node_a:
            return node_a.val == node_b.val and is_same(node_a.left, node_b.left) and is_same(node_a.right,
                                                                                              node_b.right)
        return True

    def traverse(node):
        if node:
            if node.val == subRoot.val:
                if is_same(node, subRoot):
                    return True
            return traverse(node.left) or traverse(node.right)
        return False

    return traverse(root)


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[Node]:
    index_mapping = {value: i for i, value in enumerate(inorder)}

    preorder = collections.deque(preorder)

    def traverse(left, right):
        if left <= right:
            node = Node(preorder.popleft())
            node.left = traverse(left, index_mapping[node.val] - 1)
            node.right = traverse(index_mapping[node.val] + 1, right)
            return node

    return traverse(0, len(preorder) - 1)


def isValidBST(root: Optional[Node]) -> bool:
    def traverse(node, low, high):
        if node:
            if node.val <= low or node.val >= high:
                return False
            return traverse(node.left, low, node.val) and traverse(node.right, node.val, high)
        return True

    return traverse(root, float('-inf'), float('inf'))


def kthSmallest(root: Optional[Node], k: int) -> int:
    counter = 0

    def traverse(node):
        nonlocal counter
        if node:
            left = traverse(node.left)
            if left is not None:
                return left
            counter += 1
            if counter == k:
                return node.val
            right = traverse(node.right)
            if right is not None:
                return right
        return None

    return traverse(root)


def lowestCommonAncestor(root: Node, p: Node, q: Node) -> Node:
    def traverse(node):
        if node:
            if node == p or node == q:
                return node
            left = traverse(node.left)
            right = traverse(node.right)
            if left and right:
                return node
            return left or right

    return traverse(root)


class TrieNode:
    def __init__(self):
        self.word = None
        self.children = collections.defaultdict(TrieNode)


class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        def recursive_insert(node, word_remaining):
            if not word_remaining:
                node.word = word
            else:
                letter = word_remaining[0]
                if letter not in node.children:
                    node.children[letter] = TrieNode()
                recursive_insert(node.children[letter], word_remaining[1:])

        recursive_insert(self.head, word)

    def search(self, word: str) -> bool:
        def recursive_search(node, word_remaining):
            if not word_remaining:
                return node.word is not None
            else:
                letter = word_remaining[0]
                if letter not in node.children:
                    return False
                return recursive_search(node.children[letter], word_remaining[1:])

        return recursive_search(self.head, word)

    def startsWith(self, prefix: str) -> bool:
        def recursive_mode(node, word_remaining):
            if not word_remaining:
                return True
            letter = word_remaining[0]
            if letter not in node.children:
                return False
            return recursive_mode(node.children[letter], word_remaining[1:])

        return recursive_mode(self.head, prefix)


class WordDictionaryNode:
    def __init__(self):
        self.word = None
        self.children = collections.defaultdict(WordDictionaryNode)


class WordDictionary:

    def __init__(self):
        self.head = WordDictionaryNode()

    def addWord(self, word: str) -> None:
        def recursive_add(node, word_remaining):
            if not word_remaining:
                node.word = word
            else:
                letter = word_remaining[0]
                if letter not in node.children:
                    node.children[letter] = WordDictionaryNode()
                recursive_add(node.children[letter], word_remaining[1:])

        recursive_add(self.head, word)

    def search(self, word: str) -> bool:
        def recursive_search(node, word_remaining):
            if not word_remaining:
                return node.word is not None
            else:
                letter = word_remaining[0]
                if letter == '.':
                    return any([recursive_search(x, word_remaining[1:]) for x in node.children.values()])
                elif letter in node.children:
                    return recursive_search(node.children[letter], word_remaining[1:])
                return False

        return recursive_search(self.head, word)


class TrieNode:
    def __init__(self, word=None):
        self.word = word
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def add_word(self, word):
        def recurse_add(node, word_remaining):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    node.children[word_remaining[0]] = TrieNode()
                recurse_add(node.children[word_remaining[0]], word_remaining[1:])

        recurse_add(self.head, word)

    def traverse_position(self, board, x, y):
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def recursive_traverse(node, x, y, visited):
            result = []
            if node.word:
                result.append(node.word)
                node.word = None
            for x_direction, y_direction in directions:
                x_target, y_target = x + x_direction, y + y_direction
                if 0 <= x_target < len(board) and 0 <= y_target < len(board[0]):
                    letter = board[x_target][y_target]
                    if letter in node.children and (x_target, y_target) not in visited:
                        child_results, delete_child = recursive_traverse(node.children[letter], x_target, y_target,
                                                                         visited | {(x_target, y_target)})
                        result.extend(child_results)
                        if delete_child:
                            del node.children[letter]

            if not node.word and not node.children:
                return result, True
            return result, False

        letter = board[x][y]
        result = []

        if letter in self.head.children:
            result, delete_child = recursive_traverse(self.head.children[letter], x, y, {(x, y)})
            if delete_child:
                del self.head.children[letter]
        return result


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    trie = Trie()
    for word in words:
        trie.add_word(word)

    result = []
    for x, row in enumerate(board):
        for y, value in enumerate(row):
            result.extend(trie.traverse_position(board, x, y))

    return result


class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None


def print_list(head: ListNode):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    print(result)


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = None

    while head:
        head.next, head, dummy_head = dummy_head, head.next, head
    return dummy_head


def hasCycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False
    slow, head = head, head.next
    while head and head.next:
        if head == slow:
            return True
        slow = slow.next
        head = head.next.next
    return False


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    result = ListNode()
    dummy_head = result
    while list1 and list2:
        if list1.value < list2.value:
            result.next, result, list1 = list1, list1, list1.next
        else:
            result.next, result, list2 = list2, list2, list2.next
    if list1:
        result.next = list1
    if list2:
        result.next = list2
    return dummy_head.next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for node_head in lists:
        heapq.heappush(heap, [node_head.value, node_head])
    dummy_head = ListNode()
    result = dummy_head
    while heap:
        value, node_head = heapq.heappop(heap)
        result.next, result, node_head = node_head, node_head, node_head.next
        if node_head:
            heapq.heappush(heap, [node_head.value, node_head])
    return dummy_head.next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy_head = ListNode()
    dummy_head.next = head
    cursor = dummy_head

    for _ in range(n):
        if not head:
            return dummy_head.next
        head = head.next

    while head:
        head = head.next
        cursor = cursor.next

    cursor.next = cursor.next.next
    return dummy_head.next


def reorderList(head: Optional[ListNode]) -> None:
    def get_mid_node_and_index(node):
        fast_pointer = node
        while fast_pointer and fast_pointer.next:
            node = node.next
            fast_pointer = fast_pointer.next.next
        return node

    dummy_head = ListNode()
    dummy_head.next = head
    stack = []
    middle_node = get_mid_node_and_index(head)
    while middle_node:
        stack.append(middle_node)
        middle_node = middle_node.next

    while stack and head.next:
        head.next, head.next.next = stack.pop(), head.next
        head = head.next.next
    head.next = None


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Node) -> Node:
    node_map = collections.defaultdict(Node)

    def recursive_build_map(node):
        node_map[node] = Node(node.val)
        for adjacent in node.neighbors:
            if adjacent not in node_map:
                recursive_build_map(adjacent)

    recursive_build_map(node)
    visited_set = {node}

    def recursive_link_nodes(node):
        new_node = node_map[node]
        new_node.neighbors = [node_map[x] for x in node.neighbors]
        for adjacent in node.neighbors:
            if adjacent not in visited_set:
                visited_set.add(adjacent)
                recursive_link_nodes(adjacent)

    recursive_link_nodes(node)

    return node_map[node]
