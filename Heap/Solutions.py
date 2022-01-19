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


def number_of_cabs(n, cabTravelTime):
    a_heap = []
    current_time = 0
    total_trips = 0
    for travel_time in cabTravelTime:
        heapq.heappush(a_heap, [travel_time, travel_time])

    while total_trips < n:
        current_time += 1
        while total_trips < n and a_heap[0][0] == current_time:
            time_taken, travel_time = heapq.heappop(a_heap)
            total_trips += 1
            heapq.heappush(a_heap, [time_taken + travel_time, travel_time])

    return current_time
