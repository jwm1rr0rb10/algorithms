def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i

# Example usage:
print(twoSum([2,7,11,15], 9))  # Output: [0, 1]