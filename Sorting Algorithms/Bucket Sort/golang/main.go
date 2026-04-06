package main

import (
	"fmt"
	"sort" // Using the standard sort package for sorting buckets
)

// bucketSort sorts a list of floating-point numbers between 0.0 and 1.0
// numBuckets - number of buckets
func bucketSort(arr []float64, numBuckets int) {
	n := len(arr)
	if n == 0 || numBuckets <= 0 {
		return
	}

	// 1. Create buckets
	// Use a slice of slices to represent the buckets
	buckets := make([][]float64, numBuckets)
	// Initialize each bucket as an empty slice
	for i := range buckets {
		buckets[i] = []float64{}
	}

	// 2. Distribute elements into buckets
	for _, value := range arr {
		// Determine the bucket index. value * numBuckets gives a number in [0, numBuckets)
		// Integer truncation gives the index.
		// Ensure value = 1.0 goes into the last bucket (numBuckets - 1)
		bucketIndex := int(value * float64(numBuckets))
		if bucketIndex == numBuckets { // If value = 1.0, index would be numBuckets
			bucketIndex-- // Move it to the last bucket
		}
		if bucketIndex < 0 || bucketIndex >= numBuckets {
			// Handle values out of the [0.0, 1.0) range, if needed
			// This example assumes all values are within that range
			continue
		}
		buckets[bucketIndex] = append(buckets[bucketIndex], value)
	}

	// 3. Sort each bucket and 4. Merge the buckets
	// Merging happens while copying back into the original array
	k := 0 // Index for the original array
	for i := 0; i < numBuckets; i++ {
		// Sort the current bucket (you could use another algorithm like insertion sort)
		// For simplicity, we use Go’s standard sort
		sort.Float64s(buckets[i])

		// Copy the sorted elements from the bucket back to the original array
		for _, value := range buckets[i] {
			arr[k] = value
			k++
		}
	}
}

func main() {
	data := []float64{0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68}
	fmt.Println("Original array (Bucket Sort):", data)
	bucketSort(data, 10) // 10 buckets
	fmt.Println("Sorted array (Bucket Sort):", data)

	data2 := []float64{0.5, 0.1, 0.9, 0.3, 0.7, 0.2, 0.8, 0.4, 0.6, 1.0}
	fmt.Println("Original array (Bucket Sort):", data2)
	bucketSort(data2, 10) // 10 buckets
	fmt.Println("Sorted array (Bucket Sort):", data2)
}
