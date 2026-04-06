# ⚡ Fast Power (Exponentiation by Squaring)

## 📌 Problem Description

Fast exponentiation is used to compute `a^b % mod` efficiently, especially when `b` is large (up to 10¹⁸ or more).  
The naive approach takes O(b) time, but **Exponentiation by Squaring** reduces it to O(log b).

---

## 💡 Idea and Approach

The key idea is:

- If `b` is even:  
  `a^b = (a^(b/2))^2`

- If `b` is odd:  
  `a^b = a × a^(b - 1)`

This allows us to reduce the exponent by half at each step.

---

## 🧪 Python Example

```python
def fast_pow(a, b, mod):
    result = 1
    a %= mod
    while b > 0:
        if b % 2 == 1:
            result = result * a % mod
        a = a * a % mod
        b //= 2
    return result

# Example
print(fast_pow(2, 10, 1000))  # Output: 24 (since 2^10 = 1024, 1024 % 1000 = 24)
```

---

## ⏱️ Complexity
- Time: O(log b)
- Space: O(1) (iterative version)

---

## 🧭 Applications
- Modular exponentiation (e.g., RSA, Fermat’s Little Theorem)
- Computing large powers in combinatorics (e.g., inverse factorials)
- Binary exponentiation in matrix exponentiation
- Fast Fibonacci computation

---

## 🔗 Useful Links
- [**CP Algo *Binary Exponentiation**](https://cp-algorithms.com/algebra/binary-exp.html)
- [**GeeksForgeeks Modular Exponentiation**](https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/)