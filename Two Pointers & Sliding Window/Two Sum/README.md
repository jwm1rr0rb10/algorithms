# Two Sum

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Example:**  
Input: nums = [2,7,11,15], target = 9  
Output: [0,1]  
Explanation: nums[0] + nums[1] == 9, so return [0, 1].

---

## Algorithm Idea and Approach

- Use a hash map (dictionary) to store the numbers and their indices as you iterate through the array.
- For each element `x`, check if `target - x` exists in the map.
  - If it exists, you found the pair.
  - Otherwise, add `x` and its index to the map.

---

## Python Example

```python
def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i

# Example usage:
print(twoSum([2,7,11,15], 9))  # Output: [0, 1]
```

---

## Complexity Analysis

- **Time:** O(n), where n is the number of elements in the array (single pass).
- **Space:** O(n), due to hash map storage.

---

## Real-Life Applications

- Finding pairs in financial data that meet a target sum (e.g., transactions matching a specific amount).
- Pairing resources or tasks for optimal allocation.
- Used as a subroutine in more complex algorithms (e.g., 3Sum, 4Sum).

---

## Useful Links

- [Two Sum — LeetCode](https://leetcode.com/problems/two-sum/)
- [Hash Table — GeeksforGeeks](https://www.geeksforgeeks.org/python-dictionary/)

---

## LeetCode Practice

| Difficulty | Problem        | Link                                                                              |
|------------|---------------|-----------------------------------------------------------------------------------|
| Easy       | Two Sum       | [#1 Two Sum](https://leetcode.com/problems/two-sum/)                              |
| Medium     | Two Sum II    | [#167 Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)   |
| Medium     | 3Sum          | [#15 3Sum](https://leetcode.com/problems/3sum/)                                   |
| Medium     | 4Sum          | [#18 4Sum](https://leetcode.com/problems/4sum/)                                   |

---