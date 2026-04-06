# Divide Two Integers (Bitwise Division)

## Problem Description

Given two integers, `dividend` and `divisor`, compute their integer division (`dividend // divisor`) using only bitwise operations (no `/`, `//`, `%`, or `*`).

---

## Idea and Approach

- Division can be performed by repeated subtraction, but to make it efficient, we use bit shifting to subtract the largest possible multiples of the divisor in each step.
- This approach is similar to manual long division, but in binary.
- The sign of the result is negative if one operand is negative and the other is positive.

---

## Python Example

```python
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("division by zero")
    negative = (dividend < 0) != (divisor < 0)
    a, b = abs(dividend), abs(divisor)
    result = 0
    for i in range(31, -1, -1):
        if (a >> i) >= b:
            result += 1 << i
            a -= b << i
    return -result if negative else result

# Examples:
print(divide(13, 3))    # 4
print(divide(-15, 4))   # -3
print(divide(20, -5))   # -4
print(divide(-100, -7)) # 14
```

---

## How It Works

1. Take the absolute values of both numbers.
2. For each bit position from highest to lowest:
    - If `divisor << i` can be subtracted from the current dividend, do so and add `1 << i` to the result.
3. Apply the sign to the result depending on inputs.

---

## Table: Examples

| Dividend | Divisor | Result |
|----------|---------|--------|
|   13     |   3     |   4    |
|  -15     |   4     |  -3    |
|   20     |  -5     |  -4    |
| -100     |  -7     |  14    |

---

## Notes

- Division by zero is not allowed (`ZeroDivisionError` is raised).
- For 32-bit signed integers, you may need to clamp the result to `[-2^31, 2^31-1]` if required by the task.
- This method works for both positive and negative numbers.

---

## Applications

- Low-level libraries and embedded systems where division instruction is unavailable or slow.
- Interview and algorithmic tasks to test understanding of bitwise operations.

---

## Useful Links

- [Bitwise operations — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)
- [LeetCode #29 — Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

---