from typing import List


def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    sum_so_far = sum(arr[:k])

    result = 0

    if sum_so_far / k >= threshold:
        result += 1

    pointer_a, pointer_b = 0, k

    while pointer_b < len(arr):
        sum_so_far += -arr[pointer_a] + arr[pointer_b]
        if sum_so_far / k >= threshold:
            result += 1
        pointer_a += 1
        pointer_b += 1
    return result


arr = [1, 1, 1, 1, 1]
k = 1
threshold = 1
print(numOfSubarrays(arr, k, threshold))
