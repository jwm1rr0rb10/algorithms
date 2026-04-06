def sieve_of_eratosthenes(n):
    # Create a boolean array "isPrime[0..n]" and initialize
    # all entries it as true. A value in isPrime[i] will
    # finally be false if i is Not a prime, else true.
    isPrime = [True] * (n + 1)
    
    # 0 and 1 are not prime numbers
    if n >= 0:
        isPrime[0] = False
    if n >= 1:
        isPrime[1] = False

    p = 2
    while (p * p <= n):
        # If isPrime[p] is still true, then it is a prime
        if isPrime[p] == True:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                isPrime[i] = False
        p += 1 # Move to the next number

    # Collect all prime numbers
    primes = []
    for p in range(n + 1):
        if isPrime[p]:
            primes.append(p)
            
    return primes

# Example Usage (Примеры Использования):
print(f"Primes up to 10: {sieve_of_eratosthenes(10)}") # Output: [2, 3, 5, 7]
print(f"Primes up to 30: {sieve_of_eratosthenes(30)}") # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(f"Primes up to 2: {sieve_of_eratosthenes(2)}")   # Output: [2]
print(f"Primes up to 0: {sieve_of_eratosthenes(0)}")   # Output: []