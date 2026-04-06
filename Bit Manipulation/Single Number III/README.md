# Single Number III

## Problem Description

Given an integer array `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

---

## Approach

The optimal solution uses bitwise operations:

1. **XOR All Numbers:**  
   XOR all the elements in the array. The result will be `a ^ b`, where `a` and `b` are the two unique numbers (since all other numbers XOR to zero).

2. **Find a Differentiating Bit:**  
   Find any set bit (1) in the XOR result. This bit is set in one unique number and not in the other.

3. **Partition and XOR:**  
   Partition the numbers into two groups — one group with this bit set, another with it unset. XOR-ing each group separately yields the two unique numbers.

---

## Python Example

```python
def singleNumber(nums):
    xor = 0
    for num in nums:
        xor ^= num
    # Find rightmost set bit
    diff = xor & -xor
    a = b = 0
    for num in nums:
        if num & diff:
            a ^= num
        else:
            b ^= num
    return [a, b]

# Example:
nums = [1,2,1,3,2,5]
print(singleNumber(nums))  # Output: [3, 5] (order may vary)
```

---

## How It Works

- The XOR of the entire array gives `a ^ b`
- The rightmost set bit tells us where `a` and `b` differ
- Partitioning and XOR-ing recovers each unique number

---

## Applications

- Finding two unique elements in an array with all others duplicated
- Efficient bit manipulation for data analysis and error detection

---

## Useful Links

- [LeetCode #260 — Single Number III](https://leetcode.com/problems/single-number-iii/)
- [Bitwise operation — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

---