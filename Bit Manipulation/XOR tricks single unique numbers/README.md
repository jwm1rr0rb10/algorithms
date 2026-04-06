# XOR Tricks for Single/Unique Numbers

## Problem Description

Bitwise XOR (`^`) is a powerful tool for finding unique or single elements in arrays where others appear in pairs or k-times. Below are common XOR-based techniques:

---

## Find the Single Number (All Others Appear Twice)

If every number appears twice except one, XOR all elements:
- All pairs cancel out (`a ^ a = 0`), leaving the unique number.

**Python Example:**
```python
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example:
print(singleNumber([2,2,1]))  # Output: 1
```

---

## Find Two Unique Numbers (All Others Appear Twice)

If exactly two numbers appear once, rest appear twice:
1. XOR all numbers to get `a ^ b`.
2. Find a bit where `a` and `b` differ.
3. Partition numbers by that bit, XOR separately.

**Python Example:**
```python
def singleNumber(nums):
    xor = 0
    for num in nums:
        xor ^= num
    diff = xor & -xor
    a = b = 0
    for num in nums:
        if num & diff:
            a ^= num
        else:
            b ^= num
    return [a, b]

# Example:
print(singleNumber([1,2,1,3,2,5]))  # Output: [3, 5] (order may vary)
```

---

## Find Single Number (All Others Appear k Times)

If every number appears k times except one:
- For each bit position, count the number of 1s.
- If count % k != 0, that bit belongs to the unique number.

**Python Example (for k = 3):**
```python
def singleNumber(nums):
    result = 0
    for i in range(32):
        count = 0
        for num in nums:
            if (num >> i) & 1:
                count += 1
        if count % 3:
            if i == 31:
                result -= (1 << 31)
            else:
                result |= (1 << i)
    return result

# Example:
print(singleNumber([2,2,3,2]))  # Output: 3
```

---

## Why It Works

- XOR is commutative and associative.
- `a ^ a = 0`, so pairs cancel out.
- For k-times, bitwise counting captures the unique pattern.

---

## Applications

- Data integrity checks
- Finding outliers in large datasets
- Coding interviews and algorithm challenges

---

## Useful Links

- [LeetCode #136 — Single Number](https://leetcode.com/problems/single-number/)
- [LeetCode #260 — Single Number III](https://leetcode.com/problems/single-number-iii/)
- [LeetCode #137 — Single Number II](https://leetcode.com/problems/single-number-ii/)
- [Bitwise operation — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

---