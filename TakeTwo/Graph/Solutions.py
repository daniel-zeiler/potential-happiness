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
    def build_graph():
        graph = collections.defaultdict(list)
        for [origin, destination], value in zip(equations, values):
            graph[origin].append((destination, value))
            graph[destination].append((origin, 1 / value))
        return graph

    graph = build_graph()

    def traverse(index: str, target: str, visited: set, curr_value: float) -> float:
        if index not in graph:
            return -1.0
        if index == target:
            return curr_value
        for adjacent, multiple in graph[index]:
            if adjacent not in visited:
                result = traverse(adjacent, target, visited | set(adjacent), curr_value * multiple)
                if result != -1:
                    return result
        return -1.0

    return [traverse(query[0], query[1], set(query[0]), 1.0) for query in queries]


def numBusesToDestination(routes: List[List[int]], source: int, target: int) -> int:
    def build_graph():
        graph_stops, graph_buses = collections.defaultdict(list), collections.defaultdict(list)
        for i, route in enumerate(routes):
            for r in route:
                graph_stops[r].append(i)
                graph_buses[i].append(r)
        return graph_stops, graph_buses

    graph_stops, graph_buses = build_graph()

    def traverse_distance(position: int, destination: int, visited_buses: set, visited_stops: set, at_bus: bool):
        if position == destination and not at_bus:
            return 1

        if at_bus:
            visited, graph = visited_stops, graph_buses
        else:
            visited, graph = visited_buses, graph_stops

        for adjacent in graph[position]:
            if adjacent not in visited:
                visited.add(adjacent)

                distance = traverse_distance(adjacent, destination, visited_buses, visited_stops, not at_bus)
                if distance != -1:
                    return distance + 1

                if at_bus:
                    visited_stops.remove(adjacent)
                else:
                    visited_buses.remove(adjacent)

        return -1

    distance = traverse_distance(source, target, set(), {source}, False)
    return int(distance / 2) if distance != -1 else distance


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def getImportance(employees: List['Employee'], id: int) -> int:
    def traverse(employee: Employee):
        return (employee.importance +
                sum([traverse(employees[subordinate - 1]) for subordinate in employee.subordinates]))

    for employee in employees:
        if id == employee.id:
            return traverse(employee)
    return -1


def kSimilarity(s1: str, s2: str) -> int:
    def get_adjacent(input_string: str) -> List[str]:
        result = []
        for x in range(len(input_string)):
            for y in range(x + 1, len(input_string)):
                tmp = list(input_string)
                tmp[x], tmp[y] = tmp[y], tmp[x]
                result.append("".join(tmp))
        return result

    queue = collections.deque([(0, s1)])
    visited = {s1}
    while queue:
        distance, string = queue.popleft()
        if string == s2:
            return distance
        for adjacent in get_adjacent(string):
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append((distance + 1, adjacent))

    return -1


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    def build_graph():
        graph = collections.defaultdict(list)
        for word in wordList + [beginWord]:
            for x in range(len(word)):
                connecting_word = word[:x] + '*' + word[x + 1:]
                graph[connecting_word].append(word)
                graph[word].append(connecting_word)
        return graph

    if endWord not in wordList:
        return 0
    visited, graph, queue = {beginWord}, build_graph(), collections.deque([(1, beginWord)])
    while queue:
        distance, word = queue.popleft()
        if word == endWord:
            return int(distance / 2) + 1
        for adjacent in graph[word]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append((distance + 1, adjacent))
    return 0


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    def build_graph_and_degree() -> {dict, dict}:
        in_degree = {i: 0 for i in range(numCourses)}
        graph = collections.defaultdict(list)
        for after, prereq in prerequisites:
            in_degree[after] += 1
            graph[prereq].append(after)
        return in_degree, graph

    in_degree, graph = build_graph_and_degree()
    queue = collections.deque([])
    for key, degree in in_degree.items():
        if degree == 0:
            queue.append(key)

    while queue:
        node = queue.popleft()
        for adjacent in graph[node]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                queue.append(adjacent)

    return sum(in_degree.values()) == 0


import heapq


def minimumCost(n: int, connections: List[List[int]]) -> int:
    def get_graph() -> dict:
        graph = collections.defaultdict(list)
        for origin, destination, weight in connections:
            graph[origin].append((weight, destination))
            graph[destination].append((weight, origin))
        return graph

    graph = get_graph()
    queue = [(0, connections[0][0])]
    visited = set()
    total_weight = 0
    while queue:
        weight, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            total_weight += weight
            if len(visited) == n:
                return total_weight
            for weight, adjacent in graph[node]:
                if adjacent not in visited:
                    heapq.heappush(queue, (weight, adjacent))
    return -1


def currency_exchange(currency_one, currency_two, data):
    def build_graph() -> dict:
        graph = collections.defaultdict(list)
        for origin, destination, ask, bid in data:
            graph[origin].append((bid, destination))
            graph[destination].append((ask, origin))
        return graph

    graph = build_graph()
    if currency_one not in graph or currency_two not in graph:
        return -1

    queue = [(1, currency_one)]
    visited = set()
    while queue:
        rate, currency = heapq.heappop(queue)
        if currency not in visited:
            visited.add(currency)
            if currency == currency_two:
                return rate
            for adjacent_rate, adjacent in graph[currency]:
                if adjacent not in visited:
                    heapq.heappush(queue, (rate * adjacent_rate, adjacent))
    return -1


def half_prereq(prerequisites):
    def build_graph_and_degree():
        graph, in_degree = collections.defaultdict(list), collections.defaultdict(int)
        for prereq, course in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
            if prereq not in in_degree:
                in_degree[prereq] = 0
        return graph, in_degree

    graph, in_degree = build_graph_and_degree()
    queue, order = collections.deque([]), []

    for key, value in in_degree.items():
        if value == 0:
            queue.append(key)

    while queue:
        class_name = queue.popleft()
        order.append(class_name)
        for adjacent in graph[class_name]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                queue.append(adjacent)

    return order[len(order) // 2 - 1] if len(order) % 2 == 0 else order[len(order) // 2]


def countPaths(n: int, roads: List[List[int]]) -> int:
    min_distance = float('inf')
    count_at_min_distance = 0

    def build_graph():
        graph = collections.defaultdict(list)
        for origin, destination, weight in roads:
            graph[origin].append((destination, weight))
            graph[destination].append((origin, weight))
        return graph

    graph = build_graph()

    def traverse(index, distance, visited):
        nonlocal min_distance, count_at_min_distance
        if index == n - 1:
            if distance < min_distance:
                count_at_min_distance = 1
                min_distance = distance
            elif distance == min_distance:
                count_at_min_distance += 1
        else:
            for adjacent, weight in graph[index]:
                if adjacent not in visited:
                    traverse(adjacent, distance + weight, visited | {adjacent})

    traverse(0, 0, set())
    return count_at_min_distance


def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    def build_graph_and_degree() -> {dict, dict}:
        graph, in_degree = collections.defaultdict(list), {i: 0 for i in range(numCourses)}
        for before, after in prerequisites:
            graph[before].append(after)
            in_degree[after] += 1
        return graph, in_degree

    graph, in_degree = build_graph_and_degree()
    prereq_dictionary, queue = collections.defaultdict(set), collections.deque([])
    for node, degree in in_degree.items():
        if degree == 0:
            queue.append(node)

    while queue:
        node = queue.popleft()
        for adjacent in graph[node]:
            prereq_dictionary[adjacent].add(node)
            prereq_dictionary[adjacent].update(prereq_dictionary[node])
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                queue.append(adjacent)

    return [origin in prereq_dictionary[destination] for origin, destination in queries]


import heapq


def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    def build_graph():
        graph = collections.defaultdict(set)
        for u, v, distance in edges:
            if distance <= distanceThreshold:
                graph[u].add((v, distance))
                graph[v].add((u, distance))
        return graph

    def traverse_bfs(node):
        heap = []
        # bound by distanceThreshold
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
                    if neighbor not in visited and remaining_distance >= 0:
                        heapq.heappush(heap, ((remaining_distance - distance) * -1, neighbor))
        return count - 1

    graph = build_graph()
    min_count, ans = float('inf'), -1

    for source in range(n):
        count = traverse_bfs(source)
        if count <= min_count:
            min_count = count
            ans = source
    return ans


def makeConnected(n: int, connections: List[List[int]]) -> int:
    parents = [i for i in range(n)]
    rank = [1 for _ in range(n)]

    def union(node_origin, node_destination):
        parent_origin = find(node_origin)
        parent_destination = find(node_destination)
        if parent_origin == parent_destination:
            return False
        rank_origin = rank[parent_origin]
        rank_destination = rank[parent_destination]
        if rank_origin > rank_destination:
            rank[parent_origin] += rank_destination
            parents[parent_origin] = parent_destination
        else:
            rank[parent_destination] += rank_origin
            parents[parent_destination] = parent_origin
        return True

    def find(node):
        if parents[node] == node:
            return node
        parents[node] = find(parents[node])
        return parents[node]

    num_redundant_connections = 0

    for origin, destination in connections:
        if not union(origin, destination):
            num_redundant_connections += 1

    for i in range(n):
        find(i)

    num_groups = len(set(parents))
    if num_groups > num_redundant_connections + 1:
        return -1
    return num_groups - 1


def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    def build_graph():
        graph = collections.defaultdict(list)
        for (origin, destination), probability in zip(edges, succProb):
            graph[origin].append((probability, destination))
            graph[destination].append((probability, origin))
        return graph

    def traverse_dfs(node, visited, weight):
        if node == end:
            return weight
        prob = 0.0

        for adjacent_weight, adjacent_node in graph[node]:
            if adjacent_node not in visited:
                prob = max(prob, traverse_dfs(adjacent_node, visited | {adjacent_node}, weight * adjacent_weight))

        return prob

    graph = build_graph()
    return traverse_dfs(start, {start}, 1)


def shortestAlternatingPaths(n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    def build_graphs(edges):
        graph = collections.defaultdict(list)
        for origin, destination in edges:
            graph[origin].append(destination)
        return graph

    red_graph, blue_graph = build_graphs(redEdges), build_graphs(blueEdges)

    result = [-1 for _ in range(n)]

    def traverse(node, distance, visited, blue_is_next):
        result[node] = distance if result[node] == -1 else min(distance, result[node])

        graph = blue_graph if blue_is_next else red_graph

        for adjacent in list(filter(lambda x: x not in visited, graph[node])):
            traverse(adjacent, distance + 1, visited | {adjacent}, not blue_is_next)

    traverse(0, 0, {0}, True)
    traverse(0, 0, {0}, False)
    return result


from collections import defaultdict


def loudAndRich(richer: List[List[int]], quiet: List[int]) -> List[int]:
    result = [None for _ in range(len(quiet))]

    def build_graph():
        graph = defaultdict(list)
        for origin, destination in richer:
            graph[destination].append(origin)
        return graph

    def traverse(node) -> (int, int):
        quietest, minimum_quiet_node = quiet[node], node
        for adjacent in graph[node]:
            if result[adjacent] is None:
                quiet_node, quiet_level = traverse(adjacent)
            else:
                quiet_node, quiet_level = result[adjacent], quiet[result[adjacent]]
            if quiet_level < quietest:
                quietest, minimum_quiet_node = quiet_level, quiet_node

        result[node] = minimum_quiet_node
        return minimum_quiet_node, quietest

    graph = build_graph()

    for i in range(len(quiet)):
        if result[i] is None:
            traverse(i)
    return result


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    def build_graph():
        graph = defaultdict(list)
        for origin, destination, price in flights:
            graph[origin].append((destination, price))
        return graph

    graph = build_graph()
    visited = set()
    queue = [(0, src, 0)]

    while queue:
        total_cost, node, total_distance = heapq.heappop(queue)
        if node not in visited and total_distance - 1 <= k:
            visited.add(node)
            if node == dst:
                return total_cost
            for adjacent, cost in graph[node]:
                if adjacent not in visited:
                    heapq.heappush(queue, (total_cost + cost, adjacent, total_distance + 1))
    return -1


def minCostConnectPoints(points: List[List[int]]) -> int:
    def calcuate_distance(point_one, point_two):
        return abs(point_one[0] - point_two[0]) + abs(point_one[1] - point_two[1])

    parents = [i for i in range(len(points))]
    rank = [0 for _ in range(len(points))]

    def union(origin, destination):
        parent_origin = find(origin)
        parent_destination = find(destination)
        if parent_origin == parent_destination:
            return False
        rank_origin = rank[parent_origin]
        rank_destination = rank[parent_destination]
        if rank_origin < rank_destination:
            parents[parent_origin] = parent_destination
            rank[parent_origin] += rank_destination
        else:
            parents[parent_destination] = parent_origin
            rank[parent_destination] += rank_origin
        return True

    def find(node):
        if parents[node] != node:
            parents[node] = find(parents[node])
        return parents[node]

    distances = []
    for x in range(len(points)):
        for y in range(x + 1, len(points)):
            distance = calcuate_distance(points[x], points[y])
            heapq.heappush(distances, (distance, x, y))

    result = 0
    while distances:
        distance, origin, destination = heapq.heappop(distances)
        if union(origin, destination):
            result += distance
    return result
