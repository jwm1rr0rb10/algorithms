# Toggle ith Bit

## Problem Description

Given an integer `n` and a bit position `i` (0-based, counting from the least significant bit), toggle (flip) the ith bit in `n`. All other bits should remain unchanged.

---

## Approach

- Use the bitwise XOR operation (`^`) with a mask that has only the ith bit set.
- The mask is created as `1 << i`.
- The operation `n ^ (1 << i)` flips the ith bit in `n` (1 becomes 0, 0 becomes 1).

---

## Python Example

```python
def toggle_ith_bit(n, i):
    return n ^ (1 << i)

# Examples:
print(bin(toggle_ith_bit(0b1010, 1)))  # 0b1010 ^ 0b0010 => 0b1000 (bit 1 was 1, now 0)
print(bin(toggle_ith_bit(0b1010, 2)))  # 0b1010 ^ 0b0100 => 0b1110 (bit 2 was 0, now 1)
print(bin(toggle_ith_bit(0b0, 3)))     # 0b0000 ^ 0b1000 => 0b1000 (bit 3 was 0, now 1)
```

---

## How It Works

- `1 << i` creates a mask with only the ith bit set.
- XOR (`^`) flips the ith bit: if it was 0, it becomes 1; if it was 1, it becomes 0.

---

## Applications

- Bitmask manipulations
- Toggling flags, settings, or features
- Efficient state switching in games and systems programming

---

## Useful Links

- [Bitwise operations — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

---