# All Combinations (Any Length) / Subsets — Recursive (Backtracking) Approach

## Problem Description

Given an array of numbers (or a range from 1 to n), return **all possible combinations (subsets) of any size** — from the empty set to the full array.

**Example:**  
Input: [1, 2, 3]  
Output:  
```
[
  [],
  [1],
  [2],
  [3],
  [1,2],
  [1,3],
  [2,3],
  [1,2,3]
]
```

---

## Algorithm Idea and Approach

- This is the classic **power set** (all subsets) problem.
- For each element, you have two choices: include it in the current subset or not.
- Recursively and with backtracking: at each step, add the current set (path) to the result, then try to add the next element.

---

## Python Example

```python
def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(list(path))
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # backtracking

    backtrack(0, [])
    return result

# Example usage:
print(subsets([1, 2, 3]))
# [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```

---

## How It Works

1. Start with an empty set (path) and position start = 0.
2. Add the current path to the result (even if it's empty).
3. For each i from start to the end:
    - Add nums[i] to path.
    - Recursively search for subsets from the next index.
    - After recursion, remove the last element (backtracking).

---

## Complexity

- **Time:** O(2^n * n), where n is the array length (there are 2^n subsets, each can have up to n elements).
- **Space:** O(2^n * n) for storing all subsets.

---

## Real-Life Applications

- Exploring all feature/setting/combination variants.
- Optimization and dynamic programming over subsets.
- Generating test data, bitmask algorithms, set analysis.

---

## Useful Links

- [Subsets — LeetCode](https://leetcode.com/problems/subsets/)
- [Power set — Wikipedia](https://en.wikipedia.org/wiki/Power_set)
- [Backtracking Algorithms — GeeksforGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/)

---

## LeetCode Practice

| Difficulty | Problem       | Link                                                                 |
|------------|--------------|----------------------------------------------------------------------|
| Medium     | Subsets       | [#78 Subsets](https://leetcode.com/problems/subsets/)                |
| Medium     | Subsets II    | [#90 Subsets II](https://leetcode.com/problems/subsets-ii/)          |
| Medium     | Permutations  | [#46 Permutations](https://leetcode.com/problems/permutations/)      |
| Medium     | Combinations  | [#77 Combinations](https://leetcode.com/problems/combinations/)      |

---