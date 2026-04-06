def singleNumber(nums):
    xor = 0
    for num in nums:
        xor ^= num
    # Find rightmost set bit
    diff = xor & -xor
    a = b = 0
    for num in nums:
        if num & diff:
            a ^= num
        else:
            b ^= num
    return [a, b]

# Example:
nums = [1,2,1,3,2,5]
print(singleNumber(nums))  # Output: [3, 5] (order may vary)