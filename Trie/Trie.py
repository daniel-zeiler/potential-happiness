import collections


class TrieNode:
    def __init__(self, word=None):
        self.word = word
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def print(self):

        def helper(root):
            word_list = []
            if root:
                if root.word:
                    word_list.append(root.word)
                for child in root.children.values():
                    word_list.extend(helper(child))
            return word_list

        return helper(self.head)

    def search(self, word):
        pass

    def prefix_search(self, prefix):
        pass

    def insert(self, original_word):

        def insert_to_root(root, word):
            if not word:
                root.word = original_word
            else:
                character = word[0]
                if character not in root.children:
                    node = TrieNode()
                    root.children[character] = node
                insert_to_root(root.children[character], word[1:])

        insert_to_root(self.head, original_word)

    def delete(self, word):
        pass
