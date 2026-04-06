# Breadth-First Search (BFS)

## What it is

**Breadth-First Search (BFS)** is a fundamental algorithm for traversing or searching tree or graph data structures. BFS explores all vertices at the current "level" (all immediate neighbors of the starting vertex), before moving on to nodes at the next level.

---

## How it works

Imagine throwing a stone into a pond: BFS spreads out like ripples, exploring all nodes at distance 1 from the start, then all at distance 2, and so on.

**Algorithm steps:**
1. Start from the chosen starting vertex.
2. Add the starting vertex to a queue and mark it as visited.
3. While the queue is not empty:
    - Remove a vertex from the front of the queue. Process (visit) it.
    - For each unvisited neighbor:
        - Mark it as visited.
        - Add it to the end of the queue.

BFS is naturally implemented using a queue data structure (FIFO — First In, First Out).

---

## Complexity

| Complexity      | Value                   |
|:---------------:|:----------------------:|
| **Time**        | O(V + E)               |
| **Space**       | O(V) (worst case)      |

- **V** — number of vertices
- **E** — number of edges  
- Each vertex and edge is processed at most once.

---

## Applications

- **Finding the shortest path in an unweighted graph:** BFS guarantees the shortest path (in terms of number of edges) from the starting node to all reachable nodes.
- **Level-order traversal of a tree**
- **Finding all nodes within a certain distance**
- **Web crawlers**
- **Connected component finding**
- **Minimum spanning tree construction (Prim's algorithm base idea, though Prim uses a priority queue)**

---

## Go Example

```go
package main

import "fmt"

// Graph represents a graph using an adjacency list.
type Graph map[int][]int

func BFS(graph Graph, startNode int) {
	visited := make(map[int]bool)
	queue := []int{startNode}
	visited[startNode] = true

	for len(queue) > 0 {
		currentNode := queue[0]
		queue = queue[1:]

		fmt.Printf("Visited node: %d\n", currentNode)

		for _, neighbor := range graph[currentNode] {
			if !visited[neighbor] {
				visited[neighbor] = true
				queue = append(queue, neighbor)
			}
		}
	}
}

func main() {
	graph := Graph{
		0: {1, 2},
		1: {0, 3, 4},
		2: {0, 5},
		3: {1},
		4: {1},
		5: {2},
		6: {7},
		7: {6},
	}

	fmt.Println("Starting BFS from node 0:")
	BFS(graph, 0)
}
```

---

## Python Example

```python
from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2],
    6: [7],
    7: [6],
}

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        current = queue.popleft()
        print(f"Visited node: {current}")

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("Starting BFS from node 0:")
bfs(graph, 0)
```

---

## Explanation

- Both examples use an adjacency list to represent the graph.
- BFS uses a queue (slice in Go, deque in Python) and a visited set/map to avoid revisiting nodes.
- Each node is processed in the order it is discovered, guaranteeing level-order traversal.
- In Python, `collections.deque` is preferred for O(1) pops from the left.

---

## Useful Links

- [Wikipedia: Breadth-First Search](https://en.wikipedia.org/wiki/Breadth-first_search)
- [GeeksforGeeks: Breadth-First Search](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
- [Visualgo: BFS Animation](https://visualgo.net/en/dfsbfs)
- [LeetCode Explore: Graph BFS](https://leetcode.com/explore/learn/card/graph/619/breadth-first-search-in-graph/)

---

## LeetCode BFS Practice Problems

### Easy

|    # | Title                                              | Link                                                                               |
| :--- | :------------------------------------------------- | :--------------------------------------------------------------------------------- |
|  542 | 01 Matrix                                         | [LeetCode 542](https://leetcode.com/problems/01-matrix/)                           |
|  733 | Flood Fill                                        | [LeetCode 733](https://leetcode.com/problems/flood-fill/)                          |
|  994 | Rotting Oranges                                   | [LeetCode 994](https://leetcode.com/problems/rotting-oranges/)                     |

### Medium

|    # | Title                                              | Link                                                                               |
| :--- | :------------------------------------------------- | :--------------------------------------------------------------------------------- |
|  200 | Number of Islands                                 | [LeetCode 200](https://leetcode.com/problems/number-of-islands/)                   |
|  130 | Surrounded Regions                                | [LeetCode 130](https://leetcode.com/problems/surrounded-regions/)                  |
|  752 | Open the Lock                                     | [LeetCode 752](https://leetcode.com/problems/open-the-lock/)                       |
|  785 | Is Graph Bipartite?                               | [LeetCode 785](https://leetcode.com/problems/is-graph-bipartite/)                  |
|  994 | Rotting Oranges                                   | [LeetCode 994](https://leetcode.com/problems/rotting-oranges/)                     |

### Hard

|    # | Title                                              | Link                                                                               |
| :--- | :------------------------------------------------- | :--------------------------------------------------------------------------------- |
|  847 | Shortest Path Visiting All Nodes                   | [LeetCode 847](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)    |
|  1192| Critical Connections in a Network                  | [LeetCode 1192](https://leetcode.com/problems/critical-connections-in-a-network/)  |

---

**Tip:**  
BFS is not suitable for weighted graphs (with different edge weights). For shortest paths in weighted graphs, use [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).
