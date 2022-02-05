import collections


class DoubleLinkedNode:
    def __init__(self, key, value):
        self.next = None
        self.previous = None
        self.key = key
        self.value = value


class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_capacity = 0
        self.head = DoubleLinkedNode(None, None)
        self.tail = DoubleLinkedNode(None, None)
        self.tail.next, self.head.previous = self.head, self.tail
        self.dictionary = collections.defaultdict(DoubleLinkedNode)

    def delete(self, key):
        if key in self.dictionary:
            self.current_capacity -= 1
            node = self.dictionary[key]
            self.remove(node)

    def set(self, key, value):
        if key in self.dictionary:
            node = self.dictionary[key]
            self.remove(node)
            node.value = value
            self.add_to_head(node)
        else:
            if self.current_capacity == self.capacity:
                del self.dictionary[self.remove_from_tail().key]
            node = DoubleLinkedNode(key, value)
            self.dictionary[key] = node
            self.add_to_head(node)

    def remove_from_tail(self):
        node = self.tail.next
        self.tail.next = self.tail.next.next
        self.tail.next.next.prev = self.tail
        return node

    def add_to_head(self, node):
        self.head.previous, self.head.previous.next, node.previous, node.next = node, node, self.head.previous, self.head

    def remove(self, node):
        node.previous.next, node.next.previous = node.next, node.previous

    def get(self, key):
        if key in self.dictionary:
            node = self.dictionary[key]
            self.remove(node)
            self.add_to_head(node)
            return node.value
        return None


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
                return
            letter = word_remaining[0]
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
            recursive_add(node, word_remaining[1:])

        recursive_add(self.head, word)

    def prefix_search(self, prefix):
        def recursive_traverse(node, word):
            letter = word[0]
            if not word:
                return node
            elif letter in node.children:
                return recursive_traverse(node.children[letter], word[1:])
            return None

        def recursive_gather(node):
            result = []
            if node.word:
                result.append(node.word)
            for node in node.children.values():
                result.extend(recursive_gather(node))
            return result

        node = recursive_traverse(self.head, prefix)
        if not node:
            return []
        return recursive_gather(node)

    def delete(self, word):
        def recursive_delete(node, word_remaining):
            if not word_remaining and node.word:
                node.word = None
                return len(word.children) == 0
            letter = word_remaining[0]
            if letter in node.children:
                delete_child = recursive_delete(node.children[letter], word_remaining[1:])
                if delete_child:
                    del node.children[letter]
                return len(word.children) == 0
            return False

        recursive_delete(self.head, word)
