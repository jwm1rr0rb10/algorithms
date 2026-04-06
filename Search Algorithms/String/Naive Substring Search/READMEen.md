# Naive Substring Search Algorithm

## Where is it used?

**Naive Substring Search** is the simplest method for finding all occurrences of a pattern in a text.  
It is used:
- For educational purposes, to understand the basics of substring search algorithms.
- For searching in small texts where performance is not critical.
- As a basic solution or a foundation for building more advanced algorithms.

---

## Time and Space Complexity

- **Time:** O((n - m + 1) * m), where n is the length of the text and m is the length of the pattern.
    - In the worst case — O(n·m), especially if the text and pattern consist of repeating characters.
- **Space:** O(1) — requires no extra memory (except for storing the text and pattern).

---

## How it Works

1. For each position `i` from 0 to `n - m` in the text:
    - All characters of the pattern are compared with the corresponding characters in the text.
    - If all characters match, the occurrence is found and the index is added to the result.
    - If any character does not match, move to the next position.
2. Repeat until the end of the text.

---

## Python Example with Explanation

```python
def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    result = []
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            result.append(i)
    return result

# Example usage:
text = "abababca"
pattern = "ab"
print(naive_search(text, pattern))  # Output: [0, 2, 4]
```

### Explanation

- The outer loop iterates over all possible positions for the pattern within the text.
- The inner loop compares each character of the pattern with the corresponding character in the text.
- If all characters match, the index is added to the result list.
- The function returns a list of all positions where the pattern occurs in the text.

---