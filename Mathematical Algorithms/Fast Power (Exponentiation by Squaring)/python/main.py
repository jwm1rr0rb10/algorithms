def fast_pow(a, b, mod):
    result = 1
    a %= mod
    while b > 0:
        if b % 2 == 1:
            result = result * a % mod
        a = a * a % mod
        b //= 2
    return result

# Example
print(fast_pow(2, 10, 1000))  # Output: 24 (since 2^10 = 1024, 1024 % 1000 = 24)