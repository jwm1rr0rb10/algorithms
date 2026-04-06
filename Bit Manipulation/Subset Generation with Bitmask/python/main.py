def subsets(nums):
    n = len(nums)
    all_subsets = []
    for mask in range(1 << n):  # 0..2^n-1
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        all_subsets.append(subset)
    return all_subsets

# Example:
nums = [1, 2, 3]
print(subsets(nums))
# Output:
# [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]