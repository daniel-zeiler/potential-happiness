import random


class RandomizedSetWeights:
    def __init__(self, weights, values):
        self.intervals = self.set_weights(weights, values)

    def set_weights(self, weights, values):
        intervals = []
        sum = 0
        for weight, value in zip(weights, values):
            intervals.append([sum, sum + weight, value])
            sum += weight + 1
        return intervals

    def pick(self):
        def binary_search(low, high, choice):
            mid_index = int((low + high) / 2)
            [start, end], value = self.intervals[mid_index]
            if start < choice < end:
                return value
            elif choice < start:
                return binary_search(low, mid_index, choice)
            else:
                return binary_search(mid_index, high, choice)

        max_value = self.intervals[-1][1]
        return binary_search(0, len(self.intervals), random.randint(0, max_value))
