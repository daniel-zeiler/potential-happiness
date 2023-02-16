"""
Design and implement a data structure that allows efficient insertion and retrieval of time-based events. Each
event has a start time and an end time, and events can overlap in time. The data structure should support operations
to insert an event, delete an event, and query for all events that overlap with a given time range.
"""


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

"""
Design and implement a data structure to store time-based logs from multiple sources. Each log entry has a 
timestamp, a source identifier, and a message. The data structure should support operations to insert a log entry, 
retrieve all log entries from a given source within a time range, and retrieve all log entries within a time range. 
"""

"""
Design and implement a data structure to store a collection of time-based tasks with varying priorities. Each task 
has a deadline, a priority level, and a description. The data structure should support operations to insert a task, 
delete a task, and query for the highest-priority task that is due within a given time range. The data structure 
should also support efficient computation of aggregate statistics over time, such as the number of tasks completed 
per day or the average priority of tasks completed over a given week. 
"""
