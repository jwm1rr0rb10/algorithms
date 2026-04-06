# Subset Generation with Bitmask

---

## Problem Description

Given an array of `n` elements, generate all possible subsets (the power set).

---

## Approach

The optimal approach uses bitmasks:

1. **Each subset corresponds to a bitmask:**  
   For each number from `0` to `2^n - 1`, interpret its binary representation as a mask: the `i`-th bit is 1 if the `i`-th element is included in the subset.

2. **Iterate all masks:**  
   Traverse all masks to generate all subsets.

---

## Python Example

```python
def subsets(nums):
    n = len(nums)
    all_subsets = []
    for mask in range(1 << n):  # 0..2^n-1
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        all_subsets.append(subset)
    return all_subsets

# Example:
nums = [1, 2, 3]
print(subsets(nums))
# Output:
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

---

## How It Works

- There are `2^n` possible bitmasks.
- For each bitmask, we check every bit: if it's set, include the corresponding element.

---

## Applications

- Generating all combinations (subsets) of a set
- Bitmask Dynamic Programming (Bitmask DP)
- Problems like subset sum, partition, combinatorics

---

## When to Use

- When `n` is small (≤ 20–22)
- For problems that require all subsets

---

## When Not to Use

- When `n` is large: complexity is exponential

---

## Complexity

- **Time:** O(n × 2^n)  
  (for each of 2^n subsets, up to n checks)
- **Space:** O(n × 2^n) (if storing all subsets)

---

## Useful Links

- [LeetCode — Subsets](https://leetcode.com/problems/subsets/)
- [Bit Manipulation — Wikipedia](https://en.wikipedia.org/wiki/Bit_manipulation)
- [Power set — Wikipedia](https://en.wikipedia.org/wiki/Power_set)