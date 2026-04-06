def prime_factorization(n):
    factors = {} # Using a dictionary to store factors and their counts

    # Handle factor 2
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2

    # Handle odd factors from 3 up to sqrt(n)
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 2 # Only check odd numbers

    # If n is still greater than 1, it must be a prime factor itself
    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    return factors

# Example
print(prime_factorization(12)) # Output: {2: 2, 3: 1}
print(prime_factorization(100)) # Output: {2: 2, 5: 2}
print(prime_factorization(17)) # Output: {17: 1}
print(prime_factorization(999999937)) # Output: {999999937: 1} (a prime number)
print(prime_factorization(720)) # Output: {2: 4, 3: 2, 5: 1}