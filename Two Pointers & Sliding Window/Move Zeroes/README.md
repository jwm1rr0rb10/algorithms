# Move Zeroes

## Problem Description

Given an integer array `nums`, move all `0`'s to the end of the array while maintaining the relative order of the non-zero elements. Do this in-place with the minimum number of operations.

**Example:**  
Input: nums = [0,1,0,3,12]  
Output: [1,3,12,0,0]  
Explanation: All non-zero elements are moved to the front, and all zeroes are moved to the end.

---

## Algorithm Idea and Approach

- Use the two pointers technique to shift all non-zero elements to the beginning of the array, then fill the rest with zeroes.
- Initialize a pointer `last_non_zero` to keep track of where the next non-zero element should go.
- Iterate through the array:
  - If the current element is not zero, assign it to `nums[last_non_zero]` and increment `last_non_zero`.
- After the first pass, fill the remaining positions in the array with zeroes.

---

## Python Example

```python
def moveZeroes(nums):
    last_non_zero = 0
    # Move non-zero elements forward
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1
    # Fill the rest with zeroes
    for i in range(last_non_zero, len(nums)):
        nums[i] = 0

# Example usage:
arr = [0,1,0,3,12]
moveZeroes(arr)
print(arr)  # Output: [1, 3, 12, 0, 0]
```

---

## Complexity Analysis

- **Time:** O(n), where n is the number of elements in the array (two passes over the array).
- **Space:** O(1), operates in-place.

---

## Real-Life Applications

- Data cleaning: moving missing or empty values (represented as zero) to the end for easier processing.
- Reordering lists for efficient computation.
- Optimizing memory access by grouping non-zero (active) data elements.

---

## Useful Links

- [Move Zeroes — LeetCode](https://leetcode.com/problems/move-zeroes/)
- [Array Manipulation — GeeksforGeeks](https://www.geeksforgeeks.org/move-zeroes-end-array/)

---

## LeetCode Practice

| Difficulty | Problem      | Link                                                                    |
|------------|-------------|-------------------------------------------------------------------------|
| Easy       | Move Zeroes  | [#283 Move Zeroes](https://leetcode.com/problems/move-zeroes/)          |
| Easy       | Remove Element | [#27 Remove Element](https://leetcode.com/problems/remove-element/)    |
| Easy       | Remove Duplicates from Sorted Array | [#26 Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) |

---