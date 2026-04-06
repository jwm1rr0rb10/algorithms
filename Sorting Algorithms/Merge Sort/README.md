# Merge Sort

**Merge Sort** is a classic sorting algorithm based on the "divide and conquer" principle, similar to Quick Sort but with different logic. It was developed by John von Neumann.

---

## Key Idea

- **Divide:** Recursively split the array into two halves until each subarray contains only one element (a single-element array is considered sorted).
- **Conquer:** Sort the subarrays (this happens implicitly, as recursion continues down to single elements).
- **Combine/Merge:** Gradually merge the sorted subarrays back into larger sorted arrays until the entire original array is merged.

The central operation is merging two already sorted subarrays into one sorted array.

---

## The "Merge" Step

Suppose we have two sorted subarrays:
- Left: `[1, 5, 8]`
- Right: `[2, 7, 10]`

To merge them into one sorted array:

1. Create an empty result array (or use a temporary auxiliary array).
2. Use two pointers (indices), one for each subarray, starting at their beginnings.
3. Compare the elements pointed to by the pointers.
4. Copy the smaller element to the result array and advance the corresponding pointer.
5. Repeat steps 3–4 until one subarray is exhausted.
6. Copy any remaining elements from the other subarray into the result array (these are already sorted).

**Example of Merging:**

Left: `[1, 5, 8]`, pointer `i` at `1`  
Right: `[2, 7, 10]`, pointer `j` at `2`  
Result: `[]`  
- Compare `1` and `2`. Copy `1` to result.  
  Result: `[1]`
- Compare `5` and `2`. Copy `2`.  
  Result: `[1, 2]`
- Compare `5` and `7`. Copy `5`.  
  Result: `[1, 2, 5]`
- Compare `8` and `7`. Copy `7`.  
  Result: `[1, 2, 5, 7]`
- Compare `8` and `10`. Copy `8`.  
  Result: `[1, 2, 5, 7, 8]`
- Left is exhausted; copy remaining `10`.  
  Result: `[1, 2, 5, 7, 8, 10]`

---

## The "Divide" Process

Example array: `[10, 7, 8, 9, 1, 5]`

1. Divide: `[10, 7, 8]` and `[9, 1, 5]`
2. Divide `[10, 7, 8]`: `[10]` and `[7, 8]`
3. Divide `[7, 8]`: `[7]` and `[8]`
4. Divide `[9, 1, 5]`: `[9]` and `[1, 5]`
5. Divide `[1, 5]`: `[1]` and `[5]`

Now, merge on the way back up:
- Merge `[7]` and `[8]` → `[7, 8]`
- Merge `[1]` and `[5]` → `[1, 5]`
- Merge `[10]` and `[7, 8]` → `[7, 8, 10]`
- Merge `[9]` and `[1, 5]` → `[1, 5, 9]`
- Merge `[7, 8, 10]` and `[1, 5, 9]` → `[1, 5, 7, 8, 9, 10]`

---

## Go Implementation

Merge Sort typically requires an auxiliary array for merging.

```go
package main

import "fmt"

// mergesort - the main function that calls recursive sorting
func mergesort(arr []int) []int {
	if len(arr) <= 1 {
		return arr // Base case: already sorted
	}

	mid := len(arr) / 2
	left := mergesort(arr[:mid])
	right := mergesort(arr[mid:])

	return merge(left, right)
}

// merge - merges two sorted slices
func merge(left, right []int) []int {
	result := make([]int, 0, len(left)+len(right))
	i, j := 0, 0

	for i < len(left) && j < len(right) {
		if left[i] <= right[j] {
			result = append(result, left[i])
			i++
		} else {
			result = append(result, right[j])
			j++
		}
	}

	for i < len(left) {
		result = append(result, left[i])
		i++
	}
	for j < len(right) {
		result = append(result, right[j])
		j++
	}

	return result
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
```

---

## Code Breakdown (Go)

- `mergesort(arr []int) []int`: Main recursive function. If the array is empty or has one element, returns as is. Otherwise, splits the array, recursively sorts each half, then merges them.
- `merge(left, right []int) []int`: Merges two sorted slices into a single sorted slice.

---

## Merge Sort Complexity

- **Time Complexity:** O(n log n) in best, worst, and average cases (log n levels of division, and each merge step is O(n)).
- **Space Complexity:** O(n) due to the auxiliary array for merging.

---

## Advantages of Merge Sort

- Guaranteed O(n log n) time complexity in all cases.
- Stable sort (preserves the relative order of equal elements).

---

## Disadvantages of Merge Sort

- Requires O(n) additional memory for auxiliary array.
- Can be slower than Quick Sort in practice (because of copying overhead), though its worst-case time is better.

---

## Python Implementation

```python
# Function to merge two sorted lists
def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Main recursive Merge Sort function
def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)

# Usage examples:
data = [10, 7, 8, 9, 1, 5]
print("Original list:", data)
sorted_data = mergesort(data)
print("Sorted list:", sorted_data)

data2 = [4, 2, 7, 1, 9, 3, 6, 8, 5]
print("Original list:", data2)
sorted_data2 = mergesort(data2)
print("Sorted list:", sorted_data2)
```

---

> _Merge Sort is a foundational algorithm in computer science, known for its predictable O(n log n) performance and stability. It is a key example of the divide-and-conquer strategy._

---