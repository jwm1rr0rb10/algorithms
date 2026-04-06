# Count Set Bits (Hamming Weight)

## Problem Description

Given a non-negative integer `n`, count the number of bits that are set to 1 in its binary representation.  
This count is also known as the **Hamming weight**.

**Example:**  
- Input: `n = 13` (binary: `1101`)  
- Output: `3` (since there are three 1's)

---

## Idea and Approach

There are several ways to count the number of set bits in an integer:

### 1. Iterative (check each bit)

- While `n` is not zero:
  - Add `n & 1` to a counter (checks if the least significant bit is set).
  - Shift `n` right by 1.

```python
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

### 2. Brian Kernighan’s Algorithm (fastest for sparse bits)

- While `n` is not zero:
  - Do `n = n & (n - 1)` (removes the lowest set bit).
  - Increment the counter.

```python
def count_set_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
```

### 3. Python Built-In

- For Python 3.10 and above:  
  `n.bit_count()`
- For older versions:  
  `bin(n).count('1')`

---

## Table: Examples

| n    | bin(n) | set bits |
|------|--------|----------|
| 0    | 0      | 0        |
| 1    | 1      | 1        |
| 2    | 10     | 1        |
| 3    | 11     | 2        |
| 4    | 100    | 1        |
| 5    | 101    | 2        |
| 6    | 110    | 2        |
| 7    | 111    | 3        |
| 8    | 1000   | 1        |
| 13   | 1101   | 3        |

---

## Applications

- Checking the number of flags set in a bitmask.
- Population count in cryptography and error-correcting codes.
- Optimization and bit-parallel algorithms.

---

## Complexity

- **Time:** O(number of bits) for the iterative method, O(number of set bits) for the Kernighan method.
- **Space:** O(1)

---

## Useful Links

- [Hamming weight — Wikipedia](https://en.wikipedia.org/wiki/Hamming_weight)
- [Bitwise operations — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)
- [LeetCode #191 — Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

---