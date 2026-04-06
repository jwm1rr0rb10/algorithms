package main

import "fmt"

// Graph represents a graph as an adjacency list.
// map[int][]int: key - vertex, value - slice of adjacent vertices.
type Graph map[int][]int

// DFS performs a depth-first search starting from the given start vertex.
// visited is a map used to track visited vertices.
func DFS(graph Graph, startNode int, visited map[int]bool) {
	// 1. Visit the current vertex
	visited[startNode] = true
	fmt.Printf("Visited vertex: %d\n", startNode)

	// 2. Iterate through all neighbors of the current vertex
	neighbors, ok := graph[startNode]
	if !ok {
		// This vertex has no neighbors (it's isolated or a dead-end)
		return
	}

	// 3. For each neighbor...
	for _, neighbor := range neighbors {
		// ...if it hasn't been visited yet...
		if !visited[neighbor] {
			// ...recursively call DFS on this neighbor (go deeper)
			DFS(graph, neighbor, visited)
		}
	}
	// 4. After visiting all neighbors and returning from recursive calls, we "backtrack"
}

func main() {
	// Example graph (undirected)
	// Representing an undirected edge A-B means adding B to A’s list and A to B’s list.
	graph := Graph{
		0: {1, 2},
		1: {0, 3, 4},
		2: {0, 5},
		3: {1},
		4: {1},
		5: {2},
		6: {7}, // Isolated component
		7: {6},
	}

	// Map to track visited vertices. Initially, all are false (unvisited).
	visited := make(map[int]bool)

	fmt.Println("Starting DFS from vertex 0:")
	DFS(graph, 0, visited)

	fmt.Println("\nContinuing DFS for remaining unvisited components:")
	// Check for vertices that were not reachable from the starting point (e.g., vertex 6)
	for node := range graph {
		if !visited[node] {
			DFS(graph, node, visited)
		}
	}

	// We can also check for isolated vertices that are not keys in the adjacency list,
	// but for that, we would need to know the total number of vertices or have a full list.
	// In this example, all vertices with edges are included as keys.
}
