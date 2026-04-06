## Python Example (O(n^2) Solution)

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

## Fast Solution (O(n log n))

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