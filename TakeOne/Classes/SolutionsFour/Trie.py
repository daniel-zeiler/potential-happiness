import collections
from typing import List


class TrieNode:
    def __init__(self, word=None):
        self.word = word
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def add_word(self, word) -> None:
        def traverse(node, characters_remaining) -> None:
            if characters_remaining:
                letter = characters_remaining[0]
                if letter not in node.children:
                    node.children[letter] = TrieNode()
                traverse(node.children[letter], characters_remaining[1:])
            else:
                node.word = word

        traverse(self.head, word)

    def search(self, word) -> bool:
        def traverse(node, characters_remaining) -> bool:
            if not characters_remaining:
                if node.word and node.word == word:
                    return True
                return False
            letter = characters_remaining[0]
            if letter not in node.children:
                return False
            return traverse(node.children[letter], characters_remaining[1:])

        return traverse(self.head, word)

    def prefix_search(self, prefix) -> List[str]:
        def traverse(node, characters_remaining) -> List[str]:
            if not characters_remaining:
                return gather(node)
            letter = characters_remaining[0]
            if letter not in node.children:
                return []
            return traverse(node.children[letter], characters_remaining[1:])

        def gather(node) -> List[str]:
            result = []
            if node.word:
                result.append(node.word)
            for child in node.children:
                result.extend(gather(node.children[child]))
            return result

        return traverse(self.head, prefix)

    def delete_word(self, word):
        def traverse(node, characters_remaining):
            if node.word and node.word == word:
                node.word = None
                if not node.children:
                    return True
                return False
            letter = characters_remaining[0]
            if letter not in node.children:
                return False
            deleted = traverse(node.children[letter], characters_remaining[1:])
            if deleted:
                del node.children[letter]
            if deleted and not node.children and not node.word:
                return True
            return False

        traverse(self.head, word)


trie = Trie()
trie.add_word("cat")
trie.add_word("catch")
trie.add_word("ant")
trie.add_word(("c"))

print(trie.search("c"))
print(trie.search("cat"))
print(trie.search("asdf"))
print(trie.prefix_search("c"))
trie.delete_word("cat")
print(trie.prefix_search("c"))

