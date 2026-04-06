# Paint House — Dynamic Programming

## Problem Description

You are given a row of `n` houses, each house can be painted in one of `k` colors.  
The cost of painting each house with a certain color is given in a `costs` matrix of size `n x k`, where `costs[i][j]` is the cost of painting house `i` with color `j`.  
No two adjacent houses can be painted with the same color.

**Goal:**  
Minimize the total cost to paint all houses.

---

## Algorithm Idea and Approach

- Use dynamic programming:
  - Let `dp[i][j]` be the minimum cost to paint up to house `i`, where house `i` is painted with color `j`.
  - For each house and color, set `dp[i][j] = costs[i][j] + min(dp[i-1][c])` for all `c ≠ j`.
  - For the first house, `dp[0][j] = costs[0][j]`.
  - The answer is `min(dp[n-1])`.

---

## Python Example

```python
def min_cost(costs):
    if not costs or not costs[0]:
        return 0
    n, k = len(costs), len(costs[0])
    dp = [cost for cost in costs[0]]
    for i in range(1, n):
        new_dp = [0]*k
        for j in range(k):
            new_dp[j] = costs[i][j] + min(dp[c] for c in range(k) if c != j)
        dp = new_dp
    return min(dp)

# Example usage:
costs = [
    [17, 2, 17],
    [16, 16, 5],
    [14, 3, 19]
]
print(min_cost(costs))  # Output: 10
```

---

## Complexity Analysis

- **Time:** O(n * k²) (can be optimized to O(n * k) for k > 2)
- **Space:** O(k) (using rolling arrays)

---

## Applications

- Scheduling with constraints
- Resource allocation problems
- Graph coloring variants

---

## Useful Links

- [Paint House — LeetCode #256](https://leetcode.com/problems/paint-house/)
- [Paint House II — LeetCode #265 (k > 3)](https://leetcode.com/problems/paint-house-ii/)
- [GeeksforGeeks: Paint House Problem](https://www.geeksforgeeks.org/paint-house-algorithm/)

---

## LeetCode Practice

| Difficulty | Problem             | Link                                                                |
|------------|---------------------|---------------------------------------------------------------------|
| Medium     | Paint House         | [#256 Paint House](https://leetcode.com/problems/paint-house/)      |
| Hard       | Paint House II      | [#265 Paint House II](https://leetcode.com/problems/paint-house-ii/)|