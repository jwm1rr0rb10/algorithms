# Bidirectional Breadth-First Search (Bidirectional BFS)

## What is it?

**Bidirectional BFS** is an efficient algorithm for finding the shortest path between two nodes in an unweighted graph.  
Unlike regular BFS, which searches from the start node towards the goal, bidirectional BFS runs two simultaneous BFS searches: one from the start node and one from the goal node.  
The search ends when the two search frontiers meet.

---

## When to use

- When both the start and goal nodes are known.
- When the graph is very large and a full BFS is too expensive.
- Useful in navigation, social networks, games, and anywhere shortest path between two points is needed.

---

## Complexity

| Complexity      | Value                            |
|:---------------:|:--------------------------------:|
| **Time**        | O(b^{d/2})                       |
| **Space**       | O(b^{d/2})                       |

- **b** — average branching factor (number of neighbors per node)
- **d** — length of the shortest path

---

## How it works

- Start BFS from both the start and goal nodes.
- Alternate expanding the search from each side.
- When the two searches meet, reconstruct the path.

---

## Python Example

```python
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
```

---

## Where Bidirectional BFS is Used in Real Products

1. **Finding the shortest path between two points on a map (navigation, games)**

    **Example:**  
    In navigation apps (like Google Maps or Yandex.Maps), you need to find the shortest route from point A to point B.  
    If the map is huge (like a whole city), normal BFS from A will scan a massive number of streets, but bidirectional BFS searches from both A and B at the same time — this almost halves the work.  
    **In games:** In strategy games with large maps, when a unit needs to quickly get to a target location, bidirectional BFS finds the path efficiently.

2. **Social networks — finding the shortest connection chain between people (friend-of-a-friend)**

    **Example:**  
    On Facebook, you might want to know how two users are connected — through which “friends”.  
    Bidirectional BFS quickly finds the shortest acquaintance chain (e.g., the “six degrees of separation”).

3. **Network protocols and routing (finding optimal data transfer routes)**

    **Example:**  
    In large computer networks (like data centers), you need to find the shortest path between two servers for data transfer.  
    Bidirectional BFS saves resources when building such routes.

4. **Solving puzzles, mazes, Rubik's cube, etc.**

    **Example:**  
    If you have a start and a goal state (for example, positions in a puzzle), you can search from both ends — this significantly speeds up finding the solution.

5. **Searching in huge graphs where full traversal is impractical**

    **Example:**  
    In recommendation systems (“people you may know”, “movies similar to this one”) — finding the minimal number of transitions between two entities in a massive graph.

## Useful Links

- [Wikipedia: Bidirectional Search](https://en.wikipedia.org/wiki/Bidirectional_search)
- [GeeksforGeeks: Bidirectional Search](https://www.geeksforgeeks.org/bidirectional-search/)
- [LeetCode: Shortest Path in Binary Matrix (uses BFS)](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
