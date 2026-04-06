# Find Rightmost Set Bit

## Problem Description

Given an integer `n`, find the position (index) of its rightmost set bit (the least significant bit that is set to 1).  
The index is usually counted from 0 (rightmost bit is position 0).

**Example:**  
- `n = 18` (`10010₂`) → rightmost set bit at index 1  
- `n = 12` (`1100₂`) → index 2  
- `n = 0b100000` → index 5

---

## Idea and Approach

### 1. Get the rightmost set bit as a mask

You can isolate the rightmost set bit with:

```python
rightmost = n & -n
```

- `-n` is the two's complement of `n` (all bits inverted plus one).
- The result is a mask with only the rightmost set bit as 1, all others are 0.

### 2. Find the index of the rightmost set bit

To get the index (position) of this bit:

#### a) Using a loop

```python
def rightmost_set_bit_index(n):
    if n == 0:
        return -1  # No set bits
    pos = 0
    while (n & 1) == 0:
        n >>= 1
        pos += 1
    return pos

# Examples:
print(rightmost_set_bit_index(18))  # 1
print(rightmost_set_bit_index(12))  # 2
print(rightmost_set_bit_index(32))  # 5
```

#### b) Using `bit_length`

Alternatively, you can use Python's `bit_length` and the mask:

```python
def rightmost_set_bit_index(n):
    if n == 0:
        return -1
    mask = n & -n
    return mask.bit_length() - 1
```

---

## How It Works

For `n = 18` (`10010₂`):

- `-n`: two's complement of 18 is `01110₂` (in 5 bits).
- `n & -n = 10010₂ & 01110₂ = 00010₂` (which is 2), so bit at index 1.

---

## Table: Examples

| n    | Binary   | Rightmost set bit (mask) | Index |
|------|----------|--------------------------|-------|
| 18   | 10010    | 00010 (2)                | 1     |
| 12   | 01100    | 00100 (4)                | 2     |
| 32   | 100000   | 100000 (32)              | 5     |
| 0    | 00000    | 00000 (0)                | -1    |

---

## Applications

- Bit manipulation and optimization
- Finding subset masks
- Algorithms in combinatorics and dynamic programming
- Low-level hardware interfacing

---

## Useful Links

- [Bitwise operations — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)
- [Rightmost set bit — GeeksforGeeks](https://www.geeksforgeeks.org/position-of-rightmost-set-bit/)

---