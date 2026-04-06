# Union-Find (Disjoint Set Union, DSU)

**Union-Find** (also known as **Disjoint Set Union**, DSU) is a data structure that efficiently supports merging sets and checking whether elements are in the same set.

## Brief Description

- Supports two main operations:
    - **find(x):** Determine the set (find the “root”) that element x belongs to.
    - **union(x, y):** Merge the sets containing x and y.
- Uses optimizations:
    - **Path compression** — speeds up find.
    - **Union by rank/size** — speeds up union.
- Amortized time complexity per operation is almost O(1).

## Applications

- Minimum Spanning Tree construction (Kruskal’s algorithm).
- Finding connected components in a graph.
- Detecting cycles in undirected graphs.
- Networks, clusters, dynamic connectivity problems.

## Python Example

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # Already in the same set
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
        return True

# Example usage:
uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
print(uf.find(0) == uf.find(2))  # True
print(uf.find(0) == uf.find(3))  # False
```

## Visualization

```
Before union:
0  1  2  3  4

After union(0, 1):
0-1  2  3  4

After union(1, 2):
0-1-2  3  4
```

## Complexity

- **Time:** O(α(n)) — almost constant (where α is the inverse Ackermann function).
- **Space:** O(n)

## Further Reading

- [Wikipedia: Disjoint-set data structure](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)
- [GeeksforGeeks: Disjoint Set (Union-Find)](https://www.geeksforgeeks.org/disjoint-set-data-structures/)
- [YouTube: DSU in 10 Minutes](https://www.youtube.com/watch?v=0jNmHPfA_yE)

## Practice Problems

- [LeetCode 547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)
- [LeetCode 684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)
- [LeetCode 990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/)