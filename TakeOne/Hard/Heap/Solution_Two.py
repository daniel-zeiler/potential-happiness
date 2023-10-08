# Definition for an Interval.
import heapq


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


def employeeFreeTime(schedule: '[[Interval]]') -> '[Interval]':
    heap = []
    for a_schedule in schedule:
        for interval in a_schedule:
            heapq.heappush(heap, [interval.start, interval.end])
    result = []
    merged = []
    while heap:
        if not merged:
            merged.append(heapq.heappop(heap))
        elif heap[0][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], heapq.heappop(heap)[1])
        else:
            result.append(Interval(merged[-1][1], heap[0][0]))
            merged.append(heapq.heappop(heap))
    return result
