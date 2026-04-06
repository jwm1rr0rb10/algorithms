# Z-Algorithm

---

## Problem Description

The Z-algorithm is an efficient method for string matching and pattern processing.  
It computes the Z-array for a string:  
Z[i] is the length of the longest substring starting at `i` that is also a prefix of the string.

Applications:
- Pattern matching (finding all occurrences of a substring)
- Counting repeated substrings
- Fast searching for patterns in text

---

## Approach

The Z-array can be built in O(n) time for a string of length n.  
Idea:
- Maintain a window [l, r] where S[l..r] matches the prefix.
- For each position, try to extend the window as far as possible, reusing previously computed values to avoid redundant comparisons.

---

## Python Example

```python
def z_algorithm(s):
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

# Example:
s = "abacaba"
print(z_algorithm(s))  # Output: [0, 0, 1, 0, 3, 0, 1]
```

---

## How It Works

- z[0] is always 0 (by definition, usually not used).
- If i is inside the current [l, r] window, reuse known values for speed.
- Otherwise, do character-by-character matching.

---

## Applications

- Fast pattern search: concatenate pattern + '$' + text, compute Z-array, and positions where Z[i] == len(pattern) are matches.
- Finding periods and repeated substrings in a string.

---

## When to Use

- When you need fast substring search
- For analyzing periodicity and repeated substrings

---

## When Not to Use

- For very long or complex patterns (other algorithms such as Aho-Corasick or KMP may be more efficient in those cases)

---

## Complexity

- **Time:** O(n)
- **Space:** O(n)

---

## Useful Links

- [Z-Algorithm — Wikipedia](https://en.wikipedia.org/wiki/Z_algorithm)
- [LeetCode — Implement strStr()](https://leetcode.com/problems/implement-strstr/)