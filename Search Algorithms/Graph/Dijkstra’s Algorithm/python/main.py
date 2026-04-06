import heapq

def dijkstra(graph, start):
    """
    graph: dict, adjacency list (node: list of (neighbor, weight))
    start: starting node
    Returns: (distances, predecessors)
    """
    # Initialize distances and predecessors
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[start] = 0

    # Priority queue: (distance, node)
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        # Skip if we've already found a better path
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

    return distances, predecessors

def reconstruct_path(predecessors, start, target):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = predecessors[node]
    path.reverse()
    if path[0] == start:
        return path
    else:
        return []  # No path found

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

distances, predecessors = dijkstra(graph, 'A')
print("Shortest distances:", distances)
print("Path from A to D:", reconstruct_path(predecessors, 'A', 'D'))