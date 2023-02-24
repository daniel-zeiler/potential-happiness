import collections
from typing import List


def find_town_judge(n: int, trust: List[List[int]]) -> int:
    in_degree = collections.defaultdict(int)
    out_degree = collections.defaultdict(int)
    for origin, destination in trust:
        in_degree[destination] += 1
        out_degree[origin] += 1
    for i in range(n):
        if in_degree[n] == n - 1 and n not in out_degree:
            return n
    return -1


def all_paths_source_to_target(graph):
    def recursive_traverse(node, path):
        result = []
        path = path + [node]
        if node == len(graph) - 1:
            result.append(path)
        else:
            for adjacent in graph[node]:
                result.extend(recursive_traverse(adjacent, path))
        return result

    return recursive_traverse(0, [])


def redundant_connections(edges):
    parents = [i for i in range(len(edges) + 1)]
    rank = [1 for _ in range(len(edges) + 1)]

    def union(origin, destination):
        parent_origin = find(origin)
        parent_destination = find(destination)
        if parent_origin == parent_destination:
            return False
        rank_origin = rank[parent_origin]
        rank_destination = rank[parent_destination]
        if rank_origin < rank_destination:
            parents[parent_origin] = parent_destination
            rank[parent_destination] += rank_origin
        else:
            parents[parent_destination] = parent_origin
            rank[parent_origin] += rank_destination
        return True

    def find(node):
        if parents[node] != node:
            parents[node] = find(parents[node])
        return parents[node]

    result = []
    for origin, destination in edges:
        if not union(origin, destination):
            result = [origin, destination]
    return result
