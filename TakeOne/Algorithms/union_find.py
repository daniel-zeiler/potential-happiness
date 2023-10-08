from typing import List


# this will find the parent of a given node
def find(x, parents):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x], parents)
    return parents[x]


# this will join the parents of two sets
def union(x, y, parents):
    root_x = find(x, parents)
    root_y = find(y, parents)
    if root_x == root_y:
        return False
    parents[root_x] = root_y
    return True


# This algorithm will determine the total number of paritions within a set of nodes.
# if the union function returns false, then the edge is already within the same set.
def union_find(edges: List[List[int]]):
    parents = [i for i in range(len(edges) + 1)]
    for origin, destination in edges:
        union(origin, destination, parents)
    return len(set(parents))
