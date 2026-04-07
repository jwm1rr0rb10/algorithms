# 📌 Core Algorithms for FAANG Interviews

- [**The Leetcode Guide**](https://dev.to/dfs_with_memo/leetcode-survival-guide-1cp3)

- [**Backtracking Patterns**](https://medium.com/leetcode-patterns/leetcode-pattern-3-backtracking-5d9e5a03dc26)
- [**Sliding Window patterns**]( https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1175088/C++-Maximum-Sliding-Window-Cheatsheet-Template/)
- [**Sliding Windows on Strings Pattern:**](https://medium.com/leetcode-patterns/leetcode-pattern-2-sliding-windows-for-strings-e19af105316b)
- [**Two Pointers Patterns**](https://leetcode.com/discuss/post/1688903/solved-all-two-pointers-problems-in-100-z56cn/) 
- [**Substring Problem Patterns**](https://leetcode.com/problems/minimum-window-substring/solutions/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems/)
- [**Tree Patterns:**](https://leetcode.com/discuss/post/937307/iterative-recursive-dfs-bfs-tree-travers-e1f4/)
- [**Tree Iterative Traversal:**](https://medium.com/leetcode-patterns/leetcode-pattern-0-iterative-traversals-on-trees-d373568eb0ec)
- [**Dynamic Programming Patterns:**](https://leetcode.com/discuss/post/458695/dynamic-programming-patterns-by-aatalyk-pmgr/)
- [**Binary Search Patterns:**](https://leetcode.com/discuss/post/786126/python-powerful-ultimate-binary-search-t-rwv8/)
- [**Monotonic Stack Patterns:**](https://leetcode.com/discuss/post/2347639/a-comprehensive-guide-and-template-for-m-irii/)
- [**Graph Patterns:**](https://leetcode.com/discuss/post/655708/graph-for-beginners-problems-pattern-sam-06fb/)
- [**DFS + BFS Patterns (1):**](https://medium.com/leetcode-patterns/leetcode-pattern-1-bfs-dfs-25-of-the-problems-part-1-519450a84353)
- [**DFS + BFS Patterns (2):**](https://medium.com/leetcode-patterns/leetcode-pattern-2-dfs-bfs-25-of-the-problems-part-2-a5b269597f52)

## [**🛠 Recursion and Backtracking**](https://github.com/jwm1rr0rb10/algorithms/tree/main/%20Recursion%20and%20Backtracking)

| **Algorithm**                                                                                                                                                                                    | **Time Complexity**                            | **Space Complexity**                                        |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------|:------------------------------------------------------------|
| [**Combinations All Combinations (any length)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/%20Recursion%20and%20Backtracking/Combinations%20All%20Combinations%20(any%20length))       | O(2^n) (each element can be included/excluded) | O(n) (stack), O(2^n × n) (if storing all)                   |
| [**Combinations Recursive (Backtracking) Approach**](https://github.com/jwm1rr0rb10/algorithms/tree/main/%20Recursion%20and%20Backtracking/Combinations%20Recursive%20(Backtracking)%20Approach) | O(C(n, k)) — n choose k                        | O(k) (recursion stack)                                      |
| [**Generate Parentheses**](https://github.com/jwm1rr0rb10/algorithms/tree/main/%20Recursion%20and%20Backtracking/Generate%20Parentheses)                                                         | O(4^n / √n), nth Catalan number                | O(n) (stack)                                                |
| [**Letter Combinations of a Phone Number**](https://github.com/jwm1rr0rb10/algorithms/tree/main/%20Recursion%20and%20Backtracking/Letter%20Combinations%20of%20a%20Phone%20Number)               | O(4^n) (n = digits, max 4 letters per digit)   | O(n) (stack)                                                |
| [**N-Queens problem**](https://github.com/jwm1rr0rb10/algorithms/tree/main/%20Recursion%20and%20Backtracking/N-Queens%20problem)                                                                                                                                                                         | O(n!)                                          | O(n²)                                                       |
| [**Palindrome Partitioning**](https://github.com/jwm1rr0rb10/algorithms/tree/main/%20Recursion%20and%20Backtracking/Palindrome%20Partitioning)                                                                                                                                                                  | O(2^n) (all possible partitions)               | O(n) (stack)                                                |
| [**Partition problem**](https://github.com/jwm1rr0rb10/algorithms/tree/main/%20Recursion%20and%20Backtracking/Partition%20problem)                                                                                                                                                                        | O(2^n) — try all subsets                       | O(n) (stack)                                                |
| [**Permutations**](https://github.com/jwm1rr0rb10/algorithms/tree/main/%20Recursion%20and%20Backtracking/Permutations)                                                                                                                                                                             | O(n × n!)                                      | O(n)                                                        |
| [**Restore IP Addresses**](https://github.com/jwm1rr0rb10/algorithms/tree/main/%20Recursion%20and%20Backtracking/Restore%20IP%20Addresses)                                                                                                                                                                     | O(1) (bounded, splits into 4 parts)            | O(1) (stack)                                                |
| [**Subset sum**](https://github.com/jwm1rr0rb10/algorithms/tree/main/%20Recursion%20and%20Backtracking/Subset%20sum)                                                                                                                                                                               | O(n * sum)                                     | O(sum) (if using space optimization), otherwise O(n * sum)  |
| [**Sudoku solver**](https://github.com/jwm1rr0rb10/algorithms/tree/main/%20Recursion%20and%20Backtracking/Sudoku%20solver)                                                                                                                                                                            | O(9^(n))                                       | O(n)                                                        |
| [**Word Search**](https://github.com/jwm1rr0rb10/algorithms/tree/main/%20Recursion%20and%20Backtracking/Word%20Search)                                                                                                                                                                              | O(N × 4^L) (N=board size, L=word)              | O(L)                                                        |

---

**Legend:**  
- *n* — number of elements (digits, size, etc.)  
- *k* — length of a combination  
- *N* — number of cells in the board (Word Search)  
- *L* — length of the word (Word Search)  
- *m* — number of empty cells (Sudoku)  
- *C(n, k)* — “n choose k”

**Notes:**  
- Space complexity is typically recursion stack depth.  
- If you need to store all solutions, total memory can be much higher.  
- These are classic interview problems for FAANG/MANGO and similar companies.

---

## [**💡 Bit Manipulation**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation)

| **Algorithm / Pattern**                                                                                                                                                   | **Time Complexity**              | **Space Complexity** |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------|:---------------------|
| [**Bit masking**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Bit%20masking)                                                                                                                                                       | O(1) per op                      | O(1)                 |
| [**Bitmask DP (TSP, etc.)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Bitmask%20DP%20(TSP%2C%20etc.))                                          | O(2^n × n)                       | O(2^n)               |
| [**Bitwise AND of Numbers Range**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Bitwise%20AND%20of%20Numbers%20Range)                               | O(1)                             | O(1)                 |
| [**Bitwise Complement (inversion)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Bitwise%20Complement%20(inversion))                               | O(1)                             | O(1)                 |
| [**Clear ith bit**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Clear%20ith%20bit)                                                              | O(1)                             | O(1)                 |
| [**Count set bits (Hamming weight)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Count%20set%20bits%20(Hamming%20weight))                         | O(log n)                         | O(1)                 |
| [**Detect if two numbers have opposite signs**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Detect%20if%20two%20numbers%20have%20opposite%20signs) | O(1)                             | O(1)                 |
| [**Divide Two Integers (bitwise division)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Divide%20Two%20Integers%20(bitwise%20division))          | O(1) (32-bit int)                | O(1)                 |
| [**Find Missing Number using XOR**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Find%20Missing%20Number%20using%20XOR)                             | O(n)                             | O(1)                 |
| [**Find Rightmost Set Bit**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Find%20Rightmost%20Set%20Bit)                                            | O(1)                             | O(1)                 |
| [**Get ith bit**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Get%20ith%20bit)                                                                   | O(1)                             | O(1)                 |
| [**Gray Code generation**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Gray%20Code%20generation)                                                   | O(2^n)                           | O(2^n)               |
| [**Hamming Distance**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Hamming%20Distance)                                                             | O(1)                             | O(1)                 |
| [**Maximum Product of Word Lengths**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Maximum%20Product%20of%20Word%20Lengths)                         | O(n^2)                           | O(n)                 |
| [**Power of Two check**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Power%20of%20Two%20check)                                                     | O(1)                             | O(1)                 |
| [**Reverse bits of an integer**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Reverse%20bits%20of%20an%20integer)                                  | O(1)                             | O(1)                 |
| [**Set ith bit**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Set%20ith%20bit)                                                                   | O(1)                             | O(1)                 |
| [**Single Number I**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Single%20Number%20I)                                                          | O(n)                             | O(1)                 |
| [**Single Number II**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Single%20Number%20II)                                                           | O(n)                             | O(1)                 |
| [**Single Number III**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Single%20Number%20III)                                                         | O(n)                             | O(1)                 |
| [**Subsets using bits**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Subsets%20using%20bits)                                                      | O(2^n × n)                       | O(1)                 |
| [**Subset Generation with Bitmask**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Subset%20Generation%20with%20Bitmask)                         |       O(n × 2^n)     |  O(n × 2^n)                                            |
| [**Sum without '+' (bitwise sum)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Sum%20without%20'%2B'%20(bitwise%20sum))                         | O(1) (32-bit int)                | O(1)                 |
| [**Toggle ith bit**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/Toggle%20ith%20bit)                                                            | O(1)                             | O(1)                 |
| [**XOR tricks single/unique numbers**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/XOR%20tricks%20single%20unique%20numbers)                      | O(n) (array)                     | O(1)                 |
| [**XOR tricks swap**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Bit%20Manipulation/XOR%20tricks%20swap)                                                             | O(n) (array), O(1) (swap)        | O(1)                 |
---

**Legend:**  
- *n* — number of bits or elements in array

**Notes:**  
- Bit manipulation is key for optimization and clever solutions in many FAANG/MANGO coding interviews.
- "Single Number" problems (I/II/III) are LeetCode classics for unique element finding with XOR and bitwise ops.
- Bitmask DP and subset generation are advanced, often used in "hard" dynamic programming problems.
- It’s important to understand set/get/clear/toggle bit tricks for both data representation and interview puzzles.

---

## [**♾️ Divide and Conquer**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Divide%20and%20Conquer)

| **Algorithm**                                                                                                                                                             | **Time Complexity** | **Space Complexity** |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------|:--------------------|
| [**Closest Pair of Points**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Divide%20and%20Conquer/Closest%20Pair%20of%20Points)                                     | O(n log n)      | O(n)             |
| [**Convex Hull (Divide-and-Conquer version)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Divide%20and%20Conquer/Convex%20Hull%20(Divide-and-Conquer%20version)) | O(n log n)      | O(n)             |
| [**Count Inversions**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Divide%20and%20Conquer/Count%20Inversions)                                                                                                                                                  | O(n log n)      | O(n)             |
| [**Karatsuba Algorithm**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Divide%20and%20Conquer/Karatsuba%20Algorithm)                                                                                                                                               |O(n^log₂3) ≈ O(n^1.585)|O(n)|
| [**Kth Element (QuickSelect)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Divide%20and%20Conquer/Kth%20Element%20(QuickSelect))                                                                                                                                         | O(n) avg / O(n²) worst | O(1)      |
| [**Majority Element (D&C version)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Divide%20and%20Conquer/Majority%20Element%20(D%26C%20version))                                                                                                                                    | O(n log n)      | O(log n)         |
| [**Maximum Subarray (D&C version)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Divide%20and%20Conquer/Maximum%20Subarray%20(D%26C%20version))                                                                                                                                    | O(n log n)      | O(log n)         |
| [**Strassen’s Matrix Multiplication**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Divide%20and%20Conquer/Strassen%E2%80%99s%20Matrix%20Multiplication)                                                                                                                                  |O(n^log₂7) ≈ O(n^2.81)|O(n²)|

---

**Legend:**  
- *n* — number of elements/points
- For **Karatsuba Algorithm** Where n is the number of digits in the number.
The algorithm is faster than classical O(n²) multiplication due to the use of divide and conquer.
- For **StrassClosest Pair of Points: Подробное объяснениеen’s Matrix Multiplication** Where n is the dimension of the square matrix (n x n).
The algorithm is faster than standard O(n³) matrix multiplication by reducing the number of recursive multiplications.

**Notes:**  
- Divide and conquer is a general approach: break problems into subproblems, solve recursively, and combine solutions.
- Many classic sorting and searching algorithms are divide and conquer (see other sections).
- Computational geometry problems like Closest Pair and Convex Hull are classic D&C interview questions.

---

## [**Dynamic Programming**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming)

| **Algorithm**                                                                                                                                  | **Time Complexity**  | **Space Complexity**   |
|:-----------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|:-----------------------|
| [**Coin Change**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/Coin%20Change)                                         | O(n * amount)        | O(amount)              |
| [**DP on Graphs**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/DP%20on%20Graphs)                                    | O(V + E)             | O(V + E)               |
| [**DP on Trees**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/DP%20on%20Trees)                                       | O(n)                 | O(n)                   |
| [**Edit Distance**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/Edit%20Distance)                                    | O(m * n)             | O(m * n)               |
| [**House Robber**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/House%20Robber)                                       | O(n)                 | O(1)                   |
| [**Knapsack**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/Knapsack)                                                 | O(n * W)             | O(n * W)               |
| [**Longest Common Subsequence**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/Longest%20Common%20Subsequence)         | O(m * n)             | O(m * n)               |
| [**Longest Increasing Subsequence**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/Longest%20Increasing%20Subsequence) | O(n * log n)         | O(n)                   |
| [**Longest Palindromic Substring**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/Longest%20Palindromic%20Substring)   | O(n^2)               | O(n^2)                 |
| [**Matrix Chain Multiplication**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/Matrix%20Chain%20Multiplication)       | O(n^3)               | O(n^2)                 |
| [**Memoization**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/Memoization)                                           | O(n)                 | O(n)                   |
| [**Paint House**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/Paint%20House)                                         | O(n)                 | O(n)                   |
| [**Palindrome Subarray**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/Palindrome%20Subarray)                           | O(n^2)               | O(n^2)                 |
| [**Palindrome Subsequence**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/Palindrome%20Subsequence)                   | O(n^2)               | O(n^2)                 |
| [**Partition problem**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/Partition%20problem)                             | O(n * sum)           | O(n * sum)             |
| [**Tabulation**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/Tabulation)                                             | O(n * sum/2)         | O(n * sum/2)           |
| [**Word Break**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Dynamic%20Programming/Word%20Break)                                           | O(n²)                | O(n)                   |

### **Legend**

- *n*   — The number of elements (e.g., in an array, or nodes in a tree).
- *m*   — The length of the string in problems like Edit Distance or Longest Common Subsequence.
- *W*   — The weight capacity in the Knapsack problem.
- *V*   — The number of vertices in a graph.
- *E*   — The number of edges in a graph.
- *sum* — The total sum or capacity in problems like Partition Problem.

---

## [**📐 Geometry**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Geometry)

| **Algorithm**                                       | **Time Complexity** | **Space Complexity** |
|:----------------------------------------------------|:--------------------|:---------------------|
| [**Area of polygon**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Geometry/Area%20of%20polygon)                            | O(n)                | O(1)                 |
| [**Circle Intersection**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Geometry/Circle%20Intersection)                         | O(1)                | O(1)                 |
| [**Closest pair of points**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Geometry/Closest%20pair%20of%20points)                     | O(n log n)          | O(n)                 |
| [**Convex Hull Graham Scan**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Geometry/Convex%20Hull%20Graham%20Scan)                     | O(n log n)          | O(n)                 |
| [**Convex Hull Jarvis March**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Geometry/Convex%20Hull%20Jarvis%20March)                    | O(nh)               | O(1)                 |
| [**Line intersection**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Geometry/Line%20intersection)                           | O(1)                | O(1)                 |
| [**Line Segment Intersection**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Geometry/Line%20Segment%20Intersection)                  | O(1)                | O(1)                 |
| [**Point in Polygon (Ray Casting)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Geometry/Point%20in%20Polygon%20(Ray%20Casting))              | O(n)                | O(1)                 |
| [**Rectangle Intersection**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Geometry/Rectangle%20Intersection)                      | O(1)                | O(1)                 |
| [**Rectangle Overlap**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Geometry/Rectangle%20Overlap)                           | O(1)                | O(1)                 |
| [**Rotating Calipers (Convex Polygon Diameter)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Geometry/Rotating%20Calipers%20(Convex%20Polygon%20Diameter)) | O(n)                | O(1)                 |

---

**Legend:**  
- *n* — number of points.  
- *h* — number of points on the convex hull.

**Notes:**  
- Most geometry problems in interviews will be on convex hull, area, and closest pair.
- "Point in Polygon" and "Line Segment Intersection" are sometimes asked, especially for graphics or computational geometry roles.
- "Rectangle Overlap" is a classic in LeetCode and can be asked as a subproblem.
- "Rotating Calipers" and "Circle Intersection" are rare but useful for advanced/quant/graphics interviews.

---

## [**Greedy**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Greedy%20Algorithms)

| **Algorithm**                         | **Time Complexity** | **Space Complexity** |
|:--------------------------------------|:--------------------|:---------------------|
| [**Activity Selection**]((https://github.com/jwm1rr0rb10/algorithms/tree/main/Greedy%20Algorithms/Activity%20Selection)           | O(n)	              | O(1)                 |
| [**Fractional Knapsack**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Greedy%20Algorithms/Fractional%20Knapsack)           | O(n log n)          | O(1)                 |
| [**Huffman Encoding**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Greedy%20Algorithms/Huffman%20Encoding)              | O(n log n)          | O(n)                 |
| [**Job Scheduling**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Greedy%20Algorithms/Job%20Scheduling)                | O(n log n)          | O(n)                 |
| [**Minimum Spanning Tree Kruskal**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Greedy%20Algorithms/Minimum%20Spanning%20Tree%20Kruskal) | O(E log E)          | O(E)                 |
| [**Minimum Spaning Tree Prim**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Greedy%20Algorithms/Minimum%20Spanning%20Tree%20Prim)     | O(E + V log V)      | O(V + E)             |

---

**Legend:**  
- *n* — The number of elements (e.g., activities, jobs, or items in a knapsack).  
- *V* — The number of vertices (nodes) in a graph (used in Minimum Spanning Tree algorithms like Kruskal's and Prim's).
- *E* — The number of edges in a graph (used in Minimum Spanning Tree algorithms like Kruskal's and Prim's).
- *h* — The height of the disjoint-set (union-find) structure in Kruskal’s algorithm (usually close to O(log n) in practice).

---

## [**🧮 Mathematical Algorithms**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Mathematical%20Algorithms)

| **Algorithm**        | **Time Complexity** | **Space Complexity** |
|:-----------------------------|:----------------------|:----------------------------------|
| [**Chinese Remainder Theorem**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Mathematical%20Algorithms/Chinese%20Remainder%20Theorem)                | O(k log n)         | O(1)             |
| [**Combinatorics (nCr, factorials with mod)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Mathematical%20Algorithms/Combinatorics%20(nCr%2C%20factorials%20with%20mod)) | O(n) preprocessing | O(n)             |
| [**Extended Euclidean Algorithm**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Mathematical%20Algorithms/Extended%20Euclidean) | O(log n)  | O(1)               |                  |
| [**Fast Power (Exponentiation by Squaring)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Mathematical%20Algorithms/Fast%20Power%20(Exponentiation%20by%20Squaring))  | O(log n)           | O(1)             |
| [**Fermat’s Little Theorem**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Mathematical%20Algorithms/Fermat%E2%80%99s%20Little%20Theorem)                  | O(log n)           | O(1)             |
| [**GCD (Euclidean Algorithm)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Mathematical%20Algorithms/GCD%20Euclidean%20)                | O(log n)           | O(1)             |
| [**LCM (Euclidean Algorithm)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Mathematical%20Algorithms/LCM%20Euclidean%20)                | O(log n)           | O(1)             |
| [**Modular Inverse**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Mathematical%20Algorithms/Modular%20Inverse)                         |       O(log(min(a,m)))             |     O(log(min(a,m)))             |
| [**Primality Test (Miller-Rabin)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Mathematical%20Algorithms/Primality%20Test%20(Miller-Rabin))            | O(klog3n)              | O(logn)           |
| [**Prime Factorization**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Mathematical%20Algorithms/Prime%20Factorization)                      | O(√n)              | O(1)             |
| [**Sieve of Eratosthenes**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Mathematical%20Algorithms/Sieve%20of%20Eratosthenes)                    | O(n log log n)     | O(n)             |

---

**Legend:** 
- *n* — input number or range limit (depending on the algorithm).
- *k* — number of moduli (for CRT).

**Notes:**  
- The "optional" algorithms are only needed for very advanced or competitive coding rounds.
- Your current list is sufficient for 99% of FAANG/MANGO interviews.

---

## [**🧬 Miscellaneous Must-Know**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Miscellaneous)

| **Algorithm**                                                                                                                                                                    | **Time Complexity**   | **Space Complexity** |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|:---------------------|
| [**Deque (Double-ended Queue)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Miscellaneous/Deque%20(Double-ended%20Queue))                                                                                                                                               | O(1) per op           | O(n)                 |
| [**Hashing (HashMap / HashSet usage)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Miscellaneous/Hashing%20(HashMap%20%26%20HashSet%20usage))                                                                                                                                        | O(1) avg / O(n) worst | O(n)                 |
| [**LFU Cache**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Miscellaneous/LFU%20Cache)                                                                                                                                                                  | O(1) per op           | O(n)                 |
| [**LRU Cache (with Doubly Linked List + HashMap)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Miscellaneous/LRU%20Cache%20(with%20Doubly%20Linked%20List%20%2B%20HashMap)) | O(1) per op           | O(n)                 |
| [**Monotonic Queue**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Miscellaneous/Monotonic%20Queue)                                                                           | O(n)                  | O(n)                 |
| [**Monotonic Stack**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Miscellaneous/Monotonic%20Stack)                                                                          | O(n)                  | O(n)                 |
| [**Ordered Map/Set(TreeMap/TreeSet)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Miscellaneous/Ordered%20Map-Set(TreeMap-TreeSet))                                       | O(log n) per op       | O(n)                 |
| [**Priority Queue (Heap)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Miscellaneous/Priority%20Queue%20(Heap))                                                            | O(log n) per op       | O(n)                 |
| [**Top K Elements (Heap + Map)**](https://github.com/jwm1rr0rb10/algorithms/tree/main/Miscellaneous/Top%20K%20Elements%20(Heap%20%2B%20Map))                                                                                                                                              | O(n log k)            | O(k)                 |               

---

**Legend:**  
- *n* — number of elements in the data structure.
- *k* — value for "Top K" queries.
- *α(n)* — inverse Ackermann function, nearly constant for all practical purposes.

**Notes:**  
- These data structures and patterns frequently appear as subroutines or optimizations in FAANG/MANGO interviews.
- Monotonic stacks/queues are essential for range queries, histogram, and sliding window max/min.
- Union Find is a must-know for graph connectivity and Kruskal’s MST.
- LRU/LFU Cache are classic design/implementation questions, requiring O(1) time for both get and put.
- Top K Elements are commonly asked in streaming and big data scenarios.
- Trie is key for prefix search, word dictionary, and autocomplete features.
- Ordered Map/Set (TreeMap/TreeSet) is useful for interval problems and order statistics.
- Deque is used for sliding window max/min and 0-1 BFS.

---

## [**🔄 Search Algorithms**]()

### [**Graph Search**]()

| Algorithm                                                                                                                                          | Time Complexity                     | Space Complexity |
|:---------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|:-----------------|
| [**A-star Search**]()                                                                                                                              | O(E) (depends on heuristic)         | O(V)             |
| [**Bellman-Ford Algorithm**]()                                                                                                                     | O(VE)                               | O(V)             |
| [**Bidirectional BFS**]()                                                                                                                          | O(2^(d/2))                          | O(V)             |
| [**Breadth-First Search (BFS)**]()                                                                                                                 | O(V + E)                           | O(V)             |
| [**Connected Components**]()                                                                                                                       |       O(V + E)     |        O(V + E)                | O(V)
| [**Cycle Detection**]()                                                                                                                            |         O(V + E)        |                  O(V)      |
| [**Depth-First Search (DFS)**]                                                                                                                     | O(V + E)                            | O(V) (O(h) for trees) |
| [**Dijkstra’s Algorithm**]()                                                                                                                       | O((V + E) log V)                    | O(V)             |
| [**Floyd-Warshall**]()                                                                                                                               |O(V³)|O(V²)|
| [**Kruskal**]()                                      | O(E log E)                          | O(V)             |
| [**Prim**]()                                             | O(E + V log V) (with min-heap)      | O(V)             |
| [**Tarjan**]()                                        | O(V + E)                            | O(V + E)         |
| [**Topological Sort**]()                   | O(V + E)                            | O(V)             |
| [**Union-Find (DSU)**]()                   | O(α(n)) per op (almost O(1)), O(n) init | O(n)        |

**Legend:**  
V — number of vertices (nodes)  
E — number of edges  
d — shortest path distance  
h — tree height  
α(n) — inverse Ackermann function, considered constant in practice

---

### [**Array/List Search**]()

| Algorithm                       | Time Complexity         | Space Complexity |
|:--------------------------------|:-----------------------|:-----------------|
| [**Binary Search (must-know)**]()        | O(log n)               | O(1)             |
| [**Exponential Search**]()               | O(log i)               | O(1)             |
| [**Jump Search**]()                      | O(√n)                  | O(1)             |
| [**Linear Search**]()                    | O(n)                   | O(1)             |
| [**Search in 2D Matrix**]()              | O(m + n) or O(log(mn)) | O(1)             |
| [**Search in Rotated Sorted Array**]()   | O(log n)               | O(1)             |
| [**Ternary Search (rare)**]()           | O(log₃ n)              | O(1)             |

**Legend:**  
h — height of tree (log n for balanced, up to n for skewed)
i — index of target.
n — number of elements in array.
m — pattern length (for string search)

---

### [**String Search**]()

| Algorithm              | Time Complexity              | Space Complexity |
|:------------------------|:-----------------------------|:------------------|
| [**Boyer-Moore**]()            | O(n + m)                    | O(m + k)         |
| [**KMP (Knuth-Morris-Pratt)**]()| O(n + m)                   | O(m)             |
| [**Manacher’s Algorithm**]()                |   O(n)          |        O(n)          |
| [**Naive Substring Search**]() | O((n-m+1)m)                 | O(1)             |
| [**Rabin-Karp**]()            | O(n + m) (avg) / O(nm) (worst) | O(1)          |
| [**Z-Algorithm**]()                |         O(n)      |        O(n)         |

**Legend:**  
n — number of elements in array  
m — pattern length (for string search)  
k — alphabet size (number of possible unique characters in the input, e.g. 26 for lowercase, 256 for ASCII)

---

### [**Tree Search**]()

| **Algorithm**                              | **Time Complexity** | **Space Complexity** |
|:-------------------------------------------|:--------------------|:---------------------|
| [**Binary Search Tree Search**]()        | O(h) (O(log n) for balanced)    | O(1)        |
| [**Deserialize Binary Tree**]() |          |             O(n)         | O(n)                      |
| [**Fenwick Tree (Binary Indexed Tree)**]() |    O(log n)                 |       O(n)               |
| [**Lowest Common Ancestor**]() |           |     O(n)                | O(n)                     |
| [**Segment Tree**]()                       |    O(log n)                 |       O(n)               |
| [**Serialize Binary Tree**]() |            |     O(n)                |       O(n)               |
| [**Traversals: In-order**]()               |     O(n)                |         O(n)             |
| [**Traversals: Post-order**]()             |             O(n)        |     O(h)                 |
| [**Traversals: Pre-order**]()              |       O(n)              |     O(h)                 |
| [**Trie(Prefix Tree)**]()                  |   O(L)                  |          O(N*L)            |

### Legend

- **n** — Number of nodes in the tree (or size of the input array for some data structures).
- **h** — Height of the tree (for a balanced binary tree, h = O(log n); for an unbalanced tree, h can be up to O(n)).
- **L** — Length of the word (used in Trie operations; refers to the length of the string being processed).
- **N** — Number of words stored in the Trie.
- **O(1)** — Constant time or space, i.e., does not depend on input size.

#### Additional notes:
- For traversal algorithms, space complexity can be O(h) if implemented recursively (due to call stack), or O(n) if all nodes are stored (e.g., in a result list).
- For balanced trees (like AVL or Red-Black trees, or balanced Segment/Fenwick Trees), time complexity is typically O(log n).
- For Trie, time complexity is proportional to the length of the word being inserted or searched (`O(L)`), and space complexity is proportional to the total number of stored characters (`O(N*L)`).

---
**Notation:**
- `O(...)` — Big O notation: describes the upper bound of time/space complexity in terms of input size.

---


## [**🔁 Sorting Algorithms**]()

| **Algorithm**      | **Time Complexity (Best / Avg / Worst)** | **Space Complexity** |
|:-------------------|:-----------------------------------------|:--------------------|
| [**Bubble Sort**]()    | O(n) / O(n²) / O(n²)                 | O(1)             |
| [**Bucket Sort**]()    | O(n + k) (avg), O(n²) (worst)        | O(n + k)         |
| [**Counting Sort (for integers or limited range)**]()  | O(n + k)                             | O(k)             |
| [**Heap Sort**]()      | O(n log n) / O(n log n) / O(n log n) | O(1)             |
| [**Insertion Sort**]() | O(n) / O(n²) / O(n²)                 | O(1)             |
| [**Merge Sort**]()     | O(n log n) / O(n log n) / O(n log n) | O(n)             |
| [**Quick Sort**]()      | O(n log n) / O(n log n) / O(n²)      | O(log n)         |
| [**Radix Sort**]()     | O(nk)                                | O(n + k)         |
| [**Selection Sort**]() | O(n²) / O(n²) / O(n²)                | O(1)             |

---

**Legend:**  
- *n* — number of elements to be sorted  
- *k* — range of input values (for Counting, Radix, and Bucket sorts), or number of possible buckets  

**Notes:**  
- Counting Sort, Radix Sort, and Bucket Sort are non-comparison-based sorts, usually efficient when the range of input values (*k*) is not significantly larger than the number of elements (*n*).
- For more on each algorithm, see the dedicated folder links above.

---

## [**🧩 Two Pointers / Sliding Window**]()

| **Algorithm**                                                                                                                                                                             | **Time Complexity** | **Space Complexity** |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|:---------------------|
| [**Backspace String Compare**]()                                                                                                                                                          | O(n)                | O(1)                 |
| [**Container With Most Water**]()                                                                                                                                                         | O(n)                | O(1)                 |
| [**Find All Anagrams in a String**]()                                                                                                                                                     | O(n)                | O(1) or O(k)         |
| [**Four Sum**]()                                                                                                                                                                          | O(n² / n³)          | O(n)                 |
| [**Longest Repeating Character Replacement**]()                                                                                                                                           | O(n)                | O(1)                 |
| [**Longest Substring Without Repeating Characters**]()                                                                                                                                    | O(n)                | O(n)                 |
| [**Maximum Subarray (Kadane’s Algorithm)**]()                                                                                                                                             | O(n)                | O(1)                 |
| [**Minimum Size Subarray Sum**]()                                                                                                                                                         | O(n)                | O(1)                 |
| [**Minimum Window Substring**]()                                                                                                                                                          | O(n)                | O(n)                 |
| [**Move Zeroes**]()                                                                                                                                                                       | O(n)                | O(1)                 |
| [**Remove Duplicates from Sorted Array**]()                                                                                                                                               | O(n)                | O(1)                 |
| [**Sliding Window**]()                                                                                                                                                                      |O(n)|O(1)|
| [**Sort Colors (Dutch National Flag)**]()                | O(n)                | O(1)                 |
| [**Three Sum**]()                                                                      | O(n² / n³)          | O(n)                 |
| [**Trapping Rain Water**]()                                               | O(n)                | O(1)                 |
| [**Two Sum**]()                                                                         | O(n² / n³)          | O(n)                 |

---

**Legend:**  
- *n* — length of the input array or string.  
- *k* — number of distinct characters (for anagrams).

**Notes:**
- Mastering two pointers/sliding window is critical for interview success.
- These patterns efficiently solve many array and string problems in O(n) time.

---


