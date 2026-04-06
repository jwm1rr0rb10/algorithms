# Radix Sort

**Radix Sort** is a non-comparative sorting algorithm that sorts numbers by processing their digits (or bits). It works by repeatedly applying a **stable sort** to each digit of the number, starting from the least significant digit and ending with the most significant digit.

---

## Key Idea

- Radix Sort sorts the list by each digit, starting from the least significant digit (LSD) and moving to the most significant digit (MSD).
- It uses a **stable sorting algorithm** (like Counting Sort) for each digit.
- Because stable sort is used, elements with the same digit preserve the order from previous passes, resulting in correct global ordering after all digits are processed.

---

## Requirements

- A **stable sorting algorithm** for digit-wise sorting (Counting Sort is ideal for digits 0-9).
- Elements must have "digits" or "keys" that can be processed individually (e.g., digits in a number, characters in a fixed-length word).

---

## Example (Ascending Order, Decimal Numbers)

Given array: `[170, 45, 75, 90, 802, 24, 2, 66]`

**Step 1: Sort by Units Digit (LSD):**  
After stable sort by units: `[170, 90, 802, 2, 24, 45, 75, 66]`

**Step 2: Sort by Tens Digit:**  
After stable sort by tens: `[802, 2, 90, 24, 45, 66, 170, 75]`

**Step 3: Sort by Hundreds Digit:**  
After stable sort by hundreds: `[2, 24, 45, 66, 75, 90, 170, 802]`

Result is the sorted array.

---

## ✅ Go Implementation

```go
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

// countSortForRadix performs Counting Sort for a given digit place (exp)
func countSortForRadix(arr []int, exp int) {
	n := len(arr)
	output := make([]int, n)
	count := make([]int, 10) // Digits 0-9

	for i := 0; i < n; i++ {
		digit := (arr[i] / exp) % 10
		count[digit]++
	}
	for i := 1; i < 10; i++ {
		count[i] += count[i-1]
	}
	for i := n - 1; i >= 0; i-- {
		digit := (arr[i] / exp) % 10
		pos := count[digit] - 1
		output[pos] = arr[i]
		count[digit]--
	}
	for i := 0; i < n; i++ {
		arr[i] = output[i]
	}
}

func radixSort(arr []int) {
	n := len(arr)
	if n <= 1 {
		return
	}
	m := getMax(arr)
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

	data3 := []int{123, 45, 6, 7890, 1, 555}
	fmt.Println("Original array:", data3)
	radixSort(data3)
	fmt.Println("Sorted array:", data3)
}
```

---

## Code Breakdown

- `getMax(arr []int) int`: Finds the maximum value to determine digit count.
- `countSortForRadix(arr []int, exp int)`: Stable Counting Sort for the digit at place `exp`.
    - `(arr[i] / exp) % 10` extracts the digit at the current position.
    - Builds `count` array, computes cumulative counts, fills output in reverse for stability.
    - Copies sorted output back to the original array.
- `radixSort(arr []int)`: Orchestrates the sort by calling `countSortForRadix` for each digit place.

---

## Radix Sort Complexity

- **Time Complexity:** O(nk), where n = number of elements, k = number of digits in the largest number.
    - For base 10 and reasonably sized integers, k is small and Radix Sort approaches O(n).
- **Space Complexity:** O(n + b), where b = base (e.g., 10 for decimal digits).

---

## Advantages

- Can be faster than comparison sorts if the number of digits is small relative to n.
- Stable sort (if the digit sort is stable).

## Disadvantages

- Only works for data with a digit/key structure (numbers, fixed-length strings).
- Requires a stable sort internally.
- Not in-place (due to output array).

---

## ✅ Python Implementation

```python
# Helper: get digit at a given place
def get_digit(number, exp):
    return (number // exp) % 10

def count_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count digits
    for i in range(n):
        digit = get_digit(arr[i], exp)
        count[digit] += 1
    # Accumulate
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Build output (reverse for stability)
    for i in range(n - 1, -1, -1):
        digit = get_digit(arr[i], exp)
        pos = count[digit] - 1
        output[pos] = arr[i]
        count[digit] -= 1
    # Copy output back to arr
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    n = len(arr)
    if n <= 1:
        return
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        count_sort_for_radix(arr, exp)
        exp *= 10

# Examples:
data_radix = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original list (Radix Sort):", data_radix)
radix_sort(data_radix)
print("Sorted list (Radix Sort):", data_radix)

data_radix_2 = [4, 2, 7, 1, 9, 3, 6, 8, 5]
print("Original list (Radix Sort):", data_radix_2)
radix_sort(data_radix_2)
print("Sorted list (Radix Sort):", data_radix_2)

data_radix_3 = [123, 45, 6, 7890, 1, 555, 10000]
print("Original list (Radix Sort):", data_radix_3)
radix_sort(data_radix_3)
print("Sorted list (Radix Sort):", data_radix_3)
```

---

> _Radix Sort is a powerful linear-time sorting algorithm for integers and other data types with a fixed digit/key structure, provided the internal sort is stable. It demonstrates how dropping comparison-based sorting can lead to faster algorithms in specialized cases._

---