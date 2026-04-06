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


## ✅ Check:
## 23 % 3 = 2
## 23 % 5 = 3
## 23 % 7 = 2