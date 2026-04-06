# Partition Problem — Dynamic Programming

## Problem Description

Given a set (or array) of positive integers, determine if it can be partitioned into two subsets with equal sum.

Variants:
- Decide if such a partition exists (True/False).
- Sometimes: Find one such partition.

---

## Algorithm Idea and Approach

- The problem reduces to checking if there is a subset whose sum is exactly half of the total sum.
- If total sum is odd — answer is False.
- Use dynamic programming (similar to subset sum):
  - Let `dp[i]` be True if a subset sum of `i` is possible.
  - For each number, update the DP array from high to low.

---

## Python Example: Partition Equal Subset Sum

```python
def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]

# Example usage:
nums = [1, 5, 11, 5]
print(can_partition(nums))  # Output: True ([1, 5, 5] and [11])
```

---

## Complexity Analysis

- **Time:** O(n * sum/2)
- **Space:** O(sum/2)
  - n = number of elements, sum = total sum of elements

---

## Applications

- Resource allocation
- Scheduling and load balancing
- Fair division problems

---

## Useful Links

- [LeetCode #416: Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
- [GeeksforGeeks: Partition Problem](https://www.geeksforgeeks.org/partition-problem-dp-18/)

---

## LeetCode Practice

| Difficulty | Problem                        | Link                                                                          |
|------------|--------------------------------|-------------------------------------------------------------------------------|
| Medium     | Partition Equal Subset Sum     | [#416 Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |