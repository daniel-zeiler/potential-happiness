import heapq
import math


def findMaxProduct(arr):
    result = [-1 for _ in range(len(arr))]
    max_heap = []
    for i, num in enumerate(arr):
        heapq.heappush(max_heap, -num)
        if i >= 2:
            result[i] = math.prod([-x for x in heapq.nsmallest(3, max_heap)])
    return result
