import collections


class LRUNode:
    def __init__(self, next=None, previous=None, value=None, key=None):
        self.next = next
        self.previous = previous
        self.value = value
        self.key = key


class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.current_size = 0
        self.head, self.tail = LRUNode(), LRUNode()
        self.head.next, self.tail.previous = self.tail, self.head
        self.map = collections.defaultdict(LRUNode)

    def add(self, key, value):
        if key in self.map:
            self.set(key, value)
        else:
            if self.current_size >= self.max_size:
                node = self.remove_from_tail()
                del self.map[node.key]
            else:
                self.current_size += 1
            node = LRUNode(value=value, key=key)
            self.add_to_head(node)
            self.map[key] = node

    def remove_node(self, node) -> LRUNode:
        node.previous.next, node.next.previous = node.next, node.previous
        return node

    def remove(self, key) -> bool:
        if key in self.map:
            self.remove_node(self.map[key])
            del self.map[key]
            self.current_size -= 1
            return True
        return False

    def remove_from_tail(self):
        self.current_size -= 1
        return self.remove_node(self.tail.previous)

    def add_to_head(self, node):
        self.head.next.previous, self.head.next, node.previous, node.next = node, node, self.head, self.head.next

    def set(self, key, value) -> bool:
        if key in self.map:
            node = self.remove_node(self.map[key])
            node.value = value
            self.add_to_head(node)
            return True
        return False

    def get(self, key) -> any:
        if key in self.map:
            node = self.remove_node(self.map[key])
            self.add_to_head(node)
            return node.value
        return None


lru_cache = LRUCache(4)
lru_cache.add("1", "a")
print(lru_cache.get("1"))
lru_cache.add("2", "b")
lru_cache.set("1", "f")
lru_cache.add("3", "c")
lru_cache.add("4", "d")
print(lru_cache.get("1"))
lru_cache.set("1", "f")
lru_cache.add("5", "e")
print(lru_cache.get("1"))
print(lru_cache.get("2"))
