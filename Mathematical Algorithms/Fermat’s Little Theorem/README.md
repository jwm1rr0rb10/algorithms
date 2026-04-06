# 🔁 Fermat’s Little Theorem

## 📌 Problem Description

**Fermat’s Little Theorem** states:

> If `p` is a prime number and `a` is an integer such that `a % p ≠ 0`, then:
>
> ```
> a^(p - 1) ≡ 1 mod p
> ```

From this, we can derive the modular inverse of `a` modulo `p`:

- `a^(-1) ≡ a^(p - 2) mod p`


This is extremely useful for computing modular inverses when `p` is prime.

---

## 💡 Idea and Approach

To compute `a^(-1) mod p`:

1. Ensure `p` is prime and `gcd(a, p) = 1`
2. Use fast exponentiation to compute `a^(p - 2) % p`

---

## 🧪 Python Example

```python
def mod_inverse(a, p):
    return pow(a, p - 2, p)  # Fermat’s Little Theorem

# Example
print(mod_inverse(3, 7))  # Output: 5, since 3 * 5 ≡ 1 mod 7
```

---

## ⏱️ Complexity
- Time: O(log p) using fast exponentiation
- Space: O(1)

---

## 🧭 Applications
- Modular inverse in combinatorics (nCr % p)
- RSA cryptography (when modulus is prime)
- Solving modular equations
- Simplifying fractions under modulo

---

## ⚠️ Limitations
- Only works when p is prime
- If mod is not prime, use the Extended Euclidean Algorithm instead

---

## 🔗 Useful Links
- [**CP Algorithms Fermat Theorem**](https://cp-algorithms.com/algebra/fermat-theorem.html)
- [**GeeksForgeeks Fermats Little Theorem**](https://www.geeksforgeeks.org/fermats-little-theorem/)

--