# Bit Masking

## Problem Description

Bit masking is a technique for manipulating individual bits of a number using bitwise operations (AND, OR, XOR, NOT, shifts). A “mask” is a number where certain bits are set to 1 or 0, allowing you to select, change, or check specific bits in another number.

---

## Where It Works

- Storing and modifying multiple boolean flags in a single integer (e.g., user permissions, object states).
- Memory and speed optimization in handling large data sets.
- Generating all subsets (power set) using bit representations.
- Graph algorithms and dynamic programming over subsets.
- Games, cryptography, low-level hardware work.

---

## Python Example

```python
x = 0b1010  # 10 in decimal

# Set the 2nd bit (counting from 0)
x = x | (1 << 2)
print(bin(x))  # 0b1110

# Check if the 3rd bit is set
is_set = (x >> 3) & 1
print(is_set)  # 1 (bit is set)

# Clear the 1st bit
x = x & ~(1 << 1)
print(bin(x))  # 0b1100
```

---

## How It Works

1. **Set a bit:** `x | (1 << i)` — sets the i-th bit to 1.
2. **Clear a bit:** `x & ~(1 << i)` — clears the i-th bit to 0.
3. **Check a bit:** `(x >> i) & 1` — returns the value of the i-th bit (0 or 1).
4. **Flip a bit:** `x ^ (1 << i)` — toggles the i-th bit.

---

## Complexity

- **Time:** O(1) for main operations (set, clear, check).
- **Space:** O(1) if no additional data is stored.

---

## Real-Life Applications

- Representing subsets (e.g., knapsack, traveling salesman).
- Compact state storage (as opposed to boolean arrays).
- User permissions, feature flags, access control.

---

## Useful Links

- [Bit Manipulation — LeetCode](https://leetcode.com/tag/bit-manipulation/)
- [Bit Masks — Wikipedia](https://en.wikipedia.org/wiki/Mask_(computing))
- [Bitwise Operators in Python — Real Python](https://realpython.com/python-bitwise-operators/)

---

## LeetCode Practice

| Difficulty | Problem                                 | Link                                                            |
|------------|-----------------------------------------|-----------------------------------------------------------------|
| Medium     | Subsets                                 | [#78 Subsets](https://leetcode.com/problems/subsets/)           |
| Medium     | Single Number                           | [#136 Single Number](https://leetcode.com/problems/single-number/) |
| Medium     | Counting Bits                           | [#338 Counting Bits](https://leetcode.com/problems/counting-bits/) |
| Medium     | Bitwise AND of Numbers Range            | [#201 Bitwise AND](https://leetcode.com/problems/bitwise-and-of-numbers-range/) |

---