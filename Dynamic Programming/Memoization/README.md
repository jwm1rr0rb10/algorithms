# Memoization Algorithm

## What is Memoization?

**Memoization** is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again. It is especially useful in recursive algorithms that solve overlapping subproblems, such as in dynamic programming.

---

## How Memoization Works

1. **Check Cache:** Before computing a result, check if it’s already stored (cached).
2. **Compute If Needed:** If not cached, compute the result and store it.
3. **Return Result:** Always return the cached result for repeated inputs.

---

## Example: Fibonacci Numbers (Python)

Without memoization (inefficient):

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

With memoization (efficient):

```python
def fib(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

---

## When to Use Memoization

- When your algorithm solves the same subproblems multiple times (overlapping subproblems).
- In recursive solutions to problems like Fibonacci, knapsack, edit distance, etc.

---

## Benefits

- **Performance boost:** Reduces exponential time algorithms to polynomial time.
- **Simple to implement:** Often just a few extra lines of code.

---

## Drawbacks

- **Memory usage:** Stores all computed results, which can use a lot of memory for large input spaces.

---

## Applications

- Dynamic programming problems (Fibonacci, knapsack, coin change, etc.)
- Caching results in web servers or APIs
- Optimizing recursive functions

---

## Resources

- [Wikipedia: Memoization](https://en.wikipedia.org/wiki/Memoization)
- [GeeksforGeeks: Memoization](https://www.geeksforgeeks.org/memoization-1d-2d-and-3d/)
- [LeetCode problems using memoization](https://leetcode.com/tag/dynamic-programming/)
