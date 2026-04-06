def karatsuba(x, y):
    # Base case for small numbers
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split numbers
    x1, x0 = divmod(x, 10**m)
    y1, y0 = divmod(y, 10**m)

    # Recursively compute
    z0 = karatsuba(x0, y0)
    z2 = karatsuba(x1, y1)
    z1 = karatsuba(x0 + x1, y0 + y1) - z2 - z0

    return z2 * 10**(2*m) + z1 * 10**m + z0

# Usage example:
x = 1234
y = 5678
print(karatsuba(x, y))  # 7006652