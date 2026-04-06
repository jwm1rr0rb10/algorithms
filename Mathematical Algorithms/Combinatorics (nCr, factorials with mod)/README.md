# 🎲 Combinatorics: nCr and Factorials with Modulo

## 📌 Problem Description

In many algorithmic problems, we need to compute combinations:

- `nCr = n! / (r! × (n - r)!)`


But when `n` is large or results must be computed modulo a prime (e.g., 10⁹+7), we use modular arithmetic to avoid overflow and ensure correctness.

---

## 💡 Idea and Approach

To compute `nCr % mod` efficiently:

1. **Precompute Factorials**  
   `fact[i] = i! % mod` for all `i` up to `n`.

2. **Precompute Inverse Factorials**  
   Using Fermat’s Little Theorem (if `mod` is prime):  
   `inv_fact[i] = (fact[i])^(mod - 2) % mod`

3. **Compute nCr**  
   `nCr % mod = fact[n] × inv_fact[r] × inv_fact[n - r] % mod`

---

## 🧪 Python Example

```python
MOD = 10**9 + 7
MAX = 10**6 + 10

fact = [1] * MAX
inv_fact = [1] * MAX

# Precompute factorials
for i in range(1, MAX):
    fact[i] = fact[i - 1] * i % MOD

# Fast exponentiation
def mod_pow(a, b, mod):
    result = 1
    while b:
        if b % 2:
            result = result * a % mod
        a = a * a % mod
        b //= 2
    return result

# Precompute inverse factorials
inv_fact[MAX - 1] = mod_pow(fact[MAX - 1], MOD - 2, MOD)
for i in range(MAX - 2, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

# Example
print(nCr(10, 3))  # Output: 120
```
---

## ⏱️ Complexity
- Preprocessing: O(n)
- Query: O(1)
- Space: O(n)

---

## 🧭 Applications
- Counting combinations and permutations
- DP with combinatorics
- Probability problems
- Modular arithmetic in cryptography
- Pascal’s Triangle under modulo

---

## 🔗 Useful Links
- [**CP-Algo Binomial Coefficients**](https://cp-algorithms.com/combinatorics/binomial-coefficients.html)
- [**GeeksForgeeks - nCr%p**](https://www.geeksforgeeks.org/compute-ncr-p-set-1-introduction-and-dynamic-programming-solution/)

--