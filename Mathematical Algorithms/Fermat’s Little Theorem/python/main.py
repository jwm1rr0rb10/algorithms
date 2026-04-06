def mod_inverse(a, p):
    return pow(a, p - 2, p)  # Fermat’s Little Theorem

# Example
print(mod_inverse(3, 7))  # Output: 5, since 3 * 5 ≡ 1 mod 7