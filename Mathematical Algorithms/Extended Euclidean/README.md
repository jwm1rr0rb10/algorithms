# 📐 Extended Euclidean Algorithm

## 📌 Problem Description

The **Extended Euclidean Algorithm** is an extension of the classic Euclidean Algorithm for computing the greatest common divisor (GCD) of two integers `a` and `b`. In addition to computing `gcd(a, b)`, it also finds integers `x` and `y` such that:

- `a·x + b·y = gcd(a, b)`


This identity is known as **Bézout's identity**.

---

## 💡 Idea and Approach

The algorithm is recursive and works as follows:

- Base case:  
  If `a = 0`, then `gcd(a, b) = b`, and the solution is `x = 0`, `y = 1`.

- Recursive case:  
  Call `extended_gcd(b % a, a)` and backtrack to compute `x` and `y`.

This is especially useful for:
- Finding modular inverses: `a⁻¹ mod m` exists if and only if `gcd(a, m) = 1`
- Solving linear Diophantine equations
- CRT when moduli are not coprime

---

## 🧪 Python Example

```python
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Example: Solve 30x + 20y = gcd(30, 20)
g, x, y = extended_gcd(30, 20)
print(f"gcd = {g}, x = {x}, y = {y}")  # Output: gcd = 10, x = 1, y = -1
```

---

## ⏱️ Complexity
- Time: O(log max(a, b))
- Space: O(log max(a, b)) due to recursion

---

## 🧭 Applications
- Modular inverse: a⁻¹ mod m = x if a·x ≡ 1 mod m
- Solving ax + by = c for integers x, y
- Chinese Remainder Theorem (non-coprime moduli)
- RSA key generation (modular inverse of e mod φ(n))

---

## 🔗 Useful Links
- [**CP-Algo Extended Euclid Algorithm**](https://cp-algorithms.com/algebra/extended-euclid-algorithm.html)
- [**GeeksForgeeks - Extended GCD**](https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/)

---