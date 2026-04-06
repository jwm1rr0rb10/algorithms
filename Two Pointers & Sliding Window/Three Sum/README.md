# 3Sum

## Problem Description

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j != k`, and `nums[i] + nums[j] + nums[k] == 0`.  
The solution set must not contain duplicate triplets.

**Example:**  
Input: nums = [-1,0,1,2,-1,-4]  
Output: [[-1,-1,2], [-1,0,1]]  
Explanation: The triplets [-1,-1,2] and [-1,0,1] sum to zero. Duplicates are omitted.

---

## Algorithm Idea and Approach

- Sort the array to enable two-pointer search and easy duplicate skipping.
- Iterate through the array with index `i`:
  - For each `i`, use two pointers (`left = i+1`, `right = len(nums)-1`) to find pairs such that `nums[i] + nums[left] + nums[right] == 0`.
  - Move pointers inward based on the sum comparison.
  - Skip duplicates for all pointers.

---

## Python Example

```python
def threeSum(nums):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, n-1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return res

# Example usage:
print(threeSum([-1,0,1,2,-1,-4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
```

---

## Complexity Analysis

- **Time:** O(n^2), where n is the length of the array (due to nested loops).
- **Space:** O(1) (excluding the output list).

---

## Real-Life Applications

- Finding zero-sum combinations in financial data.
- Chemistry: balancing equations or finding stable triplets.
- Computer vision: identifying sets of features that together satisfy a constraint.

---

## Useful Links

- [3Sum — LeetCode](https://leetcode.com/problems/3sum/)
- [Two Pointer Technique — GeeksforGeeks](https://www.geeksforgeeks.org/two-pointers-technique/)
- [Sorting Algorithms — Wikipedia](https://en.wikipedia.org/wiki/Sorting_algorithm)

---

## LeetCode Practice

| Difficulty | Problem         | Link                                                                               |
|------------|----------------|------------------------------------------------------------------------------------|
| Medium     | 3Sum           | [#15 3Sum](https://leetcode.com/problems/3sum/)                                    |
| Medium     | 3Sum Closest   | [#16 3Sum Closest](https://leetcode.com/problems/3sum-closest/)                    |
| Medium     | 4Sum           | [#18 4Sum](https://leetcode.com/problems/4sum/)                                    |
| Medium     | Two Sum II     | [#167 Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) |

---