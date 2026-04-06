# Hamming Distance

## Problem Description

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

**Example:**  
- `x = 3` (011 in binary)  
- `y = 5` (101 in binary)  
- Differ in positions 0 and 2 ⇒ Hamming distance = 2

---

## Idea and Approach

1. XOR the two numbers: `diff = x ^ y`.  
   The result will have 1s in the positions where the bits differ.
2. Count the number of 1s in the result — that is the Hamming distance.

---

## Python Example

```python
def hamming_distance(x, y):
    diff = x ^ y
    count = 0
    while diff:
        count += diff & 1
        diff >>= 1
    return count

# Or, using Python's built-in:
def hamming_distance_fast(x, y):
    return bin(x ^ y).count('1')

# Examples:
print(hamming_distance(3, 5))      # 2
print(hamming_distance(1, 4))      # 2 (001 vs 100)
print(hamming_distance(7, 15))     # 1 (0111 vs 1111: only bit 3 differs)
```

---

## How It Works

- XOR puts 1s in positions where bits differ.
- Counting those 1s gives the answer.

---

## Table: Examples

| x | y | x (bin) | y (bin) | x ^ y (bin) | Hamming Distance |
|---|---|---------|---------|-------------|------------------|
| 3 | 5 | 011     | 101     | 110         | 2                |
| 1 | 4 | 001     | 100     | 101         | 2                |
| 7 |15 | 0111    | 1111    | 1000        | 1                |

---

## Applications

- Error-detecting and error-correcting codes (ECC, parity checks)
- Comparing binary strings, feature masks
- Genetic algorithms, machine learning

---

## Useful Links

- [Hamming distance — Wikipedia](https://en.wikipedia.org/wiki/Hamming_distance)
- [LeetCode #461 — Hamming Distance](https://leetcode.com/problems/hamming-distance/)

---