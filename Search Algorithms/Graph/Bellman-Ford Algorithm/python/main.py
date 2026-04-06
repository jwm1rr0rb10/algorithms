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