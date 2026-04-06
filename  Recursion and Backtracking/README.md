# Recursion and Backtracking Algorithms — Overview

Recursion and backtracking are fundamental techniques for solving search, enumeration, and constraint satisfaction problems where you need to try all possible options, build results step by step, and "backtrack" (undo choices) as needed. These approaches are widely used for combinatorial problems, optimization with constraints, and exhaustive search.

---

## Main Algorithms and Their Complexities

| Algorithm                                 | Time Complexity             | Space Complexity             |
|--------------------------------------------|-----------------------------|------------------------------|
| **Permutations**                          | O(n × n!)                   | O(n) (stack)                 |
| **N-Queens problem**                      | O(n!)                       | O(n²)                        |
| **Sudoku solver**                         | O(9^m) (m = empty cells)    | O(1)                         |
| **Subset sum**                            | O(2^n)                      | O(n) (stack)                 |
| **Word Search**                           | O(N × 4^L)                  | O(L) (stack)                 |
| **Combinations (n choose k)**             | O(C(n, k))                  | O(k) (stack)                 |
| **All Combinations (any length)**         | O(2^n)                      | O(n) (stack), O(2^n×n) (res) |
| **Partition problem**                     | O(2^n)                      | O(n) (stack)                 |
| **Palindrome Partitioning**               | O(2^n)                      | O(n) (stack)                 |
| **Letter Combinations of a Phone Number** | O(4^n) (n = digits)         | O(n) (stack)                 |
| **Restore IP Addresses**                  | O(1) (bounded, 4 parts)     | O(1) (stack)                 |
| **Generate Parentheses**                  | O(4^n / √n)                 | O(n) (stack)                 |

---

## Applications: Where Recursion & Backtracking Shine

### 1. **Generating All Variants**
- **Permutations, Combinations, Subsets, Generate Parentheses**
- Generating all possible configurations (tests, searches, passwords, combinations).

### 2. **Constraint Satisfaction/Placement**
- **N-Queens, Sudoku, Word Search, Partition problem, Palindrome Partitioning**
- Finding solutions under strict constraints (placement, splitting, rule-based search).

### 3. **Path Finding & Partitioning**
- **Word Search, Restore IP Addresses, Palindrome Partitioning**
- Finding all paths or ways to split data into valid pieces.

### 4. **Combinatorial Optimization**
- **Subset sum, Partition problem**
- Finding subsets with a certain sum or property.

---

## Where to Avoid (Or Use Cautiously)

- **Large Input Sizes:** Exponential complexity is only practical for small n (usually n ≤ 20–25).
- **If More Efficient Solutions Exist:** If a problem allows greedy, dynamic programming, or algorithmic solutions — use them!
- **When Only an Efficient Answer is Needed:** For simple lookup, numeric, or streaming tasks.

---

## Must-Have (Essential) Algorithms

- **Permutations:** For all orderings, arrangement tasks.
- **Combinations, All Combinations (Subsets):** For any selection/choice problems.
- **Generate Parentheses:** Classic for parsing and nested structures.
- **N-Queens:** Classic constrained backtracking on boards.

---

## Less Useful / Niche Cases

- **Sudoku solver:** Educational, not practical for large or real puzzles.
- **Restore IP Addresses:** Only for specific parsing tasks.
- **Palindrome Partitioning:** Rare in production, more for algorithm practice.

---

## Grouping by Problem Type

### **All Variants Generation**
- Permutations
- Combinations (Fixed k and Any Length)
- Subsets (All Combinations)
- Generate Parentheses
- Letter Combinations of a Phone Number

### **Constraint Satisfaction**
- N-Queens
- Sudoku solver
- Word Search
- Partition problem
- Palindrome Partitioning

### **Partitioning and Parsing**
- Restore IP Addresses
- Palindrome Partitioning

---

## Tips

- **Backtracking** is powerful, but use it when you really need to try all possibilities or the problem is inherently combinatorial.
- When possible, add **pruning**, **memoization**, or use **dynamic programming** for efficiency.
- For small n (10–15), don't hesitate to use backtracking for generation or search.

---

## References

- [Backtracking — GeeksforGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [LeetCode Explore: Recursion](https://leetcode.com/explore/learn/card/recursion-i/)
- [LeetCode Explore: Backtracking](https://leetcode.com/explore/learn/card/recursion-ii/)

---