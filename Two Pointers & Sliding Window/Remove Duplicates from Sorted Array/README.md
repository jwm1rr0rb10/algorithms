# Remove Duplicates from Sorted Array

## Problem Description

Given a sorted array `nums`, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.  
After removing the duplicates, return the number of unique elements in `nums`. You must do this in-place with O(1) extra memory.

**Example:**  
Input: nums = [1,1,2]  
Output: 2, nums = [1,2,_]  
Explanation: Your function should return length = 2, and the first two elements of nums should be 1 and 2.  
It does not matter what you leave beyond the returned length.

---

## Algorithm Idea and Approach

- Use the two pointers technique:
  - `i` will point to the position of the last unique element found.
  - `j` will iterate through the array.
- For each element, if `nums[j]` does not equal `nums[i]`, increment `i` and set `nums[i] = nums[j]`.
- After the loop, the first `i + 1` elements of `nums` are unique.

---

## Python Example

```python
def removeDuplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# Example usage:
arr = [1,1,2]
length = removeDuplicates(arr)
print(length)     # Output: 2
print(arr[:length])  # Output: [1, 2]
```

---

## Complexity Analysis

- **Time:** O(n), where n is the length of the array (one linear pass).
- **Space:** O(1), done in-place.

---

## Real-Life Applications

- Data cleaning: removing repeated entries from sorted datasets.
- Optimizing database or log storage.
- Pre-processing for algorithms that require unique sorted data.

---

## Useful Links

- [Remove Duplicates from Sorted Array — LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [Two Pointers Technique — GeeksforGeeks](https://www.geeksforgeeks.org/two-pointers-technique/)

---

## LeetCode Practice

| Difficulty | Problem                          | Link                                                                                  |
|------------|----------------------------------|---------------------------------------------------------------------------------------|
| Easy       | Remove Duplicates from Sorted Array  | [#26 Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) |
| Easy       | Remove Element                   | [#27 Remove Element](https://leetcode.com/problems/remove-element/)                   |
| Medium     | Remove Duplicates from Sorted Array II | [#80 Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) |
| Medium     | Remove Duplicates from Sorted List II (Linked List) | [#82 Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) |

---