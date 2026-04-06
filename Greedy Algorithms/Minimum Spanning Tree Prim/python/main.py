import heapq
from collections import defaultdict

def prim(n, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, vertex)
    total_weight = 0
    mst = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight

        for w, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                mst.append((u, v, w))

    return mst, total_weight

# Example usage
edges = [(0, 1, 1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (2, 3, 5)]
mst, weight = prim(4, edges)
print("MST:", mst)
print("Total Weight:", weight)