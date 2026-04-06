package main

import "fmt"

// heapify restores the Max-Heap property for the subtree rooted at index i.
// n is the size of the heap.
func heapify(arr []int, n int, i int) {
	largest := i     // Initialize largest as root
	left := 2*i + 1  // Left child = 2*i + 1
	right := 2*i + 2 // Right child = 2*i + 2

	// If left child is larger than root
	if left < n && arr[left] > arr[largest] {
		largest = left
	}

	// If right child is larger than the current largest
	if right < n && arr[right] > arr[largest] {
		largest = right
	}

	// If largest is not the root
	if largest != i {
		arr[i], arr[largest] = arr[largest], arr[i] // Swap

		// Recursively heapify the affected subtree
		heapify(arr, n, largest)
	}
}

// heapsort is the main function that performs Heap Sort
func heapsort(arr []int) {
	n := len(arr)

	// Phase 1: Build a Max-Heap from the array.
	// Start from the last non-leaf node (n/2 - 1) and move up to the root (0).
	for i := n/2 - 1; i >= 0; i-- {
		heapify(arr, n, i)
	}

	// Phase 2: Extract elements from the heap one by one.
	// The last element is swapped with the root (maximum element).
	// Heap size is reduced, and heap property is restored for the new root.
	for i := n - 1; i > 0; i-- {
		// Move current root (largest element) to the end
		arr[0], arr[i] = arr[i], arr[0]

		// Call heapify on the reduced heap
		heapify(arr, i, 0)
	}
}

func main() {
	data := []int{10, 7, 8, 9, 1, 5}
	fmt.Println("Original array:", data)
	heapsort(data)
	fmt.Println("Sorted array:", data)

	data2 := []int{4, 2, 7, 1, 9, 3, 6, 8, 5}
	fmt.Println("Original array:", data2)
	heapsort(data2)
	fmt.Println("Sorted array:", data2)
}
