import collections
import heapq
from typing import List


def find_town_judge(n: int, trust: List[List[int]]) -> int:
    trusts = {i + 1: 0 for i in range(n)}
    outgoing = {i + 1 for i in range(n)}

    for origin, destination in trust:
        if origin in outgoing:
            outgoing.remove(origin)
        trusts[destination] += 1

    if len(outgoing) == 1 and trusts[list(outgoing)[0]] == n - 1:
        return list(outgoing)[0]
    return -1


def all_paths_source_to_target(graph):
    result = []

    def traverse(node_id, path, visited):
        if node_id in visited:
            return 1
        visited.add(node_id)
        if node_id == len(graph) - 1:
            result.append(path)
        else:
            if any([traverse(adjacent, path + [adjacent], visited | {node_id}) for adjacent in graph[node_id]]):
                return 1
        return 0

    if traverse(0, [0], set()) == 1:
        return []
    return result


def minimum_vertices_reach_all_nodes(n: int, edges: List[List[int]]) -> List[int]:
    in_degree = {i: 0 for i in range(n)}
    for origin, destination in edges:
        in_degree[destination] += 1
    return list(filter(lambda x: in_degree[x] == 0, in_degree.keys()))


def keys_and_rooms(rooms: List[List[int]]) -> bool:
    visited = {0}
    queue = collections.deque([0])

    while queue:
        node_id = queue.popleft()
        for adjacent in rooms[node_id]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)

    return len(rooms) == len(visited)


def number_of_provinces(is_connected):
    parents = [i for i in range(len(is_connected))]
    rank = [1 for _ in range(len(is_connected))]

    def find(node_id):
        if parents[node_id] != node_id:
            parents[node_id] = find(parents[node_id])
        return parents[node_id]

    def union(node_a, node_b):
        parent_a = find(node_a)
        parent_b = find(node_b)
        if parent_a == parent_b:
            return
        rank_a = rank[parent_a]
        rank_b = rank[parent_b]
        if rank_a > rank_b:
            parents[parent_b] = parent_a
            rank[parent_a] += 1
        else:
            parents[parent_a] = parent_b
            rank[parent_b] += 1

    for x, row in enumerate(is_connected):
        for y, value in enumerate(row):
            if y > x and value == 1:
                union(x, y)

    for x in range(len(is_connected)):
        find(x)
    return len(set(parents))


def redundant_connections(edges):
    parents = [i for i in range(len(edges) + 1)]
    rank = [1 for _ in range(len(edges) + 1)]

    def find(node_id):
        if parents[node_id] != node_id:
            parents[node_id] = find(parents[node_id])
        return parents[node_id]

    def union(node_a, node_b):
        parent_a = find(node_a)
        parent_b = find(node_b)
        if parent_a == parent_b:
            return True
        rank_a = rank[parent_a]
        rank_b = rank[parent_b]
        if rank_a > rank_b:
            rank[parent_a] += 1
            parents[node_b] = parent_a
        else:
            parents[node_a] = parent_b
            rank[parent_b] += 1
        return False

    result = []
    for origin, destination in edges:
        if union(origin, destination):
            result = [origin, destination]
    return result


def maximal_network_rank(n, roads):
    def get_graph():
        graph = collections.defaultdict(set)
        for origin, destination in roads:
            graph[origin].add(destination)
            graph[destination].add(origin)
        return graph

    graph = get_graph()

    max_rank = 0

    for x in range(n):
        for y in range(x + 1, n):
            rank = len(graph[x]) + len(graph[y])
            if x in graph[y]:
                rank -= 1
            max_rank = max(max_rank, rank)
    return max_rank


def find_eventual_safe_nodes(graph):
    safe = set()
    unsafe = set()

    def traverse(node_id, visited):
        if node_id in visited:
            unsafe.add(node_id)
            return False
        for adjacent in graph[node_id]:
            if adjacent in unsafe:
                unsafe.add(node_id)
                return False
            if adjacent not in safe and not traverse(adjacent, visited | {node_id}):
                unsafe.add(node_id)
                return False
        safe.add(node_id)
        return True

    for node_id in range(len(graph)):
        if node_id not in safe and node_id not in unsafe:
            traverse(node_id, set())

    return list(safe)


def is_graph_bipartite(graph):
    colors = collections.defaultdict(bool)

    def traverse(node_id, color):
        colors[node_id] = color
        for adjacent in graph[node_id]:
            if adjacent in colors and colors[adjacent] == color:
                return False
            if adjacent not in colors and not traverse(adjacent, not color):
                return False
        return True

    for node_id in range(len(graph)):
        if node_id not in colors:
            if not traverse(node_id, True):
                return False
    return True


def flower_planting_no_adjacent(n, paths):
    flowers = collections.defaultdict(int)
    flower_colors = {1, 2, 3, 4}

    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination in paths:
            graph[origin].append(destination)
            graph[destination].append(origin)
        return graph

    graph = get_graph()

    def get_color(node_id):
        colors = set()
        for adjacent in graph[node_id]:
            if adjacent in flowers:
                colors.add(flowers[adjacent])
        return list(flower_colors.difference(colors))[0]

    def traverse(node_id):
        flowers[node_id] = get_color(node_id)
        for adjacent in graph[node_id]:
            if adjacent not in flowers:
                traverse(adjacent)

    for node_id in range(1, n + 1):
        if node_id not in flowers:
            traverse(node_id)
    result = [None for _ in range(n)]

    for key, value in flowers.items():
        result[key - 1] = value
    return result


def network_delay_time(times, n, k):
    queue = [[0, k]]
    visited = set()

    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination, weight in times:
            graph[origin].append([weight, destination])
        return graph

    graph = get_graph()
    while queue:
        total_time, node_id = heapq.heappop(queue)
        visited.add(node_id)
        if len(visited) == n:
            return total_time
        for adjacent_weight, adjacent_node in graph[node_id]:
            if adjacent_node not in visited:
                heapq.heappush(queue, [total_time + adjacent_weight, adjacent_node])
    return -1


def course_schedule_two(num_courses, prerequisites):
    def get_graph():
        graph = collections.defaultdict(list)
        in_degree = {x: 0 for x in range(num_courses)}
        for destination, origin in prerequisites:
            graph[origin].append(destination)
            in_degree[destination] += 1
        return graph, in_degree

    graph, in_degree = get_graph()
    queue = collections.deque(list(filter(lambda x: in_degree[x] == 0, in_degree.keys())))
    result = []
    while queue:
        node_id = queue.popleft()
        result.append(node_id)
        for adjacent in graph[node_id]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                queue.append(adjacent)
    if len(result) == num_courses:
        return result
    return []


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    def get_graph():
        graph = collections.defaultdict(list)
        for [origin, destination], value in zip(equations, values):
            graph[origin].append([value, destination])
            graph[destination].append([1 / value, origin])
        return graph

    graph = get_graph()

    def traverse(node_id, target_node, temp_result, visited):
        if node_id == target_node:
            return temp_result
        for weight, adjacent in graph[node_id]:
            if adjacent not in visited:
                result = traverse(adjacent, target_node, temp_result * weight, visited | {node_id})
                if result != -1:
                    return result
        return -1

    result = []
    for node_id, target_id in queries:
        if node_id not in graph or target_id not in graph:
            result.append(float(-1))
        else:
            result.append(traverse(node_id, target_id, 1, set()))

    return result


def numBusesToDestination(routes: List[List[int]], source: int, target: int) -> int:
    def get_graph():
        bus_graph = collections.defaultdict(list)
        stop_graph = collections.defaultdict(list)
        for i, stops in enumerate(routes):
            for stop in stops:
                bus_graph[i + 1].append(stop)
                stop_graph[stop].append(i + 1)
        return bus_graph, stop_graph

    bus_graph, stop_graph = get_graph()
    bus_visited, stop_visited = set(), set()
    queue = collections.deque([[0, source, 0]])
    while queue:
        total, location_id, turn = queue.popleft()
        if turn == 0:
            if location_id == target:
                return total
            for adjacent in stop_graph[location_id]:
                if adjacent not in bus_visited:
                    bus_visited.add(adjacent)
                    queue.append([total + 1, adjacent, 1])
        else:
            for adjacent in bus_graph[location_id]:
                if adjacent not in stop_visited:
                    stop_visited.add(adjacent)
                    queue.append([total, adjacent, 0])
    return -1


def kSimilarity(s1: str, s2: str) -> int:
    visited = set()

    def get_neighbors(input_string):
        neighbors = []
        for x in range(len(input_string)):
            for y in range(x + 1, len(input_string)):
                temp_string = list(input_string)
                temp_string[x], temp_string[y] = temp_string[y], temp_string[x]
                neighbors.append(''.join(temp_string))
        return neighbors

    queue = collections.deque([[0, s1]])
    visited.add(s1)
    while queue:
        value, input_string = queue.popleft()
        if input_string == s2:
            return value
        for neighbor in get_neighbors(input_string):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([value + 1, neighbor])
    return -1


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    def get_graph():
        graph = collections.defaultdict(list)
        for word in wordList + [beginWord]:
            for i, letter in enumerate(word):
                graph[word[:i] + '*' + word[i + 1:]].append(word)
        return graph

    if endWord not in wordList:
        return -1
    graph = get_graph()
    visited = {beginWord}
    queue = collections.deque([[1, beginWord]])
    while queue:
        distance, word = queue.popleft()
        if word == endWord:
            return distance + 1
        for i, letter in enumerate(word):
            transform = word[:i] + '*' + word[i + 1:]
            for word in graph[transform]:
                if word not in visited:
                    visited.add(word)
                    queue.append([distance + 1, word])
    return -1
