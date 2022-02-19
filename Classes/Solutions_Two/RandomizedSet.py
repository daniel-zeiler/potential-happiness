import random


class RandomizedSetWeights:
    def __init__(self, values, weights):
        self.sum = 0
        self.value_list = []
        for value, weight in zip(values, weights):
            self.value_list.append([self.sum, self.sum + weight, value])
            self.sum += weight

    def get(self):
        random_choice = random.choice(range(self.sum))

        def binary_search(low, high):
            if low > high:
                return -1
            mid_point = (low + high) // 2
            mid_range = self.value_list[mid_point]
            if mid_range[0] <= random_choice < mid_range[1]:
                return mid_range[2]
            elif mid_range[0] > random_choice:
                return binary_search(low, mid_point - 1)
            else:
                return binary_search(mid_point + 1, high)

        return binary_search(0, len(self.value_list) - 1)


values = ['a', 'cat', 'belongs', 'here']
weights = [5, 5, 25, 20]

randomized_set = RandomizedSetWeights(values, weights)
for _ in range(2000000):
    randomized_set.get()
