# Single Number I

## Problem Description

Given a non-empty array of integers, every element appears exactly twice except for one. Find that single one.

---

## Approach

The optimal way is to use the bitwise XOR operation:

- `a ^ a = 0`
- `a ^ 0 = a`
- XOR is commutative and associative

If you XOR all the elements, all pairs cancel out, and the result is the unique element.

---

## Python Example

```python
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example:
nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # Output: 4
```

---

## How It Works

- XOR-ing identical numbers gives 0.
- XOR with 0 keeps the number unchanged.
- All duplicates become 0, leaving only the single number.

---

## Applications

- Finding unique elements in a list of duplicates.
- Bit manipulation tricks in interview problems.
- Fast, memory-efficient data integrity checks.

---

## Useful Links

- [LeetCode #136 — Single Number](https://leetcode.com/problems/single-number/)
- [Bitwise operation — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

---