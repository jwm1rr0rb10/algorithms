def quickselect(arr, k):
    def partition(left, right):
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i

    def select(left, right, k_smallest):
        if left == right:
            return arr[left]
        pivot_index = partition(left, right)
        if k_smallest == pivot_index:
            return arr[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)

    return select(0, len(arr) - 1, k - 1)

# Usage example:
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(quickselect(arr, k))  # 7