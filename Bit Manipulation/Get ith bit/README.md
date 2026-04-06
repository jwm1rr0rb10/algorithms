# Get ith Bit

## Problem Description

Given an integer `n` and an index `i` (bit position, usually starting from 0 — the rightmost bit), determine the value (0 or 1) of the bit at position `i` in the binary representation of `n`.

---

## Idea and Approach

- To get the value of the ith bit, shift `n` right by `i` bits: `n >> i`.
- Then, use bitwise AND with 1: `(n >> i) & 1`.
    - If the result is 1, the bit at position `i` is set.
    - If the result is 0, the bit at position `i` is not set.

---

## Python Example

```python
def get_ith_bit(n, i):
    return (n >> i) & 1

# Examples:
print(get_ith_bit(13, 0))  # 1 (13 = 1101, bit 0 is 1)
print(get_ith_bit(13, 1))  # 0 (bit 1 is 0)
print(get_ith_bit(13, 2))  # 1 (bit 2 is 1)
print(get_ith_bit(13, 3))  # 1 (bit 3 is 1)
```

---

## How It Works

- `n >> i` moves the ith bit to the 0th position.
- `& 1` isolates the least significant bit (0th bit), giving the value (0 or 1) of the original ith bit.

---

## Table: Examples

| n   | Binary | i | get_ith_bit(n, i) | Explanation             |
|-----|--------|---|-------------------|-------------------------|
| 13  | 1101   | 0 | 1                 | rightmost bit is 1      |
| 13  | 1101   | 1 | 0                 | next bit is 0           |
| 13  | 1101   | 2 | 1                 | third bit is 1          |
| 13  | 1101   | 3 | 1                 | leftmost bit is 1       |
| 8   | 1000   | 3 | 1                 | only bit 3 is 1         |
| 8   | 1000   | 2 | 0                 | bits 2,1,0 are 0        |

---

## Applications

- Checking the state of a flag in a bitmask.
- Bitwise algorithms and optimizations.
- Combinatorial problems, feature encoding, permissions.

---

## Useful Links

- [Bitwise operations — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)
- [Python bitwise operators — GeeksforGeeks](https://www.geeksforgeeks.org/python-bitwise-operators/)

---
