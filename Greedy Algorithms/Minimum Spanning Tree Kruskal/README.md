# 🌲 Minimum Spanning Tree — Kruskal's Algorithm

## 📌 What is Kruskal's Algorithm?

**Kruskal’s Algorithm** is a greedy algorithm used to find the **Minimum Spanning Tree (MST)** of a connected, undirected, weighted graph.  
It builds the MST by always choosing the edge with the smallest weight that doesn't form a cycle.

---

## 🎯 Why is it Important?

- Guarantees the minimum total edge weight  
- Works well on sparse graphs  
- Forms the basis for network design, clustering, and circuit layout

---

## ⚙️ How Does the Algorithm Work?

### Step 1: Sort all edges by weight (ascending)

### Step 2: Initialize Disjoint Set Union (DSU)
- Each node starts in its own set

### Step 3: Iterate through edges
- For each edge (u, v):
  - If u and v are in different sets → add edge to MST and union their sets
  - Else → skip (would form a cycle)

---

## 🧪 Python Example

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        self.parent[yr] = xr
        return True

def kruskal(n, edges):
    # edges: list of (weight, u, v)
    edges.sort()
    dsu = DSU(n)
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        if dsu.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

# Example usage
edges = [(1, 0, 1), (4, 0, 2), (3, 1, 2), (2, 1, 3), (5, 2, 3)]
mst, weight = kruskal(4, edges)
print("MST:", mst)
print("Total Weight:", weight)
```

---

## ⏱️ Complexity
- Time: O(E log E) — sorting edges + DSU operations
- Space: O(E) — for storing edges and DSU structure

---

## 🧭 Applications
- Network design (telecom, electrical grids)
- Clustering in machine learning
- Image segmentation
- Approximation algorithms (e.g., TSP)

---

## ✅ Summary
- Kruskal’s Algorithm builds the MST by greedily choosing the smallest edge
- Uses Disjoint Set Union to detect cycles efficiently
- Optimal for sparse graphs and easy to implement

---