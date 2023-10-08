import collections
from typing import List


def get_graph(edges: List[int]):
    graph = collections.defaultdict(list)
    for origin, destination in edges:
        graph[origin].append(destination)
    return graph


def topological_sort(number_of_vertices, edges):
    graph = get_graph(edges)
    visited = set()
    order = []

    # dfs function. for each adjacent node we traverse if not already visited.
    # when we reach "bottom" it will add to the order all the way back up.
    def topo_sort_function(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                topo_sort_function(neighbor)
        order.append(node)

    # iterate through the vertices in our graph and execute dfs on those
    # not already visited
    for i in range(number_of_vertices):
        if i not in visited:
            topo_sort_function(i)

    # this result needs to be reversed because were appending to list from
    # this bottom up.
    return order[::-1]


vertices = [[5, 2], [0, 5], [4, 0], [4, 1], [2, 3], [3, 1]]
print(topological_sort(6, vertices))
