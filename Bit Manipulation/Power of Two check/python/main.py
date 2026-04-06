def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0

# Examples:
print(isPowerOfTwo(1))    # True (2^0)
print(isPowerOfTwo(2))    # True (2^1)
print(isPowerOfTwo(3))    # False
print(isPowerOfTwo(8))    # True (2^3)
print(isPowerOfTwo(0))    # False
print(isPowerOfTwo(-8))   # False