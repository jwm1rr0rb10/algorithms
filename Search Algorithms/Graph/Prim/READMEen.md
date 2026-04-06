# Prim's Algorithm

Prim's algorithm is a greedy algorithm for finding a minimum spanning tree (MST) in a connected, weighted graph. A minimum spanning tree is a subset of the edges that connects all vertices with the minimum possible total edge weight and without cycles.

## Brief Description

1. Pick any vertex as the starting point.
2. Add the cheapest edge that connects the current tree to a new vertex (do not form a cycle).
3. Repeat step 2 until all vertices are included in the tree.

## Applications

- Laying cables between buildings at minimum cost.
- Building road networks.
- Network infrastructure, etc.

## Python Example

```python
import heapq

def prim(graph, start=0):
    n = len(graph)
    visited = [False] * n
    min_edges = [(0, start)]  # (weight, vertex)
    total_weight = 0

    while min_edges:
        weight, u = heapq.heappop(min_edges)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_edges, (w, v))

    return total_weight

# Example graph: adjacency list (vertex indices, edge weights)
# Vertices: 0, 1, 2, 3
# Edges: (0-1, 1), (0-2, 4), (1-2, 2), (1-3, 6), (2-3, 3)
graph = [
    [(1,1), (2,4)],        # 0
    [(0,1), (2,2), (3,6)], # 1
    [(0,4), (1,2), (3,3)], # 2
    [(1,6), (2,3)]         # 3
]

print("Total weight of MST:", prim(graph))  # Output: 6
```

## Visualization

```
   1
0-----1
|\   /|
| 4 2 6
|/     \
2-------3
    3
```
Minimum spanning tree: edges (0-1, 1), (1-2, 2), (2-3, 3). Total weight: 6.

## Complexity

- Time: O(E log V), where E is the number of edges, V is the number of vertices (with a heap).
- Space: O(V + E).

## Further Reading

- [Wikipedia: Prim's Algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm)
- [GeeksforGeeks: Prim’s Minimum Spanning Tree (MST) Algorithm](https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/)
- [YouTube: Prim’s Algorithm Visualized](https://www.youtube.com/watch?v=oP2-8ysT3QQ)

## Practice Problems

- [LeetCode 1135. Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)
- [LeetCode 1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)