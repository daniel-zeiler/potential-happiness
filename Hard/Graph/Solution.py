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
