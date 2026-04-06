# Selection Sort

**Selection Sort** works on the principle of "find the minimum and place it in its correct position."

---

## Main Idea

- The array is conceptually divided into a sorted and an unsorted part.
- At each step, the algorithm finds the smallest element in the unsorted part and swaps it with the first element of the unsorted part (i.e., with the element that should be next in the sorted portion).
- The sorted part gradually grows from the left side.

---

## Example (Ascending Order)

Let's sort the array: `[10, 7, 8, 9, 1, 5]`

**Step 1:**
- Unsorted part: `[10, 7, 8, 9, 1, 5]`
- Find the smallest element: `1` (index 4).
- Swap `10` (index 0) with `1` (index 4).
- Result: `[1, 7, 8, 9, 10, 5]`
- Sorted: `[1]`, Unsorted: `[7, 8, 9, 10, 5]`

**Step 2:**
- Unsorted part: `[7, 8, 9, 10, 5]`
- Smallest is `5` (index 5).
- Swap `7` (index 1) with `5` (index 5).
- Result: `[1, 5, 8, 9, 10, 7]`
- Sorted: `[1, 5]`, Unsorted: `[8, 9, 10, 7]`

**Step 3:**
- Unsorted part: `[8, 9, 10, 7]`
- Smallest is `7` (index 5).
- Swap `8` (index 2) with `7` (index 5).
- Result: `[1, 5, 7, 9, 10, 8]`
- Sorted: `[1, 5, 7]`, Unsorted: `[9, 10, 8]`

**Step 4:**
- Unsorted part: `[9, 10, 8]`
- Smallest is `8` (index 5).
- Swap `9` (index 3) with `8` (index 5).
- Result: `[1, 5, 7, 8, 10, 9]`
- Sorted: `[1, 5, 7, 8]`, Unsorted: `[10, 9]`

**Step 5:**
- Unsorted part: `[10, 9]`
- Smallest is `9` (index 5).
- Swap `10` (index 4) with `9` (index 5).
- Result: `[1, 5, 7, 8, 9, 10]`
- Sorted: `[1, 5, 7, 8, 9]`, Unsorted: `[10]`

The last element is already in place. The array is now sorted.

---

## ✅ Go Implementation

```go
package main

import "fmt"

// selectionSort sorts an array using the Selection Sort algorithm
func selectionSort(arr []int) {
	n := len(arr)
	for i := 0; i < n-1; i++ {
		minIndex := i
		for j := i + 1; j < n; j++ {
			if arr[j] < arr[minIndex] {
				minIndex = j
			}
		}
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
```

---

## ✅ Python Implementation

```python
# selection_sort sorts a list using the Selection Sort algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Examples of using Selection Sort:
data_selection = [10, 7, 8, 9, 1, 5]
print("\nOriginal list (Selection Sort):", data_selection)
selection_sort(data_selection)
print("Sorted list (Selection Sort):", data_selection)

data_selection_2 = [4, 2, 7, 1, 9, 3, 6, 8, 5]
print("Original list (Selection Sort):", data_selection_2)
selection_sort(data_selection_2)
print("Sorted list (Selection Sort):", data_selection_2)
```

---

## Complexity

### Time Complexity

- **O(n²)** in all cases (best, average, and worst).
- The outer loop runs `n - 1` times.
- The inner loop scans the remaining unsorted part, decreasing in size.
- Total comparisons: approximately `n^2 / 2`.

### Space Complexity

- **O(1)** — Selection Sort is in-place, requiring only a constant amount of extra space.

---

## Why are these algorithms useful for understanding core concepts?

Even though algorithms like Bubble Sort, Insertion Sort, and Selection Sort have a time complexity of O(n²), they are valuable for learning because of their:

- **Simplicity:** Their logic is intuitive and closely mirrors how a person might manually sort a small set of items.
- **Visualization:** They're easy to visualize, making it easier to grasp the basic ideas of comparing and moving elements to achieve order.
- **Fundamental operations:**  
    - Comparison and swap (Bubble Sort)  
    - Comparison and shift for insertion (Insertion Sort)  
    - Finding minimum/maximum and swapping (Selection Sort)

While rarely used for large datasets due to their quadratic complexity:

- **Insertion Sort** can be efficient for very small arrays or nearly sorted data.
- **Bubble Sort** and **Selection Sort** are rarely used in practice, but Selection Sort performs the minimum number of swaps — exactly `n - 1` — which can be important when swap operations are computationally expensive.

---