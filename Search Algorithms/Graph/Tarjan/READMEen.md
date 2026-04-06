# Tarjan's Algorithm

Tarjan's algorithm is an efficient method for finding strongly connected components (SCCs) in a directed graph. A strongly connected component is a maximal set of vertices where every vertex is reachable from every other vertex in the set.

## Brief Description

1. Uses depth-first search (DFS).
2. For each vertex, computes two values: discovery time (index) and the smallest reachable index (lowlink).
3. Maintains a stack to track the current component.
4. When a vertex becomes a "root" of an SCC (index == lowlink), a new component is formed.

## Applications

- Analyzing dependency graphs (e.g., in compilers).
- Detecting cyclic dependencies in software.
- Finding modules in social networks and other network structures.

## Python Example

```python
def tarjans_scc(graph):
    n = len(graph)
    index = 0
    stack = []
    indices = [None] * n
    lowlink = [None] * n
    on_stack = [False] * n
    result = []

    def strongconnect(v):
        nonlocal index
        indices[v] = lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if indices[w] is None:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if indices[v] == lowlink[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            result.append(scc)

    for v in range(n):
        if indices[v] is None:
            strongconnect(v)

    return result

# Example graph (adjacency list)
# Vertices: 0, 1, 2, 3, 4
# Edges: 0->1, 1->2, 2->0, 1->3, 3->4
graph = [
    [1],    # 0
    [2,3],  # 1
    [0],    # 2
    [4],    # 3
    []      # 4
]

print("Strongly connected components:", tarjans_scc(graph))
# Output: [[4], [3], [0, 2, 1]]
```

## Visualization

```
0 → 1 → 2
↑    ↓
└─── 3 → 4
```
SCCs: [0,1,2], [3], [4]

## Complexity

- Time: O(V + E), where V is the number of vertices, E is the number of edges.
- Space: O(V)

## Further Reading

- [Wikipedia: Tarjan's Strongly Connected Components Algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm)
- [GeeksforGeeks: Tarjan’s Algorithm to Find Strongly Connected Components](https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/)
- [YouTube: Tarjan’s Algorithm Visualized](https://www.youtube.com/watch?v=wUgWX0nc4NY)

## Practice Problems

- [LeetCode 1192. Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/)
- [LeetCode 323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)