def exponential_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == target:
        return 0

    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    # Binary search in found range
    left = i // 2
    right = min(i, n - 1)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
print(exponential_search(arr, 16))  # Output: 7
print(exponential_search(arr, 21))  # Output: -1