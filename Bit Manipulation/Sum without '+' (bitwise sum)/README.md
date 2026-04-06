# Sum Without '+' (Bitwise Sum)

## Problem Description

Given two integers `a` and `b`, compute their sum without using the `+` or `-` operators. Only bitwise operations are allowed.

---

## Approach

We use bitwise operations to simulate addition:

- **XOR (`^`)** computes the sum of each bit without carrying.
- **AND (`&`)** followed by left shift (`<< 1`) computes the carry bits.
- Repeat the process: the sum becomes the new `a`, the carry becomes the new `b`.
- Continue until the carry is zero.

---

## Python Example

```python
def getSum(a, b):
    MAX = 0xFFFFFFFF
    MASK = 0x7FFFFFFF
    while b != 0:
        carry = (a & b) << 1
        a = (a ^ b) & MAX
        b = carry & MAX
    # Handle negative values
    return a if a <= MASK else ~(a ^ MAX)

# Example:
print(getSum(2, 3))    # 5
print(getSum(-1, 1))   # 0
```

---

## How It Works

- XOR adds bits ignoring carries.
- AND and shift find where carries should be added.
- Loop continues until no carry remains.
- For negative numbers, results are masked to emulate 32-bit signed integers (as in many coding platforms).

---

## Applications

- Implementing addition in low-level hardware or custom arithmetic logic.
- Interview problems focused on bitwise manipulation and constraint-based coding.

---

## Useful Links

- [LeetCode #371 — Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)
- [Bitwise operation — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

---