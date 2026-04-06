def hamming_distance(x, y):
    diff = x ^ y
    count = 0
    while diff:
        count += diff & 1
        diff >>= 1
    return count

# Or, using Python's built-in:
def hamming_distance_fast(x, y):
    return bin(x ^ y).count('1')

# Examples:
print(hamming_distance(3, 5))      # 2
print(hamming_distance(1, 4))      # 2 (001 vs 100)
print(hamming_distance(7, 15))     # 1 (0111 vs 1111: only bit 3 differs)