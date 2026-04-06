def gray_code_sequence(n):
    res = []
    for i in range(1 << n):  # 1 << n == 2^n
        res.append(i ^ (i >> 1))
    return res

# Example usage:
print(gray_code_sequence(2))  # [0, 1, 3, 2]
print(gray_code_sequence(3))  # [0, 1, 3, 2, 6, 7, 5, 4]

# To print as binary with leading zeros:
n = 3
for x in gray_code_sequence(n):
    print(f"{x:03b}")