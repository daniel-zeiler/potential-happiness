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


def validate_binary_tree(n, left_child, right_child):
    def build_in_degree():
        in_degree = {i: 0 for i in range(n)}
        for index, (left, right) in enumerate(zip(left_child, right_child)):
            if left != -1:
                in_degree[left] += 1
            if right != -1:
                in_degree[right] += 1
        return in_degree

    in_degree, root = build_in_degree(), None

    for index, degree in in_degree.items():
        if degree == 0:
            if root is not None:
                return False
            root = index
        if degree > 1:
            return False

    return root is not None


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    def build_graph():
        for (origin, destination), value in zip(equations, values):
            graph[origin].append((value, destination))
            graph[destination].append((1 / value, origin))

    graph = defaultdict(list)
    build_graph()

    def traverse(index, target, value, visited) -> float:
        if index not in graph or target not in graph:
            return -1.0
        if index == target:
            return value
        for adjacent_value, adjacent in graph[index]:
            if adjacent not in visited:
                adjacent_result = traverse(adjacent, target, value * adjacent_value, visited | {adjacent})
                if adjacent_result != -1:
                    return adjacent_result
        return -1.0

    return [traverse(x, y, 1.0, {x}) for x, y in queries]


def numBusesToDestination(routes: List[List[int]], source: int, target: int) -> int:
    def build_route_graph():
        graph = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)
        return graph

    visited_routes = set()
    visited_stops = {source}
    queue = deque([(source, 0)])
    route_graph = build_route_graph()

    while queue:
        position, distance = queue.popleft()

        if position == target:
            return distance

        for adjacent_route in route_graph[position]:
            if adjacent_route not in visited_routes:
                visited_routes.add(adjacent_route)
                for adjacent_stop in routes[adjacent_route]:
                    if adjacent_stop not in visited_stops:
                        visited_stops.add(adjacent_stop)
                        queue.append((adjacent_stop, distance + 1))

    return -1


def kSimilarity(s1: str, s2: str) -> int:
    def add_to_adjacency_graph(input_string):
        for x in range(len(input_string)):
            for y in range(x + 1, len(input_string)):
                temp = list(input_string)
                temp[x], temp[y] = temp[y], temp[x]
                adjacency_graph[input_string].add("".join(temp))

    adjacency_graph = defaultdict(set)
    queue = deque([(s1, 0)])
    visited = {s1}
    while queue:
        current_string, distance = queue.popleft()
        if current_string == s2:
            return distance
        add_to_adjacency_graph(current_string)
        for adjacent in adjacency_graph[current_string]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append((adjacent, distance + 1))
    return -1


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    def build_graph():
        graph = defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                temp = word[:i] + "*" + word[i + 1:]
                graph[temp].append(word)
                graph[word].append(temp)
        return graph

    graph = build_graph()

    queue = deque([(0, beginWord)])
    visited = {beginWord}
    while queue:
        distance, word = queue.popleft()
        if word == endWord:
            return (distance // 2) + 1
        for adjacent in graph[word]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append((distance + 1, adjacent))
    return 0


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    in_degree, graph, visited = defaultdict(int), defaultdict(list), set()

    def build_graph_calculate_degree():
        for destination, origin in prerequisites:
            graph[origin].append(destination)
            if origin not in in_degree:
                in_degree[origin] = 0
            in_degree[destination] += 1

    build_graph_calculate_degree()

    queue = deque([])
    for key, value in in_degree.items():
        if value == 0:
            queue.append(key)

    while queue:
        node = queue.popleft()
        visited.add(node)
        for adjacent in graph[node]:
            in_degree[adjacent] -= 1
            if not in_degree[adjacent]:
                queue.append(adjacent)
    return len(visited) == numCourses


def minimumCost(n: int, connections: List[List[int]]) -> int:
    parents = [i for i in range(n + 1)]
    rank = [1 for _ in range(n + 1)]

    def union(x, y):
        parent_x, parent_y = find(x), find(y)
        if parent_x == parent_y:
            return False
        rank_x, rank_y = rank[parent_x], rank[parent_y]
        if rank_x > rank_y:
            parents[parent_y] = parent_x
        elif rank_x < rank_y:
            parents[parent_x] = parent_y
        else:
            parents[parent_y] = parent_x
            rank[x] += 1
        return True

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    connections.sort(key=lambda x: x[2])
    result = 0
    total_edges = 0
    for origin, destination, weight in connections:
        if union(origin, destination):
            result += weight
            total_edges += 1

    return result if total_edges == n - 1 else -1


def half_prereq(prerequisites):
    graph, in_degree, queue, ordering = defaultdict(list), defaultdict(int), deque([]), []

    def build_graph_calculate_degree():
        for before, after in prerequisites:
            if before not in in_degree:
                in_degree[before] = 0
            in_degree[after] += 1
            graph[before].append(after)

    build_graph_calculate_degree()
    for key, value in in_degree.items():
        if value == 0:
            queue.append(key)

    while queue:
        course = queue.popleft()
        ordering.append(course)
        for adjacent in graph[course]:
            in_degree[adjacent] -= 1
            if not in_degree[adjacent]:
                queue.append(adjacent)

    return ordering[len(ordering) // 2 - 1] if len(ordering) % 2 == 0 else ordering[len(ordering) // 2]


def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    graph, in_degree = defaultdict(list), defaultdict(int)
    ordering = {}
    queue = deque([])

    def build_graph_and_in_degree():
        for before, after in prerequisites:
            if before not in in_degree:
                in_degree[before] = 0
            in_degree[after] += 1
            graph[before].append(after)

    build_graph_and_in_degree()

    for key, value in in_degree.items():
        if value == 0:
            queue.append((0, key))

    while queue:
        order, node = queue.popleft()
        ordering[node] = order
        for adjacent in graph[node]:
            in_degree[adjacent] -= 1
            if not in_degree[adjacent]:
                queue.append((order + 1, adjacent))

    result = []
    for x, y in queries:
        result.append(ordering[x] < ordering[y]) if x in ordering and y in ordering else result.append(False)
    return result


def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    graph = defaultdict(list)

    def build_graph():
        for u, v, distance in edges:
            if distance <= distanceThreshold:
                graph[u].append((v, distance))
                graph[v].append((u, distance))

    def traverse_bfs(node):
        heap = []
        heapq.heappush(heap, (distanceThreshold * -1, node))
        count = 0
        visited = set()
        while heap:
            neg_remaining_distance, node = heapq.heappop(heap)
            remaining_distance = neg_remaining_distance * -1

            if node not in visited:
                visited.add(node)
                count += 1

                for neighbor, distance in graph[node]:
                    if neighbor not in visited and remaining_distance - distance >= 0:
                        heapq.heappush(heap, ((remaining_distance - distance) * -1, neighbor))
        return count - 1

    build_graph()

    max_num_cities = float('inf')
    result = None

    for index in range(n):
        num_cities = traverse_bfs(index)
        if num_cities <= max_num_cities:
            result = index
            max_num_cities = num_cities
    return result


def makeConnected(n: int, connections: List[List[int]]) -> int:
    parents, rank = [i for i in range(n)], [1 for _ in range(n)]

    def union(node_origin, node_destination):
        parent_origin, parent_destination = find(node_origin), find(node_destination)
        if parent_origin == parent_destination:
            return False
        rank_origin, rank_destination = rank[parent_origin], rank[parent_destination]
        if rank_origin > rank_destination:
            parents[parent_destination] = parent_origin
        elif rank_origin < rank_destination:
            parents[parent_origin] = parent_destination
        else:
            parents[parent_destination] = parent_origin
            rank[parent_destination] += 1
        return True

    def find(node_index):
        if parents[node_index] != node_index:
            parents[node_index] = find(parents[node_index])
        return parents[node_index]

    number_redundant = 0

    for origin, destination in connections:
        if not union(origin, destination):
            number_redundant += 1

    for i in range(n):
        find(i)

    number_of_required = len(set(parents)) - 1

    return -1 if number_of_required > number_redundant else number_of_required


def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    graph = defaultdict(list)
    for (origin, destination), weight in zip(edges, succProb):
        graph[origin].append((weight, destination))
        graph[destination].append((weight, origin))

    queue = [(-1, start)]
    visited = set()
    while queue:
        probability, node_index = heapq.heappop(queue)
        if node_index == end:
            return -probability
        if node_index not in visited:
            visited.add(node_index)
            for weight, adjacent in graph[node_index]:
                if adjacent not in visited:
                    heapq.heappush(queue, (probability * weight, adjacent))
    return 0.0
