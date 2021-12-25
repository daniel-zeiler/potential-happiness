import collections
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
