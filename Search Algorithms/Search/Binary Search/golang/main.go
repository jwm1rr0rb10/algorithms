package main

import "fmt"

// BinarySearch searches for target in a sorted slice data.
// Returns the index of target if found, otherwise -1.
func BinarySearch(data []int, target int) int {
	low := 0              // Lower bound of the current search segment
	high := len(data) - 1 // Upper bound of the current search segment

	// While the lower bound has not exceeded the upper bound
	for low <= high {
		// Find the index of the middle element
		mid := low + (high-low)/2 // Avoids potential overflow for very large low/high values

		// Compare the middle element with the target value
		if data[mid] == target {
			return mid // Element found, return its index
		} else if data[mid] < target {
			// If the middle element is less than target, the target can only be to the right of mid
			low = mid + 1 // Shift the lower bound to the right
		} else { // data[mid] > target
			// If the middle element is greater than target, the target can only be to the left of mid
			high = mid - 1 // Shift the upper bound to the left
		}
	}

	// If the loop ends, the element was not found
	return -1
}

func main() {
	sortedData := []int{2, 5, 8, 12, 16, 23, 38, 56, 72, 91}
	target1 := 23
	target2 := 10

	// Search for target1
	index1 := BinarySearch(sortedData, target1)
	if index1 != -1 {
		fmt.Printf("Element %d found at index %d\n", target1, index1)
	} else {
		fmt.Printf("Element %d not found\n", target1)
	}

	// Search for target2
	index2 := BinarySearch(sortedData, target2)
	if index2 != -1 {
		fmt.Printf("Element %d found at index %d\n", target2, index2)
	} else {
		fmt.Printf("Element %d not found\n", target2)
	}
}
