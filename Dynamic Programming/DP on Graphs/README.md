# DP on Graphs: Explanation and Example

## What is DP on Graphs?

Dynamic Programming on Graphs is a technique for solving optimization and counting problems on graphs (especially Directed Acyclic Graphs, or DAGs) by breaking them into smaller subproblems.  
It is often used to find the longest/shortest paths, count paths, or solve other recursive problems where each state depends on previous results.

---

## How does DP on Graphs work?

- **State:** Usually, `dp[v]` stores the answer for vertex `v` (e.g., the longest path ending at `v`).
- **Transition:** For each vertex `v`, update its value based on its predecessors (or neighbors), e.g.:  
  `dp[v] = max(dp[u] + weight(u, v))` for all `u` with an edge to `v`.
- **Order:** Vertices are processed in topological order so that dependencies are resolved before computing each state.

---

## Python Example (Longest Path in DAG)

```python
from collections import defaultdict, deque

def longest_path_dag(n, edges):
    # Build graph
    graph = defaultdict(list)
    indegree = [0] * n
    for u, v, w in edges:
        graph[u].append((v, w))
        indegree[v] += 1

    # Topological sort
    queue = deque([i for i in range(n) if indegree[i] == 0])
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor, _ in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # DP initialization
    dp = [float('-inf')] * n
    dp[0] = 0  # Suppose node 0 is the source

    for u in topo_order:
        for v, w in graph[u]:
            if dp[u] + w > dp[v]:
                dp[v] = dp[u] + w

    return dp

# Example usage
n = 5
edges = [
    (0, 1, 3),
    (0, 2, 2),
    (1, 2, 1),
    (1, 3, 4),
    (2, 3, 2),
    (3, 4, 1)
]
print(longest_path_dag(n, edges))  # Output: [0, 3, 3, 7, 8]
```

---

## Complexity

- **Time:** O(V + E), where V is the number of vertices, E is the number of edges
- **Space:** O(V + E)

---

## Where is it used?

- Scheduling tasks with dependencies (project management, build systems)
- Counting paths or finding optimal paths in DAGs
- Solving prerequisite problems (university courses, workflow processing)
- Some game state evaluations

---

## When to use DP on Graphs?

- The problem can be reduced to subproblems on a graph structure
- The graph is a DAG, or cycles are not involved (or can be handled)
- You want an efficient solution for counting or optimizing over paths or states

---

## Real-life example

Project management software (like Gantt charts or build tools) uses DP on DAGs to determine the earliest completion time of a sequence of dependent tasks.