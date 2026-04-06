# Counting Sort

**Counting Sort** is the first algorithm in our list that is not based on comparisons. This means it doesn't sort elements by comparing elements pairwise like Quick Sort, Merge Sort, Heap Sort, Bubble Sort, Insertion Sort, and Selection Sort.

---

## Basic Idea

Counting Sort works by counting the number of occurrences of each unique element in the input array. Then, using this information, it calculates the exact positions of each element in the output sorted array.

---

## Limitations

Counting Sort works efficiently only under the following conditions:

- The elements to be sorted must be integers (or data that can be mapped to integers, such as characters).
- The range of the elements (min and max values) must be known and not too large. If the range is very large, a lot of memory will be required for the auxiliary counting array.

---

## Steps of the Algorithm

Suppose we want to sort the array `arr` in ascending order, and all its elements lie in the range from `min_val` to `max_val`:

1. **Find the range:** Determine the maximum (and possibly minimum) value in `arr`.
2. **Create the counting array:** Create an auxiliary array `count` of size `max_val - min_val + 1`, initialized to zeros.
3. **Count the occurrences:** Iterate over `arr` and increment the counter for each value in `count`.
4. **Calculate positions (cumulative sum):** Modify `count` such that `count[i]` contains the number of elements ≤ the value corresponding to index `i`. This provides the final position for each value.
5. **Create the output array:** Allocate an output array of the same size as `arr`.
6. **Fill the output array:** Iterate through `arr` in reverse for stability, placing each value at its calculated position and decrementing its counter.
7. **Copy the result:** Copy `output` back to `arr` if in-place sorting is needed.

---

## Example

**Input:** `[4, 2, 2, 8, 3, 3, 1]`  
**Value range:** 1 to 8

1. **Find range:** `max_val = 8`
2. **Counting array (`count`):** `[0, 1, 2, 2, 1, 0, 0, 0, 1]` (indexes 0-8)
3. **Positions (cumulative sum):** `[0, 1, 3, 5, 6, 6, 6, 6, 7]`
4. **Filling output:**  
   - Place each element in its correct position (see full step-by-step in the description above)
5. **Result:** `[1, 2, 2, 3, 3, 4, 8]`

---

## ✅ Go Implementation

```go
package main

import (
	"fmt"
)

// countingSort sorts an array of non-negative integers
func countingSort(arr []int) []int {
	n := len(arr)
	if n == 0 {
		return arr
	}

	// 1. Find the maximum value
	maxVal := arr[0]
	for _, value := range arr {
		if value > maxVal {
			maxVal = value
		}
	}

	// 2. Create the counting array
	count := make([]int, maxVal+1)

	// 3. Count occurrences
	for _, value := range arr {
		count[value]++
	}

	// 4. Compute cumulative sum (positions)
	for i := 1; i <= maxVal; i++ {
		count[i] += count[i-1]
	}

	// 5. Create the output array
	output := make([]int, n)

	// 6. Fill the output array in reverse order (for stability)
	for i := n - 1; i >= 0; i-- {
		value := arr[i]
		pos := count[value] - 1
		output[pos] = value
		count[value]--
	}

	return output
}

// countingSortFullRange handles negative numbers
func countingSortFullRange(arr []int) []int {
	n := len(arr)
	if n == 0 {
		return arr
	}

	minVal, maxVal := arr[0], arr[0]
	for _, value := range arr {
		if value < minVal {
			minVal = value
		}
		if value > maxVal {
			maxVal = value
		}
	}
	valueRange := maxVal - minVal + 1
	offset := -minVal

	count := make([]int, valueRange)
	for _, value := range arr {
		count[value+offset]++
	}
	for i := 1; i < valueRange; i++ {
		count[i] += count[i-1]
	}
	output := make([]int, n)
	for i := n - 1; i >= 0; i-- {
		value := arr[i]
		pos := count[value+offset] - 1
		output[pos] = value
		count[value+offset]--
	}
	return output
}

func main() {
	data := []int{4, 2, 2, 8, 3, 3, 1}
	fmt.Println("Original array:", data)
	sortedData := countingSort(data)
	fmt.Println("Sorted array:", sortedData)

	data2 := []int{-5, -10, 0, 8, 10, 4, 5, -10, 0}
	fmt.Println("Original array:", data2)
	sortedData2 := countingSortFullRange(data2)
	fmt.Println("Sorted array:", sortedData2)
}
```

---

## ✅ Python Implementation

### For Non-Negative Integers

```python
def counting_sort_non_negative(arr):
    n = len(arr)
    if n == 0:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)
    for value in arr:
        count[value] += 1
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]
    output = [0] * n
    for i in range(n - 1, -1, -1):
        value = arr[i]
        pos = count[value] - 1
        output[pos] = value
        count[value] -= 1
    return output

# Example usage:
data_counting_nn = [4, 2, 2, 8, 3, 3, 1, 0, 5, 7]
print("Original list (Counting Sort Non-Negative):", data_counting_nn)
sorted_data_counting_nn = counting_sort_non_negative(data_counting_nn)
print("Sorted list (Counting Sort Non-Negative):", sorted_data_counting_nn)
```

### For Full Range (Including Negatives)

```python
def counting_sort_full_range(arr):
    n = len(arr)
    if n == 0:
        return arr
    min_val = min(arr)
    max_val = max(arr)
    value_range = max_val - min_val + 1
    offset = -min_val
    count = [0] * value_range
    for value in arr:
        count[value + offset] += 1
    for i in range(1, value_range):
        count[i] += count[i - 1]
    output = [0] * n
    for i in range(n - 1, -1, -1):
        value = arr[i]
        pos = count[value + offset] - 1
        output[pos] = value
        count[value + offset] -= 1
    return output

# Example usage:
data_counting_full = [-5, -10, 0, 8, 10, 4, 5, -10, 0, 3]
print("\nOriginal list (Counting Sort Full Range):", data_counting_full)
sorted_data_counting_full = counting_sort_full_range(data_counting_full)
print("Sorted list (Counting Sort Full Range):", sorted_data_counting_full)
```

---

## Complexity

- **Time Complexity:** O(n + k), where `n` is the number of elements and `k` is the range (`max_val - min_val + 1`).
- **Space Complexity:** O(n + k) for the output and counting arrays.

---

## Advantages

- Very fast for small integer ranges.
- Stable sorting (relative order of equal elements is preserved).

## Disadvantages

- Only works for integers (or data mapped to integers).
- Requires knowledge of the value range.
- Memory usage increases if the range is large.

---

> _Counting Sort is a great example of how knowing extra information about your data (the value range) can enable much faster sorting than comparison-based algorithms!_

---