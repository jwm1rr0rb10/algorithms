def moveZeroes(nums):
    last_non_zero = 0
    # Move non-zero elements forward
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1
    # Fill the rest with zeroes
    for i in range(last_non_zero, len(nums)):
        nums[i] = 0

# Example usage:
arr = [0,1,0,3,12]
moveZeroes(arr)
print(arr)  # Output: [1, 3, 12, 0, 0]