"""
Design and implement a data structure that allows efficient insertion and retrieval of time-based events. Each
event has a start time and an end time, and events can overlap in time. The data structure should support operations
to insert an event, delete an event, and query for all events that overlap with a given time range.
"""
import collections
import datetime


class IntervalTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.mid_point = (self.end + self.start) / 2
        self.left = None
        self.right = None


class IntervalTree:
    def __init__(self):
        self.head = None

    def insert(self, start, end):
        def recursive_insert(node):
            if not node:
                return IntervalTreeNode(start, end)
            if start <= node.mid_point:
                node.left = recursive_insert(node.left)
            else:
                node.right = recursive_insert(node.right)
            return node

        self.head = recursive_insert(self.head)

    def delete(self, start, end):
        def recursive_delete(node):
            if node:
                if node.start == start and node.end == end:
                    return node.left or node.right
                elif start <= node.mid_point:
                    node.left = recursive_delete(node.left)
                else:
                    node.right = recursive_delete(node.right)

        if self.head:
            self.head = recursive_delete(self.head)

    def query(self, start, end):
        def recursive_query(node):
            result = []
            if node:
                if node.start >= start and node.end <= end:
                    result.append([node.start, node.end])
                if node.end <= end:
                    result.extend(recursive_query(node.right))
                if node.start >= start:
                    result.extend(recursive_query(node.left))
            return result

        return recursive_query(self.head)


"""
Design and implement a data structure to store a collection of time-series data points. Each data point has a 
timestamp and a value. The data structure should support operations to insert a data point, delete a data point, 
and query for all data points within a given time range. Additionally, the data structure should support efficient 
computation of aggregate statistics over time, such as the average value per day or the maximum value over a given 
week.
"""


class TSDataPoint:
    def __init__(self, timestamp, value):
        self.timestamp = timestamp
        self.value = value


class TSDataCollection:
    def __init__(self):
        self.data_points = []

    def __str__(self):
        return [str(timestamp) for timestamp in self.data_points]

    def insert(self, timestamp, value):
        def binary_search(low, high):
            if low >= high:
                return low

            mid = (low + high) // 2
            if self.data_points[mid].timestamp < timestamp:
                return binary_search(mid + 1, high)
            else:
                return binary_search(low, mid)

        self.data_points.insert(binary_search(0, len(self.data_points)), TSDataPoint(timestamp, value))

    def delete(self, timestamp):
        def binary_search(low, high):
            if low >= high:
                return -1
            mid = (low + high) // 2
            if self.data_points[mid].timestamp == timestamp:
                return mid
            elif self.data_points[mid].timestamp < timestamp:
                return binary_search(mid + 1, high)
            return binary_search(low, mid)

        index = binary_search(0, len(self.data_points))
        if index != -1:
            self.data_points.pop(index)

    def query_within_range(self, begin_time, end_time):
        def bin_search_left(low, high):
            if low >= high:
                return -1
            mid = (low + high) // 2
            if self.data_points[mid].timestamp < begin_time:
                return bin_search_left(mid + 1, high)
            return bin_search_left(low, mid)

        def bin_search_right(low, high):
            if low >= high:
                return -1
            mid = (low + high) // 2
            if self.data_points[mid].timestamp <= end_time:
                return bin_search_right(mid + 1, high)
            return bin_search_right(low, mid)

        return self.data_points[bin_search_left(0, len(self.data_points)):bin_search_right(0, len(self.data_points))]


class DataPoint:
    def __init__(self, timestamp: datetime.datetime, value: int):
        self.timestamp = timestamp
        self.values = collections.defaultdict(int)
        self.values[value] += 1
        self.left = None
        self.right = None


class DataPointCollection:
    def __init__(self):
        self.head = None

    def insert(self, timestamp: datetime.datetime, value: int):

        def recursive_insert(node):
            if not node:
                return DataPoint(timestamp, value)
            if node.timestamp == timestamp:
                node.values[value] += 1
            elif node.timestamp < timestamp:
                node.right = recursive_insert(node.right)
            else:
                node.left = recursive_insert(node.left)
            return node

        self.head = recursive_insert(self.head)

    def delete(self, timestamp, value):
        def recursive_delete(node):
            if not node:
                return
            if node.timestamp == timestamp:
                node.values[value] -= 1
                if node.values[value] == 0:
                    del node.values[value]
                if not node.values:
                    return node.left or node.right
            elif node.timestamp < timestamp:
                return recursive_delete(node.right)
            return recursive_delete(node.left)

        return recursive_delete(self.head)

    def query(self, begin_time, end_time):
        def recursive_query(node):
            result = []
            if node:
                if node.timestamp >= begin_time:
                    result.extend(recursive_query(node.left))
                if begin_time <= node.timestamp <= end_time:
                    for key, value in node.values.items():
                        for _ in range(value):
                            result.append(key)
                if node.timestamp <= end_time:
                    result.extend(recursive_query(node.right))
            return result

        return recursive_query(self.head)


# Get the current time
now = datetime.datetime.now()

# Create 5 datetime objects within 1 minute of the current time
dt1 = now + datetime.timedelta(seconds=10)
dt2 = now + datetime.timedelta(seconds=20)
dt3 = now + datetime.timedelta(seconds=30)
dt4 = now + datetime.timedelta(seconds=40)
dt5 = now + datetime.timedelta(seconds=-50)

data_point_collection = DataPointCollection()
data_point_collection.insert(now, 0)
data_point_collection.insert(dt1, 1)
data_point_collection.insert(dt1, 1)
data_point_collection.insert(dt1, 7)
data_point_collection.insert(dt1, 1)
data_point_collection.insert(dt2, 2)
data_point_collection.insert(dt3, 3)
data_point_collection.insert(dt4, 4)
data_point_collection.insert(dt5, 5)
print(data_point_collection.query(dt5, dt4))
data_point_collection.delete(now, 0)
data_point_collection.delete(dt1, 1)
print(data_point_collection.query(dt5, dt4))
"""
Design and implement a data structure to store time-based logs from multiple sources. Each log entry has a 
timestamp, a source identifier, and a message. The data structure should support operations to insert a log entry, 
retrieve all log entries from a given source within a time range, and retrieve all log entries within a time range. 
"""


class Log:
    def __init__(self, timestamp, source_identifier, message):
        self.timestamp = timestamp
        self.source_identifier = source_identifier
        self.messages = [message]
        self.left = None
        self.right = None


class LogCollection:
    def __init__(self):
        self.sources = collections.defaultdict(Log)

    def insert_log(self, timestamp, source_identifier, message):
        def recursive_insert(node):
            if not node:
                return Log(timestamp, source_identifier, message)
            if node.timestamp == timestamp:
                node.messages.append(message)
            elif node.timestamp > timestamp:
                node.left = recursive_insert(node.left)
            else:
                node.right = recursive_insert(node.right)
            return node

        if source_identifier not in self.sources:
            self.sources[source_identifier] = Log(timestamp, source_identifier, message)
        else:
            recursive_insert(self.sources[source_identifier])

    def retrieve_log_entries(self, begin_time, end_time):
        def recursive_rectrieve_logs(node):
            result = []
            if node:
                if node.timestamp >= begin_time:
                    result.extend(recursive_rectrieve_logs(node.left))
                if end_time <= node.timestamp <= end_time:
                    result.append(node)
                if node.timestamp <= end_time:
                    result.extend(recursive_rectrieve_logs(node.right))
            return result

        def merge_sorted_logs(logs_a, logs_b):
            result = []
            pointer_a = 0
            pointer_b = 0
            while pointer_a < len(logs_a) and pointer_b < len(logs_b):
                if logs_a[pointer_a].timestamp < logs_b[pointer_b].timestamp:
                    result.append(logs_a[pointer_a])
                    pointer_a += 1
                else:
                    result.append(logs_b[pointer_b])
                    pointer_b += 1
            result.extend(logs_a[pointer_a:])
            result.extend(logs_b[pointer_b:])
            return result

        result = []
        for source in self.sources.keys():
            merge_sorted_logs(result, recursive_rectrieve_logs(self.sources[source]))

    def retrieve_log_entries_source(self, begin_time, end_time, source_identifier):
        def recursive_rectrieve_logs(node):
            result = []
            if node:
                if node.timestamp >= begin_time:
                    result.extend(recursive_rectrieve_logs(node.left))
                if end_time <= node.timestamp <= end_time:
                    result.extend(node.messages)
                if node.timestamp <= end_time:
                    result.extend(recursive_rectrieve_logs(node.right))
            return result

        if source_identifier in self.sources:
            return recursive_rectrieve_logs(self.sources[source_identifier])
        return []


"""
Design and implement a data structure to store a collection of time-based tasks with varying priorities. Each task 
has a deadline, a priority level, and a description. The data structure should support operations to insert a task, 
delete a task, and query for the highest-priority task that is due within a given time range. The data structure 
should also support efficient computation of aggregate statistics over time, such as the number of tasks completed 
per day or the average priority of tasks completed over a given week. 
"""


class Task:
    def __init__(self, deadline, priority_level, description):
        self.deadline = deadline
        self.priority_level = priority_level
        self.description = description


class TaskCollection:
    def __int__(self):
        self.task_map = collections.defaultdict(Task)
        self.tasks = []

    def insert_task(self, deadline, priority_level, description):
        pass

    def query_range(self, begin_time, end_time):
        def binary_search_being(low, high):
            pass

        def binary_search_end(low, high):
            pass

        low, high = binary_search_being(0, len(self.tasks)), binary_search_end(0, len(self.tasks))
        return self.tasks[low:high - 1]
