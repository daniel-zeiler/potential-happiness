import collections
from typing import List


def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]:
    parents = []

    matrix = [[-1 for _ in range(n)] for _ in range(m)]

    def union(origin, destination):
        origin_parent = find(origin)
        origin_destination = find(destination)
        if origin_parent == origin_destination:
            return False
        parents[origin_parent] = origin_destination
        return True

    def find(node_index):
        if node_index != parents[node_index]:
            parent = find(parents[node_index])
            parents[node_index] = parent
            return parent
        return node_index

    result = []
    size = 0
    for x, y in positions:
        if matrix[x][y] != -1:
            result.append(size)
            continue

        size += 1
        matrix[x][y] = len(parents)
        parents.append(len(parents))
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for x_direction, y_direction in directions:
            x_target, y_target = x + x_direction, y + y_direction
            if 0 <= x_target < len(matrix) and 0 <= y_target < len(matrix[0]):
                if matrix[x_target][y_target] != -1 and union(len(parents) - 1, matrix[x_target][y_target]):
                    size -= 1

        result.append(size)
    return result


def numBusesToDestination(routes: List[List[int]], source: int, target: int) -> int:
    if source == target: return 0
    graph = collections.defaultdict(set)
    for i, r1 in enumerate(routes):
        for j in range(i + 1, len(routes)):
            r2 = routes[j]
            if any(r in r2 for r in r1):
                graph[i].add(j)
                graph[j].add(i)

    if source == target:
        return 0
    visited = set()
    targets = set()
    for bus, route in enumerate(routes):
        if target in route:
            targets.add(bus)
        if source in route:
            visited.add(bus)

    queue = collections.deque([[1, node] for node in visited])
    while queue:
        distance, current_node = queue.popleft()
        visited.add(current_node)
        if current_node in targets:
            return distance

        for adjacent in graph[current_node]:
            if adjacent not in visited:
                queue.append([distance + 1, adjacent])

    return -1
