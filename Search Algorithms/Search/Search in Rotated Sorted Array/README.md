# Search in Rotated Sorted Array

## What is a Rotated Sorted Array?

A **rotated sorted array** is a sorted array that has been "rotated" (shifted) at some pivot so that the order is preserved, but the starting point is different.

**Example:**  
Original: `[1, 2, 3, 4, 5, 6, 7]`  
Rotated:  `[5, 6, 7, 1, 2, 3, 4]`

---

## The Problem

Given a rotated sorted array and a target value, determine the index of the target in the array, or return -1 if not found.

---

## Why Regular Binary Search Doesn't Work

Standard binary search assumes the entire array is sorted. After rotation, only one segment is sorted at any time, so we can't apply classic binary search directly.

---

## The Solution: Modified Binary Search

At every step, **one half of the array is still sorted**. We use this property to decide which half to search:

1. Set `left` and `right` pointers at the start and end of the array.
2. While `left <= right`:
    - Find `mid = (left + right) // 2`.
    - If `arr[mid] == target` — return `mid`.
    - Determine which half is sorted:
        - If `arr[left] <= arr[mid]` (left half is sorted):
            - If `target` is in `[arr[left], arr[mid]]`, search left (`right = mid - 1`).
            - Else, search right (`left = mid + 1`).
        - Else (right half is sorted):
            - If `target` is in `[arr[mid], arr[right]]`, search right (`left = mid + 1`).
            - Else, search left (`right = mid - 1`).
3. Return -1 if not found.

---

## Complexity

- **Time:** O(log n)
- **Space:** O(1)

---

## Python Example

```python
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
```

---

## Summary

You can efficiently search in a rotated sorted array with a modified binary search by always identifying which half is sorted. This allows you to maintain O(log n) time complexity.