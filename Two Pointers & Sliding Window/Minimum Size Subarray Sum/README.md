# Minimum Size Subarray Sum

## Problem Description

Given an array of positive integers `nums` and a positive integer `target`, find the minimal length of a contiguous subarray of which the sum is greater than or equal to `target`. If there is no such subarray, return 0 instead.

**Example:**  
Input: nums = [2,3,1,2,4,3], target = 7  
Output: 2  
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

---

## Algorithm Idea and Approach

- Use the Sliding Window (two pointers) technique to efficiently find the minimal subarray length.
- Initialize two pointers:  
  - `start` — the left boundary of the window.
  - `end` — the right boundary of the window.
- Use a variable `window_sum` to store the sum of the current window.
- Expand the window by moving `end` and adding values to `window_sum`.
- When `window_sum` is greater than or equal to `target`, move `start` forward to minimize the window size and update the answer.
- Continue until the end of the array.

---

## Python Example

```python
def minSubArrayLen(target, nums):
    n = len(nums)
    min_length = float('inf')
    window_sum = 0
    start = 0

    for end in range(n):
        window_sum += nums[end]
        while window_sum >= target:
            min_length = min(min_length, end - start + 1)
            window_sum -= nums[start]
            start += 1
    return 0 if min_length == float('inf') else min_length

# Example usage:
print(minSubArrayLen(7, [2,3,1,2,4,3]))  # Output: 2
```

---

## Complexity Analysis

- **Time:** O(n), where n is the number of elements in the array (each element is visited at most twice).
- **Space:** O(1), only a few variables are used.

---

## Real-Life Applications

- Finding the shortest period where a sum threshold is met (e.g., minimum consecutive days with sales over a target).
- Optimizing resource allocation in time windows.
- Analyzing time-series data for rapid threshold crossings.

---

## Useful Links

- [Minimum Size Subarray Sum — LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)
- [Sliding Window Technique — GeeksforGeeks](https://www.geeksforgeeks.org/window-sliding-technique/)
- [Array — Wikipedia](https://en.wikipedia.org/wiki/Array_data_structure)

---

## LeetCode Practice

| Difficulty | Problem                          | Link                                                                              |
|------------|----------------------------------|-----------------------------------------------------------------------------------|
| Medium     | Minimum Size Subarray Sum        | [#209 Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) |
| Medium     | Longest Substring Without Repeating Characters | [#3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| Medium     | Subarray Product Less Than K     | [#713 Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) |
| Medium     | Maximum Average Subarray I       | [#643 Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) |

---