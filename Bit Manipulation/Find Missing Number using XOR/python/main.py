def find_missing_number(nums):
    n = len(nums)
    missing = 0
    for i in range(n + 1):
        missing ^= i
    for num in nums:
        missing ^= num
    return missing

# Examples:
print(find_missing_number([3, 0, 1]))    # 2
print(find_missing_number([0, 1]))       # 2
print(find_missing_number([9,6,4,2,3,5,7,0,1])) # 8