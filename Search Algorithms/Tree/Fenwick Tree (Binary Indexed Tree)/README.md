# Fenwick Tree (Binary Indexed Tree)

---

## Problem Description

**Fenwick Tree** (or Binary Indexed Tree, BIT) is a data structure that efficiently supports:
- Prefix sum queries (sum from start to position i)
- Element updates (adding or changing a value at a position)

Both operations are performed in O(log n) time.

Used for range sum queries, inversion counting, online query processing, and more.

---

## Approach (Algorithm)

The Fenwick Tree maintains an array of partial sums, allowing:
- Prefix sum queries [1, i] in O(log n)
- Point updates (add or change a single value) in O(log n)

It uses bit manipulation with the least significant bit (LSB) of indices.

---

## Python Example

```python
class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)  # 1-based indexing

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i  # move to parent

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i  # move to next ancestor
        return res

    def range_sum(self, l, r):
        return self.query(r) - self.query(l - 1)

# Example usage:
ft = FenwickTree(8)
for idx, val in enumerate([3,2,1,6,5,4,7,8], start=1):
    ft.update(idx, val)

print(ft.range_sum(3, 6))  # Sum from 3 to 6: 1+6+5+4 = 16
```

---

## How It Works

- Each tree node is responsible for the sum of a specific range in the original array.
- Bit manipulation of indices allows fast traversal and updates of relevant ranges.

---

## Applications

- Dynamic prefix/range sum queries (when range modifications are not required)
- Inversion counting
- Online query processing (prefix sums, point updates)
- Some order statistic problems (k-th element, number of smaller/larger elements, etc.)

---

## When to Use

- When you need fast prefix sum queries and single point updates
- When you do not need range modifications (use Segment Tree for that)

---

## When Not to Use

- If you need to modify/query arbitrary ranges (not just prefixes), or need range updates—Segment Tree is more suitable
- For small arrays, brute force is sufficient

---

## Complexity

- **Time:** O(log n) for update and query
- **Space:** O(n)

---

## Useful Links

- [Fenwick Tree — Wikipedia](https://en.wikipedia.org/wiki/Fenwick_tree)
- [LeetCode — Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)