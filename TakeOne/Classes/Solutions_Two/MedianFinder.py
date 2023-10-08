import heapq


class MedianFinder:
    def __init__(self):
        self.lower_heap = []
        self.upper_heap = []

    def get_median(self):
        if len(self.lower_heap) == len(self.upper_heap):
            return (-self.lower_heap[0] + self.upper_heap[0]) / 2
        elif len(self.lower_heap) > len(self.upper_heap):
            return -self.lower_heap[0]
        return self.upper_heap[0]

    def rebalance(self):
        if len(self.lower_heap) - len(self.upper_heap) >= 2:
            heapq.heappush(self.upper_heap, -heapq.heappop(self.lower_heap))
        elif len(self.upper_heap) - len(self.lower_heap) >= 2:
            heapq.heappush(self.lower_heap, -heapq.heappop(self.upper_heap))

    def add_value(self, value):
        if len(self.upper_heap) == 0 or value < self.upper_heap[0]:
            heapq.heappush(self.lower_heap, -value)
        else:
            heapq.heappush(self.upper_heap, value)
        self.rebalance()


median_finder = MedianFinder()
for i in range(100):
    median_finder.add_value(i)
    print(median_finder.get_median())
    print(median_finder.lower_heap)
    print(median_finder.upper_heap)
    print('~~~~~~~~~~~~~~~~~')
