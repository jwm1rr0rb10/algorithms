# Boyer-Moore Substring Search Algorithm

## Description

**Boyer-Moore** is one of the fastest substring search algorithms. Unlike most other algorithms, it starts comparing from the end of the pattern, which allows it to skip large sections of text and avoid unnecessary comparisons.

## Applications

- Searching in large texts (text editors, search engines)
- Signature search in antivirus and filtering systems
- Bioinformatics (sequence search)
- Data storage and processing systems

## How it Works

1. Preprocesses the pattern, building "bad character" and "good suffix" tables.
2. Compares pattern characters with the text from right to left.
3. On mismatch, uses the tables to shift the pattern as far as possible.
4. Repeats the process until the end of the text.

## Complexity

- Average case: much faster than O(n), often close to O(n / m)
- Worst case: O(n + m)
- Space: O(m + k), where m is the pattern length and k is the alphabet size

## Python Example

```python
def bad_character_table(pattern):
    table = {}
    for i, char in enumerate(pattern):
        table[char] = i
    return table

def boyer_moore_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return []
    bad_char = bad_character_table(pattern)
    result = []
    shift = 0

    while shift <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            result.append(shift)
            shift += m - bad_char.get(text[shift + m], -1) if shift + m < n else 1
        else:
            shift += max(1, j - bad_char.get(text[shift + j], -1))
    return result

# Example usage:
text = "ABAAABCD"
pattern = "ABC"
print(boyer_moore_search(text, pattern))  # Output: [4]
```

## Advantages

- Very fast in practice for long patterns and large texts
- Enables large shifts in the text, reducing the number of comparisons
- Used in standard libraries and industrial solutions

---

If you need more examples or comparisons with other algorithms, feel free to ask!