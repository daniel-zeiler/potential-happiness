import collections


class Node:
    def __init__(self, key, value, next=None, previous=None):
        self.key = key
        self.value = value
        self.next = next
        self.previous = previous


class LRUCache:
    def __init__(self, capacity=10):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.map = collections.defaultdict(Node)
        self.capacity = capacity
        self.current_capacity = 0

        self.head.next = self.tail
        self.tail.previous = self.head

    def add_to_head(self, node):
        self.head.next, self.head.next.previous, node.previous, node.next = node, node, self.head, self.head.next

    def remove_from_tail(self):
        node = self.tail.previous
        self.remove(node)

    def remove(self, node):
        node.previous.next, node.next.previous = node.next, node.previous

    def add_item(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.remove(node)
        else:
            node = Node(key, value)

        if self.capacity == self.current_capacity:
            self.remove_from_tail()
        else:
            self.current_capacity += 1

        self.add_to_head(node)

    def get_item(self, key):
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.add_to_head(node)
            return node.value
