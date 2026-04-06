package main

import "fmt"

// bubbleSort sorts an array using the bubble sort algorithm
func bubbleSort(arr []int) {
	n := len(arr)
	// Outer loop iterates through all elements
	for i := 0; i < n-1; i++ {
		swapped := false // Optimization flag: if no swaps occur, the array is already sorted

		// Inner loop compares adjacent elements
		// (n-i-1) because the last i elements are already in place
		for j := 0; j < n-i-1; j++ {
			// If the current element is greater than the next, swap them
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = true // Mark that a swap occurred
			}
		}

		// If no swaps occurred in this pass, the array is sorted
		if !swapped {
			break
		}
	}
}

func main() {
	data := []int{10, 7, 8, 9, 1, 5}
	fmt.Println("Original array:", data)
	bubbleSort(data)
	fmt.Println("Sorted array:", data)

	data2 := []int{1, 2, 3, 4, 5} // Already sorted
	fmt.Println("Original array:", data2)
	bubbleSort(data2)
	fmt.Println("Sorted array:", data2)
}
