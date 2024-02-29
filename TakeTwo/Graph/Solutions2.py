from typing import List
from collections import defaultdict, deque


def find_town_judge(n: int, trust: List[List[int]]) -> int:
    def find_in_and_out_degree():
        in_degree = {i: 0 for i in range(1, n + 1)}
        out_degree = {i: 0 for i in range(1, n + 1)}
        for origin, destination in trust:
            in_degree[destination] += 1
            out_degree[origin] += 1
        return in_degree, out_degree

    in_degree, out_degree = find_in_and_out_degree()
    for i in range(1, n + 1):
        if in_degree[i] == n - 1 and out_degree[i] == 0:
            return i
    return -1


def all_paths_source_to_target(graph):
    result = []

    def traverse(index, path, visited):
        if index == len(graph) - 1:
            result.append(path)
        else:
            for adjacent in graph[index]:
                if adjacent not in visited:
                    traverse(adjacent, path + [adjacent], visited | {adjacent})

    traverse(0, [0], {0})
    return result


def minimum_vertices_reach_all_nodes(n: int, edges: List[List[int]]) -> List[int]:
    def get_in_degree():
        in_degree = {i: 0 for i in range(n)}
        for origin, destination in edges:
            in_degree[destination] += 1
        return in_degree

    in_degree = get_in_degree()

    return list(filter(lambda x: in_degree[x] == 0, in_degree.keys()))


def keys_and_rooms(rooms: List[List[int]]) -> bool:
    if not rooms:
        return True
    visited = {0}
    queue = deque([0])
    while queue:
        index = queue.popleft()
        for adjacent in rooms[index]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
    return len(visited) == len(rooms)


def number_of_provinces(is_connected):
    parents = [i for i in range(len(is_connected))]
    rank = [1 for i in range(len(is_connected))]

    # due to path compression this is a linear operation.
    def union(origin, destination):
        parent_origin = find(origin)
        parent_destination = find(destination)
        if parent_origin == parent_destination:
            return
        rank_origin = rank[parent_origin]
        rank_destination = rank[parent_destination]
        if rank_origin > rank_destination:
            parents[parent_destination] = parent_origin
            rank[parent_origin] += rank_destination
        else:
            parents[parent_origin] = parent_destination
            rank[parent_destination] += rank_origin

    def find(index):
        if parents[index] != index:
            parents[index] = find(parents[index])
        return parents[index]

    # O(n) operation
    for x, row in enumerate(is_connected):
        for y, value in enumerate(row):
            if x > y and value == 1:
                union(x, y)

    for i in range(len(is_connected)):
        find(i)

    return len(set(parents))


def redundant_connections(edges):
    def initialize_parents_and_rank():
        parents, rank = defaultdict(int), defaultdict(int)
        for origin, destination in edges:
            rank[origin], rank[destination] = 1, 1
            parents[origin], parents[destination] = origin, destination
        return parents, rank

    parents, rank = initialize_parents_and_rank()

    def union(origin: int, destination: int) -> bool:
        parent_origin, parent_destination = find(origin), find(destination)
        if parent_origin == parent_destination:
            return False

        rank_origin, rank_destination = rank[parent_origin], rank[parent_destination]

        if rank_origin > rank_destination:
            parents[parent_destination] = parent_origin
            rank[rank_origin] += rank_destination
        else:
            parents[parent_origin] = parent_destination
            rank[parent_destination] += rank_origin
        return True

    def find(index: int) -> int:
        if parents[index] != index:
            parents[index] = find(parents[index])
        return parents[index]

    result = []
    for origin, destination in edges:
        if not union(origin, destination):
            result = [origin, destination]
    return result


def maximal_network_rank(n, roads):
    def get_rank():
        rank = defaultdict(set)

        for origin, destination in roads:
            rank[origin].add(destination)
            rank[destination].add(origin)
        return rank

    rank = get_rank()
    max_network_rank = 0

    for x in range(n):
        for y in range(x + 1, n):
            rank_between_cities = len(rank[x]) + len(rank[y])
            if x in rank[y]:
                rank_between_cities -= 1
            max_network_rank = max(max_network_rank, rank_between_cities)

    return max_network_rank


def find_eventual_safe_nodes(graph):
    safe = set()
    unsafe = set()

    def traverse(index, visited):
        for adjacent in graph[index]:
            if adjacent in visited or adjacent in unsafe or not traverse(adjacent, visited | {adjacent}):
                unsafe.add(index)
                return False
        safe.add(index)
        return True

    for x in range(len(graph)):
        if x not in safe and x not in unsafe:
            traverse(x, {x})

    return list(safe)


def is_graph_bipartite(graph):
    visited = defaultdict(bool)

    def traverse(index, assignment):
        visited[index] = assignment
        for adjacent in graph[index]:
            if adjacent not in visited:
                if not traverse(adjacent, not assignment):
                    return False
            elif visited[adjacent] == assignment:
                return False
        return True

    for x in range(len(graph)):
        if x not in visited:
            if not traverse(x, True):
                return False
    return True


def flower_planting_no_adjacent(n, paths):
    flowers = {1, 2, 3, 4}
    flower_dict = defaultdict(int)

    def get_graph():
        graph = defaultdict(list)
        for origin, destination in paths:
            graph[origin].append(destination)
            graph[destination].append(origin)
        return graph

    graph = get_graph()

    def get_available_flower(index):
        nearby_flowers = set()
        for neighbor in graph[index]:
            if neighbor in flower_dict:
                nearby_flowers.add(flower_dict[neighbor])
        return list(flowers.difference(nearby_flowers))[0]

    for x in range(1, n + 1):
        flower_dict[x] = get_available_flower(x)

    return list(flower_dict.values())


import heapq


def network_delay_time(times, n, k):
    def build_graph():
        graph = defaultdict(list)
        for origin, destination, time in times:
            graph[origin].append((time, destination))
        return graph

    graph, queue, visited = build_graph(), [(0, k)], set()

    while queue:
        time, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            if len(visited) == n:
                return time
            for additional_time, adjacent in graph[node]:
                if adjacent not in visited:
                    heapq.heappush(queue, (time + additional_time, adjacent))
    return -1


def possible_bipartition(n, dislikes):
    visited = defaultdict(bool)

    def build_graph():
        graph = defaultdict(list)
        for origin, destination in dislikes:
            graph[origin].append(destination)
        return graph

    graph = build_graph()

    def traverse(index, group) -> bool:
        visited[index] = group
        for adjacent in graph[index]:
            if adjacent in visited:
                if visited[adjacent] == group:
                    return False
            elif not traverse(adjacent, not group):
                return False
        return True

    for x in range(1, n + 1):
        if x not in visited and not traverse(x, True):
            return False
    return True


def course_schedule_two(num_courses, prerequisites):
    def build_graph_and_in_degree():
        in_degree = {i: 0 for i in range(num_courses)}
        graph = {i: [] for i in range(num_courses)}
        for destination, origin in prerequisites:
            graph[origin].append(destination)
            in_degree[destination] += 1
        return graph, in_degree

    graph, in_degree = build_graph_and_in_degree()
    queue, result = deque([]), []

    for index, value in in_degree.items():
        if value == 0:
            queue.append(index)

    while queue:
        node = queue.popleft()
        result.append(node)
        for adjacent in graph[node]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                queue.append(adjacent)

    if len(result) == num_courses:
        return result
    return []
