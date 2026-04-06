# Connected Components in an Undirected Graph

---

## Problem Description

Given an undirected graph, find all its connected components.  
A connected component is a group of nodes where each node is reachable from any other node in the same group.

---

## Approach

Use Depth-First Search (DFS) or Breadth-First Search (BFS):

1. For each unvisited node, start a DFS/BFS traversal.
2. Mark all reachable nodes as visited — they form one connected component.
3. Repeat for all nodes.

---

## Python Example

```python
def connected_components(graph):
    visited = set()
    components = []

    def dfs(node, comp):
        visited.add(node)
        comp.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, comp)

    for node in graph:
        if node not in visited:
            comp = set()
            dfs(node, comp)
            components.append(comp)
    return components

# Example:
graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4],
    4: [3]
}
print(connected_components(graph))
# Output: [{0, 1, 2}, {3, 4}]
```

---

## How It Works

- Each DFS/BFS traversal finds one “island” of reachable nodes.
- All nodes are marked as visited to avoid repeated work.

---

## Applications

- Finding isolated clusters in networks (social, road, communication)
- Preprocessing for graph algorithms
- Analyzing connectivity

---

## When to Use

- When you need to find all isolated “clusters” in a graph.

---

## When Not to Use

- For directed graphs: use Strongly Connected Components (SCC) instead.
- If you only need to check if the graph is connected.

---

## Complexity

- **Time:** O(V + E)
- **Space:** O(V)

---

## Useful Links

- [LeetCode — Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
- [Connected Component — Wikipedia](https://en.wikipedia.org/wiki/Connected_component_(graph_theory))