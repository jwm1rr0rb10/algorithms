# Subsets Using Bits

## Problem Description

Given a set (or array) of `n` elements, generate all possible subsets (the power set) using bit manipulation.

---

## Approach

Each subset can be represented by an `n`-bit number, where each bit indicates whether the corresponding element is included.

- There are `2^n` possible subsets.
- For each integer from `0` to `2^n - 1`, the binary representation tells which elements to include in the subset.

---

## Python Example

```python
def subsets(nums):
    n = len(nums)
    result = []
    for mask in range(1 << n):  # from 0 to 2^n - 1
        subset = []
        for i in range(n):
            if (mask >> i) & 1:
                subset.append(nums[i])
        result.append(subset)
    return result

# Example:
nums = [1, 2, 3]
print(subsets(nums))
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

---

## How It Works

- Loop over all numbers from `0` to `2^n - 1`.
- Each number's bits represent inclusion/exclusion of elements in the subset.

---

## Applications

- Generating all combinations or subsets for combinatorial problems.
- Solving problems like Subset Sum, Knapsack, etc.
- Useful in coding interviews for exhaustive search.

---

## Useful Links

- [LeetCode #78 — Subsets](https://leetcode.com/problems/subsets/)
- [Power set — Wikipedia](https://en.wikipedia.org/wiki/Power_set)

---