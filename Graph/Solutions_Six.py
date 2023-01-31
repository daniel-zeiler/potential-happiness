import collections
from typing import List


def find_town_judge(n: int, trust: List[List[int]]) -> int:
    in_count = [0 for _ in range(1, n + 2)]
    out_count = [0 for _ in range(1, n + 2)]
    for origin, destination in trust:
        in_count[destination] += 1
        out_count[origin] += 1

    for i, (into, out) in enumerate(zip(in_count, out_count)):
        if out == 0 and into == n - 1:
            return i
    return -1


def all_paths_source_to_target(graph):
    def traverse(current_location, path_so_far):
        result = []
        if current_location == len(graph) - 1:
            result.append(path_so_far)
        else:
            for adjacent in graph[current_location]:
                result.extend(traverse(adjacent, path_so_far + [adjacent]))
        return result

    return traverse(0, [0])


def minimum_vertices_reach_all_nodes(n: int, edges: List[List[int]]) -> List[int]:
    result = []
    in_count = collections.defaultdict(int)
    for origin, destination in edges:
        in_count[destination] += 1
    for i in range(0, n):
        if i not in in_count:
            result.append(i)
    return result


def keys_and_rooms(rooms: List[List[int]]) -> bool:
    visited = {0}
    queue = collections.deque([0])
    while queue:
        index = queue.popleft()
        for adjacent in rooms[index]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
    return len(visited) == len(rooms)


def redundant_connections(edges):
    parents = [i for i in range(len(edges) + 1)]
    rank = [1 for _ in range(len(edges) + 1)]

    def union(origin, destination):
        origin_parent = find(origin)
        destination_parent = find(destination)
        if origin_parent == destination_parent:
            return False
        if rank[origin_parent] > rank[destination_parent]:
            rank[origin_parent] += rank[destination_parent]
            parents[destination_parent] = origin_parent
        else:
            rank[destination_parent] += rank[origin_parent]
            parents[origin_parent] = destination_parent
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


def maximal_network_rank(n, roads):
    pass
