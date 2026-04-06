# 0/1 Knapsack Problem — Dynamic Programming

## Problem Description

Given `n` items, each with a weight and a value, and a knapsack with capacity `W`, determine the maximum total value that can be put in the knapsack.  
Each item can be selected **at most once** (0/1 constraint).

**Example:**  
Input: weights = [1,3,4,5], values = [1,4,5,7], W = 7  
Output: 9  
Explanation: Choose items with weights 3 and 4 (values 4 + 5).

---

## Algorithm Idea and Approach

- Use dynamic programming:
  - Let `dp[i][w]` be the max value for the first `i` items and capacity `w`.
  - For each item, decide to **include** it (if possible) or **exclude** it.
  - State transition:  
    - If weights[i-1] > w: dp[i][w] = dp[i-1][w]
    - Else: dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])

---

## Python Example

```python
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
    return dp[n][W]

# Example usage:
print(knapsack([1,3,4,5], [1,4,5,7], 7))  # Output: 9
```

---

## Complexity Analysis

- **Time:** O(n * W)
- **Space:** O(n * W), can be optimized to O(W) using a 1D array.

---

## Applications

- Resource allocation
- Budget management
- Cargo loading problems
- Subset selection with constraints

---

## Useful Links

- [0/1 Knapsack — LeetCode](https://leetcode.com/problems/knapsack/)
- [0/1 Knapsack — GeeksforGeeks](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)
- [Wikipedia: Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem)

---

## LeetCode Practice

| Difficulty | Problem                 | Link                                                                            |
|------------|-------------------------|---------------------------------------------------------------------------------|
| Medium     | Partition Equal Subset Sum | [#416 Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |
| Medium     | Last Stone Weight II    | [#1049 Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/)          |
| Medium     | Target Sum              | [#494 Target Sum](https://leetcode.com/problems/target-sum/)                    |

---