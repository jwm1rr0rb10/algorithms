# ⚡ Greedy Algorithms: Overview and Applications

Greedy algorithms make a series of locally optimal choices with the hope that these choices lead to a globally optimal solution.  
They are efficient, intuitive, and often surprisingly powerful — especially when the problem exhibits the **greedy-choice property** and **optimal substructure**.

---

## 📊 Algorithm Summary

| **Algorithm**                         | **Time Complexity**     | **Space Complexity** | **Best Use Cases**                                      |
|:-------------------------------------|:-------------------------|:---------------------|:---------------------------------------------------------|
| **Activity Selection**               | O(n)                     | O(1)                 | Scheduling non-overlapping tasks                        |
| **Fractional Knapsack**              | O(n log n)               | O(1)                 | Resource allocation with divisible items                |
| **Huffman Encoding**                 | O(n log n)               | O(n)                 | Data compression (lossless)                             |
| **Job Scheduling (with deadlines)**  | O(n log n)               | O(n)                 | Maximizing profit under time constraints                |
| **MST — Kruskal's Algorithm**        | O(E log E)               | O(E)                 | Sparse graphs, edge-centric MST construction            |
| **MST — Prim's Algorithm**           | O(E + V log V)           | O(V + E)             | Dense graphs, vertex-centric MST construction           |

---

## 🧠 When to Use Which Algorithm?

### ✅ Activity Selection
- **Use when**: You need to schedule the maximum number of non-overlapping intervals.
- **Strength**: Simple and fast.
- **Limitation**: Assumes all activities take equal time or are indivisible.

### ✅ Fractional Knapsack
- **Use when**: Items can be divided (e.g., partial resources, bandwidth).
- **Strength**: Greedy is optimal.
- **Limitation**: Doesn’t work for 0/1 Knapsack (indivisible items).

### ✅ Huffman Encoding
- **Use when**: You need optimal prefix codes for compression.
- **Strength**: Guarantees minimal total encoding length.
- **Limitation**: Requires frequency analysis and tree traversal.

### ✅ Job Scheduling with Deadlines
- **Use when**: Tasks have deadlines and profits.
- **Strength**: Maximizes total reward under time constraints.
- **Limitation**: Each task must take exactly 1 unit of time.

### ✅ Kruskal’s MST
- **Use when**: Graph is sparse or edges are already sorted.
- **Strength**: Simple with Disjoint Set Union (DSU).
- **Limitation**: Requires sorting all edges.

### ✅ Prim’s MST
- **Use when**: Graph is dense or represented as adjacency list.
- **Strength**: Efficient with priority queue.
- **Limitation**: Slightly more complex to implement.

---

## ⚔️ Kruskal vs. Prim: Quick Comparison

| Feature               | Kruskal                          | Prim                             |
|:----------------------|:---------------------------------|:---------------------------------|
| Grows by              | Edges                            | Vertices                         |
| Data structure        | Disjoint Set Union (DSU)         | Min-heap (priority queue)        |
| Best for              | Sparse graphs                    | Dense graphs                     |
| Edge sorting needed?  | ✅ Yes                            | ❌ No                             |
| Cycle detection       | Explicit via DSU                 | Implicit via visited set         |

---

## 🧭 Real-World Applications

- **Scheduling**: Activity Selection, Job Scheduling  
- **Compression**: Huffman Encoding (ZIP, JPEG, MP3)  
- **Resource Allocation**: Fractional Knapsack (bandwidth, logistics)  
- **Network Design**: Kruskal & Prim (telecom, electrical grids)  
- **Clustering & ML**: MST-based clustering, image segmentation

---

## ✅ Summary

Greedy algorithms are powerful tools when:
- The problem has **greedy-choice property** (local choice leads to global optimum)
- The solution has **optimal substructure** (can be built from optimal subproblems)

They are not always correct — but when they are, they’re often the most efficient solution available.

