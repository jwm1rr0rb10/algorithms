# Ternary Search

## What it is

Ternary search is a "divide and conquer" search algorithm. Like binary search, it operates on sorted data, but instead of dividing the interval into two halves, it divides it into three parts. Ternary search is rarely used for searching an element in a sorted array (binary search is better for that), but is commonly used for finding the extremum (minimum or maximum) of a unimodal function on an interval.

---

## How it works (searching for an element in a sorted array)

1. Start with a search interval `[low, high]`.
2. Compute two points:  
   - `mid1 = low + (high - low) // 3`  
   - `mid2 = high - (high - low) // 3`  
   (`mid1 < mid2`)
3. Compare the target value to `data[mid1]` and `data[mid2]`:
    - If `target == data[mid1]`: return `mid1`.
    - If `target == data[mid2]`: return `mid2`.
    - If `target < data[mid1]`: search in the left third `[low, mid1 - 1]`.
    - If `target > data[mid2]`: search in the right third `[mid2 + 1, high]`.
    - If `data[mid1] < target < data[mid2]`: search in the middle third `[mid1 + 1, mid2 - 1]`.
4. Repeat until the element is found or the interval is empty (`low > high`).

**Prerequisite:** The array (list) must be sorted.

---

## Complexity

- **Time:** $O(\log_3 n)$, which is asymptotically equivalent to $O(\log n)$, but ternary search does more comparisons per step than binary search, so it's typically slower for element search in arrays.
- **Space:**
    - Iterative: $O(1)$
    - Recursive: $O(\log_3 n)$

---

## When to use

- For **element search in a sorted array**: usually *not recommended* (binary search is better).
- For **finding the minimum/maximum of a unimodal function** on a segment: ternary search is the standard approach.

---

## Go Example (element search in sorted slice)

```go
package main

import "fmt"

// TernarySearch searches for target in a sorted slice data.
// Returns the index of target if found, otherwise -1.
func TernarySearch(data []int, target int) int {
	low := 0
	high := len(data) - 1

	for low <= high {
		mid1 := low + (high-low)/3
		mid2 := high - (high-low)/3

		if data[mid1] == target {
			return mid1
		}
		if data[mid2] == target {
			return mid2
		}

		if target < data[mid1] {
			high = mid1 - 1
		} else if target > data[mid2] {
			low = mid2 + 1
		} else {
			low = mid1 + 1
			high = mid2 - 1
		}
	}
	return -1
}

func main() {
	sortedData := []int{2, 5, 8, 12, 16, 23, 38, 56, 72, 91}
	targets := []int{38, 10}

	for _, target := range targets {
		index := TernarySearch(sortedData, target)
		if index != -1 {
			fmt.Printf("Element %d found at index %d\n", target, index)
		} else {
			fmt.Printf("Element %d not found\n", target)
		}
	}
}
```

---

## Python Example (element search in sorted list)

```python
def ternary_search(data, target):
    """
    Searches for target in a sorted list data using ternary search.
    Returns the index of target if found, otherwise -1.
    """
    low = 0
    high = len(data) - 1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if data[mid1] == target:
            return mid1
        if data[mid2] == target:
            return mid2

        if target < data[mid1]:
            high = mid1 - 1
        elif target > data[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1

    return -1

# Example usage
sorted_data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
targets = [38, 10]

for target in targets:
    index = ternary_search(sorted_data, target)
    if index != -1:
        print(f"Element {target} found at index {index}")
    else:
        print(f"Element {target} not found")
```

---

## Note

Ternary search is rarely used for element search in arrays (binary search is almost always better). Its main application is in optimization (finding min/max of unimodal functions).
---

## 🟢 Easy Problems

| #    | Title                                      | Acceptance Rate |
|:-----|:-------------------------------------------|:----------------|
| 704  | Binary Search                              | 59.4%           |
| 35   | Search Insert Position                     | 48.7%           |
| 897  | Increasing Order Search Tree               | 78.6%           |
| 270  | Closest Binary Search Tree Value           | 49.9%           |
| 700  | Search in a Binary Search Tree             | 81.5%           |
| 501  | Find Mode in Binary Search Tree            | 57.4%           |
| 108  | Convert Sorted Array to Binary Search Tree | 73.9%           |
| 603  | Consecutive Available Seats                | 65.4%           |
| 2037 | Minimum Number of Moves to Seat Everyone   | 87.3%           |

## 🟡 Medium Problems

| #    | Title                                                | Acceptance Rate |
|:-----|:-----------------------------------------------------|:----------------|
| 439  | Ternary Expression Parser                            | 61.9%           |
| 79   | Word Search                                          | 45.0%           |
| 1268 | Search Suggestions System                            | 65.0%           |
| 74   | Search a 2D Matrix                                   | 52.1%           |
| 96   | Unique Binary Search Trees                           | 62.3%           |
| 98   | Validate Binary Search Tree                          | 34.2%           |
| 99   | Recover Binary Search Tree                           | 55.9%           |
| 173  | Binary Search Tree Iterator                          | 74.6%           |
| 33   | Search in Rotated Sorted Array                       | 42.6%           |
| 95   | Unique Binary Search Trees II                        | 60.2%           |
| 240  | Search a 2D Matrix II                                | 54.9%           |
| 669  | Trim a Binary Search Tree                            | 66.4%           |
| 1382 | Balance a Binary Search Tree                         | 84.6%           |
| 1586 | Binary Search Tree Iterator II                       | 63.2%           |
| 81   | Search in Rotated Sorted Array II                    | 38.8%           |
| 701  | Insert into a Binary Search Tree                     | 73.5%           |
| 1038 | Binary Search Tree to Greater Sum Tree               | 88.2%           |
| 109  | Convert Sorted List to Binary Search Tree            | 64.2%           |
| 211  | Design Add and Search Words Data Structure           | 46.9%           |
| 255  | Verify Preorder Sequence in Binary Search Tree       | 50.8%           |
| 1008 | Construct Binary Search Tree from Preorder Traversal | 83.1%           |
| 1305 | All Elements in Two Binary Search Trees              | 80.0%           |
| 235  | Lowest Common Ancestor of a Binary Search Tree       | 68.0%           |
| 702  | Search in a Sorted Array of Unknown Size             | 72.7%           |
| 2476 | Closest Nodes Queries in a Binary Search Tree        | 42.4%           |
| 426  | Convert BST to Sorted Doubly Linked List             | 65.4%           |
| 1966 | Binary Searchable Numbers in an Unsorted Array       | 62.4%           |
| 1386 | Cinema Seat Allocation                               | 42.7%           |
| 1845 | Seat Reservation Manager                             | 66.3%           |
| 1227 | Airplane Seat Assignment Probability                 | 66.6%           |
| 3140 | Consecutive Available Seats II                       | 57.1%           |

## 🔴 Hard Problems

| #   | Title                               | Acceptance Rate |
|:----|:------------------------------------|:----------------|
| 212 | Word Search II                      | 37.2%           |
| 642 | Design Search Autocomplete System   | 49.3%           |
| 745 | Prefix and Suffix Search            | 40.4%           |
| 272 | Closest Binary Search Tree Value II | 60.2%           |
