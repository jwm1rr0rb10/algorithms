# 📏 GCD — Euclidean Algorithm

## 📌 Problem Description

The **Greatest Common Divisor (GCD)** of two integers `a` and `b` is the largest number that divides both without leaving a remainder.  
The **Euclidean Algorithm** efficiently computes `gcd(a, b)` using the identity:

- `gcd(a, b) = gcd(b, a % b)`


This continues until `b = 0`, at which point `gcd(a, 0) = a`.

---

## 💡 Idea and Approach

The algorithm is based on the fact that:

- If `a = bq + r`, then `gcd(a, b) = gcd(b, r)`
- This reduces the problem size at each step

---

## 🧪 Python Example

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example
print(gcd(30, 18))  # Output: 6
```

---

## ⏱️ Complexity
- Time: O(log min(a, b))
- Space: O(1) (iterative version)

---

## 🧭 Applications
- Simplifying fractions: a / b → reduce by gcd(a, b)
- Modular inverse (via extended GCD)
- LCM computation: lcm(a, b) = a * b / gcd(a, b)
- Number theory, cryptography, Diophantine equations

---

## 🔗 Useful Links
- [**CP Algorithms Euclid Algo**](https://cp-algorithms.com/algebra/euclid-algorithm.html)
- [**GeeksForgeeks GCD**]( https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/)

---