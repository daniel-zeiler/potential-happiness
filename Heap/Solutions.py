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


class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def rebalance(self):
        if len(self.min_heap) - len(self.max_heap) == 2:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.min_heap) - len(self.max_heap) == -2:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def addNum(self, num):
        if len(self.min_heap) == 0 or num <= -self.min_heap[0]:
            heapq.heappush(self.min_heap, -num)
        else:
            heapq.heappush(self.max_heap, num)

        self.rebalance()

    def findMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            return (self.max_heap[0] - self.min_heap[0]) / 2.0
        return -float(self.min_heap[0]) if len(self.min_heap) > len(self.max_heap) else float(self.max_heap[0])
