# Dijkstra’s Algorithm

## What is it?

**Dijkstra’s Algorithm** is a classic algorithm for finding the shortest paths from a single source vertex to all other vertices in a graph with non-negative edge weights. It’s widely used in routing, navigation, and many other applications.

---

## How does it work?

1. **Initialization:**  
   - Set the distance to the source node as 0, and to all other nodes as infinity.
   - Mark all nodes as unvisited.  
   - Use a priority queue (min-heap) to always select the node with the smallest tentative distance.

2. **Main Loop:**  
   - While there are unvisited nodes:
     - Select the unvisited node with the smallest distance.
     - For each neighbor of this node:
       - If the path through the current node is shorter, update the neighbor’s distance.
     - Mark the node as visited.

3. **Finish:**  
   - When all nodes are visited, you have the shortest distances from the source to all nodes.
   - Optionally, you can reconstruct the shortest path to any target node by storing predecessors.

---

## Key Features

- **Does not work** with negative edge weights.
- Efficient with a priority queue (min-heap).
- Finds both the shortest distance and the actual path.

---

## Complexity

| Complexity      | Value                      |
|:---------------:|:-------------------------:|
| **Time**        | O((V + E) log V)          |
| **Space**       | O(V)                      |

- **V** — number of vertices
- **E** — number of edges

---

## Applications

- GPS navigation systems and map routing (e.g., Google Maps, Waze).
- Network routing protocols (OSPF, IS-IS).
- Games: AI pathfinding on maps and grids.
- Logistics and supply chain optimization.
- Urban planning (shortest paths in road networks).

---

## Python Example

```python
import heapq

def dijkstra(graph, start):
    """
    graph: dict, adjacency list (node: list of (neighbor, weight))
    start: starting node
    Returns: (distances, predecessors)
    """
    # Initialize distances and predecessors
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[start] = 0

    # Priority queue: (distance, node)
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        # Skip if we've already found a better path
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

    return distances, predecessors

def reconstruct_path(predecessors, start, target):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = predecessors[node]
    path.reverse()
    if path[0] == start:
        return path
    else:
        return []  # No path found

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

distances, predecessors = dijkstra(graph, 'A')
print("Shortest distances:", distances)
print("Path from A to D:", reconstruct_path(predecessors, 'A', 'D'))
```

---

## Useful Links

- [Wikipedia: Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [GeeksforGeeks: Dijkstra’s Shortest Path Algorithm](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
- [Visualgo: Dijkstra Animation](https://visualgo.net/en/sssp)
- [Brilliant.org: Dijkstra’s Algorithm](https://brilliant.org/wiki/dijkstras-short-path-finder/)

---

## LeetCode Practice

|    # | Title                                   | Link                                                                             |
| :--- | :-------------------------------------- | :------------------------------------------------------------------------------- |
|  743 | Network Delay Time                      | [LeetCode 743](https://leetcode.com/problems/network-delay-time/)                |
| 1631 | Path With Minimum Effort                | [LeetCode 1631](https://leetcode.com/problems/path-with-minimum-effort/)         |
| 1514 | Path with Maximum Probability           | [LeetCode 1514](https://leetcode.com/problems/path-with-maximum-probability/)    |
| 787  | Cheapest Flights Within K Stops         | [LeetCode 787](https://leetcode.com/problems/cheapest-flights-within-k-stops/)   |
| 882  | Reachable Nodes In Subdivided Graph     | [LeetCode 882](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/) |
| 399  | Evaluate Division (variation, uses BFS) | [LeetCode 399](https://leetcode.com/problems/evaluate-division/)                 |