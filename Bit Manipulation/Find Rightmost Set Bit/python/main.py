def rightmost_set_bit_index(n):
    if n == 0:
        return -1  # No set bits
    pos = 0
    while (n & 1) == 0:
        n >>= 1
        pos += 1
    return pos

# Examples:
print(rightmost_set_bit_index(18))  # 1
print(rightmost_set_bit_index(12))  # 2
print(rightmost_set_bit_index(32))  # 5