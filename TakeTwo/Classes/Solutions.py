import heapq
from typing import List


class AutoCompleteSystemNode:
    def __init__(self, sentence: str = None, hotness: int = 0):
        self.sentence = sentence
        self.children = defaultdict(AutoCompleteSystemNode)
        self.hotness = hotness


class AutocompleteSystem:
    def __init__(self, words: List[str], times: [int]):
        self.head = AutoCompleteSystemNode()
        for word, time in zip(words, times):
            self.insert(word, time)
        self.cursor_node = self.head
        self.current_input = ""

    def insert(self, sentence: str, hotness: int):
        def insert_helper(sentence_remaining, node, hotness):
            if not sentence_remaining:
                node.sentence = sentence
                node.hotness += hotness
                return
            elif sentence_remaining[0] not in node.children:
                node.children[sentence_remaining[0]] = AutoCompleteSystemNode()
            insert_helper(sentence_remaining[1:], node.children[sentence_remaining[0]], hotness)

        insert_helper(sentence, self.head, hotness)

    def gather(self) -> List[AutoCompleteSystemNode]:
        def gather_helper(node: AutoCompleteSystemNode) -> List[AutoCompleteSystemNode]:
            result = []
            if node.sentence:
                result.append(node)
            for child in node.children.values():
                result.extend(gather_helper(child))
            return result

        return gather_helper(self.cursor_node)

    def input_character(self, character: str) -> List[str]:
        if character == "#":
            self.insert(self.current_input, 1)
            self.current_input = ""
            self.cursor_node = self.head
            return []
        self.current_input += character
        if not self.cursor_node:
            return []
        elif character not in self.cursor_node.children:
            self.cursor_node = None
            return []
        else:
            self.cursor_node = self.cursor_node.children[character]
            gathered_nodes = self.gather()
            gathered_nodes.sort(key=lambda node: node.hotness)
            return [node.sentence for node in gathered_nodes]


from collections import defaultdict


class File:
    def __init__(self, name: str, contents: str):
        self.file_name = name
        self.contents = contents


class Directory:
    def __init__(self, directory_path: str):
        self.files = []
        self.directory_path = directory_path
        self.children = defaultdict(Directory)
        self.files = defaultdict(File)


class FileSystem:
    def __init__(self):
        self.root = Directory("")
        self.root.children[""] = Directory("")

    def add_file(self, file_path, contents):
        path_parts = file_path.split("/")

        def add_file_helper(directory, path_remaining):
            if len(path_remaining) == 1:
                directory.files[path_remaining[0]] = File(path_remaining[0], contents)
            elif path_remaining[0] not in directory.children:
                raise Exception(f"file_path {file_path[:-1]} does not exist")
            else:
                add_file_helper(directory.children[path_remaining[0]], path_remaining[1:])

        add_file_helper(self.root, path_parts)

    def add_directory(self, file_path):
        path_parts = file_path.split("/")

        def add_directory_helper(directory, path_remaining):
            if not path_remaining:
                return
            if path_remaining[0] not in directory.children:
                directory.children[path_remaining[0]] = Directory(path_remaining[0])
            add_directory_helper(directory.children[path_remaining[0]], path_remaining[1:])

        add_directory_helper(self.root, path_parts)

    def list_directory(self, file_path):
        def traverse(node, file_path_remaining):
            if not file_path_remaining:
                return list(node.children.keys()) + list(node.files.keys())
            elif file_path_remaining[0] not in node.children:
                return []
            return traverse(node.children[file_path_remaining[0]], file_path_remaining[1:])

        return traverse(self.root, file_path.split("/"))

    def read_file(self, file_path):
        path_parts = file_path.split("/")

        def traverse(node, file_path_remaining):
            if len(file_path_remaining) == 1:
                return node.files[file_path_remaining[0]].contents if file_path_remaining[0] in node.files else ""
            if file_path_remaining[0] not in node.children:
                return ""
            return traverse(node.children[file_path_remaining[0]], file_path_remaining[1:])

        return traverse(self.root, path_parts)


class LRUCacheNode:
    def __init__(self, key: str = None, value: int = None):
        self.previous = None
        self.next = None
        self.key = key
        self.value = value


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = defaultdict(LRUCacheNode)
        self.head = LRUCacheNode()
        self.tail = LRUCacheNode()
        self.tail.next, self.tail.previous, self.head.next, self.head.previous = self.head, self.head, self.tail, self.tail
        self.size = 0
        self.capacity = capacity

    def add_item(self, key: str, value: int):
        if key in self.cache:
            self.update_item(key, value)
        else:
            if self.size == self.capacity:
                del self.cache[self.tail.next.key]
                self._remove_from_tail()
            else:
                self.size += 1
            node = LRUCacheNode(key, value)
            self.cache[key] = node
            self._add_item_to_head(node)

    def _remove_node(self, node):
        node.previous.next, node.next.previous = node.next, node.previous
        node.previous, node.next = None, None

    def _remove_from_tail(self):
        self._remove_node(self.tail.next)

    def _add_item_to_head(self, node):
        self.head.previous.next, self.head.previous, node.previous, node.next = node, node, self.head.previous, self.head

    def get_item(self, key: str):
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._add_item_to_head(node)
            return node.value

    def update_item(self, key: str, value: int):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_item_to_head(node)


class Order:
    def __init__(self, price: int, quantity: int, type: str):
        self.price = price
        self.quantity = quantity
        self.type = type


class StockExchange:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []

    def process_order(self, order) -> int:
        if order.type == "buy":
            return self.process_buy_order(order)
        elif order.type == "sell":
            return self.process_sell_order(order)
        raise Exception(f"invalid type {order.type}")

    def process_buy_order(self, order) -> int:
        amount_bought = 0
        while order.quantity and self.sell_orders and self.sell_orders[0].price <= order.price:
            sell_order = self.sell_orders[0][1]
            buying = min(order.quantity, sell_order.quantity)
            sell_order.quantity -= buying
            order.quantity -= buying
            amount_bought += buying
            if sell_order.quantity == 0:
                heapq.heappop(self.sell_orders)
        if order.quantity:
            heapq.heappush(self.buy_orders, (-order.price, order))
        return amount_bought

    def process_sell_order(self, order) -> int:
        amount_sold = 0
        while order.quantity and self.buy_orders and -self.buy_orders[0].price >= order.price:
            buy_order = self.buy_orders[0][1]
            selling = min(order.quantity, buy_order.quantity)
            buy_order.quantity -= selling
            order.quantity -= selling
            amount_sold += selling
            if buy_order.quantity == 0:
                heapq.heappop(self.buy_orders)
        if order.quantity:
            heapq.heappush(self.sell_orders, (order.price, order))
        return amount_sold
