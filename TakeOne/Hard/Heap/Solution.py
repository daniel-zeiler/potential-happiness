import heapq


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


def employeeFreeTime(schedule: '[[Interval]]') -> '[Interval]':
    heap = []
    for a_schedule in schedule:
        for an_interval in a_schedule:
            heapq.heappush(heap, [an_interval.start, an_interval.end])

    merge = []
    interval = heapq.heappop(heap)
    while heap:
        next_interval = heapq.heappop(heap)
        if next_interval[0] <= interval[1]:
            interval[1] = max(next_interval[1], interval[1])
            continue
        merge.append(Interval(interval[1], next_interval[0]))
        interval[1] = max(next_interval[1], interval[1])
    return merge
