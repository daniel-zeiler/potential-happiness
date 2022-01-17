"""
The 0 /1 knapsack

Select items in subset that is maximal in value but stays within a constraint.
Find maximum value for items underneat weight.
weights = [1,2,3,5]
values = [30,70,50,60]
max_weight = 5

What is zero - one ? We can't split items.  We either take it or we don't.
One option is to do brute force, complete search.  Complete search of
all subsets.  O(2^n) total subsets.

What is recurrence relation?

Weight left     Possible choices    total value
5               1,2,3,4             0

"""


def zero_one_backtracking(weights, values, max_weight):
    def backtracking_function(weights_remaining, values_remaining, target_weight_remaining, value_so_far):
        result = 0
        if not weights_remaining or target_weight_remaining == 0:
            return value_so_far
        for i, (weight, value) in enumerate(zip(weights_remaining, values_remaining)):
            if weight >= target_weight_remaining:
                result = max(result, backtracking_function(weights_remaining[:i] + weights_remaining[i + 1:],
                                                           values_remaining[:i] + values_remaining[i + 1:],
                                                           target_weight_remaining - weight, value + value))
        return result

    return backtracking_function(weights, values, max_weight, 0)


def zero_one_knapsack(weights, values, max_weight):
    result = [[0 for _ in range(max_weight + 1)] for _ in range(len(weights) + 1)]

    for x in range(1, len(result)):
        for y in range(1, len(result[0])):
            weight = weights[x - 1]
            value = values[x - 1]
            target_weight = y
            if weight <= target_weight:
                result[x][y] = max(result[x - 1][y], result[x - 1][y - weight] + value)
            else:
                result[x][y] = result[x - 1][y]
    return result[-1][-1]


print(zero_one_knapsack([1, 2, 3, 5], [30, 70, 50, 60], 5))
print(zero_one_backtracking([1, 2, 3, 5], [30, 70, 50, 60], 5))
