# Search in 2D Matrix

## Problem Statement

Given a 2D matrix with the following properties:
- Each row is sorted in ascending order from left to right.
- The first integer of each row is greater than the last integer of the previous row.

**Example:**
```
[
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
```

Given a target value, determine if it exists in the matrix.

---

## Approach

Since the matrix can be "flattened" into a single sorted array, you can perform a binary search without physically converting the matrix.

### Algorithm

1. Let `m` be the number of rows and `n` be the number of columns.
2. Set `left = 0` and `right = m * n - 1`.
3. While `left <= right`:
    - Compute `mid = (left + right) // 2`.
    - Map this index to matrix coordinates: `row = mid // n`, `col = mid % n`.
    - Compare `matrix[row][col]` with the target:
        - If equal, return `True` (or the index).
        - If less, search the right half.
        - If more, search the left half.
4. If not found, return `False`.

---

## Complexity

- **Time:** O(log(m * n))
- **Space:** O(1)

---

## Python Example

```python
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        row, col = mid // n, mid % n
        num = matrix[row][col]
        if num == target:
            return True
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Example usage
matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(search_matrix(matrix, 3))   # Output: True
print(search_matrix(matrix, 13))  # Output: False
```

---

## Summary

By treating the 2D matrix as a flat sorted array, you can use binary search for efficient lookup in O(log(m * n)) time.