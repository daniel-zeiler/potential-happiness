import collections
from typing import List


def all_paths_source_to_target(graph):
    result = []
    target = len(graph) - 1

    def traverse(node_id, path, visited):
        if node_id == target:
            result.append(path)
        for adjacent in graph[node_id]:
            if adjacent not in visited:
                traverse(adjacent, path + [adjacent], visited | {adjacent})

    traverse(0, [0], {0})
    return result


def minimum_vertices_reach_all_nodes(n: int, edges: List[List[int]]) -> List[int]:
    in_degree = {i: 0 for i in range(n)}
    for origin, destination in edges:
        in_degree[destination] += 1
    return list(filter(lambda x: in_degree[x] == 0, in_degree.keys()))


def keys_and_rooms(rooms: List[List[int]]) -> bool:
    queue = collections.deque([0])
    visited = {0}
    while queue:
        room_id = queue.popleft()
        for adjacent in rooms[room_id]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
    return len(visited) == len(rooms)


def number_of_provinces(is_connected):
    parents = [n for n in range(len(is_connected))]
    rank = [1 for _ in range(len(is_connected))]

    def find(node_id):
        while parents[node_id] != node_id:
            parents[node_id] = find(parents[node_id])
            node_id = parents[node_id]
        return parents[node_id]

    def union(node_one, node_two):
        parent_one = find(node_one)
        parent_two = find(node_two)
        if parent_one == parent_two:
            return False
        rank_one = rank[parent_one]
        rank_two = rank[parent_two]
        if rank_one > rank_two:
            rank[parent_one] += rank_two
            parents[parent_two] = parent_one
        else:
            rank[parent_two] += rank_one
            parents[parent_one] = parent_two
        return True

    number_of_provinces = 0
    for x in range(len(is_connected)):
        number_of_provinces += 1
        for y in range(x + 1, len(is_connected)):
            if is_connected[x][y] == 1:
                if union(x, y):
                    number_of_provinces -= 1
    return number_of_provinces


def redundant_connections(edges):
    rank = [1 for _ in range(0, len(edges) + 1)]
    parents = [n for n in range(0, len(edges) + 1)]

    def find(node_id):
        if node_id != parents[node_id]:
            parents[node_id] = find(parents[node_id])
        return parents[node_id]

    def union(node_one, node_two):
        parent_one = find(node_one)
        parent_two = find(node_two)

        if parent_one == parent_two:
            return False

        rank_one = rank[parent_one]
        rank_two = rank[parent_two]

        if rank_one > rank_two:
            rank[parent_one] += rank_two
            parents[parent_two] = parent_one
        else:
            rank[parent_two] += rank_two
            parents[parent_one] = parent_two
        return True

    redundant_connection = []
    for origin, destination in edges:
        if not union(origin, destination):
            redundant_connection = [origin, destination]
    return redundant_connection


def maximal_network_rank(n, roads):
    graph = collections.defaultdict(set)
    for origin, destination in roads:
        graph[origin].add(destination)
        graph[destination].add(origin)
    max_net_rank = 0

    for x in range(n):
        for y in range(x + 1, n):
            net_rank = len(graph[x]) + len(graph[y])
            if x in graph[y]:
                net_rank -= 1
            max_net_rank = max(max_net_rank, net_rank)
    return max_net_rank


def find_eventual_safe_nodes(graph):
    unsafe = set()
    safe = set()

    def traverse(node_id, visited):
        if len(graph[node_id]) == 0:
            safe.add(node_id)
            return True
        for adjacent in graph[node_id]:
            if adjacent in visited or not traverse(adjacent, visited | {adjacent}):
                unsafe.add(node_id)
                return False
        safe.add(node_id)
        return True

    for x in range(len(graph)):
        if x not in safe and x not in unsafe:
            traverse(x, {x})

    return list(safe)
