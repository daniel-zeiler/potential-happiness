import collections
from typing import List


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
                node = node.children[word_remaining[0]]
                recurse_add(node, word_remaining[1:])

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
                        child_results, delete_child = recursive_traverse(node.children[letter], x_target, y_target, visited | {(x_target, y_target)})
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
