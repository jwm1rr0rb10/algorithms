# Find Missing Number using XOR

## Problem Description

Given an array containing `n` distinct numbers taken from the range `0` to `n`, find the one number that is missing from the array.

**Example:**  
Input: `[3, 0, 1]`  
Output: `2`  
Explanation: The numbers in the range are 0, 1, 2, 3. The array is missing 2.

---

## Idea and Approach

- XOR all numbers from `0` to `n`.
- XOR all elements in the array.
- The result of these two XORs will be the missing number, because all numbers that appear in both sets will cancel each other out (`x ^ x = 0`).

---

## Python Example

```python
def find_missing_number(nums):
    n = len(nums)
    missing = 0
    for i in range(n + 1):
        missing ^= i
    for num in nums:
        missing ^= num
    return missing

# Examples:
print(find_missing_number([3, 0, 1]))    # 2
print(find_missing_number([0, 1]))       # 2
print(find_missing_number([9,6,4,2,3,5,7,0,1])) # 8
```

---

## How It Works

For array `[3, 0, 1]`:
- XOR of all numbers from 0 to 3: `0 ^ 1 ^ 2 ^ 3`
- XOR of all array elements: `3 ^ 0 ^ 1`
- The missing number is: `(0 ^ 1 ^ 2 ^ 3) ^ (3 ^ 0 ^ 1) = 2`

---

## Table: Examples

| Array                | n | Range          | Missing |
|----------------------|---|----------------|---------|
| [3, 0, 1]            | 3 | 0, 1, 2, 3     |   2     |
| [0, 1]               | 2 | 0, 1, 2        |   2     |
| [9,6,4,2,3,5,7,0,1]  | 9 | 0,1,2,3,4,5,6,7,8,9 | 8     |

---

## Advantages

- Time complexity: O(n)
- Space complexity: O(1)
- No need for extra arrays or sorting

---

## Applications

- Finding missing elements in sequences
- Data integrity checks
- Error detection in transmission

---

## Useful Links

- [LeetCode #268 — Missing Number](https://leetcode.com/problems/missing-number/)
- [Bitwise operations — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)

---