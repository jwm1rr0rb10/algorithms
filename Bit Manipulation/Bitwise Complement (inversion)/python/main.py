def bitwiseComplement(n):
    if n == 0:
        return 1
    mask = (1 << n.bit_length()) - 1
    return n ^ mask

# Example usage:
print(bitwiseComplement(5))   # Output: 2
print(bitwiseComplement(0))   # Output: 1
print(bitwiseComplement(8))   # Output: 7