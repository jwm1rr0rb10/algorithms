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