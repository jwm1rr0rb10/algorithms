# Jump Search

## What it is

Jump Search is a searching algorithm for **sorted arrays or lists**. It is a compromise between Linear Search (slow, simple) and Binary Search (fast, but splits in half). Jump Search divides the array into blocks of fixed size and "jumps" ahead by block size, looking for the block that might contain the target. Then, it performs a linear search within that block.

---

## How it works

1. Suppose the array has length `n`. Choose a step (block size) of `m` (commonly `m = sqrt(n)`).
2. Start from the first element and jump ahead by `m` elements at a time, checking the last element of each block.
3. Stop jumping when the block's endpoint is **greater than or equal to** the target, or you reach the end of the array.
4. Perform a linear search within the found block.
5. If you find the target, return its index. If not, return -1.

---

## Complexity

- **Time Complexity:** O(√n)
    - Maximum O(√n) jumps, plus O(√n) scans within the block
- **Space Complexity:** O(1)
    - Only a few variables for indexes

---

## When to Use

- The array is **sorted**
- You want an algorithm simpler than binary search, but faster than linear search
- Binary search is not suitable for some reason (e.g., expensive random access)

## When Not to Use

- The array is **unsorted** (Jump Search doesn't work)
- The array is **very small** (use Linear Search or Binary Search)
- **Binary search** is usually faster (O(log n) vs O(√n)), so prefer it if possible

---

## Python Example

```python
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Jump ahead in blocks
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search within the block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 13, 17, 21, 29, 35, 42, 56]
print(jump_search(arr, 21))  # Output: 7
print(jump_search(arr, 6))   # Output: -1
```

---

## Summary

Jump Search is a rarely used algorithm for sorted arrays. It is faster than linear search, but slower than binary search. In modern practice, binary search is almost always preferred for sorted data.