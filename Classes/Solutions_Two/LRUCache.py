import collections


class LinkedListNode:
    def __init__(self, key=None, value=None):
        self.previous = None
        self.next = None
        self.key = key
        self.value = value


class LRUCache:
    def __init__(self, max_capacity=3):
        self.max_capacity = max_capacity
        self.capacity = 0
        self.head = LinkedListNode()
        self.tail = LinkedListNode()
        self.head.previous = self.tail
        self.tail.next = self.head
        self.dict = collections.defaultdict(LinkedListNode)

    def remove(self, node):
        node.previous.next, node.next.previous = node.next, node.previous

    def add_to_head(self, node):
        self.head.previous.next, self.head.previous, node.previous, node.next = node, node, self.head.previous, self.head

    def add(self, key, value):
        if key in self.dict:
            node = self.dict[key]
            node.value = value
            self.remove(node)
            self.add_to_head(node)
        else:
            if self.capacity == self.max_capacity:
                del self.dict[self.tail.next.key]
                self.remove(self.tail.next)
            else:
                self.capacity += 1
            node = LinkedListNode(key, value)
            self.dict[key] = node
            self.add_to_head(node)

    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.add_to_head(node)
            return node.value

    def __str__(self):
        node = self.head
        result = {'head': {}, 'tail': {}}
        while node:
            if node.value:
                result['head'][node.key] = node.value
            node = node.previous
        node = self.tail
        while node:
            if node.value:
                result['tail'][node.key] = node.value
            node = node.next
        return str(result)


lru_cache = LRUCache(5)
keys = ['a', 'b', 'c', 'd', 'e', 'f']
values = [1, 2, 3, 4, 5, 6]
for key, value in zip(keys, values):
    lru_cache.add(key, value)
print(lru_cache)
lru_cache.get('b')
print(lru_cache)
lru_cache.add('c', 'how now brown cow')
print(lru_cache)
