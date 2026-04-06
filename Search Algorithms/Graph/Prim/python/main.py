import heapq

def prim(graph, start=0):
    n = len(graph)
    visited = [False] * n
    min_edges = [(0, start)]  # (weight, vertex)
    total_weight = 0

    while min_edges:
        weight, u = heapq.heappop(min_edges)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_edges, (w, v))

    return total_weight

# Example graph: adjacency list (vertex indices, edge weights)
# Vertices: 0, 1, 2, 3
# Edges: (0-1, 1), (0-2, 4), (1-2, 2), (1-3, 6), (2-3, 3)
graph = [
    [(1,1), (2,4)],        # 0
    [(0,1), (2,2), (3,6)], # 1
    [(0,4), (1,2), (3,3)], # 2
    [(1,6), (2,3)]         # 3
]

print("Total weight of MST:", prim(graph))  # Output: 6