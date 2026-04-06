# Clear ith Bit

## Problem Description

Given an integer `n` and a bit position `i` (with 0-based indexing from the right, where the least significant bit is index 0), clear the ith bit in `n` (set it to 0), leaving all other bits unchanged.

**Example:**  
Input: `n = 13` (binary: `1101`), `i = 2`  
Output: `n = 9` (binary: `1001`)

---

## Idea and Approach

1. **Create a mask** where only the ith bit is 0 and all other bits are 1.
2. **Apply bitwise AND (`&`)** between `n` and the mask.
3. This operation zeros out just the ith bit and keeps all other bits intact.

**How to make the mask:**
- Compute `(1 << i)`: a number with only the ith bit set to 1.
- Invert it with `~(1 << i)`: all bits become 1 except the ith, which is 0.

---

## Python Example

```python
def clear_ith_bit(n, i):
    mask = ~(1 << i)
    return n & mask

# Example usage:
n = 13      # 1101
i = 2
print(clear_ith_bit(n, i))  # 9 (1001)
```

---

## How It Works

1. 13 in binary: `1101`
2. i = 2 (third bit from the right, counting from 0)
3. Mask:
   - `(1 << 2)` = `0b100` (4)
   - `~4` = `...11111011` (all ones except the third bit, which is zero)
4. `1101 & 1011 = 1001` (which is 9)

---

## Table: Examples of Clearing Bits

| n    | bin(n) | i | Result (bin) | Result (dec) |
|------|--------|---|--------------|--------------|
| 13   | 1101   | 2 | 1001         | 9            |
| 15   | 1111   | 0 | 1110         | 14           |
| 15   | 1111   | 1 | 1101         | 13           |
| 15   | 1111   | 2 | 1011         | 11           |
| 8    | 1000   | 3 | 0000         | 0            |

---

## Applications

- Managing bit flags and states.
- Optimizing storage of settings.
- Modifying individual control bits in protocols, registers, or low-level data structures.
- Microcontroller register programming.

---

## Useful Links

- [Bit Manipulation — Wikipedia](https://en.wikipedia.org/wiki/Bit_manipulation)
- [Bitwise operations — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

---