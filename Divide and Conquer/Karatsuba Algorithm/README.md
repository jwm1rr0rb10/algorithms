# Karatsuba Algorithm — Divide & Conquer

## Problem description

**Karatsuba algorithm** is a fast multiplication algorithm for large numbers, using the divide & conquer principle. It multiplies two numbers faster than the traditional “schoolbook” algorithm.

**Task:**  
Given two large numbers (as strings or arrays of digits), compute their product.

**Example:**
```python
x = 1234
y = 5678
# Output: 7006652
```

## Algorithm (Karatsuba)

1. Split each number into two parts (high and low digits):
   - x = x1 * 10^m + x0
   - y = y1 * 10^m + y0
2. Recursively compute:
   - z0 = x0 * y0
   - z1 = (x0 + x1) * (y0 + y1)
   - z2 = x1 * y1
3. Combine the results:
   - x * y = z2 * 10^(2m) + (z1 - z2 - z0) * 10^m + z0

### Python code example

```python
def karatsuba(x, y):
    # Base case for small numbers
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split numbers
    x1, x0 = divmod(x, 10**m)
    y1, y0 = divmod(y, 10**m)

    # Recursively compute
    z0 = karatsuba(x0, y0)
    z2 = karatsuba(x1, y1)
    z1 = karatsuba(x0 + x1, y0 + y1) - z2 - z0

    return z2 * 10**(2*m) + z1 * 10**m + z0

# Usage example:
x = 1234
y = 5678
print(karatsuba(x, y))  # 7006652
```

## Time complexity

- O(n^log2(3)) ≈ O(n^1.585), where n is the number of digits.

## When to use

- Working with long/integer arithmetic (cryptography, scientific calculations).
- In calculators, symbolic computation, scientific libraries.

## Drawbacks

- For very small numbers, schoolbook multiplication is faster and simpler.
- Needs extra memory for recursion.

---

## Useful links

- [Wikipedia: Karatsuba algorithm](https://en.wikipedia.org/wiki/Karatsuba_algorithm)
- [GeeksforGeeks: Karatsuba algorithm for fast multiplication](https://www.geeksforgeeks.org/karatsuba-algorithm-for-fast-multiplication/)
- [YouTube: Karatsuba Multiplication Visualized](https://www.youtube.com/watch?v=7K1sB05pE0A)

---

## LeetCode Problems

- [43. Multiply Strings (Medium)](https://leetcode.com/problems/multiply-strings/) — implement multiplication of large numbers as strings.
- [2. Add Two Numbers (Medium)](https://leetcode.com/problems/add-two-numbers/) — digit-by-digit addition (similar approach).

---