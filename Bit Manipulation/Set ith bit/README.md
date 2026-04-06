# Set ith Bit

## Problem Description

Given an integer `n` and a bit position `i` (0-based, counting from the least significant bit), set the ith bit of `n` to `1`. All other bits should remain unchanged.

---

## Approach

- Use the bitwise OR operation with a mask that has only the ith bit set to 1.
- The mask is created by shifting `1` to the left by `i` positions: `1 << i`.
- Applying `n | (1 << i)` sets the ith bit of `n` to 1, regardless of its previous value.

---

## Python Example

```python
def set_ith_bit(n, i):
    return n | (1 << i)

# Examples:
print(bin(set_ith_bit(0b1010, 1)))  # 0b1010 | 0b0010 => 0b1010 (bit 1 already set)
print(bin(set_ith_bit(0b1010, 2)))  # 0b1010 | 0b0100 => 0b1110 (bit 2 set)
print(bin(set_ith_bit(0b0, 4)))     # 0b0000 | 0b10000 => 0b10000
```

---

## How It Works

- `1 << i` creates a mask with only the ith bit set.
- Bitwise OR (`|`) ensures that bit is set in `n`; all other bits are unchanged.

---

## Applications

- Setting flags in bitmasks.
- Managing permissions or settings using bitfields.
- Efficiently toggling features or states in low-level programming.

---

## Useful Links

- [Bitwise operations — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

---