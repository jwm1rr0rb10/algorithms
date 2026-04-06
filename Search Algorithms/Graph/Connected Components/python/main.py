def connected_components(graph):
    visited = set()
    components = []

    def dfs(node, comp):
        visited.add(node)
        comp.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, comp)

    for node in graph:
        if node not in visited:
            comp = set()
            dfs(node, comp)
            components.append(comp)
    return components

# Example:
graph = {
    0: [1, 2],
    1: [0],
    2: [0],
    3: [4],
    4: [3]
}
print(connected_components(graph))
# Output: [{0, 1, 2}, {3, 4}]