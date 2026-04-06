# Cycle Detection in Graphs

---

## Problem Description

Given a graph (undirected or directed), determine whether it contains a cycle.

---

## Approach

### Undirected Graph

- Use DFS or BFS.
- Track the parent node to avoid trivial cycles.
- If a visited node is encountered that is not the parent, a cycle exists.

### Directed Graph

- Use DFS with a recursion stack (or topological sort).
- If a node is revisited while it is still on the recursion stack, a cycle exists.

---

## Python Examples

### Undirected Graph

```python
def has_cycle_undirected(graph):
    visited = set()
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False
```

### Directed Graph

```python
def has_cycle_directed(graph):
    visited = set()
    on_stack = set()
    def dfs(node):
        visited.add(node)
        on_stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in on_stack:
                return True
        on_stack.remove(node)
        return False
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False
```

---

## How It Works

- In undirected graphs, cycles are detected by finding a visited node that is not the parent.
- In directed graphs, cycles are detected by finding a node that is currently in the recursion stack.

---

## Applications

- Validating topological order
- Deadlock detection
- Dependency analysis in build systems and compilers
- State machine correctness

---

## When to Use

- When you need to check if a graph contains cycles (especially in dependency resolution, scheduling, etc).

---

## When Not to Use

- When the graph is guaranteed to be a tree (no cycles).
- If cycles are irrelevant to the problem.

---

## Complexity

- **Time:** O(V + E)
- **Space:** O(V)

---

## Useful Links

- [LeetCode — Course Schedule (cycle detection in directed graph)](https://leetcode.com/problems/course-schedule/)
- [Cycle Detection — Wikipedia](https://en.wikipedia.org/wiki/Cycle_detection)