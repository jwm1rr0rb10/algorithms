# Knuth-Morris-Pratt (KMP) Algorithm

## Where is it used?

**KMP (Knuth-Morris-Pratt)** is an efficient substring search algorithm commonly used for:
- Finding all occurrences of a pattern within a text.
- String processing in editors, compilers, and bioinformatics (e.g., DNA search).
- Any tasks where fast and guaranteed-efficient scanning for substrings is required.

---

## Time and Space Complexity

- **Time:** O(n + m), where n is the text length and m is the pattern length.
    - O(m) for building the prefix function.
    - O(n) for the search itself.
- **Space:** O(m) — for storing the prefix function.

---

## How it Works

1. **Build the prefix function** (failure function) for the pattern:
    - For each position in the pattern, compute the length of the longest proper prefix which is also a suffix for the substring ending at that position.
2. **Search for the pattern in the text**:
    - Using the prefix function, when a mismatch occurs, do not return to the start of the pattern, but "jump" to the next possible position.
    - This avoids re-checking characters that are known to match.

---

## Python Example with Explanation

```python
def compute_prefix_function(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0

    for i in range(1, m):
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
    return lps

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return []
    lps = compute_prefix_function(pattern)
    result = []
    i = j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                result.append(i - m)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result

# Example usage:
text = "ababcababcabc"
pattern = "ababc"
print(kmp_search(text, pattern))  # Output: [0, 5]
```

### Explanation

- First, the lps array (longest proper prefix which is also suffix, i.e., the prefix function) is built.
- The main loop compares text and pattern characters. If they match, both indices are incremented.
- If the end of the pattern is reached (j == m), a match is found and the index is added to the result.
- On mismatch, lps is used to avoid returning to the start of the pattern and instead jump to the next potential match.
- The function returns a list of indices where the pattern is found.

---
