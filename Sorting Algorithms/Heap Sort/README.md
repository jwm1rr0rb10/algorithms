# Heap Sort

**Heap Sort** is a comparison-based sorting algorithm that uses a data structure called a **binary heap**.

---

## What is a Binary Heap?

A **binary heap** is a special kind of complete binary tree with two key properties:

### 1. Completeness Property
- All levels of the tree are fully filled, except possibly the last.
- The last level is filled from left to right.
- This allows the heap to be efficiently represented as an array without gaps.

For an element at index `i` in an array:
- Left child: `2*i + 1`
- Right child: `2*i + 2`
- Parent: `(i - 1) / 2` (integer division)

### 2. Heap Property
There are two types of binary heaps:
- **Max Heap**: Every node’s value is greater than or equal to its children. The largest element is at the root.
- **Min Heap**: Every node’s value is less than or equal to its children. The smallest element is at the root.

For sorting in ascending order, we typically use a **Max Heap**.

---

## How Heap Sort Works

Heap Sort consists of two main phases:

### 1. Build Max Heap
Transform the input array into a Max Heap. After this, the largest element will be at the root (index 0).

### 2. Sort the Heap
- Swap the root (maximum element) with the last element.
- Reduce the heap size by 1 (exclude the last element as it’s now sorted).
- Restore the heap property by `heapify` starting from the root.
- Repeat until the heap size is 1.

In the end, the array is sorted in ascending order.

---

## The `heapify` Operation (Sift Down)

This operation restores the heap property for a subtree rooted at index `i`:

1. Assume node `i` is the root.
2. Find the largest among node `i` and its children (within the heap size `n`).
3. If one of the children is larger than node `i`, swap them.
4. Recursively call `heapify` on the new position of the swapped child.

---

## Example

Given array: `[10, 7, 8, 9, 1, 5]` (n = 6)

### Phase 1: Build Max Heap

Start from the last parent node, index `(n / 2) - 1 = 2` and move upward.

- `heapify(arr, 6, 2)`
- `heapify(arr, 6, 1)`
- `heapify(arr, 6, 0)`

After this, the array becomes (heap structure maintained):  
`[10, 9, 8, 7, 1, 5]`

### Phase 2: Heap Sort

Repeatedly swap the root with the last element in the heap and `heapify`:

```text
[10, 9, 8, 7, 1, 5] -> [5, 9, 8, 7, 1, 10] -> heapify -> [9, 7, 8, 5, 1, 10]
[9, 7, 8, 5, 1, 10] -> [1, 7, 8, 5, 9, 10] -> heapify -> [8, 7, 1, 5, 9, 10]
[8, 7, 1, 5, 9, 10] -> [5, 7, 1, 8, 9, 10] -> heapify -> [7, 5, 1, 8, 9, 10]
[7, 5, 1, 8, 9, 10] -> [1, 5, 7, 8, 9, 10] -> heapify -> [5, 1, 7, 8, 9, 10]
[5, 1, 7, 8, 9, 10] -> [1, 5, 7, 8, 9, 10] -> Done.
```
Final sorted array:  
`[1, 5, 7, 8, 9, 10]`

---

## Go Implementation

```go
package main

import "fmt"

// heapify restores the Max-Heap property for the subtree rooted at index i.
func heapify(arr []int, n int, i int) {
	largest := i
	left := 2*i + 1
	right := 2*i + 2

	if left < n && arr[left] > arr[largest] {
		largest = left
	}
	if right < n && arr[right] > arr[largest] {
		largest = right
	}
	if largest != i {
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest)
	}
}

// heapsort performs Heap Sort in-place
func heapsort(arr []int) {
	n := len(arr)
	// Build a Max-Heap
	for i := n/2 - 1; i >= 0; i-- {
		heapify(arr, n, i)
	}
	// Extract elements one by one
	for i := n - 1; i > 0; i-- {
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, i, 0)
	}
}

func main() {
	data := []int{10, 7, 8, 9, 1, 5}
	fmt.Println("Original array:", data)
	heapsort(data)
	fmt.Println("Sorted array:", data)

	data2 := []int{4, 2, 7, 1, 9, 3, 6, 8, 5}
	fmt.Println("Original array:", data2)
	heapsort(data2)
	fmt.Println("Sorted array:", data2)
}
```

---

## Code Breakdown

### `heapify(arr []int, n int, i int)`
- Accepts an array, the heap size `n`, and the index `i` of the node to restore the heap property.
- Calculates left and right child indices.
- Compares the value at `i` with its children.
- Swaps if needed and recursively heapifies the affected subtree.

### `heapsort(arr []int)`
- Builds a Max-Heap from the array.
- Iterates from the last parent node up to the root, calling `heapify`.
- Extracts the max element (root) repeatedly, placing it at the end, and heapifies the reduced heap.

---

## Heap Sort Complexity

### Time Complexity
- **Best / Average / Worst Case:** O(n log n)
  - Heap construction: O(n)
  - Each of the `n−1` extraction + heapify operations: O(log n)
  - **Total:** O(n + n log n) = O(n log n)

### Space Complexity
- O(1) – Heap Sort is in-place, requiring only a constant amount of extra space.
- Stack recursion in `heapify` is at most O(log n).

---

## Advantages of Heap Sort

- Guaranteed O(n log n) time complexity in all cases.
- In-place algorithm with O(1) additional memory usage.

## Disadvantages of Heap Sort

- Not a stable sort (equal elements may not retain their original order).
- Slightly slower in practice than Quick Sort due to more cache misses and swaps.

---

## When to Use Heap Sort

- When worst-case performance guarantees are important.
- When memory usage must be minimized.

---

## Python Implementation

```python
# Function to restore the max-heap property for a subtree rooted at index i.
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Main function for heap sort
def heapsort(arr):
    n = len(arr)
    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Usage examples:
data = [10, 7, 8, 9, 1, 5]
print("Original list:", data)
heapsort(data)
print("Sorted list:", data)

data2 = [4, 2, 7, 1, 9, 3, 6, 8, 5]
print("Original list:", data2)
heapsort(data2)
print("Sorted list:", data2)
```

---

> _Heap Sort is a robust, in-place sorting algorithm that guarantees O(n log n) performance regardless of input. It is a key example of utilizing data structures (heaps) for efficient algorithm design._

---