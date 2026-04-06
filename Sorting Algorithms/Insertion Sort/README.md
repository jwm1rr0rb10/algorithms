# Insertion Sort 

## 📋 Description

**Insertion Sort** is a simple sorting algorithm that works similarly to sorting playing cards in your hands. One element at a time is taken from the unsorted part and inserted into the correct position in the already sorted part, shifting larger elements to the right.

### 🔑 Key Idea

- The array is divided into two parts: sorted and unsorted.
- The first element is considered sorted.
- Each subsequent element is taken from the unsorted part and inserted into its correct place in the sorted part.

---

## 📈 Example (Ascending Order)

Original array:  
`[10, 7, 8, 9, 1, 5]`

Sorting steps:

1. `[10] | [7, 8, 9, 1, 5]` → `[7, 10] | [8, 9, 1, 5]`
2. `[7, 10] | [8, 9, 1, 5]` → `[7, 8, 10] | [9, 1, 5]`
3. `[7, 8, 10] | [9, 1, 5]` → `[7, 8, 9, 10] | [1, 5]`
4. `[7, 8, 9, 10] | [1, 5]` → `[1, 7, 8, 9, 10] | [5]`
5. `[1, 7, 8, 9, 10] | [5]` → `[1, 5, 7, 8, 9, 10]`

---

## 🧠 Algorithm Complexity

| Scenario              | Time Complexity | Space Complexity |
|:----------------------|:----------------|:----------------|
| Best (already sorted) | O(n)            | O(1) (in-place) |
| Average               | O(n²)           | O(1)            |
| Worst                 | O(n²)           | O(1)            |

---

## 🧪 Implementation

### ✅ Go

```go
package main

import "fmt"

// insertionSort sorts an array using the insertion sort algorithm
func insertionSort(arr []int) {
    n := len(arr)
    for i := 1; i < n; i++ {
        key := arr[i]
        j := i - 1

        for j >= 0 && arr[j] > key {
            arr[j+1] = arr[j]
            j--
        }
        arr[j+1] = key
    }
}

func main() {
    data := []int{10, 7, 8, 9, 1, 5}
    fmt.Println("Original array:", data)
    insertionSort(data)
    fmt.Println("Sorted array:", data)

    data2 := []int{4, 2, 7, 1, 9, 3, 6, 8, 5}
    fmt.Println("Original array:", data2)
    insertionSort(data2)
    fmt.Println("Sorted array:", data2)
}
```

---

### 🐍 Python

```python
# insertion_sort sorts a list using the insertion sort algorithm
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Examples of using Insertion Sort:
data_insertion = [10, 7, 8, 9, 1, 5]
print("\nOriginal list (Insertion Sort):", data_insertion)
insertion_sort(data_insertion)
print("Sorted list (Insertion Sort):", data_insertion)

data_insertion_2 = [4, 2, 7, 1, 9, 3, 6, 8, 5]
print("Original list (Insertion Sort):", data_insertion_2)
insertion_sort(data_insertion_2)
print("Sorted list (Insertion Sort):", data_insertion_2)
```

---

## 🛠️ Useful for

- Learning basic sorting algorithms
- Sorting small arrays
- Understanding the principle of "in-place sorting"

---

## 📚 Additional Notes

- Works well with nearly sorted data
- Inefficient for large datasets

---