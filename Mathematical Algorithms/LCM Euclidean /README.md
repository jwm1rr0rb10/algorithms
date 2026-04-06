# 🔁 LCM — Least Common Multiple (via Euclidean Algorithm)

## 📌 Problem Description

The **Least Common Multiple (LCM)** of two integers `a` and `b` is the smallest positive integer divisible by both `a` and `b`.

It is related to the GCD by the identity:

- `lcm(a, b) = abs(a * b) / gcd(a, b)`


This allows us to compute LCM efficiently using the Euclidean Algorithm.

---

## 💡 Idea and Approach

1. Compute `gcd(a, b)` using Euclidean Algorithm
2. Use the formula:  
   `lcm(a, b) = abs(a * b) // gcd(a, b)`

---

## 🧪 Python Example

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Example
print(lcm(12, 18))  # Output: 36
```

--- 

## ⏱️ Complexity
- Time: O(log min(a, b))
- Space: O(1)

---

## 🧭 Applications
- Synchronizing cycles (e.g., traffic lights, gears)
- Scheduling problems
- Number theory and modular arithmetic
- Cryptography (e.g., RSA uses lcm(φ(p), φ(q)))

---

## ⚠️ Caution
- Use abs(a * b) to avoid negative results
- For large a and b, use a // gcd(a, b) * b to avoid overflow

---

## 🔗 Useful Links
- [**CP Algorithms LCM**](https://cp-algorithms.com/algebra/lcm.html)
- [**GeeksForGeeks LCM and GCD**]( https://www.geeksforgeeks.org/lcm-of-given-array-elements/)

---