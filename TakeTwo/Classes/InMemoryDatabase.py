# TODO: Make this more complex.  Add trie based searching and aggregation.  Add deletion, etc.

import collections


class Database:
    def __init__(self, max_size):
        self.memory = collections.defaultdict(str)
        self.max_size = max_size
        self.current_size = 0

    def create(self, key, value):
        if key in self.memory:
            self.update(key, value)
        elif self.current_size < self.max_size:
            self.memory[key] = value
            self.current_size += 1

    def read(self, key):
        if key in self.memory:
            return self.memory[key]

    def update(self, key, value):
        if key in self.memory:
            self.memory[key] = value

    def delete(self, key):
        if key in self.memory:
            del self.memory[key]
            self.current_size -= 1

    def starts_with(self, prefix):
        n = len(prefix)
        result = []
        for value in self.memory.values():
            if len(value) >= n and value[:n] == prefix:
                result.append(value)
        return result


database = Database(10)
database.create("1", "cat")
print(database.starts_with("cat"))
