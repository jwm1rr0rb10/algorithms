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