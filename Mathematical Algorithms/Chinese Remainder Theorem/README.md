# 🧮 Chinese Remainder Theorem

## 📌 Problem Description

The **Chinese Remainder Theorem (CRT)** provides a unique solution to a system of linear congruences, given that the moduli are pairwise coprime. Specifically, if we have:

- x ≡ a₁ mod m₁ 
- x ≡ a₂ mod m₂ 
- ... 
- x ≡ aₖ mod mₖ

- where `m₁, m₂, ..., mₖ` are pairwise coprime positive integers, then there exists a unique solution for `x modulo M`, where:

- M = m₁ × m₂ × ... × mₖ


---

## 💡 Idea and Approach

To construct the solution:

1. **Compute M**:  
   Let `M = m₁ × m₂ × ... × mₖ`

2. **Compute Mᵢ**:  
   For each `i`, compute `Mᵢ = M / mᵢ`

3. **Find Modular Inverse yᵢ**:  
   For each `i`, find `yᵢ` such that:  
   `Mᵢ × yᵢ ≡ 1 mod mᵢ`  
   This is done using the Extended Euclidean Algorithm.

4. **Compute the Result**:  
   The solution is:  
    - x ≡ (a₁ × M₁ × y₁ + a₂ × M₂ × y₂ + ... + aₖ × Mₖ × yₖ) mod M


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

def mod_inverse(a, m):
 gcd, x, _ = extended_gcd(a, m)
 if gcd != 1:
     raise Exception("Modular inverse does not exist")
 return (x % m + m) % m

def chinese_remainder_theorem(congruences):
 # congruences: list of (aᵢ, mᵢ)
 M = 1
 for _, m in congruences:
     M *= m

 result = 0
 for a_i, m_i in congruences:
     M_i = M // m_i
     y_i = mod_inverse(M_i, m_i)
     result += a_i * M_i * y_i

 return result % M

# Example
congruences = [(2, 3), (3, 5), (2, 7)]
print(chinese_remainder_theorem(congruences))  # Output: 23
```

## ✅ Check:
- 23 % 3 = 2
- 23 % 5 = 3
- 23 % 7 = 2

---

## ⏱️ Complexity
- Time:
    - Calculating M: O(k)
    - For each congruence: modular inverse via Extended Euclidean Algorithm → O(log mᵢ)
    - Total: O(k log M)

- Space:
    -O(k) for storing intermediate values

---

## 🧭 Applications

 - 🔐 Cryptography: RSA, secret sharing, modular exponentiation

 - 🧮 Number Theory: Solving systems of congruences

 - 🖥️ Computer Science:

    - Arbitrary-precision arithmetic

    - Hashing and error correction

    - Parallel computation

 - 📅 Scheduling: Events with different cycles

 - 🌌 Astronomy: Predicting celestial alignments

---

## 🔗 Useful Links
- [**Wikipedia Chinese remainder theorem**](https://en.wikipedia.org/wiki/Chinese_remainder_theorem)
- [**GeeksForgeeks - CRT**](https://www.geeksforgeeks.org/chinese-remainder-theorem-set-1-introduction/)
- [**CP-Algo -CRT**](https://cp-algorithms.com/math/chinese_remainder_theorem.html)

---

## 🧩 LeetCode Connection

- While CRT isn’t always directly named, its principles appear in problems involving modular reasoning.

- Example:

    - LeetCode 1709 — Guess the Result in a Hidden Array (Hard)

        - You query nums[i] % nums[j] and reconstruct hidden values.

        - The logic of deducing a number from multiple remainders is closely related to CRT.

- CRT is a mathematical tool that often appears as a hidden layer in number theory and modular arithmetic problems.

---