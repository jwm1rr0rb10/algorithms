def clear_ith_bit(n, i):
    mask = ~(1 << i)
    return n & mask

# Example usage:
n = 13      # 1101
i = 2
print(clear_ith_bit(n, i))  # 9 (1001)