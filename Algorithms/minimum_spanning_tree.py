"""
Prims algorithm using heaps

"""
import heapq
from collections import defaultdict


def prims_minimum_spanning_tree(edges, number_of_nodes):
    graph = defaultdict(list)

    for node_one, node_two, weight in edges:
        graph[node_one].append((weight, node_two))
        graph[node_two].append((weight, node_one))

    visited_set = set()
    heapq.heapify(graph[0])
    heap = graph[0]

    total_cost = 0
    while len(visited_set) < number_of_nodes:
        cost, vertex = heapq.heappop(heap)
        if vertex not in visited_set:
            total_cost += cost
            visited_set.add(vertex)

            for weight, adjacent in graph[vertex]:
                if adjacent not in visited_set:
                    heapq.heappush(weight, adjacent)

    return total_cost


"""

Kruskal's Algorithm with Union-Find

"""

edges = [[1, 2, 1], [2, 3, 1]]
