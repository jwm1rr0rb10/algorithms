def majority_element_rec(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    left_major = majority_element_rec(arr, left, mid)
    right_major = majority_element_rec(arr, mid + 1, right)
    if left_major == right_major:
        return left_major
    left_count = sum(1 for i in range(left, right + 1) if arr[i] == left_major)
    right_count = sum(1 for i in range(left, right + 1) if arr[i] == right_major)
    return left_major if left_count > right_count else right_major

def majority_element(arr):
    return majority_element_rec(arr, 0, len(arr) - 1)
    
# Usage example:
arr = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(arr))  # 2