import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = None


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def add(self, word):
        def recursive_add(node, word_remaining):
            if not word_remaining:
                node.word = word
            else:
                letter = word_remaining[0]
                if letter not in node.children:
                    node.children[letter] = TrieNode()
                recursive_add(node.children[letter], word_remaining[1:])

        recursive_add(self.head, word)

    def search(self, word):
        def recursive_search(node, word_remaining):
            if not word_remaining and node.word is not None:
                return True
            letter = word_remaining[0]
            if letter not in node.children:
                return False
            return recursive_search(node.children[letter], word_remaining[1:])

        return recursive_search(self.head, word)

    def prefix_search(self, prefix):
        def recursive_traverse(node, prefix_remaining):
            if not prefix_remaining:
                return recursive_gather(node)
            letter = prefix_remaining[0]
            if letter not in node.children:
                return []
            return recursive_traverse(node.children[letter], prefix_remaining[1:])

        def recursive_gather(node):
            result = []
            if node.word is not None:
                result.append(node.word)
            for child in node.children.values():
                result.extend(recursive_gather(child))
            return result

        return recursive_traverse(self.head, prefix)

    def remove(self, word):
        def recursive_remove(node, word_remaining):
            if not word_remaining and node.word is not None:
                node.word = None
                return not node.children
            letter = word_remaining[0]
            if letter in node.children:
                delete_child = recursive_remove(node.children[letter], word_remaining[1:])
                if delete_child:
                    del node.children[letter]
                return not node.children
            return False

        recursive_remove(self.head, word)


trie = Trie()
words = ['how', 'now', 'brown', 'cow', 'cat', 'cats', 'catheter']
for word in words:
    trie.add(word)
print(trie.prefix_search('c'))
print(trie.remove('cat'))
print(trie.prefix_search('c'))
print(trie.remove('catheter'))
print(trie.prefix_search('c'))
