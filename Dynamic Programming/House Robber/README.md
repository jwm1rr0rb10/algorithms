# House Robber — Dynamic Programming

## Problem Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, represented by an array `nums`.  
You cannot rob two adjacent houses (they have security systems connected).  
Return the maximum amount of money you can rob tonight without alerting the police.

**Example:**  
Input: nums = [2,7,9,3,1]  
Output: 12  
Explanation: Rob house 1 (2) + house 3 (9) + house 5 (1) = 12.

---

## Algorithm Idea and Approach

- Use dynamic programming:  
  - `dp[i]` — the maximum amount you can rob from the first `i` houses.
  - For each house, you can either:
    - Rob it (add its amount to `dp[i-2]`), or
    - Skip it (take `dp[i-1]`).
  - The answer is `max(dp[i-1], dp[i-2] + nums[i])` for each `i`.

---

## Python Example

```python
def rob(nums):
    prev1 = 0
    prev2 = 0
    for num in nums:
        temp = prev1
        prev1 = max(prev2 + num, prev1)
        prev2 = temp
    return prev1

# Example usage:
print(rob([2,7,9,3,1]))  # Output: 12
```

---

## Complexity Analysis

- **Time:** O(n), where n is the number of houses.
- **Space:** O(1), only constant extra space is used.

---

## Applications

- Interval scheduling with constraints
- Resource allocation with adjacency restrictions

---

## Useful Links

- [House Robber — LeetCode](https://leetcode.com/problems/house-robber/)
- [Dynamic Programming — GeeksforGeeks](https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/)
- [Wikipedia: Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming)

---

## LeetCode Practice

| Difficulty | Problem                   | Link                                                                |
|------------|---------------------------|---------------------------------------------------------------------|
| Medium     | House Robber              | [#198 House Robber](https://leetcode.com/problems/house-robber/)    |
| Medium     | House Robber II           | [#213 House Robber II](https://leetcode.com/problems/house-robber-ii/) |
| Medium     | Delete and Earn           | [#740 Delete and Earn](https://leetcode.com/problems/delete-and-earn/) |

---