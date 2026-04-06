# ⚡ Primality Test: Miller-Rabin Algorithm

## 📌 Problem Description

- The **Miller-Rabin Primality Test** is a probabilistic algorithm used to determine whether a given large number n is prime or composite. Unlike deterministic primality tests (which are slower for very large numbers), Miller-Rabin provides a high probability of correctness, making it highly practical for applications like cryptography.

- The test's core idea is based on properties that hold true for prime numbers but are unlikely to hold for composite numbers. If n is prime, it will always pass the test. If n is composite, it will fail the test with a high probability. Running multiple iterations (k times) significantly reduces the probability of a composite number being declared "probably prime" (a false positive).

---

## 💡 Idea and Approach

1. The Miller-Rabin test relies on two fundamental properties of prime numbers:

    - **Fermat's Little Theorem**: If p is a prime number, then for any integer a such that `$1 \< a \< p$`, we have ap−1equiv1pmodp.

    - **Quadratic Residues (Square Roots of 1 mod p)**: If p is an odd prime, the only solutions to x2equiv1pmodp are xequiv1pmodp and xequiv−1pmodp.

2. The algorithm proceeds as follows for a given odd integer `n > 2` and a number of iterations `k`:

    1. **Handle trivial cases:**

        1. If `n < 2`, return False (not prime).

        2. If `n == 2` or `n == 3`, return True (are prime).

        3. If `n` is even `(and n > 2)`, return False (composite).

    2. **Express `n-1` in the form `2scdotd`:**
    Since `n` is an odd number, `n-1` is even. We can repeatedly divide `n-1` by `2` until we get an odd number `d`.
    So, `n−1=2scdotd`, where d is odd and `s >= 1`.

    3. **Perform k rounds of testing:**
    
    For each of the `k` iterations:

    - **Choose a random base a**:
        - `Select a randomly such that 2lealen−2`.

    - **Compute x=adpmodn**: 
        - `Use modular exponentiation (Fast Power).`

    - **Check the first condition:**
        - `If xequiv1pmodn or xequivn−1pmodn (which is equivalent to xequiv−1pmodn), then n passes this round. Continue to the next iteration.`

    - **Check subsequent conditions (repeated squaring):**
        - `If the first condition fails, then for j from 0 to s−1:`

        - `Compute x=x2pmodn.`

        - `If xequivn−1pmodn, n passes this round. Break this inner loop and continue to the next iteration.`

        - `If xequiv1pmodn (and x was not n−1 in the previous step), then n is definitely composite. Return False.`

    - If the inner loop completes without n passing (i.e., x never became n−1 and eventually became 1, or just never became 1 or n−1), then n is composite. Return False.

    - **Conclusion:** 
        - `If n passes all k rounds, it is declared "probably prime".`

---

## Why this works:

- If n is prime, then by Fermat's Little Theorem, an−1equiv1pmodn.

- Also, if n is prime, the sequence ad,a2d,a4d,dots,a2s−1d,a2sdpmodn (where the last term is an−1pmodn) must either start with 1, or eventually hit -1 before hitting 1. If it hits 1 without ever hitting -1 (except at the very first step adpmodn being 1), it means there was a non-trivial square root of 1 (a value xnepm1 such that x2equiv1pmodn), which is only possible if n is composite.

---

## 🧪 Python Example

```python
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
```

---

## ⏱️ Complexity

- Time Complexity: `O(klog3n)`

    - Where k is the number of iterations (random bases).

    - logn comes from the number of bits in n.

    - The power function (modular exponentiation) takes O(logd) modular multiplications. Since $d \< n$, this is O(logn) modular multiplications.

    - Each modular multiplication of numbers up to n takes O(log2n) time using standard algorithms (e.g., Karatsuba can be faster).

    - The while d % 2 == 0 loop runs O(logn) times to find s.

    - The inner while d != n - 1 loop (or for loop depending on implementation) also runs O(logn) times (s steps).

    - Combining these, one iteration takes O(logncdotlog2n)=O(log3n).

    - Since we run k iterations, the total time complexity is O(klog3n).

- Space Complexity: `O(logn)`

    - Mainly due to the recursion stack of power if implemented recursively, or O(1) for the iterative power function. The variables store numbers up to n, so their space is proportional to logn (number of bits).

---

## ⚠️ Probabilistic Nature and Accuracy

- The Miller-Rabin test is probabilistic, meaning there's a small chance of a composite number being misidentified as prime (a "strong pseudoprime").

- For any composite n, the probability that it passes a single Miller-Rabin test (i.e., a randomly chosen a is a "strong liar") is at most 1/4.

- By running k independent iterations, the probability of a composite number passing all k tests is at most (1/4)k.

- This error rate can be made arbitrarily small by increasing k. For cryptographic applications, k is typically chosen such that the error probability is negligible (e.g., k=40 for an error chance of 10−24).

- For relatively small numbers (e.g., less than 264), there are known sets of small bases that make the Miller-Rabin test deterministic. If a number passes the test for all bases in such a set, it is guaranteed to be prime.

---

## 🧭 Applications

- Cryptography:

    - RSA Key Generation: Miller-Rabin is the most widely used algorithm for generating large prime numbers needed for RSA public-key cryptography.

    - Diffie-Hellman Key Exchange: Used to find large primes for the modulo operations.

    - Elliptic Curve Cryptography (ECC): Also requires large primes.

- Hash Table Sizing: Choosing prime numbers for hash table sizes can help reduce collisions.

- Random Number Generation: Used to verify the primality of randomly generated numbers for various purposes.

- Number Theory Research: Essential tool for computational number theorists.

- Coding Theory: Used in the construction of error-correcting codes.

---

## 🔗 Useful Links

- [**Wikipedia - Miller-Rabin Primality Test**](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) 

- [**GeeksforGeeks - Primality Test | Set 3 (Miller–Rabin)**](https://www.geeksforgeeks.org/dsa/primality-test-set-3-miller-rabin/)    

- [**CP-Algorithms - Miller-Rabin Primality Test**](https://cp-algorithms.com/algebra/primality_tests.html)

- [**Rosetta Code - Miller–Rabin Primality Test (various languages)**](https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test)

---

## 🧩 LeetCode Connection

- While LeetCode problems rarely require you to implement Miller-Rabin from scratch due to its complexity and the need for large number arithmetic, understanding its principles is crucial for:

    1. Interview Discussion: Being able to explain how to efficiently test for primality, especially for large numbers, demonstrates a deep understanding of number theory and algorithms.

    2. Background Knowledge for Cryptography-Related Problems: If you encounter problems that involve modular arithmetic, large primes, or public-key concepts, knowing Miller-Rabin provides valuable context.

    3. Problems on "Probable Primes": Some competitive programming problems might implicitly or explicitly mention probable primes, hinting at the need for probabilistic tests.

    4. Custom Test Cases: If you're building a system that needs to handle large prime numbers (e.g., for generating test data), Miller-Rabin would be a practical choice.

---     