# Sieve of Eratosthenes

## 📌 Problem Description 

The **Sieve of Eratosthenes** is an ancient and efficient algorithm for finding all prime numbers up to a specified integer $N$. It works by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the first prime number, 2.

**Input:** An integer $N$.
**Output:** A list or boolean array indicating all prime numbers up to $N$.

## 💡 Idea and Approach

The algorithm operates on the principle that every composite number has a prime factor less than or equal to its square root.

1.  **Initialization:** Create a boolean array `isPrime` (or similar structure) of size $N+1$, and initialize all entries from `isPrime[2]` to `isPrime[N]` as `True` (assuming all numbers are prime initially). Mark `isPrime[0]` and `isPrime[1]` as `False` since 0 and 1 are not prime.

2.  **Iteration:** Start with the first prime number, $p = 2$.

3.  **Mark Multiples:**
    * If `isPrime[p]` is `True` (meaning $p$ has not been marked as composite yet, so it's a prime number):
        * Mark all multiples of $p$ as composite. Start marking from $p^2$ (because smaller multiples like $2p, 3p, \dots, (p-1)p$ would have already been marked by smaller primes). Mark $p^2, p^2+p, p^2+2p, \dots$ up to $N$ as `False` in the `isPrime` array.

4.  **Advance to Next Number:** Increment $p$ to the next number.

5.  **Termination Condition:** Continue this process as long as $p^2 \le N$. After this loop finishes, any number $i$ for which `isPrime[i]` is still `True` is a prime number.

---

## 🧪 Python Example

```python
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
```

---

## ⏱️ Complexity

* **Time Complexity (Временная сложность):** $O(N \log \log N)$
    * This is highly efficient. The outer loop runs up to $\sqrt{N}$. The inner loop marks multiples. The number of operations is approximately:
        $N/2 + N/3 + N/5 + \dots = N \sum_{p \le N, p \text{ is prime}} \frac{1}{p}$, which converges to $N \log \log N$.
* **Space Complexity (Пространственная сложность):** $O(N)$
    * Required to store the boolean array `isPrime` of size $N+1$.

---

## 🧭 Applications

* **Finding Primes:** The primary use case for generating a list of prime numbers up to a certain limit.
* **Number Theory Problems:** Useful as a precomputation step for problems that require checking primality of many numbers or iterating through primes.
* **Factorization (precomputation for small factors):** Can be combined with trial division. Sieve finds small primes, then trial division uses those primes.
* **Competitive Programming:** Frequently used in problems requiring prime numbers within a certain range ($N$ up to $10^6$ or $10^7$).
* **Cryptography (Foundational):** While not directly used for generating large cryptographic primes (Miller-Rabin is used for that), the understanding of prime distribution is fundamental.

---

## 🔗 Useful Links

* [**Wikipedia - Sieve of Eratosthenes**](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) (English)
* [**GeeksForGeeks - Sieve of Eratosthenes**](https://www.geeksforgeeks.org/dsa/sieve-of-eratosthenes/) (English)
* [**CP-Algorithms - Sieve of Eratosthenes**](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html) (English)

---

## 🧩 LeetCode Connection

The Sieve of Eratosthenes is a classic algorithm often tested in competitive programming and technical interviews. It's used when you need to:

* Find all primes up to a given $N$.
* Count primes in a range.
* Determine primality for multiple numbers efficiently (e.g., in a loop where $N$ is large, but individual numbers are small enough to be covered by a precomputed sieve).
* Solve problems that involve prime factorization where small prime factors are important.

---

**Example LeetCode Problems:**
* [LeetCode 204. Count Primes](https://leetcode.com/problems/count-primes/)
* [LeetCode 1175. Prime Arrangements](https://leetcode.com/problems/prime-arrangements/)
* Problems involving finding prime factors or divisors where a precomputed list of primes speeds up the solution.

---