from typing import List

"""
2 arrays of integers
for any integer in arry1 we'll call the closest int from array2.  
it's sensor and the difference between the 2 integers can be called the sensor distance.  
Return the largest sensor distance.
"""


def find_largest_sensor_distance(array1: List[int], array2: List[int]) -> int:
    array2.sort()

    def binary_search_closest(array: List[int], low: int, high: int, target: int) -> int:
        if target <= array[low]:
            return array[low]
        if target >= array[high]:
            return array[high]
        center = (low + high) // 2
        if target == array[center]:
            return array[center]
        if array[center - 1] < target < array[center]:
            return array[center] if abs(target - array[center]) > abs(target - array[center - 1]) else array[center - 1]
        if array[center] > target > array[center + 1]:
            return array[center] if abs(target - array[center]) > abs(target - array[center + 1]) else array[center + 1]

        if target < array[center]:
            return binary_search_closest(array, low, center - 1, target)
        return binary_search_closest(array, center + 1, high, target)

    return max([abs(binary_search_closest(array2, 0, len(array2) - 1, value) - value) for value in array1])


array1 = [1, 2, 3, 4, 5, 99]
array2 = [3, 6, 7, 11, 12, 144]
print(find_largest_sensor_distance(array1, array2))
