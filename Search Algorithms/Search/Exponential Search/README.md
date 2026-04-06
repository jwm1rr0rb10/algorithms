# Exponential Search

## What it is

Exponential Search is an efficient searching algorithm for **sorted arrays or lists**, especially useful when the target value is expected to be near the beginning or when the array size is unknown (e.g., streams, infinite arrays). The algorithm quickly finds a range where the target may be, then applies binary search within that range.

---

## How it works

1. **Check the first element**. If it matches the target, return its index.
2. **Expand the search range exponentially**:  
   Check elements at indices 1, 2, 4, 8, 16, 32, ... (i.e., keep doubling the index) until you find an element greater than or equal to the target or you exceed the array bounds.
3. **Binary search** in the range `[i/2, min(i, n-1)]`, where `i` is the current index and `n` is the length of the array.
4. Return the index if found, otherwise -1.

---

## Complexity

- **Time Complexity:** O(log i), where `i` is the index of the target element. In the worst case: O(log n).
- **Space Complexity:** O(1) — only a few variables are used.

---

## When to Use

- The array is **sorted**.
- The size of the array is **unknown or very large** (e.g., streams, infinite data).
- You expect the target to be **near the beginning**.
- When random access by index is possible and cheap.

## When Not to Use

- On **unsorted** arrays.
- On data structures with expensive random access (e.g., linked lists).
- For small arrays (regular binary search is simpler).

---

## Python Example

```python
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
```

---

## Summary

Exponential Search is a hybrid search algorithm that quickly narrows down the search range using exponential steps, then switches to binary search. It's rarely used in everyday coding, but is powerful for huge, sorted datasets or unknown-length streams.