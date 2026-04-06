package main

import "fmt"

// selectionSort sorts an array using the Selection Sort algorithm
func selectionSort(arr []int) {
	n := len(arr)
	// Iterate through the array up to the second-to-last element
	for i := 0; i < n-1; i++ {
		// Assume the current element (arr[i]) is the smallest in the unsorted part
		minIndex := i

		// Find the index of the smallest element in the remaining unsorted part (from i+1 to end)
		for j := i + 1; j < n; j++ {
			if arr[j] < arr[minIndex] {
				minIndex = j // Found a new minimum
			}
		}

		// If the smallest element is not already at the current position i,
		// swap them. The current element (arr[i]) is placed in its correct position.
		if minIndex != i {
			arr[i], arr[minIndex] = arr[minIndex], arr[i]
		}
	}
}

func main() {
	data := []int{10, 7, 8, 9, 1, 5}
	fmt.Println("Original array:", data)
	selectionSort(data)
	fmt.Println("Sorted array:", data)

	data2 := []int{4, 2, 7, 1, 9, 3, 6, 8, 5}
	fmt.Println("Original array:", data2)
	selectionSort(data2)
	fmt.Println("Sorted array:", data2)
}
