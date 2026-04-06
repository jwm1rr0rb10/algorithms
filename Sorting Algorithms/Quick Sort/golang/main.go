package main

import "fmt"

// quicksort calls the recursive quicksortRecursive function
func quicksort(arr []int) {
	quicksortRecursive(arr, 0, len(arr)-1)
}

// quicksortRecursive sorts the subarray arr[low..high] using quick sort
func quicksortRecursive(arr []int, low, high int) {
	if low < high {
		// pi is the partitioning index, arr[pi] is now at its right place
		pi := partition(arr, low, high)

		// Recursively sort elements before partition and after partition
		quicksortRecursive(arr, low, pi-1)
		quicksortRecursive(arr, pi+1, high)
	}
}

// partition takes the last element as pivot,
// places the pivot element at its correct position in sorted array,
// and places all smaller (smaller than pivot) elements before it
// and all greater elements after it.
func partition(arr []int, low, high int) int {
	pivot := arr[high] // Choose the last element as the pivot
	i := low - 1       // Index of smaller element

	for j := low; j < high; j++ {
		// If current element is smaller than or equal to pivot
		if arr[j] <= pivot {
			i++                             // Increment index of smaller element
			arr[i], arr[j] = arr[j], arr[i] // Swap arr[i] and arr[j]
		}
	}
	arr[i+1], arr[high] = arr[high], arr[i+1] // Swap the pivot element with the element at index i+1
	return i + 1                              // Return the partitioning index
}

func main() {
	data := []int{10, 7, 8, 9, 1, 5}
	fmt.Println("Original array:", data)
	quicksort(data)
	fmt.Println("Sorted array:", data)

	data2 := []int{4, 2, 7, 1, 9, 3, 6, 8, 5}
	fmt.Println("Original array:", data2)
	quicksort(data2)
	fmt.Println("Sorted array:", data2)
}
