# Depth-First Search (DFS)

## What it is

Depth-First Search (DFS) is an algorithm used to traverse or search through data structures like trees and graphs. It explores each branch as far as possible before backtracking to explore another branch.

---

## How it works

Imagine walking through a maze. DFS is like taking one path and following it as far as it goes until you hit a dead end or a previously visited location. Then, you backtrack to the last decision point and try a different unexplored path.

---

## More formally

1. Start at a chosen node.
2. Visit the node and mark it as visited (to avoid cycles or revisiting).
3. Choose one of its unvisited neighbors.
4. Recursively or using a stack, apply DFS to that neighbor.
5. If the current node has no unvisited neighbors, backtrack (end the recursive call or pop from the stack) to the previous node and continue from there.
6. Repeat until all reachable nodes are visited or the target node is found (in case of a search).

---

## Implementation

DFS can be implemented using:

* **Recursion:** The function call stack simulates the depth-first behavior.
* **Explicit stack:** Use a stack data structure manually. Push the start node onto the stack. While the stack is not empty, pop a node, if not visited – visit it and push all its unvisited neighbors onto the stack.

---

## Complexity

* **Time Complexity:** $O(V + E)$, where V is the number of vertices and E is the number of edges. Each node and edge is visited at most once.
	* For trees, where $E = V - 1$, this simplifies to O(V).

* **Space Complexity:** $O(V)$ in the worst case — especially if the graph is deep and narrow (like a linked list), as the recursion or stack can hold up to V nodes.

---

## Where is DFS used in practice?

1. **Finding a path between two nodes in a maze or a network.**
    - In games (pathfinding for AI agents).
    - Navigation in file systems (e.g., recursive search for files).

2. **Detecting cycles in a graph.**
    - In dependency graphs (like package managers or build systems).

3. **Topological sorting.**
    - Scheduling tasks with dependencies.

4. **Finding strongly connected components in directed graphs.**
    - Analysis of social networks, web structure, or compiler optimization.

5. **Finding bridges and articulation points in networks.**
    - Network reliability analysis.

6. **Solving puzzles and backtracking problems.**
    - Sudoku, N-Queens, maze generation and solving.

---

## Example in Go (Recursive DFS on a Graph)

Let's represent a graph using an adjacency list, where each key is a vertex and the corresponding value is a list of its neighboring vertices.

```go
package main

import "fmt"

type Graph map[int][]int

func DFS(graph Graph, startNode int, visited map[int]bool) {
	visited[startNode] = true
	fmt.Printf("Visited vertex: %d\n", startNode)

	neighbors, ok := graph[startNode]
	if !ok {
		return
	}

	for _, neighbor := range neighbors {
		if !visited[neighbor] {
			DFS(graph, neighbor, visited)
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

	visited := make(map[int]bool)
	fmt.Println("Starting DFS from vertex 0:")
	DFS(graph, 0, visited)

	fmt.Println("\nContinuing DFS for remaining unvisited components:")
	for node := range graph {
		if !visited[node] {
			DFS(graph, node, visited)
		}
	}
}
```

---

## Example in Python

```python
# Depth-First Search (DFS)
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

visited = set()

def dfs(visited, graph, node):
    visited.add(node)
    print(f"Visited vertex: {node}")
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(visited, graph, neighbor)

print("Starting DFS from vertex 0:")
dfs(visited, graph, 0)

print("\nContinuing DFS for remaining unvisited components:")
for node in graph:
    if node not in visited:
        dfs(visited, graph, node)
```

---

## 🟢 Easy

|    # | Title                                              | Acceptance |
|:-----|:---------------------------------------------------|:-----------|
|  104 | Maximum Depth of Binary Tree                       |      77.0% |
|  111 | Minimum Depth of Binary Tree                       |      50.4% |
|  704 | Binary Search                                      |      59.4% |
|  278 | First Bad Version                                  |      45.8% |
|  559 | Maximum Depth of N-ary Tree                        |      72.8% |
| 1614 | Maximum Nesting Depth of the Parentheses           |      84.3% |
|   35 | Search Insert Position                             |      48.7% |
|  897 | Increasing Order Search Tree                       |      78.6% |
| 2351 | First Letter to Appear Twice                       |      74.1% |
| 2879 | Display the First Three Rows                       |      93.1% |
|  387 | First Unique Character in a String                 |      63.5% |
|  270 | Closest Binary Search Tree Value                   |      49.9% |
|  700 | Search in a Binary Search Tree                     |      81.5% |
| 2108 | Find First Palindromic String in the Array         |      83.9% |
|  501 | Find Mode in Binary Search Tree                    |      57.4% |
|  108 | Convert Sorted Array to Binary Search Tree         |      73.9% |
|   28 | Find the Index of the First Occurrence in a String |      44.8% |
| 1179 | Reformat Department Table                          |      76.7% |
| 1350 | Students With Invalid Departments                  |      89.9% |
| 1789 | Primary Department for Each Employee               |      71.2% |
|  603 | Consecutive Available Seats                        |      65.4% |
| 2037 | Minimum Number of Moves to Seat Everyone           |      87.3% |

## 🟡 Medium

|    # | Title                                                   | Acceptance |
| :--- | :------------------------------------------------------ | :--------- |
|   79 | Word Search                                             |      45.0% |
| 1429 | First Unique Number                                     |      55.2% |
| 1902 | Depth of BST Given Insertion Order                      |      42.3% |
| 1268 | Search Suggestions System                               |      65.0% |
| 1111 | Maximum Nesting Depth of Two Valid Parentheses Strings  |      71.3% |
|   74 | Search a 2D Matrix                                      |      52.1% |
|   96 | Unique Binary Search Trees                              |      62.3% |
|   98 | Validate Binary Search Tree                             |      34.2% |
|   99 | Recover Binary Search Tree                              |      55.9% |
|  173 | Binary Search Tree Iterator                             |      74.6% |
| 2661 | First Completely Painted Row or Column                  |      64.0% |
|   33 | Search in Rotated Sorted Array                          |      42.6% |
|   95 | Unique Binary Search Trees II                           |      60.2% |
|  240 | Search a 2D Matrix II                                   |      54.9% |
|  669 | Trim a Binary Search Tree                               |      66.4% |
| 1382 | Balance a Binary Search Tree                            |      84.6% |
| 1586 | Binary Search Tree Iterator II                          |      63.2% |
|  701 | Insert into a Binary Search Tree                        |      73.5% |
| 1038 | Binary Search Tree to Greater Sum Tree                  |      88.2% |
|  109 | Convert Sorted List to Binary Search Tree               |      64.2% |
|  211 | Design Add and Search Words Data Structure              |      46.9% |
|  255 | Verify Preorder Sequence in BST                         |      50.8% |
| 1008 | Construct BST from Preorder Traversal                   |      83.1% |
| 1305 | All Elements in Two BSTs                                |      80.0% |
|  235 | Lowest Common Ancestor of a BST                         |      68.0% |
|  702 | Search in a Sorted Array of Unknown Size                |      72.7% |
| 2476 | Closest Nodes Queries in a BST                          |      42.4% |
|   34 | Find First and Last Position of Element in Sorted Array |      46.6% |
| 1997 | First Day Where You Have Been in All the Rooms          |      39.6% |
| 2314 | First Day of the Max Recorded Degree in Each City       |      73.1% |
|  426 | Convert BST to Sorted Doubly Linked List                |      65.4% |
| 3175 | First Player to Win K Games in a Row                    |      39.3% |
| 1966 | Binary Searchable Numbers in Unsorted Array             |      62.4% |
|  184 | Department Highest Salary                               |      54.4% |
| 2988 | Manager of the Largest Department                       |      81.1% |
|  580 | Count Student Number in Departments                     |      59.7% |
|  626 | Exchange Seats                                          |      72.5% |
| 1386 | Cinema Seat Allocation                                  |      42.7% |
| 1845 | Seat Reservation Manager                                |      66.3% |
| 1227 | Airplane Seat Assignment Probability                    |      66.6% |
| 3140 | Consecutive Available Seats II                          |      57.1% |

## 🔴 Hard

|    # | Title                                      | Acceptance |
| :--- | :----------------------------------------- | :--------- |
|   41 | First Missing Positive                     |      40.9% |
|  212 | Word Search II                             |      37.2% |
| 3374 | First Letter Capitalization II             |      76.4% |
|  642 | Design Search Autocomplete System          |      49.3% |
|  745 | Prefix and Suffix Search                   |      40.4% |
|  272 | Closest BST Value II                       |      60.2% |
| 1972 | First and Last Call On the Same Day        |      51.0% |
| 3303 | Occurrence of First Almost Equal Substring |      13.6% |
|  185 | Department Top Three Salaries              |      57.4% |
|  615 | Avg Salary: Departments VS Company         |      56.7% |
| 1203 | Sort Items by Groups w/ Dependencies       |      65.6% |
| 2258 | Escape the Spreading Fire                  |      36.1% |