def subsets(nums):
    n = len(nums)
    result = []
    for mask in range(1 << n):  # from 0 to 2^n - 1
        subset = []
        for i in range(n):
            if (mask >> i) & 1:
                subset.append(nums[i])
        result.append(subset)
    return result

# Example:
nums = [1, 2, 3]
print(subsets(nums))
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]