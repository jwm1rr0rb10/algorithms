# Longest Common Subsequence (LCS) — Dynamic Programming

## Problem Description

Given two strings, find the length of their longest common subsequence (LCS): the longest sequence of characters that appears in both strings in the same order (not necessarily consecutively).

**Example:**  
Input:  
A = "ABCBDAB"  
B = "BDCAB"  
Output: 4  
Explanation: One possible LCS is "BCAB" (or "BDAB").

---

## Algorithm Idea and Approach

- Use dynamic programming:
  - Let `dp[i][j]` be the length of the LCS for the first `i` characters of A and first `j` characters of B.
  - If A[i-1] == B[j-1]:  
    dp[i][j] = dp[i-1][j-1] + 1
  - Else:  
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

---

## Python Example

```python
def lcs(a: str, b: str) -> int:
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

# Example usage:
a = "ABCBDAB"
b = "BDCAB"
print(lcs(a, b))  # Output: 4
```

---

## Restoring the LCS Sequence

```python
def lcs_restore(a: str, b: str) -> str:
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    res = []
    i, j = n, m
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            res.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(res))

# Example:
print(lcs_restore(a, b))  # For example, "BCAB"
```

---

## Complexity Analysis

- **Time:** O(n * m)
- **Space:** O(n * m), can be optimized to O(min(n, m)) if you only need the length.

---

## Applications

- Text/file comparison (diff, git)
- Bioinformatics (DNA/RNA sequence alignment)
- Pattern similarity search
- Plagiarism detection and spell correction

---

## Useful Links

- [LCS — LeetCode](https://leetcode.com/problems/longest-common-subsequence/)
- [LCS — GeeksforGeeks](https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/)
- [Wikipedia: LCS](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)

---

## LeetCode Practice

| Difficulty | Problem                        | Link                                                                            |
|------------|-------------------------------|---------------------------------------------------------------------------------|
| Medium     | Longest Common Subsequence     | [#1143 Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)|
| Medium     | Delete Operation for Two Strings | [#583 Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) |
| Medium     | Uncrossed Lines                | [#1035 Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines/)         |