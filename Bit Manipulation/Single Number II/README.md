# Single Number II

## Problem Description

Given an integer array `nums`, every element appears three times except for one, which appears exactly once. Find and return the single element that appears only once.

---

## Approach

The optimal solution uses bitwise operations and works in O(n) time and O(1) space.

**Idea:**  
For each bit position (0 to 31), count how many numbers have that bit set. For bits where the count is not divisible by 3, that bit belongs to the unique number.

---

## Python Example

```python
def singleNumber(nums):
    result = 0
    for i in range(32):
        count = 0
        for num in nums:
            if (num >> i) & 1:
                count += 1
        if count % 3:
            # Handle negative numbers for 32 bits
            if i == 31:
                result -= (1 << 31)
            else:
                result |= (1 << i)
    return result

# Example:
nums = [2,2,3,2]
print(singleNumber(nums))  # Output: 3
```

---

## How It Works

- For each bit index, count how many times it is set among all numbers.
- If the count % 3 != 0, then this bit is set in the unique number.
- Edge case for negative numbers is handled by checking the 31st bit (Python integers are unbounded, but LeetCode assumes 32-bit signed).

---

## Applications

- Finding unique elements in arrays with all others appearing k times
- Bit manipulation interview problems
- Data integrity checks

---

## Useful Links

- [LeetCode #137 — Single Number II](https://leetcode.com/problems/single-number-ii/)
- [Bitwise operation — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

---