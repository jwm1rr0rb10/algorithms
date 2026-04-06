# Reverse Bits of an Integer

## Problem Description

Given a 32-bit unsigned integer, reverse its bits and return the resulting integer.

**Example:**  
Input: `43261596` (`00000010100101000001111010011100` in binary)  
Output: `964176192` (`00111001011110000010100101000000` in binary)

---

## Approach

1. **Iterate through all 32 bits** of the number.
2. **Shift the result left by 1** and add the least significant bit of the original number.
3. **Shift the original number right by 1**.
4. Repeat for all 32 bits.

---

## Python Example

```python
def reverseBits(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

# Example usage:
x = 43261596
print(reverseBits(x))  # Output: 964176192
```

---

## How It Works

- Each time, take the rightmost bit of `n` and append it to the left of `result`.
- After 32 iterations, all bits of `n` are reversed in `result`.

---

## Applications

- Bit-level image and signal processing
- Efficient network protocol parsing
- Cryptographic and hash algorithms

---

## Useful Links

- [LeetCode #190 — Reverse Bits](https://leetcode.com/problems/reverse-bits/)
- [Bitwise operations — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

---