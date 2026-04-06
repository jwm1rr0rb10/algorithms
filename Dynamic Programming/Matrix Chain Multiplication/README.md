# Matrix Chain Multiplication (MCM) — Dynamic Programming

## Problem Description

Given an array of dimensions p for a chain of n matrices A₁, A₂, ..., Aₙ, where the dimensions of Aᵢ are p[i-1] x p[i].  
Find an order of multiplication (parenthesization) that minimizes the total number of scalar multiplications.

**Example:**  
Input: p = [40, 20, 30, 10, 30] (matrices: 40x20, 20x30, 30x10, 10x30)  
Output: 26000  
Explanation: The best parenthesization is ((A₁×A₂)×(A₃×A₄)), minimum multiplications is 26000.

---

## Algorithm Idea and Approach

- Use dynamic programming:
  - Let `dp[i][j]` be the minimum number of multiplications needed to multiply matrices Aᵢ through Aⱼ.
  - For each chain length, try all possible splits between i and j.
  - Recursive formula:  
    `dp[i][j] = min(dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j])` for i ≤ k < j.
  - Base case: dp[i][i] = 0 (one matrix, no multiplication).

---

## Python Example

```python
def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for l in range(2, n + 1):        # chain length
        for i in range(1, n - l + 2):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[1][n]

# Example usage:
p = [40, 20, 30, 10, 30]
print(matrix_chain_order(p))  # Output: 26000
```

---

## Complexity Analysis

- **Time:** O(n³)
- **Space:** O(n²)

---

## Applications

- Matrix multiplication optimization
- Compiler optimizations for expressions
- Planning computations in linear algebra and graphs

---

## Useful Links

- [Matrix Chain Multiplication — LeetCode](https://leetcode.com/problems/minimum-cost-to-multiply-matrices/)
- [MCM — GeeksforGeeks](https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/)
- [Wikipedia: Matrix Chain Multiplication](https://en.wikipedia.org/wiki/Matrix_chain_multiplication)

---

## LeetCode Practice

| Difficulty | Problem                        | Link                                                                            |
|------------|-------------------------------|---------------------------------------------------------------------------------|
| Hard       | Minimum Cost to Multiply Matrices | [#312 Minimum Cost to Multiply Matrices](https://leetcode.com/problems/minimum-cost-to-multiply-matrices/)|
| Hard       | Burst Balloons (MCM analog)    | [#312 Burst Balloons](https://leetcode.com/problems/burst-balloons/)            |