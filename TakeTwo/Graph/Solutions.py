from typing import List
import collections
import heapq


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
    visited = set()
    max_time = 0

    def build_graph() -> dict:
        graph = collections.defaultdict(list)
        for origin, destination, time in times:
            graph[origin].append([destination, time])
        return graph

    graph = build_graph()

    queue = [[0, k]]
    while queue:
        time, position = heapq.heappop(queue)
        if position not in visited:
            visited.add(position)
            max_time = max(time, max_time)
            for neighbor, transmit_time in graph[position]:
                heapq.heappush(queue, [transmit_time + time, neighbor])

    if len(visited) == n:
        return max_time
    return -1


def possible_bipartition(n, dislikes):
    visited = collections.defaultdict(bool)

    def build_graph() -> dict:
        graph = collections.defaultdict(list)
        for origin, destination in dislikes:
            graph[origin].append(destination)
            graph[destination].append(origin)
        return graph

    graph = build_graph()

    def traverse(node_id, partition_label):
        visited[node_id] = partition_label
        for adjacent in graph[node_id]:
            if adjacent not in visited:
                if not traverse(adjacent, not partition_label):
                    return False
            elif visited[adjacent] == partition_label:
                return False
        return True

    for i in range(1, n):
        if i not in visited:
            if not traverse(i, True):
                return False
    return True


def course_schedule_two(num_courses, prerequisites):
    def build_graph() -> {dict, dict}:
        graph = collections.defaultdict(list)
        in_degree = {n: 0 for n in range(num_courses)}
        for before, after in prerequisites:
            graph[before].append(after)
            in_degree[after] += 1
        return graph, in_degree

    result = []
    graph, in_degree = build_graph()
    visited = set()
    queue = collections.deque([])
    for key, value in in_degree.items():
        if value == 0:
            queue.append(key)

    while queue:
        position = queue.popleft()
        if position not in visited:
            result.append(position)
            for adjacent in graph[position]:
                in_degree[adjacent] -= 1
                if in_degree[adjacent] == 0:
                    queue.append(adjacent)

    if len(result) == num_courses:
        return result[::-1]
    return []


def validate_binary_tree(n: int, left_child: List[int], right_child: List[int]) -> bool:
    def get_graph_and_degree() -> {dict, dict}:
        graph = collections.defaultdict(list)
        in_degree = {i: 0 for i in range(n)}
        for i in range(n):
            left, right = left_child[i], right_child[i]
            if left != -1:
                graph[i].append(left)
                in_degree[left] += 1
            if right != -1:
                graph[i].append(right)
                in_degree[right] += 1
        return graph, in_degree

    graph, in_degree = get_graph_and_degree()
    to_visit = collections.deque([])
    visited = set()

    for key, value in in_degree.items():
        if value > 1:
            return False
        if value == 0:
            if to_visit:
                return False
            to_visit.append(key)
            visited.add(key)

    while to_visit:
        node = collections.deque.popleft(to_visit)
        for adjacent in graph[node]:
            if adjacent in visited:
                return False
            visited.add(adjacent)
            collections.deque.append(to_visit, adjacent)

    return len(visited) == n


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    pass
