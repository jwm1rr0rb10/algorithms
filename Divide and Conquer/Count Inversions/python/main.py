def merge_and_count(arr, left, mid, right):
    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]
    i = j = 0
    k = left
    inv_count = 0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
            inv_count += (len(left_part) - i)
        k += 1

    arr[k:right+1] = left_part[i:] + right_part[j:]
    return inv_count

def count_inversions(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += count_inversions(arr, left, mid)
        inv_count += count_inversions(arr, mid+1, right)
        inv_count += merge_and_count(arr, left, mid, right)
    return inv_count

# Usage example:
arr = [2, 4, 1, 3, 5]
print(count_inversions(arr, 0, len(arr)-1))  # 3