def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse_extended_euclidean(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None  # Modular inverse does not exist
    else:
        return (x % m + m) % m # Ensure result is positive

def power(base, exp, mod):
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def modular_inverse_fermat_little_theorem(a, m):
    # Only works if m is a prime number
    # and a is not a multiple of m
    if m <= 1:
        return None # Modulus must be a prime > 1
    # For simplicity, we won't add a prime check here, but it's crucial in practice.
    # In a real scenario, you'd add a prime check for m.
    
    # If a is a multiple of m, inverse doesn't exist
    if a % m == 0:
        return None 
    
    return power(a, m - 2, m)

# Example Usage

# Using Extended Euclidean Algorithm
a = 3
m = 11 # 11 is prime, but this method works for any m where gcd(a,m)=1
inv_ee = modular_inverse_extended_euclidean(a, m)
print(f"Modular inverse of {a} mod {m} (Extended Euclidean): {inv_ee}") # Output: 4 (since 3*4=12, 12%11=1)

a = 7
m = 26 # m is not prime, so Fermat's Little Theorem cannot be directly applied
inv_ee_non_prime = modular_inverse_extended_euclidean(a, m)
print(f"Modular inverse of {a} mod {m} (Extended Euclidean): {inv_ee_non_prime}") # Output: 15 (since 7*15=105, 105%26=1)

# Using Fermat's Little Theorem (m must be prime)
a = 3
m_prime = 11
inv_flt = modular_inverse_fermat_little_theorem(a, m_prime)
print(f"Modular inverse of {a} mod {m_prime} (Fermat's Little Theorem): {inv_flt}") # Output: 4

a = 5
m_prime_2 = 13
inv_flt_2 = modular_inverse_fermat_little_theorem(a, m_prime_2)
print(f"Modular inverse of {a} mod {m_prime_2} (Fermat's Little Theorem): {inv_flt_2}") # Output: 8 (since 5*8=40, 40%13=1)