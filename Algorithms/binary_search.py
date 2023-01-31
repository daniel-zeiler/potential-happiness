def binary_search(nums, target):
    def search_util(low, high):
        if high < low:
            return -1
        mid_point = int((high + low) / 2)
        mid_value = nums[mid_point]

        if mid_value == target:
            return mid_point
        elif mid_value > target:
            return search_util(low, mid_point - 1)
        else:
            return search_util(mid_point + 1, high)

    return search_util(0, len(nums) - 1)


a_list = [0, 1, 2, 3, 4, 5, 11, 22, 32, 33, 34, 40]
target = 20
print(binary_search(a_list, target))
