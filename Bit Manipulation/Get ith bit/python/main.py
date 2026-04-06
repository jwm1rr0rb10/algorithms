def get_ith_bit(n, i):
    return (n >> i) & 1

# Examples:
print(get_ith_bit(13, 0))  # 1 (13 = 1101, bit 0 is 1)
print(get_ith_bit(13, 1))  # 0 (bit 1 is 0)
print(get_ith_bit(13, 2))  # 1 (bit 2 is 1)
print(get_ith_bit(13, 3))  # 1 (bit 3 is 1)