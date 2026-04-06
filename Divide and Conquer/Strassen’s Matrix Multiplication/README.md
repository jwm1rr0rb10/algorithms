# Strassen’s Matrix Multiplication — Divide & Conquer

## Problem description

**Strassen’s algorithm** is a fast matrix multiplication algorithm using the divide & conquer principle. It multiplies two square matrices faster than the standard (naive) algorithm, especially for large sizes.

**Task:**  
Given two square matrices A and B of size 2^n × 2^n, compute their product C = A × B.

**Example:**
```python
A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
# Output: [[19, 22], [43, 50]]
```

## Algorithm (Strassen)

1. Split each matrix into four submatrices of equal size:
    - A = |A11 A12|
          |A21 A22|
    - B = |B11 B12|
          |B21 B22|
2. Compute 7 special products (M1–M7) instead of 8 as in the regular algorithm:
    - M1 = (A11 + A22) × (B11 + B22)
    - M2 = (A21 + A22) × B11
    - M3 = A11 × (B12 - B22)
    - M4 = A22 × (B21 - B11)
    - M5 = (A11 + A12) × B22
    - M6 = (A21 - A11) × (B11 + B12)
    - M7 = (A12 - A22) × (B21 + B22)
3. Assemble the result from sums and differences of these products.

### Python code example

```python
def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    mid = n // 2

    # Split matrices into 4 blocks
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # 7 Strassen products
    M1 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen(add_matrix(A21, A22), B11)
    M3 = strassen(A11, sub_matrix(B12, B22))
    M4 = strassen(A22, sub_matrix(B21, B11))
    M5 = strassen(add_matrix(A11, A12), B22)
    M6 = strassen(sub_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen(sub_matrix(A12, A22), add_matrix(B21, B22))

    # Assemble result
    def combine(C11, C12, C21, C22):
        top = [c11 + c12 for c11, c12 in zip(C11, C12)]
        bottom = [c21 + c22 for c21, c22 in zip(C21, C22)]
        return top + bottom

    C11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(sub_matrix(add_matrix(M1, M3), M2), M6)
    return combine(C11, C12, C21, C22)

# Usage example:
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(strassen(A, B))  # [[19, 22], [43, 50]]
```

## Time complexity

- O(n^log2(7)) ≈ O(n^2.81)

## When to use

- Fast multiplication of large square matrices (e.g., scientific computation, image processing, computer vision).
- When asymptotic speed is important for very large matrices.

## Drawbacks

- For small matrices, standard multiplication is faster due to overhead.
- Not suitable for non-square or non-2^n matrices without padding.
- Requires extra memory.

---

## Useful links

- [Wikipedia: Strassen algorithm](https://en.wikipedia.org/wiki/Strassen_algorithm)
- [GeeksforGeeks: Strassen’s Matrix Multiplication](https://www.geeksforgeeks.org/strassens-matrix-multiplication/)
- [YouTube: Strassen Algorithm Visualization](https://www.youtube.com/watch?v=6-4vYyq8eHc)

---

## LeetCode Problems

- [3127. Beautiful Tiling (Hard, requires large matrix multiplications)](https://leetcode.com/problems/beautiful-tiling/)
- [LCP 50. Treasure (Hard, matrix operations)](https://leetcode.com/problems/treasure/)
- [552. Student Attendance Record II (Hard, DP + matrix expo)](https://leetcode.com/problems/student-attendance-record-ii/)

---