# Maximum Subarray — Divide & Conquer

## Problem description

Given an array of integers (can include negatives), find a contiguous subarray with the maximum sum.

**Example:**
```python
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Maximum sum: 6 ([4, -1, 2, 1])
```

## Algorithm (Divide & Conquer)

1. Split the array into two parts.
2. Recursively find the maximum subarray sum in the left and right halves.
3. Find the maximum sum crossing the midpoint.
4. Return the maximum of the three options.

### Python code example

```python
def max_crossing_sum(arr, left, mid, right):
    left_sum = float('-inf')
    total = 0
    for i in range(mid, left-1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
    right_sum = float('-inf')
    total = 0
    for i in range(mid+1, right+1):
        total += arr[i]
        if total > right_sum:
            right_sum = total
    return left_sum + right_sum

def max_subarray_sum(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    max_left = max_subarray_sum(arr, left, mid)
    max_right = max_subarray_sum(arr, mid+1, right)
    max_cross = max_crossing_sum(arr, left, mid, right)
    return max(max_left, max_right, max_cross)

# Usage example:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr, 0, len(arr)-1))  # 6
```

## Time complexity

- O(n log n)

## When to use

- For educational purposes to understand Divide & Conquer principles.
- When you need to generalize the problem (e.g., to 2D arrays).
- In distributed/parallel systems.

## Drawbacks

- Slower than Kadane’s algorithm (O(n)) for the simple case.

---

## Useful links

- [GeeksforGeeks: Maximum Subarray Sum using Divide and Conquer](https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/)
- [Wikipedia: Maximum subarray problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
- [LeetCode Discuss: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/solutions/)

---

## LeetCode Problems

- [53. Maximum Subarray (Easy)](https://leetcode.com/problems/maximum-subarray/)
- [918. Maximum Sum Circular Subarray (Medium)](https://leetcode.com/problems/maximum-sum-circular-subarray/)
- [363. Max Sum of Rectangle No Larger Than K (Hard, 2D version)](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/)

---