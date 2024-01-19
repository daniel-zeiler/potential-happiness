import collections
import heapq
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    result = []
    for interval in intervals:
        if not result or interval[0] > result[-1][1]:
            result.append(interval)
        else:
            result[-1][1] = interval[1]
    return result


class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for x in range(0, min(k, len(self.stack))):
            self.stack[x] += val


def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    max_sum = 0
    for i in range(0, len(nums), 2):
        max_sum += min(nums[i], nums[i + 1])
    return max_sum


def sortArrayByParity(nums: List[int]) -> List[int]:
    nums.sort(key=lambda x: x % 2)
    return nums


def replaceElements(arr: List[int]) -> List[int]:
    prev_max = float('-inf')
    for index in range(len(arr) - 1, -1, -1):
        if prev_max == float('-inf'):
            prev_max = arr[index]
            arr[index] = -1
        else:
            prev_max, arr[index] = max(prev_max, arr[index]), prev_max
    return arr


def intervalIntersection(first_list: List[List[int]], second_list: List[List[int]]) -> List[List[int]]:
    output = []
    first_index = 0
    second_index = 0
    while first_index < len(first_list) and second_index < len(second_list):
        first_element = first_list[first_index]
        second_element = second_list[second_index]

        if second_element[0] <= first_element[1] <= second_element[1] or first_element[0] <= second_element[1] <= \
                first_element[1]:
            output.append([max(first_element[0], second_element[0]), min(first_element[1], second_element[1])])

        if first_element[0] < second_element[0]:
            first_index += 1
        else:
            second_index += 1

    return output


def permute(nums: List[int]) -> List[List[int]]:
    result = []

    def perm_function(temp_result, numbers):
        if not numbers:
            result.append(temp_result)
        for i in range(0, len(numbers)):
            perm_function(temp_result + [numbers[i]], numbers[:i] + numbers[i + 1:])

    perm_function([], nums)
    return result


def subsets(nums: List[int]) -> List[List[int]]:
    power_set = []

    def subsets_function(temp_result, numbers):
        power_set.append(temp_result)
        for i in range(0, len(numbers)):
            subsets_function(temp_result + [numbers[i]], numbers[i + 1:])

    subsets_function([], nums)
    return power_set


def cal_points(ops: List[str]) -> int:
    values = []
    for operation in ops:
        if operation.lstrip("-").isnumeric():
            values.append(int(operation))
        elif operation == "C":
            values.pop()
        elif operation == "D":
            values.append(values[-1] * 2)
        else:
            print(values)
            values.append(values[-1] + values[-2])
    return sum(values)


def relative_sort_array(arr1: List[int], arr2: List[int]) -> List[int]:
    relative_sort_map = {x: i for i, x in enumerate(arr2)}
    arr1.sort(key=lambda x: relative_sort_map[x] if x in relative_sort_map else float('inf'))
    return arr1


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1).intersection(set(nums2)))


def min_falling_path_sum(matrix: List[List[int]]) -> int:
    result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if x == 0:
                result[x][y] = matrix[x][y]
            elif y == 0:
                result[x][y] = matrix[x][y] + min(result[x - 1][y], result[x - 1][y + 1])
            elif y == len(matrix) - 1:
                result[x][y] = matrix[x][y] + min(result[x - 1][y], result[x - 1][y - 1])
            else:
                result[x][y] = matrix[x][y] + min(result[x - 1][y - 1], result[x - 1][y], result[x - 1][y + 1])
    return min(result[-1])


def validate_stack_sequence(pushed: List[int], popped: List[int]) -> bool:
    stack = []
    while pushed and popped:
        if not stack or popped[0] != stack[-1]:
            stack.append(pushed.pop(0))
        else:
            popped.pop(0)
            stack.pop()
    while popped:
        if stack[-1] != popped[0]:
            return False
        stack.pop()
        popped.pop(0)
    return True


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    pass


def last_stone_weight(stones: List[int]) -> int:
    stones = [-1 * n for n in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        stone_one = heapq.heappop(stones)
        stone_two = heapq.heappop(stones)
        if stone_one == stone_two:
            pass
        else:
            heapq.heappush(stones, -stone_one + stone_two)
    return heapq.heappop(stones)


def can_reach(arr: List[int], start: int) -> bool:
    visited = {start}
    queue = collections.deque([start])

    while queue:
        position = queue.popleft()
        value = arr[position]
        if value == 0:
            return True

        position_left = position - value
        position_right = position + value

        if position_left >= 0 and position_left not in visited:
            visited.add(position_left)
            queue.append(position_left)

        if position_right < len(arr) and position_right not in visited:
            queue.append(position_right)
            visited.add(position_right)

    return False


"""
This function has two points.  The first pointer will scan the length of nums.  The second pointer will keep track 
of the last valid position As we increment the first pointer, we will track the number of flips already present in 
section between the two.  In the event we reach a position that requires a flip and we've reached our limit, 
we will increment pointer two and try to undo the flips until we can proceed with pointer one. O(n) time complexity.  
O(1) space complexity. 
"""


def longest_ones(nums: List[int], k: int) -> int:
    number_of_flips = 0
    longest_ones = 0
    pointer_a = 0
    pointer_b = 0
    while pointer_a < len(nums):
        if nums[pointer_a] == 0:
            while number_of_flips == k:
                if nums[pointer_b] == 0:
                    number_of_flips -= 1
                pointer_b += 1
            number_of_flips += 1
        longest_ones = max(longest_ones, pointer_a - pointer_b + 1)
        pointer_a += 1
    return longest_ones


"""
I will create a temporary result list and keep track of the minimum cost to climb to each location.
The formula for each position will be temp[x] = cost[x] + min(cost[x-1],cost[x-2])
The result will be min[temp[-1],temp[-2])
This is an O(n) time and space complexity algorithm.
"""


def min_cost_climbing_stairs(costs: List[int]) -> int:
    temp = [0 for _ in range(len(costs))]
    for i, cost in enumerate(costs):
        if i == 0 or i == 1:
            temp[i] = cost
        else:
            temp[i] = cost + min(temp[i - 1], temp[i - 2])
    return min(temp[-1], temp[-2])


"""
The goal is to find the maximum sliding window of size minutes such that we maximize the number of customers with 
index matching with windows grumpy value of (1). To do this, i'll initialize a window of size (n) and count the total.
I'll then slide the window to the end.
"""


def max_satisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    window_pointer_a = 0
    window_pointer_b = 0
    current_window_flipped = 0
    already_satisfied = 0
    for i in range(minutes):
        if grumpy[i] == 1:
            current_window_flipped += customers[i]
        else:
            already_satisfied += customers[i]
        window_pointer_b += 1

    max_window = current_window_flipped

    while window_pointer_b < len(grumpy):
        if grumpy[window_pointer_a] == 1:
            current_window_flipped -= customers[window_pointer_a]
        if grumpy[window_pointer_b] == 1:
            current_window_flipped += customers[window_pointer_b]
        else:
            already_satisfied += customers[window_pointer_b]

        window_pointer_b += 1
        window_pointer_a += 1
        max_window = max(max_window, current_window_flipped)

    return already_satisfied + max_window


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    count_1, count_2, result = collections.Counter(nums1), collections.Counter(nums2), []
    for key, value in count_1.items():
        if key in count_2:
            result.extend([key for _ in range(value)])
    return result


def maxArea(height: List[int]) -> int:
    max_area, pointer_a, pointer_b = 0, 0, len(height) - 1
    while pointer_a < pointer_b:
        height_a, height_b = height[pointer_a], height[pointer_b]
        max_area = max(max_area, min(height_a, height_b) * (pointer_b - pointer_a))
        if height_a < height_b:
            pointer_a += 1
        else:
            pointer_b -= 1
    return max_area


def maxProfit(prices: List[int]) -> int:
    max_profit, min_so_far = 0, float('inf')
    for i, price in enumerate(prices):
        if i:
            max_profit = max(max_profit, price - min_so_far)
        min_so_far = min(min_so_far, price)
    return max_profit


def isAlienSorted(words: List[str], order: str) -> bool:
    ordering_dict = collections.defaultdict(int)
    for i, value in enumerate(order):
        ordering_dict[value] = i

    def check_ordering(word_one: str, word_two: str):
        pointer_one, pointer_two = 0, 0
        while pointer_one < len(word_one) and pointer_two < len(word_two):
            char_one, char_two = word_one[pointer_one], word_two[pointer_two]
            if char_one != char_two:
                return ordering_dict[char_one] < ordering_dict[char_two]
            pointer_one += 1
            pointer_two += 1
        return len(word_two) >= len(word_one)

    for i, word in enumerate(words):
        if i:
            prev_word = words[i - 1]
            if not check_ordering(prev_word, word):
                return False
    return True
