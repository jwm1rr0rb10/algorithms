# 🧮 Modular Inverse

## 📌 Problem Description

- The Modular Multiplicative Inverse of an integer a modulo m is an integer x such that:
    - `(a⋅x)≡1(modm)`

- The modular inverse exists if and only if a and m are coprime (i.e., their greatest common divisor (GCD) is 1), i.e., `textgcd(a,m)=1`.

- There are two primary methods to find the modular inverse:

    - Extended Euclidean Algorithm: This method is general and works for any m.

    - Fermat's Little Theorem: This method is applicable only when m is a prime number.

---

## 💡 Idea and Approach

**1. Extended Euclidean Algorithm**

- The Extended Euclidean Algorithm finds integers x and y such that:

```text
a⋅x+m⋅y=gcd(a,m)
```

```text
If $ \text{gcd}(a, m) = 1 $, then the equation becomes:
a⋅x+m⋅y=1
```

- Taking this equation modulo `m`:
```text
(a⋅x+m⋅y)(modm)≡1(modm)
(a⋅x)(modm)+(m⋅y)(modm)≡1(modm)
(a⋅x)(modm)+0≡1(modm)
(a⋅x)(modm)≡1(modm)
```

Thus, the `x` found by the Extended Euclidean Algorithm is the modular inverse of a modulo `m`. If `x` is negative, we can add `m` to it until it becomes positive `(x=(x)`.

**2. Fermat's Little Theorem (when m is prime)**

Fermat's Little Theorem states that if `p` is `a` prime number, then for any integer `a` not divisible by `p`:
```text
ap−1≡1(modp)
```

Multiplying both sides by `a−1`:
```text
ap−2≡a−1(modp)
```

Therefore, the modular inverse of a modulo `a` prime `p` is `ap−2pmodp`, which can be computed efficiently using modular exponentiation (binary exponentiation).

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

def modular_inverse_extended_euclidean(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None  # Modular inverse does not exist
    else:
        return (x % m + m) % m # Ensure result is positive

def power(base, exp, mod):
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def modular_inverse_fermat_little_theorem(a, m):
    # Only works if m is a prime number
    # and a is not a multiple of m
    if m <= 1:
        return None # Modulus must be a prime > 1
    # For simplicity, we won't add a prime check here, but it's crucial in practice.
    # In a real scenario, you'd add a prime check for m.
    
    # If a is a multiple of m, inverse doesn't exist
    if a % m == 0:
        return None 
    
    return power(a, m - 2, m)

# Example Usage

# Using Extended Euclidean Algorithm
a = 3
m = 11 # 11 is prime, but this method works for any m where gcd(a,m)=1
inv_ee = modular_inverse_extended_euclidean(a, m)
print(f"Modular inverse of {a} mod {m} (Extended Euclidean): {inv_ee}") # Output: 4 (since 3*4=12, 12%11=1)

a = 7
m = 26 # m is not prime, so Fermat's Little Theorem cannot be directly applied
inv_ee_non_prime = modular_inverse_extended_euclidean(a, m)
print(f"Modular inverse of {a} mod {m} (Extended Euclidean): {inv_ee_non_prime}") # Output: 15 (since 7*15=105, 105%26=1)

# Using Fermat's Little Theorem (m must be prime)
a = 3
m_prime = 11
inv_flt = modular_inverse_fermat_little_theorem(a, m_prime)
print(f"Modular inverse of {a} mod {m_prime} (Fermat's Little Theorem): {inv_flt}") # Output: 4

a = 5
m_prime_2 = 13
inv_flt_2 = modular_inverse_fermat_little_theorem(a, m_prime_2)
print(f"Modular inverse of {a} mod {m_prime_2} (Fermat's Little Theorem): {inv_flt_2}") # Output: 8 (since 5*8=40, 40%13=1)
```

---

## ⏱️ Complexity

1. Extended Euclidean Algorithm

    - `Time`: `O(log(min(a,m)))` - Same as GCD computation.

    - `Space`: `O(log(min(a,m)))` for recursive calls, or `O(1)` for an iterative version.


2. Fermat's Little Theorem (with Modular Exponentiation)

    - `Time: O(logm)` - Due to modular exponentiation.

    - Space: `O(1)`

## 🧭 Applications

1. `Cryptography`: Essential in public-key cryptosystems like RSA for key generation and decryption.

2. `Modular Arithmetic`: Solving linear congruences of the form axequivbpmodm.

3. `Number Theory`: Various problems involving modular division. (Division by a modulo m is equivalent to multiplication by the modular inverse of a modulo m).

4. `Combinatorics`: Computing "n choose k" modulo a prime number, where division by factorials is required.

## ⚠️ Caution

1. Existence: The modular inverse a−1pmodm exists if and only if textgcd(a,m)=1. Always check this condition.

2. Fermat's Little Theorem Restriction: This theorem is only applicable when the modulus m is a prime number. For composite moduli, the Extended Euclidean Algorithm must be used.

3. Negative Results: The Extended Euclidean Algorithm might return a negative x. Remember to convert it to a positive equivalent by adding m (e.g., x=(x).

## 🔗 Useful Links

1. [**CP Algorithms - Modular Inverse**](https://cp-algorithms.com/algebra/module-inverse.html)

2. [**GeeksForGeeks - Modular Multiplicative Inverse**](https://www.geeksforgeeks.org/dsa/multiplicative-inverse-under-modulo-m/) 

3. [**Khan Academy - Modular Inverse**](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-inverses)

