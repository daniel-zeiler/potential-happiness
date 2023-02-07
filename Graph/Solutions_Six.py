import collections
from typing import List


def find_town_judge(n: int, trust: List[List[int]]) -> int:
    in_count = [0 for _ in range(1, n + 2)]
    out_count = [0 for _ in range(1, n + 2)]
    for origin, destination in trust:
        in_count[destination] += 1
        out_count[origin] += 1

    for i, (into, out) in enumerate(zip(in_count, out_count)):
        if out == 0 and into == n - 1:
            return i
    return -1


def all_paths_source_to_target(graph):
    def traverse(current_location, path_so_far):
        result = []
        if current_location == len(graph) - 1:
            result.append(path_so_far)
        else:
            for adjacent in graph[current_location]:
                result.extend(traverse(adjacent, path_so_far + [adjacent]))
        return result

    return traverse(0, [0])


def minimum_vertices_reach_all_nodes(n: int, edges: List[List[int]]) -> List[int]:
    result = []
    in_count = collections.defaultdict(int)
    for origin, destination in edges:
        in_count[destination] += 1
    for i in range(0, n):
        if i not in in_count:
            result.append(i)
    return result


def keys_and_rooms(rooms: List[List[int]]) -> bool:
    visited = {0}
    queue = collections.deque([0])
    while queue:
        index = queue.popleft()
        for adjacent in rooms[index]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
    return len(visited) == len(rooms)


def redundant_connections(edges):
    parents = [i for i in range(len(edges) + 1)]
    rank = [1 for _ in range(len(edges) + 1)]

    def union(origin, destination):
        origin_parent = find(origin)
        destination_parent = find(destination)
        if origin_parent == destination_parent:
            return False
        if rank[origin_parent] > rank[destination_parent]:
            rank[origin_parent] += rank[destination_parent]
            parents[destination_parent] = origin_parent
        else:
            rank[destination_parent] += rank[origin_parent]
            parents[origin_parent] = destination_parent
        return True

    def find(node):
        if parents[node] != node:
            parents[node] = find(parents[node])
        return parents[node]

    result = []
    for origin, destination in edges:
        if not union(origin, destination):
            result = [origin, destination]
    return result


def maximal_network_rank(n, roads):
    max_rank = 0

    def get_graph():
        graph = collections.defaultdict(set)
        for origin, destination in roads:
            graph[origin].add(destination)
            graph[destination].add(origin)
        return graph

    graph = get_graph()

    for i in range(0, n):
        for j in range(i + 1, n):
            rank = len(graph[i]) + len(graph[j])
            if i in graph[j]:
                rank -= 1
            max_rank = max(max_rank, rank)

    return max_rank


def find_eventual_safe_nodes(graph):
    safe_set = set()
    unsafe_set = set()

    def traverse(node_id, visited_set):
        safe = True
        for adjacent in graph[node_id]:
            if adjacent in safe_set:
                continue
            if adjacent in unsafe_set or adjacent in visited_set or not traverse(adjacent, visited_set | {node_id}):
                safe = False
        if safe:
            safe_set.add(node_id)
        else:
            unsafe_set.add(node_id)
        return safe

    for i in range(0, len(graph)):
        if i not in safe_set and i not in unsafe_set:
            traverse(i, {i})

    return list(safe_set)


def is_graph_bipartite(graph):
    color_dictionary = collections.defaultdict(bool)

    def traverse(node_id, color):
        color_dictionary[node_id] = color
        for adjacent in graph[node_id]:
            if adjacent in color_dictionary:
                if color_dictionary[adjacent] == color:
                    return False
            elif not traverse(adjacent, not color):
                return False
        return True

    for i in range(len(graph)):
        if i not in color_dictionary and not traverse(i, True):
            return False

    return True


def flower_planting_no_adjacent(n, paths):
    flower_dictionary = collections.defaultdict(int)
    potential_flowers = {1, 2, 3, 4}

    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination in paths:
            graph[origin].append(destination)
            graph[destination].append(origin)
        return graph

    def traverse(graph_index):
        adjacent_flowers = set()
        for adjacent in graph[graph_index]:
            if adjacent in flower_dictionary:
                adjacent_flowers.add(flower_dictionary[adjacent])
        flower_dictionary[graph_index] = list(potential_flowers.difference(adjacent_flowers))[0]

        for adjacent in graph[graph_index]:
            if adjacent not in flower_dictionary:
                traverse(adjacent)

    graph = get_graph()
    for i in range(1, n + 1):
        if i not in flower_dictionary:
            traverse(i)

    return [flower_dictionary[i] for i in range(1, n + 1)]


def network_delay_time(times, n, k):
    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination, time in times:
            graph[origin].append([destination, time])
        return graph

    graph = get_graph()
    visited = {k}
    queue = collections.deque([[k, 0]])
    max_time = 0
    while queue:
        node_id, total_time = queue.popleft()
        max_time = max(max_time, total_time)
        for adjacent, time in graph[node_id]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append([adjacent, time + total_time])
    if len(visited) != n:
        return -1
    return max_time


def course_schedule_two(num_courses, prerequisites):
    def get_graph():
        graph = collections.defaultdict(list)
        in_degree = {i: 0 for i in range(num_courses)}
        for destination, origin in prerequisites:
            graph[origin].append(destination)
            in_degree[destination] += 1
        return graph, in_degree

    graph, in_degree = get_graph()
    queue = collections.deque(list(filter(lambda x: in_degree[x] == 0, in_degree.keys())))
    result = []

    while queue:
        course = queue.popleft()
        result.append(course)
        for adjacent in graph[course]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                queue.append(adjacent)
    if len(result) == num_courses:
        return result
    return []


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    def get_graph():
        graph = collections.defaultdict(list)
        for equation, value in zip(equations, values):
            graph[equation[0]].append([equation[1], value])
            graph[equation[1]].append([equation[0], 1 / value])
        return graph

    def traverse(current_node, target_node, visited, value):
        if current_node == target_node:
            return value
        for adjacent, weight in graph[current_node]:
            if adjacent not in visited:
                trev_value = traverse(adjacent, target_node, visited | {adjacent}, value * weight)
                if trev_value != -1:
                    return trev_value
        return -1

    graph = get_graph()

    result = []

    for query in queries:
        if query[0] not in graph or query[1] not in graph:
            result.append(-1.0)
        else:
            result.append(float(traverse(query[0], query[1], {query[0]}, 1)))
    return result


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def getImportance(employees: List['Employee'], id: int) -> int:
    def get_graph():
        graph = collections.defaultdict(Employee)
        for employee in employees:
            graph[employee.id] = employee
        return graph

    graph = get_graph()

    def gather(current_employee):
        result = current_employee.importance
        for adjacent in current_employee.subordinates:
            result += gather(graph[adjacent])
        return result

    return gather(graph[id])


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    def get_graph():
        graph = collections.defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                link = word[:i] + "*" + word[i + 1:]
                graph[word].append(link)
                graph[link].append(word)
        return graph

    graph = get_graph()
    if beginWord not in graph or endWord not in graph:
        return 0

    queue = collections.deque([[beginWord, 2]])
    visited = {beginWord}

    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length / 2
        for adjacent in graph[word]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append([adjacent, length + 1])
    return 0


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    def get_graph():
        graph = collections.defaultdict(list)
        in_degree = {i: 0 for i in range(numCourses)}
        for destination, origin in prerequisites:
            graph[origin].append(destination)
            in_degree[destination] += 1
        return graph, in_degree

    graph, in_degree = get_graph()
    queue = collections.deque(list(filter(lambda x: in_degree[x] == 0, in_degree.keys())))
    visited = {x for x in queue}

    while queue:
        course = queue.popleft()
        for adjacent in graph[course]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                visited.add(adjacent)
                queue.append(adjacent)

    return len(visited) == numCourses


def countPaths(n: int, roads: List[List[int]]) -> int:
    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination, time in roads:
            graph[origin].append([destination, time])
            graph[destination].append([origin, time])
        return graph

    graph = get_graph()
    result_dict = collections.defaultdict(int)

    def traverse(current_node, total_time, visited):
        if current_node == n - 1:
            result_dict[total_time] += 1
        else:
            for adjacent, weight in graph[current_node]:
                if adjacent not in visited:
                    traverse(adjacent, total_time + weight, visited | {adjacent})

    traverse(0, 0, {0})
    minimum_path = float('inf')
    min_amount = 0
    for key, value in result_dict.items():
        if key < minimum_path:
            minimum_path = key
            min_amount = value
    return min_amount


def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination, distance in edges:
            graph[origin].append([destination, distance])
            graph[destination].append([origin, distance])
        return graph

    graph = get_graph()

    def traverse(current_node, threshold_remaining, visited):
        result = 1
        for adjacent, weight in graph[current_node]:
            if adjacent not in visited and threshold_remaining - weight >= 0:
                result += traverse(adjacent, threshold_remaining - weight, visited | {adjacent})
        return result

    city = 0
    min_city = float('inf')
    for i in range(n):
        num_cities = traverse(i, distanceThreshold , {i})
        print(num_cities)
        if num_cities <= min_city:
            min_city, city = num_cities, i
    return city
