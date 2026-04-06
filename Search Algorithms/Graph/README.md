# Overview of Graph Search Algorithms

Graph search and pathfinding algorithms are fundamental in solving a variety of problems, such as traversing graphs, finding optimal or shortest paths, detecting cycles, identifying connected components, and building spanning trees. Each algorithm has its strengths and trade-offs.

---

## Hierarchy and Use Cases

### 1. Basic Traversal and Component Algorithms

- **[Depth-First Search (DFS)](./Depth-First%20Search/READMEen.md)**  
  Good for: connectivity, cycle detection, topological sorting, traversing trees and graphs.  
  Not ideal for: shortest path in unweighted graphs.
- **[Breadth-First Search (BFS)](./Breadth-First%20Search/READMEen.md)**  
  Good for: shortest path in unweighted graphs, minimal step problems.  
  Not ideal for: very wide graphs (high memory usage).
- **[Connected Components](./Connected%20Components/READMEen.md)**  
  Good for: finding all connected parts of a graph.
- **[Cycle Detection](./Cycle%20Detection/READMEen.md)**  
  Good for: detecting cycles in graphs or trees.

### 2. Advanced Search and Shortest Path

- **[Bidirectional BFS](./Bidirectional%20BFS/READMEen.md)**  
  Good for: efficient shortest path between two nodes in large graphs.
- **[A-star Search](./A%5C*%20Search/READMEen.md)**  
  Good for: optimal pathfinding with heuristics (maps, games).  
  Not ideal for: poor heuristics or large search spaces.
- **[Dijkstra’s Algorithm](./Dijkstra%E2%80%99s%20Algorithm/READMEen.md)**  
  Good for: shortest paths in graphs without negative edges.  
  Not ideal for: negative edges.
- **[Bellman-Ford Algorithm](./Bellman-Ford%20Algorithm/READMEen.md)**  
  Good for: graphs with negative edge weights, detecting negative cycles.
- **[Floyd-Warshall](./Floyd-Warshall/READMEen.md)**  
  Good for: all-pairs shortest paths in small/medium graphs.

### 3. Spanning Trees and Connectivity

- **[Kruskal](./Kruskal/READMEen.md)**  
  Good for: minimum spanning tree, sparse graphs.
- **[Prim](./Prim/READMEen.md)**  
  Good for: minimum spanning tree, works for dense and sparse graphs (with min-heap).

### 4. Specialized and Structural Algorithms

- **[Tarjan](./Tarjan/READMEen.md)**  
  Good for: strongly connected components, bridges, articulation points.
- **[Topological Sort](./Topological%20Sort/READMEen.md)**  
  Good for: ordering in DAGs, dependency resolution.
- **[Union-Find (DSU)](./Union-Find%20(DSU)/READMEen.md)**  
  Good for: dynamic connectivity, Kruskal's algorithm, connected components.

---

## Comparison Table

| Algorithm | Time Complexity | Space Complexity |
|:----------------------|:-------------------------|:---------------------|
| [A-star Search](./A%5C*%20Search/READMEen.md) | O(E) (depends on heuristic) | O(V) |
| [Bellman-Ford Algorithm](./Bellman-Ford%20Algorithm/READMEen.md) | O(VE) | O(V) |
| [Bidirectional BFS](./Bidirectional%20BFS/READMEen.md) | O(2^(d/2)) | O(V) |
| [Breadth-First Search (BFS)](./Breadth-First%20Search/READMEen.md) | O(V + E) | O(V) |
| [Connected Components](./Connected%20Components/READMEen.md) | O(V + E) | O(V + E) |
| [Cycle Detection](./Cycle%20Detection/READMEen.md) | O(V + E) | O(V) |
| [Depth-First Search (DFS)](./Depth-First%20Search/READMEen.md) | O(V + E) | O(V) (O(h) for trees) |
| [Dijkstra’s Algorithm](./Dijkstra%E2%80%99s%20Algorithm/READMEen.md) | O((V + E) log V) | O(V) |
| [Floyd-Warshall](./Floyd-Warshall/READMEen.md) | O(V³) | O(V²) |
| [Kruskal](./Kruskal/READMEen.md) | O(E log E) | O(V) |
| [Prim](./Prim/READMEen.md) | O(E + V log V) (with min-heap) | O(V) |
| [Tarjan](./Tarjan/READMEen.md) | O(V + E) | O(V + E) |
| [Topological Sort](./Topological%20Sort/READMEen.md) | O(V + E) | O(V) |
| [Union-Find (DSU)](./Union-Find%20(DSU)/READMEen.md) | O(α(n)) per op (almost O(1)), O(n) init | O(n) |

---

## When to Use Which?

- **Traversal & Components:** DFS, BFS, Connected Components, Cycle Detection, Tarjan, Union-Find
- **Shortest Paths:** BFS (unweighted), Dijkstra (no negatives), Bellman-Ford (negatives), Floyd-Warshall (all-pairs), A-star, Bidirectional BFS
- **Spanning Trees:** Kruskal, Prim (often with DSU)
- **Dependency Problems:** Topological Sort
- **Dynamic Connectivity:** Union-Find (DSU)

---

## Useful Links

- [Graph Theory on GeeksforGeeks](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)
- [Graph Algorithms (YouTube)](https://www.youtube.com/playlist?list=PLrCZzMib1e9pKjhoE1QJ49W0U3J7q9Ubp)
- [LeetCode Graph Tag](https://leetcode.com/tag/graph/)

---