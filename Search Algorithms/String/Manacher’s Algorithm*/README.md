# Manacher’s Algorithm

---

## Problem Description

Given a string, find all palindromic substrings in linear time (O(n)), and determine the longest palindromic substring.

---

## Approach

Manacher’s Algorithm finds all palindromic substrings in O(n) time.  
Idea:
- “Expand” palindromes around centers, using info from previously found palindromes.
- Preprocess the string by inserting special characters (like `#`) between all characters and at the ends, so both odd- and even-length palindromes are handled uniformly.

---

## Python Example

```python
def manacher(s):
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n  # p[i]: max radius of palindrome centered at i
    c = r = 0    # c: center of rightmost palindrome, r: its right boundary
    for i in range(n):
        mirr = 2 * c - i
        if i < r:
            p[i] = min(r - i, p[mirr])
        a, b = i + 1 + p[i], i - 1 - p[i]
        while a < n and b >= 0 and t[a] == t[b]:
            p[i] += 1
            a += 1
            b -= 1
        if i + p[i] > r:
            c, r = i, i + p[i]
    max_len = max(p)
    center_index = p.index(max_len)
    start = (center_index - max_len) // 2
    return s[start:start + max_len]

# Example:
s = "babad"
print(manacher(s))  # Output: "bab" or "aba"
```

---

## How It Works

- After preprocessing, all palindromes are of odd length.
- p[i] is the maximum palindrome radius centered at position i.
- Uses symmetry with respect to the center of the rightmost known palindrome to accelerate search.

---

## Applications

- Finding the longest palindromic substring
- Efficient enumeration of all palindromic substrings in O(n)
- Used in string analysis, bioinformatics, data compression, etc.

---

## When to Use

- When you need to find palindromes (especially the longest one) in a string very efficiently (O(n))

---

## When Not to Use

- If you just need to check if a string is a palindrome (O(n) direct check is easier)
- For very short strings, brute-force is fine

---

## Complexity

- **Time:** O(n)
- **Space:** O(n)

---

## Useful Links

- [LeetCode — Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [Manacher’s Algorithm — Wikipedia](https://en.wikipedia.org/wiki/Manacher%27s_algorithm)