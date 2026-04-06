# ♾️ Divide and Conquer — Algorithms

This section contains classic problems and algorithms solved by the **divide and conquer** paradigm. This approach recursively splits a problem into smaller subproblems, solves them separately, and combines their results.

---

## Quick overview of algorithms

| **Algorithm**        | **Time Complexity** | **Space Complexity** |
|:----------------------|:-------------------|:--------------------|
| [**Closest Pair of Points**](./Closest%20Pair%20of%20Points) | O(n log n)      | O(n)             |
| [**Convex Hull (Divide-and-Conquer version)**](./Convex%20Hull%20(Divide-and-Conquer%20version)) | O(n log n)      | O(n)             |
| [**Maximum Subarray (D&C version)**](./Maximum%20Subarray%20(D%26C%20version)) | O(n log n)      | O(log n)         |
| [**Count Inversions**](./Count%20Inversions) | O(n log n)      | O(n)             |
| [**Kth Element (QuickSelect)**](./Kth%20Element%20(QuickSelect)) | O(n) avg / O(n²) worst | O(1)      |
| [**Majority Element (D&C version)**](./Majority%20Element%20(D%26C%20version)) | O(n log n)      | O(log n)         |
| [**Karatsuba Algorithm**](./Karatsuba%20Algorithm)|O(n^log₂3) ≈ O(n^1.585)|O(n)|
| [**Strassen’s Matrix Multiplication**](./Strassen%E2%80%99s%20Matrix%20Multiplication)|O(n^log₂7) ≈ O(n^2.81)|O(n²)|

---

## Where to use and why

### 1. **Closest Pair of Points**
- **Best for:** Computational geometry, finding the closest pair among points in the plane.
- **Why D&C:** Only practical way to get O(n log n) solution.
- **When not:** For very small n, brute force is simpler.

### 2. **Convex Hull (D&C version)**
- **Best for:** Image processing, GIS, convex hull detection.
- **Why D&C:** Effective for large sets of points.
- **When not:** For small sets, Graham scan or Jarvis march may be easier.

### 3. **Maximum Subarray (D&C version)**
- **Best for:** Learning D&C paradigm, parallel or generalized solutions.
- **Why D&C:** Good for theory and when you want to parallelize.
- **When not:** Kadane’s algorithm (O(n)) is much faster and simpler for 1D case.

### 4. **Count Inversions**
- **Best for:** Measuring “disorder” in arrays, permutation analysis, bioinformatics.
- **Why D&C:** Efficient O(n log n) counting.
- **When not:** For small arrays, brute-force is fine.

### 5. **Kth Element (QuickSelect)**
- **Best for:** Quickly finding the k-th minimum/maximum (e.g., median).
- **Why D&C:** Avoids full sort for big arrays.
- **When not:** In rare worst cases (O(n²)), but can be mitigated with random pivot.

### 6. **Majority Element (D&C version)**
- **Best for:** Teaching D&C or when generalizing the problem.
- **Why D&C:** Educational and extendable.
- **When not:** Boyer-Moore (O(n), O(1) space) is superior in practice.

### 7. **Karatsuba Algorithm**
- **Best for:** Multiplying very large numbers (cryptography, scientific computing).
- **Why D&C:** Much faster than grade-school for long numbers.
- **When not:** For small numbers, classic multiplication is faster.

### 8. **Strassen’s Matrix Multiplication**
- **Best for:** Fast multiplication of large square matrices.
- **Why D&C:** Useful for huge matrices (thousands x thousands).
- **When not:** For small matrices, classic algorithm is simpler and faster; also needs square matrices of size 2^n.

---

## Summary

- **Divide and Conquer** is a powerful and universal technique for complex problems, providing speed and scalability.
- For small sizes, classical/greedy/dynamic methods are often simpler and faster.
- Be aware of memory and implementation specifics for each algorithm.

---

## Useful links

- [Wikipedia: Divide and conquer algorithm](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm)
- [GeeksforGeeks: Divide and Conquer Introduction](https://www.geeksforgeeks.org/divide-and-conquer-algorithm-introduction/)
- [Visualize algorithms](https://visualgo.net/en)

---