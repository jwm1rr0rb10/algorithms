# Palindrome Subsequence — Dynamic Programming

## Problem Description

Given a string (or array), find the longest palindromic subsequence.  
A **subsequence** can skip characters but maintains the original order.

Variants:
- Find the length of the longest palindromic subsequence.
- Reconstruct the subsequence itself.

---

## Algorithm Idea and Approach

- Use dynamic programming:
  - Let `dp[i][j]` be the length of the longest palindromic subsequence in `s[i..j]`.
  - If `s[i] == s[j]`, then `dp[i][j] = dp[i+1][j-1] + 2`.
  - Else, `dp[i][j] = max(dp[i+1][j], dp[i][j-1])`.
  - For substrings of length 1: `dp[i][i] = 1`.
- Fill the DP table for all substrings.

---

## Python Example: Length of Longest Palindromic Subsequence

```python
def longest_palindrome_subseq(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

# Example usage:
s = "bbbab"
print(longest_palindrome_subseq(s))  # Output: 4 ("bbbb")
```

---

## Complexity Analysis

- **Time:** O(n²)
- **Space:** O(n²)

---

## Applications

- DNA/protein sequence analysis
- Text and pattern recognition
- Data compression

---

## Useful Links

- [LeetCode #516: Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
- [GeeksforGeeks: Longest Palindromic Subsequence](https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/)

---

## LeetCode Practice

| Difficulty | Problem                           | Link                                                                 |
|------------|-----------------------------------|----------------------------------------------------------------------|
| Medium     | Longest Palindromic Subsequence   | [#516 Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) |