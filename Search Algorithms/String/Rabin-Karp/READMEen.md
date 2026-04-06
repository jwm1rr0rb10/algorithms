# Rabin-Karp Algorithm

## Where is it used?

**Rabin-Karp** is a substring search algorithm commonly used for:
- Finding all occurrences of a pattern within a text.
- Plagiarism detection (finding matching fragments in large documents).
- Searching for multiple patterns simultaneously (with modifications).
- Fast searching in DNA sequences or other bioinformatics tasks requiring substring matching.

---

## Time and Space Complexity

- **Time (Average/Expected case):** O(n + m), where n is the text length and m is the pattern length.
    - The algorithm leverages hashing, so hash comparisons are fast.
    - In the worst case (all hashes match but strings differ), it may degrade to O(n·m).
- **Space:** O(1) (excluding storage for the text and pattern).
    - Sometimes counted as O(m) for storing the pattern and O(1) for current hashes.

---

## How it Works

1. Compute the hash of the pattern.
2. Compute the hash of the first window of the same length in the text.
3. Compare hashes — if they match, verify by comparing the actual strings.
4. Slide the window by one character and update the hash using a "rolling hash" (efficient update).
5. Repeat until the end of the text.

---

## Python Example with Explanation

```python
def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return []

    base = 256  # Number of possible characters
    mod = 10**9 + 7  # Large prime to avoid overflow

    pattern_hash = 0
    window_hash = 0
    h = 1  # base^(m-1) % mod

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        window_hash = (base * window_hash + ord(text[i])) % mod

    result = []
    for i in range(n - m + 1):
        # If the hashes match, do a direct string comparison
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                result.append(i)
        # Calculate hash for next window
        if i < n - m:
            window_hash = (base * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
            if window_hash < 0:
                window_hash += mod
    return result

# Example usage:
text = "abracadabra"
pattern = "abra"
print(rabin_karp(text, pattern))  # Output: [0, 7]
```

### Explanation

- `base` is the number of possible characters (e.g., 256 for ASCII).
- `mod` is a large prime number to reduce hash collision and avoid overflow.
- `h` helps efficiently "remove" the first character from the rolling hash.
- Initially, hashes for the pattern and the first window are computed.
- For each window:
    - If the hashes match, perform a character-by-character check.
    - The rolling hash allows quick computation of the next window's hash.
- The function returns a list of indices where the pattern occurs in the text.

---

