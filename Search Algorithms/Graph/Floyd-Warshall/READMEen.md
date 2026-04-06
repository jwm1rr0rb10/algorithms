# Floyd-Warshall Algorithm

## What is it?

**Floyd-Warshall** is an algorithm for finding shortest paths between all pairs of vertices in a weighted graph (can handle negative edge weights, but not negative cycles).  
It’s commonly used when you need the shortest distance between every pair of nodes.

---

## How does it work?

1. **Initialization:**  
   - Create a distance matrix `dist[i][j]` where each entry is the current shortest known distance from node `i` to node `j`.
   - If there is a direct edge from `i` to `j`, set `dist[i][j] = weight`, else set to infinity (`float('inf')`), and `dist[i][i] = 0`.

2. **Core idea:**  
   - For each possible intermediate node `k`, update all pairs `(i, j)`:
     - `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`
   - If going from `i` to `j` via `k` is shorter, update the distance.

3. **Repeat for all nodes as intermediate (`k`).**  
   - At the end, `dist[i][j]` will be the length of the shortest path from `i` to `j`.

---

## Key Features

- Finds shortest distances between **all pairs of nodes**.
- Handles negative edge weights (but not negative cycles).
- Simple nested loops, easy to implement.

---

## Complexity

| Complexity      | Value     |
|:---------------:|:---------:|
| **Time**        | O(V³)     |
| **Space**       | O(V²)     |

- **V** — number of vertices

---

## Applications

- All-pairs shortest paths in transportation networks, maps, and logistics.
- Network analysis (delays, reachability).
- Computing transitive closure and reachability in graphs.
- Detecting negative cycles (if `dist[i][i] < 0` after algorithm runs).

---

## Python Example

```python
def floyd_warshall(graph):
    """
    graph: dict, adjacency list where graph[u][v] = weight of edge u->v
    Returns: matrix dist, where dist[i][j] is the shortest distance from i to j
    """
    nodes = list(graph.keys())
    n = len(nodes)
    index = {node: idx for idx, node in enumerate(nodes)}

    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    for u in nodes:
        for v in nodes:
            if u == v:
                dist[index[u]][index[v]] = 0
            elif v in graph[u]:
                dist[index[u]][index[v]] = graph[u][v]

    # Main Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist, nodes

# Example usage
graph = {
    'A': {'B': 3, 'C': 8, 'E': -4},
    'B': {'D': 1, 'E': 7},
    'C': {'B': 4},
    'D': {'A': 2, 'C': -5},
    'E': {'D': 6}
}

dist, nodes = floyd_warshall(graph)
print("Shortest distances between all pairs:")
for i, u in enumerate(nodes):
    for j, v in enumerate(nodes):
        print(f"{u} -> {v}: {dist[i][j]}")
```

---

## Useful Links

- [Wikipedia: Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)
- [GeeksforGeeks: Floyd Warshall Algorithm](https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/)
- [Visualgo: Floyd-Warshall](https://visualgo.net/en/sssp)

---

## LeetCode Practice

|    # | Title                                         | Link                                                                                 |
| :--- | :-------------------------------------------- | :----------------------------------------------------------------------------------- |
| 1334 | Find the City With the Smallest Number of Neighbors at a Threshold Distance | [LeetCode 1334](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) |
| 2642 | Design Graph With Shortest Path Calculator    | [LeetCode 2642](https://leetcode.com/problems/design-graph-with-shortest-path-calculator/) |
| 1462 | Course Schedule IV                            | [LeetCode 1462](https://leetcode.com/problems/course-schedule-iv/)                    |
| 2045 | Second Minimum Time to Reach Destination      | [LeetCode 2045](https://leetcode.com/problems/second-minimum-time-to-reach-destination/) |