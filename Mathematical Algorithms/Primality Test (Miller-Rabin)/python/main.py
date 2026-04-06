import random

def power(base, exp, mod):
    """
    Computes (base^exp) % mod using modular exponentiation (Fast Power).
    """
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def miller_rabin_test(d, n):
    """
    Performs a single round of the Miller-Rabin test.
    d: n-1 after factoring out all powers of 2 (d is odd)
    n: the number to test for primality
    """
    # Pick a random number 'a' in range [2, n-2]
    # (or [2, n-1) if n-2 is not available for small n)
    a = random.randint(2, n - 2)
    
    # Compute x = a^d % n
    x = power(a, d, n)

    if x == 1 or x == n - 1:
        return True # n is probably prime for this base 'a'

    # Repeatedly square x (s-1 times)
    # The original n-1 = 2^s * d. We already computed a^d.
    # Now we check a^(2^1 * d), a^(2^2 * d), ..., a^(2^(s-1) * d)
    while d != n - 1: # This loop runs at most (s-1) times
        x = (x * x) % n
        d *= 2
        if x == n - 1:
            return True # Found a a^(2^j * d) which is -1 mod n
        if x == 1:
            return False # Found a non-trivial square root of 1, so n is composite
    
    return False # n is composite for this base 'a'

def is_prime_miller_rabin(n, k=5):
    """
    Probabilistic primality test using Miller-Rabin.
    n: the number to test
    k: number of iterations (higher k = higher accuracy)
    """
    # Corner cases
    if n <= 1: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False # Handle even numbers > 2

    # Find d and s such that n-1 = d * 2^s
    # where d is an odd number.
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    
    # Run k iterations of the test
    for _ in range(k):
        if not miller_rabin_test(d, n):
            return False # Found a witness, so n is composite
    
    return True # n is probably prime

# Example Usage:
print(f"Is 2 prime? {is_prime_miller_rabin(2)}") # True
print(f"Is 13 prime? {is_prime_miller_rabin(13)}") # True
print(f"Is 15 prime? {is_prime_miller_rabin(15)}") # False
print(f"Is 561 prime? {is_prime_miller_rabin(561)}") # False (Carmichael number)
print(f"Is 999999937 prime? {is_prime_miller_rabin(999999937, k=10)}") # True (a large prime)
print(f"Is 1000000007 prime? {is_prime_miller_rabin(1000000007, k=10)}") # True (a large prime)

# Deterministic Miller-Rabin for numbers up to 2^64 (specific small bases)
# For n < 2,047, it is enough to test a = 2.
# For n < 1,373,653, it is enough to test a = 2, 3.
# For n < 9,080,191, it is enough to test a = 31, 73.
# For n < 25,326,001, it is enough to test a = 2, 3, 5.
# etc. (up to n < 2^64, a specific set of 12 bases is sufficient)
# If N is small enough, one can use a fixed set of 'a' values (deterministic version).
# For example, for N < 3,825,123,056,546,413,051, bases {2, 3, 5, 7, 11, 13, 17, 19, 23} are sufficient.