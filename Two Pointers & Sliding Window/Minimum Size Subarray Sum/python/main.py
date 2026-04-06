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