package main

import "fmt"

// mergesort - main function that calls the recursive sorting
func mergesort(arr []int) []int {
	if len(arr) <= 1 {
		return arr // Base case: an array with 0 or 1 element is already sorted
	}

	mid := len(arr) / 2           // Find the middle of the array
	left := mergesort(arr[:mid])  // Recursively sort the left half
	right := mergesort(arr[mid:]) // Recursively sort the right half

	return merge(left, right) // Merge the two sorted halves
}

// merge - function to merge two sorted arrays
func merge(left, right []int) []int {
	result := make([]int, 0, len(left)+len(right)) // Create the resulting array

	i, j := 0, 0 // Pointers for left and right arrays

	// While there are elements in both arrays, compare and add the smaller one
	for i < len(left) && j < len(right) {
		if left[i] <= right[j] {
			result = append(result, left[i])
			i++
		} else {
			result = append(result, right[j])
			j++
		}
	}

	// Add remaining elements from the left array (if any)
	for i < len(left) {
		result = append(result, left[i])
		i++
	}

	// Add remaining elements from the right array (if any)
	for j < len(right) {
		result = append(result, right[j])
		j++
	}

	return result // Return the merged sorted array
}

func main() {
	data := []int{10, 7, 8, 9, 1, 5}
	fmt.Println("Original array:", data)
	sortedData := mergesort(data)
	fmt.Println("Sorted array:", sortedData)

	data2 := []int{4, 2, 7, 1, 9, 3, 6, 8, 5}
	fmt.Println("Original array:", data2)
	sortedData2 := mergesort(data2)
	fmt.Println("Sorted array:", sortedData2)
}
