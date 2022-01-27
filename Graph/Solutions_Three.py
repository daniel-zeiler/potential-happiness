import collections
import heapq
from typing import List


def all_paths_source_to_target(graph):
    result = []

    def traverse(node, path_so_far, visited):
        if node == len(graph) - 1:
            result.append(path_so_far)
        else:
            for adjacent in graph[node]:
                if adjacent not in visited:
                    traverse(adjacent, path_so_far + [adjacent], visited | {adjacent})

    traverse(0, [0], {0})
    return result


def minimum_vertices_reach_all_nodes(n: int, edges: List[List[int]]) -> List[int]:
    in_degree = {i for i in range(n)}
    for origin, destination in edges:
        if destination in in_degree:
            in_degree.remove(destination)
    return list(in_degree)


def keys_and_rooms(rooms: List[List[int]]) -> bool:
    def get_graph():
        graph = collections.defaultdict(list)
        for i, room in enumerate(rooms):
            graph[i] = room
        return graph

    graph = get_graph()

    visited = {0}

    queue = collections.deque([0])

    while queue:
        node = queue.popleft()
        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
    return len(visited) == len(rooms)


def number_of_provinces(is_connected):
    parents = [i for i in range(len(is_connected))]

    def find(x):
        while x != parents[x]:
            x = parents[x]
        return x

    def union(x, y):
        x_parent = find(x)
        y_parent = find(y)
        if x_parent == y_parent:
            return False
        parents[x_parent] = y_parent
        return True

    provinces = len(parents)
    for x, row in enumerate(is_connected):
        for y in range(x + 1, len(is_connected)):
            if is_connected[x][y] == 1:
                if union(x, y):
                    provinces -= 1
    return provinces


def redundant_connections(edges):
    parents = [i for i in range(len(edges) + 1)]

    def find(x):
        while parents[x] != x:
            x = parents[x]
        return x

    def union(x, y):
        parent_x = find(x)
        parent_y = find(y)
        if parent_x == parent_y:
            return False
        parents[parent_x] = parent_y
        return True

    result = []
    for origin, destination in edges:
        if not union(origin, destination):
            result = [origin, destination]
    return result


def maximal_network_rank(n, roads):
    degree = {i: set() for i in range(n)}

    for origin, destination in roads:
        degree[origin].add(destination)
        degree[destination].add(origin)
    max_rank = 0

    for i in range(n):
        for j in range(i + 1, n):
            rank = len(degree[i]) + len(degree[j])
            if i in degree[j]:
                rank -= 1
            max_rank = max(max_rank, rank)

    return max_rank


def find_eventual_safe_nodes(graph):
    def traverse(current_node, visited):
        for adjacent in graph[current_node]:
            if adjacent in visited or not traverse(adjacent, visited | {adjacent}):
                return False
        return True

    result = []
    for i in range(len(graph)):
        if traverse(i, {i}):
            result.append(i)
    return result


def flower_planting_no_adjacent(n, paths):
    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination in paths:
            graph[origin].append(destination)
            graph[destination].append(origin)
        return graph

    graph = get_graph()
    colors = collections.defaultdict(int)
    flowers = {1, 2, 3, 4}

    def get_available_color(node_id):
        adjacent_colors = set()
        for adjacent in graph[node_id]:
            if adjacent in colors:
                adjacent_colors.add(colors[adjacent])
        return flowers - adjacent_colors

    for i in range(1, n):
        if i not in colors:
            available_color = get_available_color(i)
            colors[i] = list(available_color)[0]
            queue = collections.deque([i])
            while queue:
                node_id = queue.popleft()
                for adjacent in graph[node_id]:
                    if adjacent not in colors:
                        available_color = get_available_color(adjacent)
                        colors[adjacent] = list(available_color)[0]
                        queue.append(adjacent)

    return list(colors.values())


def network_delay_time(times, n, k):
    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination, weight in times:
            graph[origin].append([destination, weight])
        return graph

    queue = [[0, k]]
    visited = {k}
    graph = get_graph()
    max_time = 0
    while queue:
        total_weight, node_id = heapq.heappop(queue)
        max_time = max(max_time, total_weight)
        for destination, weight in graph[node_id]:
            if destination not in visited:
                visited.add(destination)
                heapq.heappush(queue, [total_weight + weight, destination])

    if len(visited) == n:
        return max_time
    return -1


def possible_bipartition(n, dislikes):
    partition_labels = collections.defaultdict(bool)

    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination in dislikes:
            graph[origin].append(destination)
            graph[destination].append(origin)
        return graph

    dislikes = get_graph()

    def check_partition(node_id, partition_label):
        for adjacent in dislikes[node_id]:
            if adjacent in partition_labels and partition_labels[adjacent] == partition_label:
                return False
        return True

    def traverse(node_id, partition_label):
        if not check_partition(node_id, partition_label):
            return False
        for adjacent in dislikes[node_id]:
            if adjacent not in partition_labels:
                partition_labels[adjacent] = not partition_label
                if not traverse(adjacent, not partition_label):
                    return False
        return True

    for i in range(1, n):
        if i not in partition_labels:
            partition_labels[i] = True
            if not traverse(i, True):
                return False
    return True
