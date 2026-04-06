# Combinations — Recursive (Backtracking) Approach

## Problem Description

Given two integers **n** and **k**, return all possible combinations of k numbers chosen from the range 1 to n (inclusive), with no repetitions and order within a combination doesn't matter.

**Example:**  
Input: n = 4, k = 2  
Output:  
```
[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4]
]
```

---

## Algorithm Idea and Approach

- Build a partial combination (path).
- At each step, add the next number from the current start up to n.
- When the combination reaches length k, add it to the result.
- After recursion, remove the last element (backtracking) to try other options.

---

## Python Example

```python
def combine(n, k):
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(list(path))
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result

# Example usage:
print(combine(4, 2))
# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
```

---

## Complexity Analysis

- **Time:** O(C(n, k) * k), where C(n, k) is the binomial coefficient (number of combinations).
- **Space:** O(k) recursion depth + space for storing results.

---

## Real-Life Applications

- Generating variants for search, brute-force, or test cases.
- Optimization problems, dynamic programming.
- Mathematics and combinatorics (combinations without repetition).
- Team selection, data sampling, variant generation.

---

## Useful Links

- [Combinations — LeetCode](https://leetcode.com/problems/combinations/)
- [Combination — Wikipedia](https://en.wikipedia.org/wiki/Combination)
- [Backtracking Algorithms — GeeksforGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/)

---

## LeetCode Practice

| Difficulty | Problem        | Link                                                                |
|------------|---------------|---------------------------------------------------------------------|
| Medium     | Combinations  | [#77 Combinations](https://leetcode.com/problems/combinations/)      |
| Medium     | Combination Sum| [#39 Combination Sum](https://leetcode.com/problems/combination-sum/)|
| Medium     | Subsets       | [#78 Subsets](https://leetcode.com/problems/subsets/)                |
| Medium     | Permutations  | [#46 Permutations](https://leetcode.com/problems/permutations/)      |

---