# Longest Increasing Subsequence (LIS) — Dynamic Programming

## Problem Description

Given an array of numbers, find the length of the longest strictly increasing subsequence (not necessarily consecutive).

**Example:**  
Input: [10, 9, 2, 5, 3, 7, 101, 18]  
Output: 4  
Explanation: One possible LIS is [2, 3, 7, 101].

---

## Algorithm Idea and Approach

- The classic solution uses dynamic programming:
  - Let `dp[i]` be the length of the LIS ending at index i.
  - For each i, check all j < i. If nums[j] < nums[i]:  
    dp[i] = max(dp[i], dp[j] + 1)
- Can be optimized to O(n log n) with binary search.

---

## Python Example (O(n^2) Solution)

```python
def lengthOfLIS(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Example usage:
print(lengthOfLIS([10,9,2,5,3,7,101,18]))  # Output: 4
```

---

## Fast Solution (O(n log n))

```python
import bisect

def lengthOfLIS(nums):
    tails = []
    for num in nums:
        idx = bisect.bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)

# Example:
print(lengthOfLIS([10,9,2,5,3,7,101,18]))  # Output: 4
```

---

## Complexity Analysis

- **O(n^2)** time, **O(n)** space — DP approach.
- **O(n log n)** time, **O(n)** space — with binary search.

---

## Applications

- Sequence trend analysis
- Pattern recognition in data
- Bioinformatics (sequence alignment)
- Signal and time series processing

---

## Useful Links

- [LIS — LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/)
- [LIS — GeeksforGeeks](https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/)
- [Wikipedia: LIS](https://en.wikipedia.org/wiki/Longest_increasing_subsequence)

---

## LeetCode Practice

| Difficulty | Problem                        | Link                                                                            |
|------------|-------------------------------|---------------------------------------------------------------------------------|
| Medium     | Longest Increasing Subsequence | [#300 Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)|
| Medium     | Russian Doll Envelopes         | [#354 Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)|
| Medium     | Maximum Length of Pair Chain   | [#646 Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/)|