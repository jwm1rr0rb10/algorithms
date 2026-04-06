# Longest Palindromic Substring (LPS) — Dynamic Programming and Center Expansion

## Problem Description

Given a string, find its longest palindromic substring (a substring that reads the same forwards and backwards).

**Example:**  
Input: "babad"  
Output: "bab"  
Note: "aba" is also a valid answer (both length 3).

---

## Algorithm Idea and Approach

- Classic approach is dynamic programming:
  - Let `dp[i][j]` be True if s[i:j+1] is a palindrome.
  - Base cases: all substrings of length 1 are palindromes; length 2 are palindromes if s[i] == s[j].
  - For longer substrings:  
    s[i] == s[j] and dp[i+1][j-1] is True.
- A faster and simpler approach is "expand around center".

---

## Python Example (Expand Around Center)

```python
def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    start, max_len = 0, 1
    n = len(s)
    for i in range(n):
        # Odd length palindrome
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                start, max_len = l, r - l + 1
            l -= 1
            r += 1
        # Even length palindrome
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                start, max_len = l, r - l + 1
            l -= 1
            r += 1
    return s[start:start + max_len]

# Example usage:
print(longestPalindrome("babad"))  # Output: "bab" or "aba"
```

---

## Complexity Analysis

- **Time:** O(n^2)
- **Space:** O(1) (expand around center), O(n^2) (DP)

---

## Applications

- String pattern matching
- Symmetry detection in data
- Text analysis and search

---

## Useful Links

- [Longest Palindromic Substring — LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)
- [LPS — GeeksforGeeks](https://www.geeksforgeeks.org/longest-palindromic-substring/)
- [Wikipedia: Palindrome](https://en.wikipedia.org/wiki/Palindrome)

---

## LeetCode Practice

| Difficulty | Problem                        | Link                                                                            |
|------------|-------------------------------|---------------------------------------------------------------------------------|
| Medium     | Longest Palindromic Substring | [#5 Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)|
| Medium     | Palindromic Substrings        | [#647 Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)|