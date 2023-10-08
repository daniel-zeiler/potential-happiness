import collections
from typing import List


def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]:
    rank = [1 for n in range(len(positions))]
    parents = [n for n in range(len(positions))]

    def find(node_id):
        while parents[node_id] != node_id:
            parents[node_id] = find(parents[node_id])
            node_id = parents[node_id]
        return parents[node_id]

    def union(node_1, node_2):
        parent_1 = find(node_1)
        parent_2 = find(node_2)
        if parent_1 == parent_2:
            return False
        rank_1 = rank[parent_1]
        rank_2 = rank[parent_2]
        if rank_1 < rank_2:
            parents[parent_1] = parent_2
            rank[parent_2] += 1
        else:
            parents[parent_2] = parent_1
            rank[parent_1] += 1
        return True

    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    added_positions = {}
    num_islands = 0
    result = []
    for index, [x, y] in enumerate(positions):
        if (x, y) in added_positions:
            result.append(num_islands)
        else:
            num_islands += 1
            for x_direction, y_direction in directions:
                x_target, y_target = x + x_direction, y + y_direction
                if 0 <= x_target < m and 0 <= y_target < n and (x_target, y_target) in added_positions:
                    if union(added_positions[(x_target, y_target)], index):
                        num_islands -= 1
            added_positions[(x, y)] = index
            result.append(num_islands)

    return result


def numBusesToDestination(routes: List[List[int]], source: int, target: int) -> int:
    def get_graph():
        bus_graph = collections.defaultdict(list)
        route_graph = collections.defaultdict(list)
        for bus, bus_stops in enumerate(routes):
            bus_graph[bus] = bus_stops
            for stop in bus_stops:
                route_graph[stop].append(bus)
        return bus_graph, route_graph

    bus_graph, route_graph = get_graph()

    queue = collections.deque([[0, 0, source]])
    visited_routes = {source}
    visited_buses = set()
    while queue:
        is_bus, num_buses, node_id = queue.popleft()
        if node_id == target and not is_bus:
            return num_buses
        if is_bus:
            for adjacent in bus_graph[node_id]:
                if adjacent not in visited_routes:
                    visited_routes.add(adjacent)
                    queue.append([not is_bus, num_buses, adjacent])
        else:
            for adjacent in route_graph[node_id]:
                if adjacent not in visited_buses:
                    visited_buses.add(adjacent)
                    queue.append([not is_bus, num_buses + 1, adjacent])

    return -1


def alienOrder(words: List[str]) -> str:
    def get_graph_and_in_degree():
        graph = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)
        for word in words:
            for letter in word:
                in_degree[letter] = 0

        for i, word in enumerate(words):
            if i > 0:
                for letter_a, letter_b in zip(words[i - 1], word):
                    if letter_a != letter_b:
                        graph[letter_a].append(letter_b)
                        in_degree[letter_b] += 1
                        break

        return graph, in_degree

    graph, in_degree = get_graph_and_in_degree()
    queue = collections.deque(list(filter(lambda x: in_degree[x] == 0, in_degree.keys())))
    result = ''

    while queue:
        letter = queue.popleft()
        result += letter
        for adjacent in graph[letter]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                queue.append(adjacent)
    if len(result) == len(in_degree):
        return result
    return ''
