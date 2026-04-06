# Power of Two Check

## Problem Description

Given an integer `n`, determine if it is a power of two (i.e., can it be written as 2^k for some integer k ≥ 0).

---

## Approach

A number is a power of two if and only if it is positive and has exactly one `1` bit in its binary representation.

**Bit Trick:**  
For any positive integer n,  
if `(n & (n - 1)) == 0`, then n is a power of two.

**Explanation:**  
- In binary, a power of two looks like `100...0`.
- Subtracting 1 flips all bits after the only set bit (and clears that bit).
- Therefore, `n & (n - 1)` will be zero only for powers of two.

---

## Python Example

```python
def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0

# Examples:
print(isPowerOfTwo(1))    # True (2^0)
print(isPowerOfTwo(2))    # True (2^1)
print(isPowerOfTwo(3))    # False
print(isPowerOfTwo(8))    # True (2^3)
print(isPowerOfTwo(0))    # False
print(isPowerOfTwo(-8))   # False
```

---

## How It Works

- Check that n is positive.
- Use the bit trick to detect a single set bit.

---

## Applications

- Fast checks for memory or data alignment
- Optimizing algorithms involving sizes or capacities
- Bitmasking, graphics, and systems programming

---

## Useful Links

- [LeetCode #231 — Power of Two](https://leetcode.com/problems/power-of-two/)
- [Wikipedia — Power of two](https://en.wikipedia.org/wiki/Power_of_two)

---