# Sort Colors (Dutch National Flag Problem)

## Problem Description

Given an array `nums` with `n` objects colored red, white, or blue (represented as 0, 1, and 2), sort them in-place so that objects of the same color are adjacent, in the order red (0), white (1), and blue (2).

You must solve this problem without using the built-in sort function.

**Example:**  
Input: nums = [2,0,2,1,1,0]  
Output: [0,0,1,1,2,2]  
Explanation: The array is sorted in the order [0,0,1,1,2,2].

---

## Algorithm Idea and Approach

- Use the Dutch National Flag algorithm, which employs three pointers:
  - `low` — tracks the position where the next 0 should go.
  - `mid` — the current element to check.
  - `high` — tracks the position where the next 2 should go.
- Traverse the array with `mid`:
  - If `nums[mid] == 0`: swap with `nums[low]`, increment both `mid` and `low`.
  - If `nums[mid] == 1`: just increment `mid`.
  - If `nums[mid] == 2`: swap with `nums[high]`, decrement `high` (do not increment `mid`).

---

## Python Example

```python
def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Example usage:
arr = [2,0,2,1,1,0]
sortColors(arr)
print(arr)  # Output: [0, 0, 1, 1, 2, 2]
```

---

## Complexity Analysis

- **Time:** O(n), single pass through the array.
- **Space:** O(1), in-place sorting.

---

## Real-Life Applications

- Sorting objects by category in a single pass (e.g., color, priority).
- Partitioning data for quick access and efficient processing.
- Used in variants of quicksort and other in-place sorting algorithms.

---

## Useful Links

- [Sort Colors — LeetCode](https://leetcode.com/problems/sort-colors/)
- [Dutch National Flag Algorithm — GeeksforGeeks](https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/)
- [Edsger Dijkstra — Wikipedia](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra)

---

## LeetCode Practice

| Difficulty | Problem         | Link                                                                             |
|------------|----------------|----------------------------------------------------------------------------------|
| Medium     | Sort Colors    | [#75 Sort Colors](https://leetcode.com/problems/sort-colors/)                    |
| Medium     | Partition List | [#86 Partition List](https://leetcode.com/problems/partition-list/)               |
| Medium     | Wiggle Sort II | [#324 Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/)              |
| Medium     | Sort List      | [#148 Sort List](https://leetcode.com/problems/sort-list/)                        |

---