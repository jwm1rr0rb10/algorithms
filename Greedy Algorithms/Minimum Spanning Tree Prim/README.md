# 🌐 Minimum Spanning Tree — Prim's Algorithm

## 📌 What is Prim's Algorithm?

**Prim’s Algorithm** is a greedy algorithm used to find the **Minimum Spanning Tree (MST)** of a connected, undirected, weighted graph.  
Unlike Kruskal, which grows the MST by edges, Prim grows it by expanding from a starting vertex and always adding the minimum-weight edge that connects to a new vertex.

---

## 🎯 Why is it Important?

- Efficient for dense graphs  
- Avoids sorting all edges  
- Used in network design, routing, and clustering

---

## ⚙️ How Does the Algorithm Work?

### Step 1: Initialize
- Start from any vertex
- Use a priority queue (min-heap) to track the minimum-weight edge to each unvisited vertex

### Step 2: Expand the MST
- At each step, pick the edge with the smallest weight that connects to an unvisited vertex
- Add that vertex to the MST
- Update the priority queue with new edges from the added vertex

---

## 🧪 Python Example (Using Heap)

```python
import heapq
from collections import defaultdict

def prim(n, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, vertex)
    total_weight = 0
    mst = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight

        for w, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                mst.append((u, v, w))

    return mst, total_weight

# Example usage
edges = [(0, 1, 1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (2, 3, 5)]
mst, weight = prim(4, edges)
print("MST:", mst)
print("Total Weight:", weight)
```

---

## ⏱️ Complexity
- Time: O(E + V log V) — with a binary heap
- Space: O(V + E) — for graph and heap

---

## 🧭 Applications
- Network routing and design
- Clustering in machine learning
- Image segmentation
- Circuit layout

---

## ✅ Summary
- Prim’s Algorithm grows the MST from a starting vertex
- Uses a priority queue to always pick the lightest edge
- More efficient than Kruskal on dense graphs

---