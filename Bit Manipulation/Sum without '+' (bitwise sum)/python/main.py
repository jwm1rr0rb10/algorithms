def getSum(a, b):
    MAX = 0xFFFFFFFF
    MASK = 0x7FFFFFFF
    while b != 0:
        carry = (a & b) << 1
        a = (a ^ b) & MAX
        b = carry & MAX
    # Handle negative values
    return a if a <= MASK else ~(a ^ MAX)

# Example:
print(getSum(2, 3))    # 5
print(getSum(-1, 1))   # 0