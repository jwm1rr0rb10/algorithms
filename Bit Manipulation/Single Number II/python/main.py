def singleNumber(nums):
    result = 0
    for i in range(32):
        count = 0
        for num in nums:
            if (num >> i) & 1:
                count += 1
        if count % 3:
            # Handle negative numbers for 32 bits
            if i == 31:
                result -= (1 << 31)
            else:
                result |= (1 << i)
    return result

# Example:
nums = [2,2,3,2]
print(singleNumber(nums))  # Output: 3