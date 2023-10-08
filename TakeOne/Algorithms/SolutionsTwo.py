import collections


def binary_search(input, target):
    def search(low, high):
        if low > high:
            return False
        mid_point = high - low // 2
        value = input[mid_point]
        if value == target:
            return True
        elif value > target:
            return search(low, mid_point - 1)
        else:
            return search(mid_point + 1, high)

    return search(0, len(input) - 1)


input = [1, 2, 3, 7, 11]
print(binary_search(input, 11))
print(binary_search(input, 1))
print(binary_search(input, -100))


def bidirectional_bfs(edges, source, target):
    def get_graph():
        graph = collections.defaultdict(list)
        for origin, destination in edges:
            graph[origin].append(destination)
            graph[destination].append(origin)
        return graph

    graph = get_graph()
    queue_source = collections.deque([[source, 0]])
    queue_target = collections.deque([[target, 0]])

    source_visited = {source: 0}
    target_visited = {target: 0}

    while queue_source and queue_target:
        node, distance = queue_source.popleft()
        if node in target_visited:
            return distance + target_visited[node]
        for adjacent in graph[node]:
            source_visited[adjacent] = distance + 1
            queue_source.append([adjacent, distance + 1])

        node, distance = queue_target.popleft()
        if node in source_visited:
            return distance + source_visited[node]
        for adjacent in graph[node]:
            target_visited[adjacent] = distance + 1
            queue_target.append([adjacent, distance + 1])

    return -1
