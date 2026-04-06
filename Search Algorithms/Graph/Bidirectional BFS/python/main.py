from collections import deque

def bidirectional_bfs(graph, start, goal):
    if start == goal:
        return [start]
    
    queue_start = deque([start])
    queue_goal = deque([goal])
    visited_start = {start: None}
    visited_goal = {goal: None}

    while queue_start and queue_goal:
        # Step from start side
        if queue_start:
            current = queue_start.popleft()
            for neighbor in graph.get(current, []):
                if neighbor not in visited_start:
                    visited_start[neighbor] = current
                    queue_start.append(neighbor)
                    if neighbor in visited_goal:
                        return reconstruct_path(visited_start, visited_goal, neighbor)
        # Step from goal side
        if queue_goal:
            current = queue_goal.popleft()
            for neighbor in graph.get(current, []):
                if neighbor not in visited_goal:
                    visited_goal[neighbor] = current
                    queue_goal.append(neighbor)
                    if neighbor in visited_start:
                        return reconstruct_path(visited_start, visited_goal, neighbor)
    return None  # No path

def reconstruct_path(visited_start, visited_goal, meeting_point):
    path = []
    node = meeting_point
    while node is not None:
        path.append(node)
        node = visited_start[node]
    path = path[::-1]
    node = visited_goal[meeting_point]
    while node is not None:
        path.append(node)
        node = visited_goal[node]
    return path

# Example usage
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

path = bidirectional_bfs(graph, 0, 5)
print("Path from 0 to 5:", path)