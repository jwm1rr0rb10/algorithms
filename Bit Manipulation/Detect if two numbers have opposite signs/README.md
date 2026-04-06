# Detect if Two Numbers Have Opposite Signs

## Problem Description

Given two integers `a` and `b`, determine whether they have opposite signs (i.e., one is positive and the other is negative).

---

## Idea and Approach

- In binary, the sign of an integer is determined by its most significant (leftmost) bit (the sign bit).
- If two numbers have opposite signs, their sign bits will be different.
- The XOR (`^`) operation sets the sign bit of the result to 1 if the sign bits of `a` and `b` are different.
- Thus, if `(a ^ b) < 0`, then `a` and `b` have opposite signs.

---

## Python Example

```python
def have_opposite_signs(a, b):
    return (a ^ b) < 0

# Examples:
print(have_opposite_signs(5, -3))   # True
print(have_opposite_signs(-7, 12))  # True
print(have_opposite_signs(8, 19))   # False
print(have_opposite_signs(-4, -100))# False
```

---

## How It Works

- `^` (XOR) compares each bit of `a` and `b`; for the sign bit, if the signs differ, the result's sign bit becomes 1 (negative number).
- Checking if the result is less than zero (`< 0`) tells you if the original numbers had opposite signs.

---

## Table: Examples

|   a   |   b   | a (bin)    | b (bin)    | a ^ b (bin) | a ^ b < 0? | Opposite Signs? |
|-------|-------|------------|------------|-------------|------------|-----------------|
|  5    |  -3   | 0101       | ...1101    | ...1000     |   True     |      Yes        |
| -7    |  12   | ...1001    | 1100       | ...0101     |   True     |      Yes        |
|  8    |  19   | 1000       | 10011      | 11011       |   False    |      No         |
| -4    | -100  | ...1100    | ...1100100 | ...1101100  |   False    |      No         |

---

## Applications

- Useful in low-level programming, algorithms, and optimizations.
- Quickly checking sign difference without branching.
- Can be used for absolute value calculations, overflow detection, etc.

---

## Useful Links

- [Bitwise operations — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)
- [StackOverflow: Detect if two integers have opposite signs](https://stackoverflow.com/questions/14555607/detect-if-two-integers-have-opposite-signs)

---