x = 0b1010  # 10 in decimal

# Set the 2nd bit (counting from 0)
x = x | (1 << 2)
print(bin(x))  # 0b1110

# Check if the 3rd bit is set
is_set = (x >> 3) & 1
print(is_set)  # 1 (bit is set)

# Clear the 1st bit
x = x & ~(1 << 1)
print(bin(x))  # 0b1100