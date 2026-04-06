# Maximum Product of Word Lengths

## Problem Description

Given a list of words, find the maximum value of `length(word1) * length(word2)` where the two words do not share any common letters. Return 0 if no such pair exists.

---

## Approach

1. **Bitmask Representation:**  
   For each word, create a 26-bit integer mask (for letters 'a' to 'z'). Set the bit if the word contains the letter.
2. **Pairwise Comparison:**  
   For all pairs of words, check if their masks have no bits in common (i.e., `mask1 & mask2 == 0`). If so, calculate the product of their lengths and update the maximum.

---

## Python Example

```python
def maxProduct(words):
    n = len(words)
    masks = [0] * n
    lengths = [len(word) for word in words]
    
    for i, word in enumerate(words):
        for c in word:
            masks[i] |= 1 << (ord(c) - ord('a'))
    
    max_prod = 0
    for i in range(n):
        for j in range(i + 1, n):
            if masks[i] & masks[j] == 0:
                max_prod = max(max_prod, lengths[i] * lengths[j])
    return max_prod

# Example usage:
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print(maxProduct(words))  # Output: 16 ("abcw" and "xtfn")
```

---

## How It Works

- **Bitmasking** efficiently checks for common letters between any two words.
- **Pairwise products** are computed only if words are disjoint in letters.

---

## Example Table

| Word    | Mask (binary)      | Length |
|---------|--------------------|--------|
| abcw    | 0000000000000000000111 | 4      |
| xtfn    | 1001001000000000000000 | 4      |
| ...     | ...                | ...    |

("abcw" and "xtfn" have no common set bits, so their product is 16.)

---

## Applications

- Feature selection with mutual exclusion
- Scheduling tasks without resource conflicts
- Optimization problems involving set disjointness

---

## Useful Links

- [LeetCode #318 — Maximum Product of Word Lengths](https://leetcode.com/problems/maximum-product-of-word-lengths/)
- [Bitmasking overview — Wikipedia](https://en.wikipedia.org/wiki/Mask_(computing))

---