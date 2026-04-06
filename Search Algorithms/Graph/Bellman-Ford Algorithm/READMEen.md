# Bellman-Ford Algorithm

The **Bellman-Ford algorithm** is a classic algorithm for finding the shortest paths from a single source vertex to all other vertices in a weighted directed graph.  
Unlike Dijkstra’s algorithm, it works correctly even when some edge weights are negative, and it can detect negative weight cycles in the graph.

---

## When to Use

- The graph may have negative edge weights.
- You need to detect negative weight cycles.
- You want a simple and reliable algorithm for sparse graphs.

---

## How the Algorithm Works

1. **Initialization:**  
   Set the distance from the source to itself as 0, and to all other vertices as infinity.

2. **Relaxation:**  
   Repeat V-1 times (where V is the number of vertices):  
   For every edge (u, v, w), if `distance[u] + w < distance[v]`, update `distance[v] = distance[u] + w`.

3. **Negative Cycle Check:**  
   Go through all edges one more time.  
   If any edge can still be relaxed, there is a negative weight cycle in the graph.

---

## Complexity

| Time Complexity | Space Complexity |
|:---------------:|:----------------:|
| O(VE)           | O(V)             |

- **V** — number of vertices  
- **E** — number of edges

---

## Python Example

```python
def bellman_ford(V, edges, source):
    """
    V: number of vertices (indexed from 0 to V-1)
    edges: list of (u, v, w) tuples for edges u -> v with weight w
    source: starting vertex
    Returns: (distances list, negative_cycle_found: bool)
    """
    INF = float('inf')
    dist = [INF] * V
    dist[source] = 0

    # Relax edges V-1 times
    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative weight cycles
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return dist, True  # Negative cycle found

    return dist, False

# Example usage
V = 5
edges = [
    (0, 1, 6),
    (0, 2, 7),
    (1, 2, 8),
    (1, 3, 5),
    (1, 4, -4),
    (2, 3, -3),
    (2, 4, 9),
    (3, 1, -2),
    (4, 3, 7),
    (4, 0, 2)
]
source = 0
distances, has_negative_cycle = bellman_ford(V, edges, source)
print("Distances:", distances)
print("Has negative cycle?", has_negative_cycle)
```

---

## Typical Applications

- Shortest path search with negative weights
- Finding negative cycles (arbitrage, debt cycles, etc.)
- Routing in networks (RIP protocol)
- Currency exchange/arbitrage detection

---

## Related Problems

| Title                                    | Difficulty | Link                                                          |
|-------------------------------------------|------------|---------------------------------------------------------------|
| Cheapest Flights Within K Stops           | Medium     | [LeetCode 787](https://leetcode.com/problems/cheapest-flights-within-k-stops/) |
| Negative Weight Cycle (GFG)               | Medium     | [GFG](https://practice.geeksforgeeks.org/problems/negative-weight-cycle3504/1) |

---

## References

- [Wikipedia: Bellman–Ford algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)
- [GeeksforGeeks: Bellman-Ford](https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/)
