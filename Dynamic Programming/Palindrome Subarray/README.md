# Palindrome Subarray — Dynamic Programming

## Problem Description

Given an array (or string), find the longest (or count of) contiguous subarrays (substrings) that are palindromes.  
A palindrome is a sequence that reads the same backward as forward.

Variants:
- Find the longest palindromic subarray (substring).
- Count all palindromic subarrays (substrings).

---

## Algorithm Idea and Approach

### 1. Expand Around Center (for strings)

- For each index, expand as center for both odd and even length palindromes.
- Time: O(n²), Space: O(1)

### 2. Dynamic Programming Table

- Let `dp[i][j]` be True if the subarray/string from i to j is a palindrome.
- Fill the table for all substrings of length 1 (True), 2 (check equality), and greater (check ends and `dp[i+1][j-1]`).
- Time: O(n²), Space: O(n²)

---

## Python Example: Count Palindromic Substrings

```python
def count_palindromic_substrings(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    count = 0
    for l in range(1, n+1):  # length of substring
        for i in range(n - l + 1):
            j = i + l - 1
            if l == 1:
                dp[i][j] = True
            elif l == 2:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
            if dp[i][j]:
                count += 1
    return count

# Example usage:
s = "abba"
print(count_palindromic_substrings(s))  # Output: 6
# ("a", "b", "b", "a", "bb", "abba")
```

---

## Python Example: Longest Palindromic Substring

```python
def longest_palindrome(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    start, maxlen = 0, 1
    for i in range(n):
        dp[i][i] = True
    for l in range(2, n+1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j]:
                if l == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if l > maxlen:
                        start, maxlen = i, l
    return s[start:start+maxlen]

# Example usage:
s = "babad"
print(longest_palindrome(s))  # Output: "bab" or "aba"
```

---

## Complexity Analysis

- **Time:** O(n²)
- **Space:** O(n²)

---

## Applications

- String processing and search
- DNA sequence analysis
- Pattern recognition

---

## Useful Links

- [LeetCode #5: Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [LeetCode #647: Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
- [GeeksforGeeks: Count Palindromic Substrings](https://www.geeksforgeeks.org/count-palindrome-sub-strings-string/)

---

## LeetCode Practice

| Difficulty | Problem                        | Link                                                                         |
|------------|-------------------------------|------------------------------------------------------------------------------|
| Medium     | Longest Palindromic Substring | [#5 Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) |
| Medium     | Palindromic Substrings        | [#647 Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)             |