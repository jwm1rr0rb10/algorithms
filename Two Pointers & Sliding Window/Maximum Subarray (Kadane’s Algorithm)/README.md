# Maximum Subarray — Kadane’s Algorithm

## Problem Description

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**  
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]  
Output: 6  
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.

---

## Algorithm Idea and Approach

- Use Kadane's Algorithm to efficiently find the maximum sum of a contiguous subarray.
- Initialize two variables:  
  - `current_sum` — the maximum sum ending at the current position (local maximum).
  - `max_sum` — the maximum sum found so far (global maximum).
- For each element in the array:
  - Update `current_sum` as the maximum of the current element and `current_sum + current element`.
  - Update `max_sum` if `current_sum` is greater than `max_sum`.

---

## Python Example

```python
def maxSubArray(nums):
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage:
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
```

---

## Complexity Analysis

- **Time:** O(n), where n is the number of elements in the array (each element is visited once).
- **Space:** O(1), only two variables are used.

---

## Real-Life Applications

- Analyzing stock price changes to find the most profitable period for trading.
- Detecting the period with the highest activity or intensity in time-series data.
- Maximum profit/loss sub-periods in financial analytics.
- Any problem involving the search for the most advantageous contiguous segment.

---

## Useful Links

- [Maximum Subarray — LeetCode](https://leetcode.com/problems/maximum-subarray/)
- [Kadane’s Algorithm — GeeksforGeeks](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)
- [Dynamic Programming — Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming)

---

## LeetCode Practice

| Difficulty | Problem                  | Link                                                                |
|------------|-------------------------|---------------------------------------------------------------------|
| Medium     | Maximum Subarray         | [#53 Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) |
| Medium     | Maximum Product Subarray | [#152 Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) |
| Medium     | Best Time to Buy and Sell Stock | [#121 Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |
| Medium     | Partition Equal Subset Sum | [#416 Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |

---