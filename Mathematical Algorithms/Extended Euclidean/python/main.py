def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Example: Solve 30x + 20y = gcd(30, 20)
g, x, y = extended_gcd(30, 20)
print(f"gcd = {g}, x = {x}, y = {y}")  # Output: gcd = 10, x = 1, y = -1