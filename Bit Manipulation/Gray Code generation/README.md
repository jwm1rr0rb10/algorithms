# Gray Code Generation

## Problem Description

Generate the sequence of n-bit Gray codes.  
A Gray code sequence is a list of all `2^n` binary numbers such that each successive number differs from the previous by exactly one bit.

**Example for n = 2:**
- 00
- 01
- 11
- 10

**Example for n = 3:**
- 000
- 001
- 011
- 010
- 110
- 111
- 101
- 100

---

## Idea and Approach

- For any integer `i`, the n-bit Gray code value is calculated as:  
  `gray = i ^ (i >> 1)`  
  where `^` is bitwise XOR and `>>` is right shift.
- To generate the full sequence, loop through all `i` from 0 to `2^n - 1` and compute `gray` for each.

---

## Python Example

```python
def gray_code_sequence(n):
    res = []
    for i in range(1 << n):  # 1 << n == 2^n
        res.append(i ^ (i >> 1))
    return res

# Example usage:
print(gray_code_sequence(2))  # [0, 1, 3, 2]
print(gray_code_sequence(3))  # [0, 1, 3, 2, 6, 7, 5, 4]

# To print as binary with leading zeros:
n = 3
for x in gray_code_sequence(n):
    print(f"{x:03b}")
```

---

## How It Works

- Each next value in the Gray code sequence differs from the previous by only one bit.
- Useful for minimizing errors in digital encoding and data transmission.

---

## Table: Examples

| i (dec) | i (bin) | i >> 1 (bin) | Gray code (bin) | Gray code (dec) |
|---------|---------|--------------|-----------------|-----------------|
|   0     | 000     | 000          | 000             | 0               |
|   1     | 001     | 000          | 001             | 1               |
|   2     | 010     | 001          | 011             | 3               |
|   3     | 011     | 001          | 010             | 2               |
|   4     | 100     | 010          | 110             | 6               |
|   5     | 101     | 010          | 111             | 7               |
|   6     | 110     | 011          | 101             | 5               |
|   7     | 111     | 011          | 100             | 4               |

---

## Applications

- Error minimization in analog-to-digital conversion (ADCs)
- Rotary encoders
- Combinatorial generation with minimal change
- Digital hardware design

---

## Useful Links

- [Gray code — Wikipedia](https://en.wikipedia.org/wiki/Gray_code)
- [LeetCode #89 — Gray Code](https://leetcode.com/problems/gray-code/)

---