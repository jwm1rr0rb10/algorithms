# XOR Swap Trick

## Problem Description

Swap the values of two variables `a` and `b` without using a temporary variable, only using bitwise operations.

---

## Approach

The classic XOR swap algorithm works as follows:

1. `a = a ^ b`
2. `b = a ^ b`  (now b is the original value of a)
3. `a = a ^ b`  (now a is the original value of b)

No extra variables are needed.

---

## Python Example

```python
a = 5
b = 9

# XOR swap:
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)  # Output: 9 5
```

---

## How It Works

- After `a = a ^ b`, `a` holds the XOR of both values.
- `b = a ^ b` extracts the original `a` value into `b`.
- `a = a ^ b` extracts the original `b` value into `a`.

---

## Caveats

- If `a` and `b` refer to the same memory location (i.e., the same variable), this method will zero out the value.
- In high-level languages, this is mostly of academic or interview interest; swapping with a temporary variable is usually clearer and just as efficient.

---

## Applications

- Low-level programming, embedded systems, interview puzzles.
- Situations with severe memory constraints (rare).

---

## Useful Links

- [XOR swap algorithm — Wikipedia](https://en.wikipedia.org/wiki/XOR_swap_algorithm)
- [Bitwise operation — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

---