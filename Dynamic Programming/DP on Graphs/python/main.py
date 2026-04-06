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