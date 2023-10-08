import collections
import heapq
from typing import List


def find_town_judge(n: int, trust: List[List[int]]) -> int:
    in_degree = {i + 1: 0 for i in range(n)}
    out_degree = {i + 1 for i in range(n)}

    for origin, destionatin in trust:
        if origin in out_degree:
            out_degree.remove(origin)
        in_degree[destionatin] += 1

    if len(out_degree) == 1:
        candidate = list(out_degree)[0]
        if in_degree[candidate] == n - 1:
            return candidate
    return -1


def all_paths_source_to_target(graph):
    result = []
    last_position = len(graph) - 1

    def traverse(position, path_so_far):
        if position == last_position:
            result.append(path_so_far)
        else:
            for adjacent in graph[position]:
                traverse(adjacent, path_so_far + [adjacent])

    traverse(0, [0])
    return result


def minimum_vertices_reach_all_nodes(n: int, edges: List[List[int]]) -> List[int]:
    out_degree = {i: 0 for i in range(n)}
    for origin, destination in edges:
        out_degree[origin] += 1
    return [x[0] for x in filter(lambda x: x[1] == 0, out_degree.items())]


def keys_and_rooms(rooms: List[List[int]]) -> bool:
    num_rooms = len(rooms)
    visited = set()

    def depth_first_search(position):
        visited.add(position)
        if len(visited) == num_rooms:
            return True
        for adjacent in rooms[position]:
            if adjacent not in visited and depth_first_search(adjacent):
                return True
        return False

    return depth_first_search(0)


def number_of_provinces(is_connected):
    parents = [i for i in range(len(is_connected))]

    def find(node):

        node_parent = parents[node]
        while node_parent != parents[node_parent]:
            node_parent = parents[node_parent]
        return node_parent

    def union(origin, destination):
        origin_parent = find(origin)
        destination_parent = find(destination)
        if origin_parent == destination_parent:
            return False
        parents[origin_parent] = destination_parent
        return True

    result = len(parents)
    for origin, row in enumerate(is_connected):
        for destination, value in enumerate(row):
            if value == 1:
                if union(origin, destination):
                    result -= 1

    return result


def redundant_connections(edges):
    parents = [i for i in range(0, len(edges) + 1)]

    def find(node):
        if node == parents[node]:
            return node
        return find(parents[node])

    def union(origin, destination):
        origin_parent = find(origin)
        destination_parent = find(destination)
        if origin_parent == destination_parent:
            return False
        parents[origin_parent] = destination_parent
        return True

    result = []
    for origin, destination in edges:
        if not union(origin, destination):
            result = [origin, destination]
    return result


def maximal_network_rank(n, roads):
    graph = [set() for _ in range(n)]
    for city_a, city_b in roads:
        graph[city_a].add(city_b)
        graph[city_b].add(city_a)

    result = 0

    for i in range(n):
        for j in range(i + 1, n):
            rank = len(graph[i]) + len(graph[j])
            if i in graph[j]:
                rank -= 1
            result = max(result, rank)
    return result


"""
The purpose here is to traverse -- if we reach a loop in the traversal it's false.  Else we continue traversing
till we reach our 
"""


def find_eventual_safe_nodes(graph):
    unsafe_set = set()
    safe_set = set()

    def traverse(position, visited):
        if position in unsafe_set or position in visited:
            return False
        elif position in safe_set or not graph[position]:
            return True
        if all([traverse(x, visited | {position}) for x in graph[position]]):
            return True
        return False

    for n in range(len(graph)):
        if n not in unsafe_set:
            if traverse(n, set()):
                safe_set.add(n)
            else:
                unsafe_set.add(n)
    return list(safe_set).sort()


"""
We're going to do dfs from a given node.  Then we'll traverse all the nodes while maintaining a visited set.  
If that nodes been visited and a visited neighbor has the same color, return false.
"""


def is_graph_bipartite(graph):
    visited = collections.defaultdict(int)

    def check_adjacent(adjacent, color):
        if adjacent in visited:
            return visited[adjacent] != color
        return traverse(adjacent, not color)

    def traverse(node, color):
        visited[node] = color
        return all([check_adjacent(adjacent, color) for adjacent in graph[node]])

    return all([traverse(node, True) if node not in visited else True for node in range(len(graph))])


def flower_planting_no_adjacent(n, paths):
    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination in paths:
            graph[origin].append(destination)
            graph[destination].append(origin)
        return graph

    graph = get_graph()
    colors = {1, 2, 3, 4}
    visited = collections.defaultdict(int)

    def gather_color(node):
        adjacent_colors = set()
        for adjacent in graph[node]:
            if adjacent in visited:
                adjacent_colors.add(visited[adjacent])
        return list(colors.difference(adjacent_colors))[0]

    def traverse(node):
        visited[node] = gather_color(node)
        for adjacent in graph[node]:
            if adjacent not in visited:
                traverse(adjacent)

    for i in range(1, n + 1):
        if i not in visited:
            traverse(i)

    return list(visited.values())


def network_delay_time(times, n, k):
    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination, weight in times:
            graph[origin].append([destination, weight])
        return graph

    graph = get_graph()
    visited = set()
    queue = [[0, k]]
    max_network_delay = 0
    while queue:
        weight, node = heapq.heappop(queue)
        if node not in visited:
            max_network_delay = weight
            visited.add(node)
            for adjacent, adjacent_weight in graph[node]:
                if adjacent not in visited:
                    heapq.heappush(queue, [weight + adjacent_weight, adjacent])

    if len(visited) == n:
        return max_network_delay
    return -1


def possible_bipartition(n, dislikes):
    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination in dislikes:
            graph[origin].append(destination)
        return graph

    graph = get_graph()
    visited = collections.defaultdict(bool)

    def check_adjacent(adjacent, color):
        if adjacent in visited:
            return visited[adjacent] != color
        return traverse(adjacent, not color)

    def traverse(node, color):
        visited[node] = color
        return all([check_adjacent(adjacent, color) for adjacent in graph[node]])

    return all([traverse(x, True) if x not in visited else True for x in range(1, n + 1)])


def course_schedule_two(numCourses, prerequisites):
    def get_graph():
        graph = collections.defaultdict(list)
        for destination, origin in prerequisites:
            graph[origin].append(destination)
        return graph

    result = []
    visited = {}
    graph = get_graph()
    is_cycle = False

    def topo_sort(node):
        visited[node] = 1
        for adjacent in graph[node]:
            if adjacent not in visited:
                topo_sort(adjacent)
            elif visited[adjacent] == 1:
                nonlocal is_cycle
                is_cycle = True
        visited[node] = 2
        result.append(node)

    for i in range(numCourses):
        if i not in visited:
            topo_sort(i)
            if is_cycle:
                return []
    return result[::-1]


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    def get_graph():
        graph = collections.defaultdict(list)
        for i, (numerator, denominator) in enumerate(equations):
            graph[numerator].append([values[i], denominator])
            graph[denominator].append([1 / values[i], numerator])
        return graph

    graph = get_graph()
    result = []

    def traverse(node, destination_node, cumulative_weight, visited):
        if node == destination_node:
            return cumulative_weight
        for weight, adjacent in graph[node]:
            if adjacent not in visited:
                result = traverse(adjacent, destination_node, cumulative_weight * weight, visited | {adjacent})
                if result != -1:
                    return result
        return -1

    for numerator, denominator in queries:
        if numerator not in graph or denominator not in graph:
            result.append(-1.0)
        else:
            result.append(float(traverse(numerator, denominator, 1, {numerator})))
    return result


# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def getImportance(employees: List['Employee'], id: int) -> int:
    def get_graph():
        graph = collections.defaultdict(list)
        for employee in employees:
            graph[employee.id] = [employee.importance, employee.subordinates]
        return graph

    graph = get_graph()

    queue = collections.deque([id])
    visited = set()
    importance = 0

    while queue:
        node = queue.popleft()
        if node not in visited:
            importance += graph[node][0]
            visited.add(node)
            for adjacent in graph[node][1]:
                if adjacent not in visited:
                    queue.append(adjacent)
    return importance


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    def get_graph():
        graph = collections.defaultdict(list)
        for i, word in enumerate(wordList):
            for j, compare in enumerate(wordList[i + 1:]):
                for i, (char_word, char_compare) in enumerate(zip(word, compare)):
                    if char_word != char_compare:
                        if word[i + 1:] == compare[i + 1:]:
                            graph[word].append(compare)
                            graph[compare].append(word)
                        break

        return graph

    wordList.append(beginWord)
    graph = get_graph()
    visited = set()
    queue = collections.deque([[1, beginWord]])

    while queue:
        distance, word = queue.popleft()
        if word == endWord:
            return distance
        if word not in visited:
            visited.add(word)
            for adjacent in graph[word]:
                if adjacent not in visited:
                    queue.append([distance + 1, adjacent])

    return -1


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    topo_sort = []

    def get_in_degree_and_graph():
        in_degree = {i: 0 for i in range(numCourses)}
        graph = collections.defaultdict(list)
        for destination, origin in prerequisites:
            in_degree[destination] += 1
            graph[origin].append(destination)
        return in_degree, graph

    in_degree, graph = get_in_degree_and_graph()
    queue = collections.deque([])

    for key, value in in_degree.items():
        if value == 0:
            queue.append(key)

    while queue:
        node_id = queue.popleft()
        topo_sort.append(node_id)
        for adjacent in graph[node_id]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                queue.append(adjacent)

    return len(topo_sort) == numCourses
