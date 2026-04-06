def singleNumber(nums):
    result = 0
    for i in range(32):
        count = 0
        for num in nums:
            if (num >> i) & 1:
                count += 1
        if count % 3:
            if i == 31:
                result -= (1 << 31)
            else:
                result |= (1 << i)
    return result

# Example:
print(singleNumber([2,2,3,2]))  # Output: 3