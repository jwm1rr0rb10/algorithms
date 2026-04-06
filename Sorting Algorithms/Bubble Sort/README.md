# 🧼 Bubble Sort

**Bubble Sort** is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until the list is sorted. Larger elements "bubble up" to the end of the list with each pass, like bubbles in water.

---

## 🔍 Idea

- Traverse the array multiple times.
- On each pass, compare adjacent elements.
- If they are in the wrong order (e.g., the first is greater than the second for ascending sort), swap them.
- Repeat until no swaps are needed — meaning the array is sorted.

---

## 🧪 Example (Sorting in Ascending Order)

Initial array:  
`[10, 7, 8, 9, 1, 5]`

### Pass 1:
- 10 > 7 → `[7, 10, 8, 9, 1, 5]`
- 10 > 8 → `[7, 8, 10, 9, 1, 5]`
- 10 > 9 → `[7, 8, 9, 10, 1, 5]`
- 10 > 1 → `[7, 8, 9, 1, 10, 5]`
- 10 > 5 → `[7, 8, 9, 1, 5, 10]`

### Pass 2:
- 7 < 8 → no swap
- 8 < 9 → no swap
- 9 > 1 → `[7, 8, 1, 9, 5, 10]`
- 9 > 5 → `[7, 8, 1, 5, 9, 10]`

### Pass 3:
- 7 < 8 → no swap
- 8 > 1 → `[7, 1, 8, 5, 9, 10]`
- 8 > 5 → `[7, 1, 5, 8, 9, 10]`

### Pass 4:
- 7 > 1 → `[1, 7, 5, 8, 9, 10]`
- 7 > 5 → `[1, 5, 7, 8, 9, 10]`

### Pass 5:
- 1 < 5 → no swap

Array is now sorted: `[1, 5, 7, 8, 9, 10]`

---

## ⚡ Optimization

If a full pass completes without any swaps, the algorithm can terminate early since the array is already sorted.

---

## 📦 Time and Space Complexity

| Complexity           | Value           |
|:-------------------- |:---------------|
| Time (Best)          | O(n)           |
| Time (Average/Worst) | O(n²)          |
| Space                | O(1) (in-place)|

---

## ✅ Go Implementation

```go
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
```

---

## 🐍 Python Implementation

```python
# bubble_sort sorts a list using the bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    # Outer loop iterates through all elements
    for i in range(n - 1):
        swapped = False  # Optimization flag

        # Inner loop compares adjacent elements
        # (n - i - 1) because the last i elements are already in place
        for j in range(n - i - 1):
            # If the current element is greater than the next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Mark that a swap occurred

        # If no swaps occurred in this pass, the list is sorted
        if not swapped:
            break

# Example usage of Bubble Sort:
data_bubble = [10, 7, 8, 9, 1, 5]
print("Original list (Bubble Sort):", data_bubble)
bubble_sort(data_bubble)
print("Sorted list (Bubble Sort):", data_bubble)

data_bubble_2 = [1, 2, 3, 4, 5]  # Already sorted
print("Original list (Bubble Sort):", data_bubble_2)
bubble_sort(data_bubble_2)
print("Sorted list (Bubble Sort):", data_bubble_2)
```

---

> _Bubble Sort is a great starting point for learning sorting algorithms, though not efficient for large datasets. Its simplicity is its main advantage._

---