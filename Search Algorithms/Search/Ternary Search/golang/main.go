package main

import "fmt"

// TernarySearch searches for target in a sorted slice data.
// Returns the index of target if found, otherwise -1.
// This is an example for searching an element, not for function optimization.
func TernarySearch(data []int, target int) int {
	low := 0              // Lower bound
	high := len(data) - 1 // Upper bound

	// While the search interval is valid
	for high >= low {
		// Calculate two points dividing the interval into approximately three parts
		mid1 := low + (high-low)/3
		mid2 := high - (high-low)/3

		// Check if target is equal to elements at mid1 or mid2
		if data[mid1] == target {
			return mid1 // Element found
		}
		if data[mid2] == target {
			return mid2 // Element found
		}

		// Determine which of the three parts the target might be in
		if target < data[mid1] {
			// Target is in the left third [low, mid1 - 1]
			high = mid1 - 1
		} else if target > data[mid2] {
			// Target is in the right third [mid2 + 1, high]
			low = mid2 + 1
		} else {
			// Target is in the middle third [mid1 + 1, mid2 - 1]
			low = mid1 + 1
			high = mid2 - 1
		}
	}

	// Element not found
	return -1
}

func main() {
	sortedData := []int{2, 5, 8, 12, 16, 23, 38, 56, 72, 91}
	target1 := 38
	target2 := 10

	// Search for target1
	index1 := TernarySearch(sortedData, target1)
	if index1 != -1 {
		fmt.Printf("Element %d found at index %d\n", target1, index1)
	} else {
		fmt.Printf("Element %d not found\n", target1)
	}

	// Search for target2
	index2 := TernarySearch(sortedData, target2)
	if index2 != -1 {
		fmt.Printf("Element %d found at index %d\n", target2, index2)
	} else {
		fmt.Printf("Element %d not found\n", target2)
	}
}
