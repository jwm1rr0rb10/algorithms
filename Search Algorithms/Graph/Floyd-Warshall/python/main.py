def floyd_warshall(graph):
    """
    graph: dict, adjacency list where graph[u][v] = weight of edge u->v
    Returns: matrix dist, where dist[i][j] is the shortest distance from i to j
    """
    nodes = list(graph.keys())
    n = len(nodes)
    index = {node: idx for idx, node in enumerate(nodes)}

    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    for u in nodes:
        for v in nodes:
            if u == v:
                dist[index[u]][index[v]] = 0
            elif v in graph[u]:
                dist[index[u]][index[v]] = graph[u][v]

    # Main Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist, nodes

# Example usage
graph = {
    'A': {'B': 3, 'C': 8, 'E': -4},
    'B': {'D': 1, 'E': 7},
    'C': {'B': 4},
    'D': {'A': 2, 'C': -5},
    'E': {'D': 6}
}

dist, nodes = floyd_warshall(graph)
print("Shortest distances between all pairs:")
for i, u in enumerate(nodes):
    for j, v in enumerate(nodes):
        print(f"{u} -> {v}: {dist[i][j]}")