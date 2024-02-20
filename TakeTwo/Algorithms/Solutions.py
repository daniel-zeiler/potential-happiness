from collections import defaultdict, deque


def bidirectional_bfs(edges, source, target):
    def build_graph():
        graph = defaultdict(list)
        for origin, destination in edges:
            graph[origin].append(destination)
            graph[destination].append(origin)
        return graph

    graph = build_graph()
    origin_deque = deque([[0, source]])
    destination_deque = deque([[0, target]])
    visited_origin = defaultdict(int)
    visited_destination = defaultdict(int)

    while origin_deque and destination_deque:
        if origin_deque:
            distance, origin = origin_deque.popleft()
            if origin in visited_destination:
                return distance + visited_destination[origin]
            visited_origin[origin] = distance
            for adjacent in graph[origin]:
                if adjacent not in visited_origin:
                    origin_deque.append([distance + 1, adjacent])

        if destination_deque:
            distance, destination = destination_deque.popleft()
            if destination in visited_origin:
                return distance + visited_origin[destination]
            visited_destination[destination] = distance
            for adjacent in graph[destination]:
                if adjacent not in visited_destination:
                    destination_deque.append([distance + 1, adjacent])
    return -1


def binary_search(input_list, target):
    def bin_search(low, high):
        if low > high:
            return -1

        mid = (low + high) // 2
        mid_value = input_list[mid]
        if mid_value == target:
            return mid
        return bin_search(low, mid - 1) if mid_value > target else bin_search(mid + 1, high)

    return bin_search(0, len(input_list) - 1)


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid_pointer = int(len(nums) / 2)
    left, right = merge_sort(nums[:mid_pointer]), merge_sort(nums[mid_pointer:])

    left_pointer, right_pointer, result = 0, 0, []

    while left_pointer < len(left) and right_pointer < len(right):
        left_val, right_val = left[left_pointer], right[right_pointer]
        if left_val < right_val:
            result.append(left_val)
            left_pointer += 1
        else:
            result.append(right_val)
            right_pointer += 1

    result.extend(left[left_pointer:] + right[right_pointer:])
    return result


