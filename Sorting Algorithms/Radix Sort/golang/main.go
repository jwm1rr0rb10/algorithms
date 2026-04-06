package main

import (
	"fmt"
)

// getMax finds the maximum value in an array
func getMax(arr []int) int {
	max := arr[0]
	for _, value := range arr {
		if value > max {
			max = value
		}
	}
	return max
}

// countSortForRadix performs Counting Sort based on the exponent exp
// (exp = 1 for units, 10 for tens, 100 for hundreds, etc.)
// This function must be STABLE.
func countSortForRadix(arr []int, exp int) {
	n := len(arr)
	output := make([]int, n) // Output array
	count := make([]int, 10) // Count array for digits 0-9

	// Count occurrences of digits
	for i := 0; i < n; i++ {
		digit := (arr[i] / exp) % 10
		count[digit]++
	}

	// Compute positions (cumulative sum)
	for i := 1; i < 10; i++ {
		count[i] += count[i-1]
	}

	// Build the output array in reverse order (for stability)
	for i := n - 1; i >= 0; i-- {
		digit := (arr[i] / exp) % 10
		position := count[digit] - 1
		output[position] = arr[i]
		count[digit]--
	}

	// Copy the sorted elements back into the original array
	for i := 0; i < n; i++ {
		arr[i] = output[i]
	}
}

// radixSort - the main function for radix sort
func radixSort(arr []int) {
	n := len(arr)
	if n <= 1 {
		return // An array of 0 or 1 element is already sorted
	}

	// Find the maximum number to determine the number of digits
	m := getMax(arr)

	// Sort by each digit. exp is the current digit place (1, 10, 100, ...)
	for exp := 1; m/exp > 0; exp *= 10 {
		countSortForRadix(arr, exp)
	}
}

func main() {
	data := []int{170, 45, 75, 90, 802, 24, 2, 66}
	fmt.Println("Original array:", data)
	radixSort(data)
	fmt.Println("Sorted array:", data)

	data2 := []int{4, 2, 7, 1, 9, 3, 6, 8, 5}
	fmt.Println("Original array:", data2)
	radixSort(data2)
	fmt.Println("Sorted array:", data2)

	// Example with numbers of different lengths
	data3 := []int{123, 45, 6, 7890, 1, 555}
	fmt.Println("Original array:", data3)
	radixSort(data3)
	fmt.Println("Sorted array:", data3)
}
