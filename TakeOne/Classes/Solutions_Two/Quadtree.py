class Location:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value


def intersection(node, x, y):
    pass


class QuadTreeNode:
    def __init__(self, top_left, top_right, bottom_left, bottom_right):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.locations = []
        self.children = []
        self.max_capacity = 10
        self.leaf = True

    def check_capacity(self):
        if len(self.locations) > self.max_capacity:
            self.leaf = False
            half_distance = (self.top_right + self.top_left) / 2
            self.children = [
                QuadTreeNode(self.top_left, None, None, None),
                QuadTreeNode(None, self.top_right, None, None),
                QuadTreeNode(None, None, self.bottom_left, None),
                QuadTreeNode(None, None, None, self.bottom_right)
            ]
            for location in self.locations:
                for child in self.children:
                    if intersection(child, location.x, location.y):
                        child.locations.append(location)
            self.locations = []
            for child in self.children:
                child.check_capacity()


class QuadTree:
    def __init__(self):
        self.root = QuadTreeNode([0, 0], [0, 100], [100, 0], [100, 100])

    def insert(self, value, x, y):
        def recursive_insert(node):
            if node.leaf:
                node.locations.append(value)
                node.check_capacity()
            else:
                for child in node.children:
                    if intersection(node, x, y):
                        recursive_insert(child)
                        break

        recursive_insert(self.root)

    def search(self, x, y):

        def recursive_search(node):
            if node.leaf:
                for location in node.locations:
                    if location.x == x and location.y == y:
                        return True
            else:
                for child in node.children:
                    if intersection(child, x, y):
                        return recursive_search(child)
            return False

        return recursive_search(self.root)
