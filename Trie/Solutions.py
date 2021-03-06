import collections
from typing import List


class TrieNode:
    def __init__(self, word=None):
        self.word = word
        self.children = collections.defaultdict(TrieNode)


class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        def insert_char(remaining_word, node):
            if not remaining_word:
                node.word = word
                return
            if remaining_word[0] not in node.children:
                node.children[remaining_word[0]] = TrieNode()
            node = node.children[remaining_word[0]]
            insert_char(remaining_word[1:], node)

        insert_char(word, self.head)

    def search(self, word: str) -> bool:
        def search_char(remaining_word, node):
            if not remaining_word:
                return node.word is not None
            if remaining_word[0] not in node.children:
                return False
            elif search_char(remaining_word[1:], node.children[remaining_word[0]]):
                return True
            return False

        return search_char(word, self.head)

    def starts_with(self, prefix: str) -> bool:
        def starts_with_char(remaining_prefix, node):
            if not remaining_prefix:
                return True
            elif remaining_prefix[0] not in node.children:
                return False
            else:
                return starts_with_char(remaining_prefix[1:], node.children[remaining_prefix[0]])

        return starts_with_char(prefix, self.head)


class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        def add_char(word_remaining, node):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    node.children[word_remaining[0]] = TrieNode()
                node = node.children[word_remaining[0]]
                add_char(word_remaining[1:], node)

        add_char(word, self.head)

    def search(self, word: str) -> bool:
        def search_char(word_remaining, node):
            if not word_remaining:
                return node.word is not None
            if word_remaining[0] == '.':
                for key in node.children:
                    if search_char(word_remaining[1:], node.children[key]):
                        return True
                return False
            elif word_remaining[0] not in node.children:
                return False
            else:
                return search_char(word_remaining[1:], node.children[word_remaining[0]])

        return search_char(word, self.head)


class ReplaceWordTrie:
    def __init__(self):
        self.head = TrieNode()

    def add(self, word):
        def add_character(word_remaining, node):
            if not word_remaining:
                node.word = word
            else:
                if word_remaining[0] not in node.children:
                    node.children[word_remaining[0]] = TrieNode()
                node = node.children[word_remaining[0]]
                add_character(word_remaining[1:], node)

        add_character(word, self.head)

    def starts_with(self, word):
        def starts_with_character(word_remaining, node):
            if node.word:
                return node.word
            elif word_remaining[0] not in node.children:
                return None
            else:
                return starts_with_character(word_remaining[1:], node.children[word_remaining[0]])

        return starts_with_character(word, self.head)


def replaceWords(dictionary: List[str], sentence: str) -> str:
    trie = ReplaceWordTrie()
    for word in dictionary:
        trie.add(word)

    result = []
    for word in sentence.split(' '):
        replacement = trie.starts_with(word)
        if replacement:
            result.append(replacement)
        else:
            result.append(word)
    return ' '.join(result)


class MagicDictionary:

    def __init__(self):
        self.head = TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        def build_character(remaining, node):
            if not remaining:
                node.word = True
            else:
                if remaining[0] not in node.children:
                    node.children[remaining[0]] = TrieNode()
                node = node.children[remaining[0]]
                build_character(remaining[1:], node)

        for word in dictionary:
            build_character(word, self.head)

    def search(self, searchWord: str) -> bool:
        def search_remaining(forgiven_one, remaining_word, node):
            if not remaining_word:
                return node.word is not None and not forgiven_one
            if remaining_word[0] not in node.children:
                if forgiven_one:
                    for child_key in node.children:
                        if search_remaining(False, remaining_word[1:], node.children[child_key]):
                            return True
                return False
            else:
                return search_remaining(forgiven_one, remaining_word[1:], node.children[remaining_word[0]])

        return search_remaining(True, searchWord, self.head)


class MapSumTrieNode:
    def __init__(self, value=0):
        self.children = collections.defaultdict(TrieNode)
        self.value = value


class MapSum:

    def __init__(self):
        self.head = MapSumTrieNode()

    def insert(self, key: str, val: int) -> None:
        def insert_remaining(remaining_key, node):
            if not remaining_key:
                node.value = val
            else:
                if remaining_key[0] not in node.children:
                    node.children[remaining_key[0]] = MapSumTrieNode()
                node = node.children[remaining_key[0]]
                insert_remaining(remaining_key[1:], node)

        insert_remaining(key, self.head)

    def sum(self, prefix: str) -> int:
        def sum_prefix(remaining_prefix, node):
            if not remaining_prefix:
                return sum_gather(node)
            elif remaining_prefix[0] not in node.children:
                return 0
            else:
                return sum_prefix(remaining_prefix[1:], node.children[remaining_prefix[0]])

        def sum_gather(node):
            value = node.value
            for child_key in node.children:
                value += sum_gather(node.children[child_key])
            return value

        return sum_prefix(prefix, self.head)


class BoldTagTrieNode:
    def __init__(self, word=None):
        self.word = word
        self.children = collections.defaultdict(BoldTagTrieNode)


class BoldTagTrie:
    def __init__(self):
        self.head = BoldTagTrieNode()
        self.pointer = self.head

    def insert(self, word):
        def recursive_insert(node, word_remaining):
            if not word_remaining:
                node.word = word
            elif word_remaining[0] in node.children:
                recursive_insert(node.children[word_remaining[0]], word_remaining[1:])
            else:
                temp_node = BoldTagTrieNode()
                node.children[word_remaining[0]] = temp_node
                recursive_insert(node.children[word_remaining[0]], word_remaining[1:])

        recursive_insert(self.head, word)

    def slow_search(self, letter):
        if letter in self.pointer.children:
            self.pointer = self.pointer.children[letter]
            return True
        return False

    def reset_pointer(self):
        self.pointer = self.head


def addBoldTag(s: str, words: List[str]) -> str:
    trie = BoldTagTrie()
    for word in words:
        trie.insert(word)

    painting = [False for _ in range(len(s))]

    for i in range(len(s)):
        for j in range(i, len(s)):
            if not trie.slow_search(s[j]):
                trie.reset_pointer()
                break
            if trie.pointer.word:
                painting[i:j + 1] = [True] * (j - i + 1)
    open = False
    result = ''

    for i, character in enumerate(s):
        if not open and painting[i] == True:
            result += '<b>'
            open = True
        elif open and painting[i] == False:
            result += '</b>'
            open = False
        result += character

    if open:
        result += '</b>'

    return result


s = "abcxyz123"
words = ["abc", "123"]
addBoldTag(s, words)


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    class FindWordNode:
        def __init__(self):
            self.word = None
            self.children = collections.defaultdict(FindWordNode)

    class FindWordTrie:
        def __init__(self, board):
            self.board = board
            self.head = FindWordNode()
            self.directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def add_word(self, word):
            def recursive_add(node, word_remaining):
                if not word_remaining:
                    node.word = word
                    return
                letter = word_remaining[0]
                if letter not in node.children:
                    node.children[letter] = FindWordNode()
                recursive_add(node.children[letter], word_remaining[1:])

            recursive_add(self.head, word)

        def traverse_position(self, x, y, node):
            result = []
            self.board[x][y], temp = None, self.board[x][y]
            if node.word:
                result.append(node.word)
            for x_direction, y_direction in self.directions:
                x_target, y_target = x + x_direction, y + y_direction
                if 0 <= x_target < len(self.board) and 0 <= y_target < len(self.board[0]):
                    letter = self.board[x_target][y_target]
                    if letter and letter in node.children:
                        result.extend(self.traverse_position(x_target, y_target, node.children[letter]))
            self.board[x][y] = temp
            return result

        def traverse_board(self):
            result = []
            for x, row in enumerate(self.board):
                for y, value in enumerate(row):
                    if value in self.head.children:
                        result.extend(self.traverse_position(x, y, self.head.children[value]))
            return result

    trie = FindWordTrie(board)
    for word in words:
        trie.add_word(word)
    return trie.traverse_board()
