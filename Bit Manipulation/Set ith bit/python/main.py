def set_ith_bit(n, i):
    return n | (1 << i)

# Examples:
print(bin(set_ith_bit(0b1010, 1)))  # 0b1010 | 0b0010 => 0b1010 (bit 1 already set)
print(bin(set_ith_bit(0b1010, 2)))  # 0b1010 | 0b0100 => 0b1110 (bit 2 set)
print(bin(set_ith_bit(0b0, 4)))     # 0b0000 | 0b10000 => 0b10000