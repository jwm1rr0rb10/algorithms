# 🔍 Prime Factorization

## 📌 Problem Description

**Prime factorization** is the process of breaking down a composite number into its prime factors—the prime numbers that, when multiplied together, give the original number. For example, the prime factors of 12 are 2, 2, and 3 ($2 \times 2 \times 3 = 12$). Every composite number has a unique prime factorization (Fundamental Theorem of Arithmetic).

---

## 💡 Idea and Approach

The most straightforward approach for prime factorization involves trial division:

1.  **Divide by 2:** Continuously divide the number `n` by 2 until it's no longer divisible. Count how many times 2 was a factor.
2.  **Divide by odd numbers:** Iterate through odd numbers `i` starting from 3 up to $\sqrt{n}$. For each `i`, continuously divide `n` by `i` as long as it's divisible. Count how many times `i` was a factor.
3.  **Handle remaining number:** If, after these divisions, `n` is still greater than 1, it means the remaining `n` is itself a prime number (and the largest prime factor).

This method works because any composite number `n` must have at least one prime factor less than or equal to $\sqrt{n}$. If it doesn't, then all its prime factors must be greater than $\sqrt{n}$. In this case, the product of any two such factors would be greater than $n$, which is a contradiction.

---

## 🧪 Python Example

```python
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
```

---

## ⏱️ Complexity

* **Time Complexity:** $O(\sqrt{n})$ in the worst case (when $n$ is prime or a product of two large primes). This is because the loop iterates up to $\sqrt{n}$.
* **Space Complexity:** $O(\log n)$ or $O(\text{number of distinct prime factors})$ for storing the factors. In the worst case, a number can have many small prime factors (e.g., $2^k$), or a few large distinct ones. The number of distinct prime factors of $n$ is generally much smaller than $O(\log n)$.

---

## ⚠️ Considerations for Large Numbers

For very large numbers (e.g., hundreds of digits), the $O(\sqrt{n})$ trial division approach becomes too slow. Specialized algorithms are used in such cases:

* **Pollard's Rho Algorithm**: More efficient than trial division for numbers with relatively small prime factors, but not guaranteed to find factors quickly.
* **Pollard's p-1 Algorithm**: Effective if $n$ has a prime factor $p$ such that $p-1$ is a product of small primes.
* **Elliptic Curve Method (ECM)**: A highly effective general-purpose factoring algorithm for finding relatively small factors of large numbers.
* **General Number Field Sieve (GNFS)**: The fastest known algorithm for factoring very large numbers (e.g., over 100 digits), often used in cryptography.

---

## 🧭 Applications

* **Cryptography:** Crucial for the security of algorithms like RSA, which relies on the difficulty of factoring large numbers.
* **Number Theory:** Fundamental operation for many problems, including finding GCD/LCM, determining perfect numbers, and solving Diophantine equations.
* **Data Compression:** Some compression algorithms use properties related to prime factorization.
* **Generating Primes:** While direct factorization isn't used to generate primes, understanding prime distribution is vital.
* **Simplifying Fractions:** Reducing fractions to their simplest form involves dividing the numerator and denominator by their common prime factors.

---

## 🔗 Useful Links

* [**Wikipedia - Prime Factorization**](https://en.wikipedia.org/wiki/Prime_factorization)
* [**GeeksForGeeks - Prime Factorization using Trial Division**](https://www.geeksforgeeks.org/prime-factorization/)
* [**CP Algorithms - Integer Factorization**](https://cp-algorithms.com/algebra/factorization.html)

---

## 🧩 LeetCode Connection

While direct implementation of advanced factoring algorithms like Pollard's Rho or ECM is rare in typical LeetCode problems due to their complexity, the basic trial division method for prime factorization (and understanding its efficiency limits) is quite common. You might encounter:

* Problems where you need to count divisors, find GCD/LCM of numbers, or determine if a number is "square-free" (not divisible by any perfect square other than 1). All these often rely on prime factorization.
* Problems that combine number theory with data structures or dynamic programming, where prime factors play a role in state transitions or optimizations.
* Interviewers might ask about the concepts behind factoring large numbers to test your fundamental understanding of number theory and its applications in real-world security.