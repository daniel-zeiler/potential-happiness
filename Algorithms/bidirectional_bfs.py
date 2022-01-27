import collections


def bidirection_bfs():
    queue_one = collections.deque([])
    queue_two = collections.deque([])
    visited_one = {node_id: 0 for node_id, distance in list(queue_one)}
    visited_two = {node_id: 0 for node_id, distance in list(queue_two)}
    graph = {}

    while queue_one and queue_two:
        distance, node = queue_one.popleft()
        visited_one[node] = distance
        if node in visited_two:
            return distance + visited_two[node]
        for adjacent in graph[node]:
            if adjacent not in visited_one:
                queue_one.append([distance + 1, adjacent])

        distance, node = queue_two.popleft()
        visited_two[node] = distance
        if node in visited_one:
            return distance + visited_one[node]
        for adjacent in graph[node]:
            if adjacent not in visited_two:
                queue_two.append([distance + 1, adjacent])

    return -1
