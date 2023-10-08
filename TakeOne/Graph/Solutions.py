import collections
import heapq
from typing import List


def find_town_judge(n: int, trust: List[List[int]]) -> int:
    visited = collections.defaultdict(int)
    originating = {i for i in range(1, n + 1)}

    for origin, destination in trust:
        visited[destination] += 1
        if origin in originating:
            originating.remove(origin)

    if len(originating) == 1 and visited[list(originating)[0]] == n - 1:
        return list(originating)[0]
    return - 1


def all_paths_source_to_target(graph: List[List[int]]) -> List[List[int]]:
    result = []

    def traverse(current_position, path_so_far):
        if current_position == len(graph) - 1:
            result.append(path_so_far)
        else:
            for adjacent in graph[current_position]:
                if adjacent not in path_so_far:
                    traverse(adjacent, path_so_far + [adjacent])

    traverse(0, [0])
    return result


def minimum_vertices_reach_all_nodes(n: int, edges: List[List[int]]) -> List[int]:
    destinations = {i for i in range(0, n)}
    for origin, destination in edges:
        if destination in destinations:
            destinations.remove(destination)
    return list(destinations)


def keys_and_rooms(rooms: List[List[int]]) -> bool:
    visited = set()
    queue = collections.deque([0])
    while queue:
        current_position = queue.popleft()
        if current_position not in visited:
            visited.add(current_position)

            for adjacent in rooms[current_position]:
                if adjacent not in visited:
                    queue.append(adjacent)
    return len(visited) == len(rooms)


def redundant_connections(edges):
    parents = [i for i in range(len(edges) + 1)]

    def find(x):
        parent_x = parents[x]
        if parent_x == x:
            return x
        return find(parent_x)

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
            result.append([origin, destination])
    return result[-1]


def maximal_network_rank(n, roads):
    def get_graph(edges):
        graph = collections.defaultdict(set)
        for origin, destination in edges:
            graph[origin].add(destination)
            graph[destination].add(origin)
        return graph

    graph = get_graph(roads)
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            network_rank_i = len(graph[i])
            network_rank_j = len(graph[j])
            network_rank_pair = network_rank_j + network_rank_i
            if i in graph[j]:
                network_rank_pair -= 1
            result = max(result, network_rank_pair)
    return result


def find_eventual_safe_nodes(graph):
    result = []

    def is_safe(index, neighbors, visited):
        if index in visited:
            return False
        visited.add(index)
        for neighbor in neighbors:
            if not is_safe(neighbor, graph[neighbor], visited):
                return False
        return True

    for index, adjacent in enumerate(graph):
        if is_safe(index, adjacent, set()):
            result.append(index)
    return result


def is_graph_bipartite(graph):
    color = {}

    def traverse(origin):
        for adjacent in graph[origin]:
            if adjacent in color and color[adjacent] == color[origin]:
                return False
            elif adjacent not in color:
                color[adjacent] = not color[origin]
                traverse(adjacent)
        return True

    for origin in range(len(graph)):
        if origin not in color:
            color[origin] = True
            if not traverse(origin):
                return False
    return True


def flower_planting_no_adjacent(n, paths):
    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination in paths:
            graph[origin].append(destination)
            graph[destination].append(origin)
        return graph

    graph = get_graph()

    flower_types = {1, 2, 3, 4}

    visited_dict = collections.defaultdict(int)

    def get_adjacent_flowers(garden_index):
        adjacent_flowers = set()
        for adjacent in graph[garden_index]:
            if adjacent in visited_dict:
                adjacent_flowers.add(visited_dict[adjacent])
        return adjacent_flowers

    def traverse(garden_index):
        visited_dict[garden_index] = list(flower_types - get_adjacent_flowers(garden_index))[0]
        for adjacent in graph[garden_index]:
            if adjacent not in visited_dict:
                traverse(adjacent)

    for garden_index in range(1, n + 1):
        if garden_index not in visited_dict:
            traverse(garden_index)

    return list(visited_dict.values())


def network_delay_time(times, n, k):
    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination, time in times:
            graph[origin].append([destination, time])
        return graph

    graph = get_graph()
    visited = set()
    node_queue = [[0, k]]

    while node_queue:
        curr_time, current_position = heapq.heappop(node_queue)
        if current_position not in visited:
            visited.add(current_position)
            if len(visited) == n:
                return curr_time
            for neighbor, time in graph[current_position]:
                if neighbor not in visited:
                    heapq.heappush(node_queue, [curr_time + time, neighbor])
    return -1


def possible_bipartition(n, dislikes):
    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination in dislikes:
            graph[origin].append(destination)
            graph[destination].append(origin)
        return graph

    graph = get_graph()

    colors = collections.defaultdict(int)

    def get_adjacent_colors(target_index):
        adjacent_colors = set()
        for adjacent in graph[target_index]:
            if adjacent in colors:
                adjacent_colors.add(colors[adjacent])
        return adjacent_colors

    def traverse(target_index, color):
        colors[target_index] = color
        if color in get_adjacent_colors(target_index):
            return False
        for adjacent in graph[target_index]:
            if adjacent not in colors:
                if not traverse(adjacent, not color):
                    return False
        return True

    for i in range(1, n + 1):
        if i not in colors:
            if not traverse(i, True):
                return False
    return True


def course_schedule_two(num_courses, prerequisites):
    if not prerequisites:
        return [n for n in range(num_courses)]

    def get_graph():
        no_in = {n for n in range(num_courses)}
        graph = collections.defaultdict(list)
        for destination, origin, in prerequisites:
            if destination in no_in:
                no_in.remove(destination)
            graph[origin].append(destination)
        if not no_in:
            return None
        return graph

    visited = set()
    ordering = []
    graph = get_graph()

    if not graph:
        return []

    def topo_sort_function(i):
        visited.add(i)
        for adjacent in graph[i]:
            if adjacent not in visited:
                topo_sort_function(adjacent)
        ordering.append(i)

    for i in range(num_courses):
        if i not in visited:
            topo_sort_function(i)

    return ordering[::-1]
