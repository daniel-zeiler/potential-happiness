def merge_sort(nums):
    def merge_util(nums):
        if len(nums) == 1:
            return nums
        mid_pointer = int(len(nums) / 2)
        left = merge_util(nums[:mid_pointer])
        right = merge_util(nums[mid_pointer:])
        result = []
        left_pointer = 0
        right_pointer = 0

        while left_pointer < len(left) and right_pointer < len(right):
            if left[left_pointer] < right[right_pointer]:
                result.append(left[left_pointer])
                left_pointer += 1
            else:
                result.append(right[right_pointer])
                right_pointer += 1

        if left_pointer != len(left):
            result.extend(left[left_pointer:])
        if right_pointer != len(right):
            result.extend(right[right_pointer:])
        return result

    return merge_util(nums)


values = [0, 1, 2, 3, 4, 5, 6, -1, 3, -2]

print(merge_sort(values))
