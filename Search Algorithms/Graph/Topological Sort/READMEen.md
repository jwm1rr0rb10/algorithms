# Topological Sort

**Topological sort** is the linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge `u → v`, vertex `u` comes before vertex `v` in the ordering. This sort is fundamental for resolving dependencies among tasks, modules, or processes.

## Brief Description

- Works only for directed acyclic graphs (DAG).
- Finds a valid order to perform tasks given dependencies.
- If the graph contains a cycle, topological sort is impossible.

## Applications

- Build systems (project compilation).
- Resolving module/package dependencies.
- Task scheduling and course planning.
- Compilers and static code analysis.

## Python Example (Kahn’s Algorithm — using in-degrees)

```python
from collections import deque

def topological_sort(graph):
    n = len(graph)
    in_degree = [0] * n
    for u in range(n):
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([u for u in range(n) if in_degree[u] == 0])
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(order) != n:
        raise ValueError("Graph contains a cycle, topological sort not possible.")
    return order

# Example graph:
# 0 -> 2
# 1 -> 2
# 2 -> 3
# 3 -> 4
graph = [
    [2],    # 0
    [2],    # 1
    [3],    # 2
    [4],    # 3
    []      # 4
]

print("Topological order:", topological_sort(graph))
# Output: [0, 1, 2, 3, 4] or [1, 0, 2, 3, 4]
```

## Visualization

```
0   1
 \ /
  2
  |
  3
  |
  4
```

## Complexity

- **Time:** O(V + E), where V is the number of vertices, E is the number of edges.
- **Space:** O(V + E)

## Further Reading

- [Wikipedia: Topological Sorting](https://en.wikipedia.org/wiki/Topological_sorting)
- [GeeksforGeeks: Topological Sorting](https://www.geeksforgeeks.org/topological-sorting/)
- [YouTube: Topological Sort Visualization](https://www.youtube.com/watch?v=Q9PIxaNGnig)

## Practice Problems

- [LeetCode 207. Course Schedule](https://leetcode.com/problems/course-schedule/)
- [LeetCode 210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
- [LeetCode 269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)