# Segment Tree

---

## Problem Description

**Segment Tree** is a data structure that allows fast O(log n) queries (like sum, min, max) on arbitrary array intervals, as well as point or range updates.

Used for efficient range queries and range updates.

---

## Approach (Algorithm)

1. Build a tree where each node stores aggregate information about a segment of the array.
2. Efficiently answer range queries (e.g., sum on [l, r]) and update single elements or ranges.

---

## Python Example (Range Sum Query, Point Update)

```python
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)
        # Fill leaves
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        # Build the tree
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    # Query sum in [l, r)
    def query(self, l, r):
        res = 0
        l += self.size
        r += self.size
        while l < r:
            if l % 2:
                res += self.tree[l]
                l += 1
            if r % 2:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res

    # Update element at idx to value
    def update(self, idx, value):
        idx += self.size
        self.tree[idx] = value
        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

# Example usage:
arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)
print(st.query(1, 5))  # Sum from 1 to 4: 3+5+7+9 = 24
st.update(3, 10)       # arr[3] = 10
print(st.query(1, 5))  # 3+5+10+9 = 27
```

---

## How It Works

- Leaves are the array elements.
- Each internal node aggregates (e.g., sum) the values of two child segments.
- Query and update walk up/down the tree, only touching necessary nodes.

---

## Applications

- Range sum/min/max queries.
- Dynamic array problems with modifications.
- Order statistics, RMQ, range updates (with lazy propagation).

---

## When to Use

- When you need fast range queries and modifications.
- When Fenwick Tree is insufficient (e.g., for range updates or complex aggregate functions).

---

## When Not to Use

- For simple or small arrays (brute force is easier).
- For prefix sums only (use Fenwick Tree).

---

## Complexity

- **Time:** O(log n) for query and update
- **Space:** O(n)

---

## Useful Links

- [Segment Tree — Wikipedia](https://en.wikipedia.org/wiki/Segment_tree)
- [LeetCode — Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)