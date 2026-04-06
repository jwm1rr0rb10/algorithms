# Partition Problem — Dynamic Programming (Tabulation)

## Problem Description

Given a set (or array) of positive integers, determine if it can be partitioned into two subsets with equal sum.

Variants:
- Decide if such a partition exists (True/False).
- Sometimes: Find one such partition.

---

## Algorithm Idea and Approach

- The problem reduces to checking if there is a subset whose sum is exactly half of the total sum.
- If total sum is odd — answer is False.
- Use dynamic programming (tabulation, bottom-up approach):
  - Let `dp[i][j]` be True if a subset of the first `i` numbers can form sum `j`.
  - For each number, fill the DP table by considering including or excluding the current number.
  - `dp[0][0] = True` (empty subset sums to zero).
  - For each `i` from 1 to n and for each `j` from 0 to target:
    - If `j < nums[i-1]`, then `dp[i][j] = dp[i-1][j]`
    - Else, `dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]`

---

## Python Example: Partition Equal Subset Sum (Tabulation)

```python
def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True  # sum 0 possible for all
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < nums[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
    return dp[n][target]

# Example usage:
nums = [1, 5, 11, 5]
print(can_partition(nums))  # Output: True ([1, 5, 5] and [11])
```

---

## Complexity Analysis

- **Time:** O(n * sum/2)
- **Space:** O(n * sum/2)
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