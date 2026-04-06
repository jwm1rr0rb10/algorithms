def search_rotated_sorted_array(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Example usage
arr = [4, 5, 6, 7, 0, 1, 2]
print(search_rotated_sorted_array(arr, 0))  # Output: 4
print(search_rotated_sorted_array(arr, 3))  # Output: -1