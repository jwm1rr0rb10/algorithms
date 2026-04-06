# Kruskal’s Algorithm

## What is it?

**Kruskal’s Algorithm** is a classic greedy algorithm to find the Minimum Spanning Tree (MST) of a weighted, undirected graph.

- The **Minimum Spanning Tree** is a subset of edges that connects all vertices with the minimal possible total edge weight and contains no cycles.

---

## How does it work?

1. **Sort all edges** in non-decreasing order by weight.
2. **Initialize the MST as empty.**
3. **Iterate through the sorted edges:**
   - For each edge, check if it connects two different components (i.e., adding it won’t form a cycle).
   - If yes, add the edge to the MST.
   - If adding the edge forms a cycle, skip it.
4. **Stop when the MST contains (V - 1) edges** (V = number of vertices).

**Cycle detection** is typically done with a Disjoint Set Union (DSU) or Union-Find data structure.

---

## Where is it used?

- Building networks (electricity, roads, computer networks) with minimal cost.
- Cluster analysis in data science.
- Network design and cost minimization problems.

---

## Key Features

- Works for undirected graphs (with or without negative weights).
- Simple, intuitive, and efficient.

---

## Complexity

| Complexity      | Value           |
|:---------------:|:--------------:|
| **Time**        | O(E log E)     |
| **Space**       | O(V)           |

- **E** — number of edges
- **V** — number of vertices

---

## Python Example

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        self.parent[yr] = xr
        return True

def kruskal(n, edges):
    """
    n: number of vertices (vertices are 0...n-1)
    edges: list of (weight, u, v)
    Returns: list of edges in the MST, total weight
    """
    edges.sort()
    dsu = DSU(n)
    mst = []
    total_weight = 0

    for w, u, v in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == n - 1:
                break

    return mst, total_weight

# Example usage
edges = [
    (1, 0, 1),
    (3, 0, 2),
    (2, 1, 2),
    (4, 1, 3),
    (5, 2, 3),
]
n = 4
mst, total = kruskal(n, edges)
print("Edges in MST:", mst)
print("Total weight:", total)
```

---

## Useful Links

- [Wikipedia: Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)
- [GeeksforGeeks: Kruskal’s Minimum Spanning Tree Algorithm](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/)
- [Visualgo: Kruskal’s Animation](https://visualgo.net/en/mst)

---

## LeetCode Practice

|    # | Title                            | Link                                                                         |
| :--- | :------------------------------- | :--------------------------------------------------------------------------- |
| 1135 | Connecting Cities With Minimum Cost | [LeetCode 1135](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) |
| 1584 | Min Cost to Connect All Points      | [LeetCode 1584](https://leetcode.com/problems/min-cost-to-connect-all-points/)      |
| 1489 | Find Critical and Pseudo-Critical Edges in MST | [LeetCode 1489](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) |