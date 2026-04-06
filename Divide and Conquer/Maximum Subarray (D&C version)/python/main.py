def max_crossing_sum(arr, left, mid, right):
    left_sum = float('-inf')
    total = 0
    for i in range(mid, left-1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
    right_sum = float('-inf')
    total = 0
    for i in range(mid+1, right+1):
        total += arr[i]
        if total > right_sum:
            right_sum = total
    return left_sum + right_sum

def max_subarray_sum(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    max_left = max_subarray_sum(arr, left, mid)
    max_right = max_subarray_sum(arr, mid+1, right)
    max_cross = max_crossing_sum(arr, left, mid, right)
    return max(max_left, max_right, max_cross)

# Usage example:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr, 0, len(arr)-1))  # 6