# Sliding Window

## Description

The **sliding window** is an algorithmic technique used to efficiently process sequences (such as arrays or strings) by maintaining a dynamic subarray (or "window") of fixed or variable size.

This approach allows you to solve problems involving subarrays or substrings without recalculating values for every possible interval, thus improving performance.

---

## How It Works

1. **Initial Window:**  
   Set up the starting range of elements (e.g., the first `k` elements of an array).
2. **Slide the Window:**  
   Move the window through the sequence: remove the leftmost element and add the next element on the right.
3. **Update the Result:**  
   After each move, update the result only for the changed elements, making the algorithm much faster.

---

## Example Problem

> Find the maximum sum of a subarray of length `k` in an array.

### Example Python Code

```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

---

## When to Use Sliding Window

- Finding the maximum/minimum/sum in a subarray of fixed length.
- Searching for substrings with certain properties in a string.
- Optimizing problems that require processing all subarrays/substrings of size `k`.

---

## Advantages

- **Speed:** Avoids redundant recalculations for each window.
- **Simplicity:** Easy to implement.
- **Versatility:** Applicable to many sequence-based problems.

---

## Useful Links

- [Wikipedia: Sliding window technique](https://en.wikipedia.org/wiki/Sliding_window_protocol)
- [LeetCode Sliding Window Patterns](https://leetcode.com/tag/sliding-window/)
