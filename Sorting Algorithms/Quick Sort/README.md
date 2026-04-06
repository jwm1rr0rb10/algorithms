# Sorting Algorithms

This section provides an overview and implementation examples of key sorting algorithms. Here, we begin with **Quick Sort**, a classic and efficient divide-and-conquer sorting method.

---

## 1. Quick Sort

**Quick Sort** is an efficient, in-place sorting algorithm that uses the **divide and conquer** approach. Developed by Tony Hoare, it is widely used because of its practical performance.

### Key Idea

1. **Choose a Pivot Element:** Select one element from the array (first, last, middle, or randomly chosen). The pivot selection can greatly influence efficiency.
2. **Partition:** Rearrange the array so that all elements less than the pivot come before it, and all elements greater than the pivot come after it. Elements equal to the pivot can be on either side.
3. **Recursively Apply:** Apply Quick Sort recursively to the subarrays of elements less than and greater than the pivot.

The process stops when subarrays contain 0 or 1 element, as they are already sorted.

---

### The "Partition" Step

This is the key step of Quick Sort. There are several partitioning strategies, but we'll use the Lomuto partition scheme, which is simple and commonly used:

1. Choose the pivot element (e.g., the last element).
2. Use a pointer `i` to track the boundary of the "lesser" part. Initially, `i = low - 1`.
3. Iterate through the array with another pointer `j` from `low` up to `high - 1`.
4. If `arr[j]` is less than or equal to the pivot:
    - Increment `i`.
    - Swap `arr[i]` and `arr[j]`.
5. After the loop, swap `arr[i+1]` and the pivot element (`arr[high]`). The element at `arr[i+1]` is now in its final sorted position.

#### Example (Lomuto Partition with last element as pivot):

Suppose we have the array: `[10, 7, 8, 9, 1, 5]` and choose the last element (`5`) as the pivot.

- `low = 0`, `high = 5`, `pivot = arr[high] = 5`
- Initialize `i = low - 1 = -1`

Iterate `j` from `low` to `high - 1` (from 0 to 4):

- `j = 0`, `arr[0] = 10` → 10 > 5, do nothing, `i = -1`
- `j = 1`, `arr[1] = 7` → 7 > 5, do nothing, `i = -1`
- `j = 2`, `arr[2] = 8` → 8 > 5, do nothing, `i = -1`
- `j = 3`, `arr[3] = 9` → 9 > 5, do nothing, `i = -1`
- `j = 4`, `arr[4] = 1` → 1 <= 5
    - Increment `i` (i = 0)
    - Swap `arr[0]` and `arr[4]`: `[1, 7, 8, 9, 10, 5]`

After the loop, swap `arr[i+1]` (`arr[1]`, which is 7) and the pivot (`arr[5]`, which is 5):
Resulting array: `[1, 5, 8, 9, 10, 7]`

Now, pivot `5` is at index 1. All elements to its left (`[1]`) are less than or equal to 5, and all elements to its right (`[8, 9, 10, 7]`) are greater.

Recursively apply Quick Sort to the subarrays `[1]` and `[8, 9, 10, 7]`.

---

### Go Implementation

```go
package main

import "fmt"

func quicksort(arr []int) {
	quicksortRecursive(arr, 0, len(arr)-1)
}

func quicksortRecursive(arr []int, low, high int) {
	if low < high {
		pi := partition(arr, low, high)
		quicksortRecursive(arr, low, pi-1)
		quicksortRecursive(arr, pi+1, high)
	}
}

func partition(arr []int, low, high int) int {
	pivot := arr[high]
	i := low - 1
	for j := low; j < high; j++ {
		if arr[j] <= pivot {
			i++
			arr[i], arr[j] = arr[j], arr[i]
		}
	}
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i + 1
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
```

---

### Code Breakdown

- `quicksort(arr []int)`: Helper function that calls `quicksortRecursive` with initial indices.
- `quicksortRecursive(arr []int, low, high int)`: The main recursive function. If `low < high`, it partitions the array and recursively sorts the subarrays.
- `partition(arr []int, low, high int) int`: Performs the Lomuto partitioning. Returns the index of the pivot in its final position.

---

### Python Implementation

```python
# Function to perform partitioning
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Main recursive Quick Sort function
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Auxiliary function to call quicksort with initial parameters
def sort_quick(arr):
    quicksort(arr, 0, len(arr) - 1)

# Usage examples:
data = [10, 7, 8, 9, 1, 5]
print("Original array:", data)
sort_quick(data)
print("Sorted array:", data)

data2 = [4, 2, 7, 1, 9, 3, 6, 8, 5]
print("Original array:", data2)
sort_quick(data2)
print("Sorted array:", data2)
```

---

### Quick Sort Complexity

**Time Complexity:**
- **Average:** O(n log n) — occurs when the pivot divides the array into roughly equal halves at each step.
- **Worst Case:** O(n²) — occurs when the pivot is always the smallest or largest element in the subarray (e.g., already sorted arrays with poor pivot choice).

**Space Complexity:**
- **Average:** O(log n) due to the recursion stack.
- **Worst Case:** O(n) in rare cases when recursion is very deep (again, with a poor pivot choice).

**Advantages:**
- Fast in practice (on average).
- In-place sorting, requiring minimal additional memory (besides the recursion stack).

**Disadvantages:**
- Worst-case time complexity is O(n²).
- Not stable (the relative order of equal elements may not be preserved).

---

> _Quick Sort is a foundational algorithm in computer science and is often used as a building block for more advanced sorting techniques. Understanding its core mechanism (partitioning) is key to mastering divide-and-conquer strategies._

---