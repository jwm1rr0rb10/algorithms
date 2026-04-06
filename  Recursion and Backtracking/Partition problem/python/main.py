def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False  # If the sum is odd, partition is impossible

    target = total // 2

    def backtrack(i, current_sum):
        # If we've found a subset with the required sum
        if current_sum == target:
            return True
        # If the sum is exceeded or no elements left
        if current_sum > target or i == len(nums):
            return False
        # Try to include or exclude the current element
        return (backtrack(i + 1, current_sum + nums[i]) or
                backtrack(i + 1, current_sum))

    return backtrack(0, 0)

# Example usage
print(can_partition([1, 5, 11, 5]))  # True ([1, 5, 5] and [11])
print(can_partition([1, 2, 3, 5]))   # False