import collections


class EventObject:
    def __init__(self, time, event):
        self.time = time
        self.event = event


def binary_search_bisect_left(array, value):
    def recursive_binary_search_bisect_left(low, high):
        mid = (high + low) // 2
        if low > high:
            return low
        if array[mid].time < value:
            return recursive_binary_search_bisect_left(mid + 1, high)
        return recursive_binary_search_bisect_left(low, mid - 1)

    return recursive_binary_search_bisect_left(0, len(array) - 1)


def binary_search_bisect_right(array, value):
    def recursive_binary_search_bisect_right(low, high):
        if low >= high:
            return low
        mid = (high + low) // 2
        if array[mid].time <= value:
            return recursive_binary_search_bisect_right(mid + 1, high)
        else:
            return recursive_binary_search_bisect_right(low, mid)

    return recursive_binary_search_bisect_right(0, len(array))


def binary_search(array, value):
    def recursive_binary_search(low, high):
        mid = (high + low) // 2
        if low > high:
            return -1
        if array[mid].time == value:
            return mid
        if array[mid].time < value:
            return recursive_binary_search(mid + 1, high)
        return recursive_binary_search(low, mid - 1)

    return recursive_binary_search(0, len(array) - 1)


class TimeSeriesEventCollection:
    def __init__(self):
        self.event_map = collections.defaultdict(int)
        self.events = []

    def insert(self, time, event):
        index = binary_search_bisect_left(self.events, time)
        self.events.insert(index, EventObject(time, event))
        self.event_map[time] = index
        for event_object in self.events[index + 1:]:
            self.event_map[event_object.time] += 1

    def find(self, time):
        if time in self.event_map:
            return self.events[self.event_map[time]]
        return None

    def query_range(self, start_time, end_time):
        index = binary_search_bisect_left(self.events, start_time)
        events = []
        for event_object in self.events[index]:
            if event_object.time > end_time:
                return events
            events.append(event_object.event)
        return events

    def delete(self, time):
        if time in self.event_map:
            index = self.event_map[time]
            del self.event_map[time]
            self.events.pop(index)
            for event_object in self.events[index:]:
                self.event_map[event_object.time] -= 1

    def get_in_range(self, start_time, end_time):
        start_index = binary_search_bisect_left(self.events, start_time)
        end_index = binary_search_bisect_right(self.events, end_time)
        return self.events[start_index:end_index]


event_collection = TimeSeriesEventCollection()
event_collection.insert(1, "one")
event_collection.insert(2, "two")
event_collection.insert(3, "three")
event_collection.insert(0, "zero")
event_collection.insert(-1, "negative one")
print([event.event for event in event_collection.events])
event_collection.delete(0)
print([event.event for event in event_collection.events])
print([event.event for event in event_collection.get_in_range(-1000, 2000)])
