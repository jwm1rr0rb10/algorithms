# Depth-First Search (DFS)
# Graph represented as a dictionary (adjacency list)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2],
    6: [7],  # Isolated component
    7: [6],
}

# Set to track visited vertices
visited = set()

def dfs(visited, graph, node):
    """
    Performs a depth-first search starting from node.
    visited - set of visited vertices.
    graph - dictionary representing the graph.
    node - current vertex.
    """
    # 1. Mark the current vertex as visited
    visited.add(node)
    print(f"Visited vertex: {node}")

    # 2. Iterate over all neighbors of the current vertex
    # Use .get(node, []) to handle cases where the vertex has no neighbors
    for neighbor in graph.get(node, []):
        # 3. If the neighbor has not been visited...
        if neighbor not in visited:
            # ...recursively call DFS from that neighbor
            dfs(visited, graph, neighbor)
    # 4. After visiting all neighbors and returning from recursive calls, we "backtrack"

# Example usage
print("Starting DFS from vertex 0:")
dfs(visited, graph, 0)

print("\nContinuing DFS for remaining unvisited components:")
# Check all vertices in the graph
for node in graph:
    if node not in visited:
        dfs(visited, graph, node)

# For graphs with vertices that have no edges (not present as dictionary keys),
# you either need to know the total number of vertices or have a separate list of them.
# In this example, all vertices that have edges are represented as keys.
