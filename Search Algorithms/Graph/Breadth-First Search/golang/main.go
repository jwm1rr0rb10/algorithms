package main

import "fmt"

// Graph represents a graph using an adjacency list.
type Graph map[int][]int

// BFS performs a breadth-first search starting from the startNode.
func BFS(graph Graph, startNode int) {
	// A map to keep track of visited nodes
	visited := make(map[int]bool)
	// A queue for nodes to visit
	queue := []int{} // Using a slice as a queue

	// 1. Start from the initial node: mark it as visited and enqueue it
	visited[startNode] = true
	queue = append(queue, startNode)

	// 2. While the queue is not empty...
	for len(queue) > 0 {
		// Dequeue a node from the front of the queue
		currentNode := queue[0]
		queue = queue[1:] // "Dequeue" the first element by slicing it out

		// Visit (process) the current node
		fmt.Printf("Visited node: %d\n", currentNode)

		// Get the neighbors of the current node
		neighbors, ok := graph[currentNode]
		if !ok {
			continue // This node has no neighbors
		}

		// For each neighbor...
		for _, neighbor := range neighbors {
			// ...if it hasn't been visited yet...
			if !visited[neighbor] {
				// ...mark it as visited and enqueue it
				visited[neighbor] = true
				queue = append(queue, neighbor)
			}
		}
	}
}

func main() {
	// Example graph (same as for DFS)
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

	// Note: BFS from a single start node will only visit one connected component.
	// To traverse the entire graph with multiple components, BFS should be called
	// for each unvisited node (similar to what is typically done in DFS main).
	// But for simplicity, we show BFS on just one component here.
}
