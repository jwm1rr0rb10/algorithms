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