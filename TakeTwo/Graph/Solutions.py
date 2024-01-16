from typing import List
import collections


def find_town_judge(n: int, trust: List[List[int]]) -> int:
    def build_graph() -> (dict, dict):
        into = collections.defaultdict(int)
        out_of = collections.defaultdict(int)
        for origin, destination in trust:
            into[destination] += 1
            out_of[origin] += 1
        return into, out_of

    into, out_of = build_graph()

    for i in range(1, n + 1):
        if into[i] == n - 1 and out_of and i not in out_of:
            return i

    return -1


def all_paths_source_to_target(graph):
    result = []

    def traverse_graph(position, path_so_far):
        if position == len(graph) - 1:
            result.append(path_so_far)
        else:
            for adjacent in graph[position]:
                traverse_graph(adjacent, path_so_far + [adjacent])

    traverse_graph(0, [0])
    return result


def minimum_vertices_reach_all_nodes(n: int, edges: List[List[int]]) -> List[int]:
    def count_destination() -> set:
        destination_count = collections.defaultdict(int)
        for origin, destination in edges:
            destination_count[destination] += 1
        return set(destination_count.keys())

    destinations_set = count_destination()
    result = []

    for i in range(0, n):
        if i not in destinations_set:
            result.append(i)

    return result


def keys_and_rooms(rooms: List[List[int]]) -> bool:
    queue = collections.deque([0])
    visited = {0}
    while queue:
        position = queue.popleft()
        for adjacent in rooms[position]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
    if len(visited) == len(rooms):
        return True
    return False


def number_of_provinces(is_connected):
    n = len(is_connected)
    parents = [i for i in range(n)]

    def union(origin, destination):
        parent_origin = find(origin)
        parent_destination = find(destination)
        if parent_origin != parent_destination:
            parents[parent_destination] = parent_origin

    def find(node_id):
        if parents[node_id] != node_id:
            parents[node_id] = find(parents[node_id])
        return parents[node_id]

    for x in range(0, n):
        for y in range(x + 1, n):
            if is_connected[x][y] == 1:
                union(x, y)

    for x in range(len(is_connected)):
        find(x)

    return len({find(x) for x in parents})


def redundant_connections(edges) -> List[int]:
    parents = [i for i in range(0, len(edges) + 1)]

    def union(origin, destination) -> bool:
        parent_origin = find(origin)
        parent_destination = find(destination)
        if parent_origin != parent_destination:
            parents[parent_origin] = parent_destination
            return True

    def find(node) -> int:
        if parents[node] == node:
            return node
        return find(parents[node])

    result = []
    for origin, destination in edges:
        if not union(origin, destination):
            result = [origin, destination]

    return result


def maximal_network_rank(n, roads):
    def get_city_graph() -> dict:
        rank = collections.defaultdict(set)
        for origin, destination in roads:
            rank[origin].add(destination)
            rank[destination].add(origin)
        return rank

    city_graph = get_city_graph()
    max_network = 0

    for x in range(n):
        for y in range(x + 1, n):
            network_rank = len(city_graph[x]) + len(city_graph[y])
            if x in city_graph[y]:
                network_rank -= 1
            max_network = max(max_network, network_rank)
    return max_network


def find_eventual_safe_nodes(graph):
    safe = set()
    unsafe = set()

    def traverse(position: int, visited: set) -> bool:
        for adjacent in graph[position]:
            if adjacent in safe:
                pass
            if adjacent in visited or adjacent in unsafe or not traverse(adjacent, visited.union({adjacent})):
                unsafe.add(position)
                return False
        return True

    for x in range(len(graph)):
        if x not in safe and x not in unsafe and traverse(x, {x}):
            safe.add(x)

    return list(safe)


def is_graph_bipartite(graph):
    visited_colors = collections.defaultdict(bool)
    nodes = len(graph)

    def traverse(position: int, color: bool) -> bool:
        visited_colors[position] = color
        for adjacent in graph[position]:
            if adjacent in visited_colors:
                if visited_colors[adjacent] == color:
                    return False
            else:
                if not traverse(adjacent, not color):
                    return False
        return True

    for i in range(nodes):
        if i not in visited_colors:
            if not traverse(i, False):
                return False
    return True


def flower_planting_no_adjacent(n, paths) -> List[int]:
    colors = {i for i in range(1, 5)}
    visited_colors = collections.defaultdict(int)

    def build_graph():
        graph = collections.defaultdict(list)
        for origin, destination in paths:
            graph[origin].append(destination)
            graph[destination].append(origin)
        return graph

    graph = build_graph()

    def traverse(graph_index):
        adjacent_flowers = set()
        for adjacent in graph[graph_index]:
            if adjacent in visited_colors:
                adjacent_flowers.add(visited_colors[adjacent])
        visited_colors[graph_index] = list(colors.difference(adjacent_flowers))[0]

        for adjacent in graph[graph_index]:
            if adjacent not in visited_colors:
                traverse(adjacent)

    for i in range(1, n):
        if i not in visited_colors:
            traverse(i)

    return list(visited_colors.values())

def network_delay_time(times, n, k):
    pass