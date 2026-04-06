# Bucket Sort

**Bucket Sort** is a non-comparison-based sorting algorithm that works by distributing elements of the original array into “buckets.”

---

## Core Idea

1. Create a set of buckets (lists or arrays). Each bucket typically corresponds to a specific range of values.
2. Iterate over the original array and place each element into the appropriate bucket based on its value.
3. Sort each bucket individually (using, for example, Insertion Sort, which is efficient for small lists).
4. Concatenate the contents of all buckets in order to obtain the final sorted array.

---

## Requirements

- Best performance is achieved when the input data is uniformly distributed.
- A mapping function is needed to determine which bucket an element should go to.
- An additional sorting algorithm is required to sort elements within each bucket.

---

## Example: Sorting Floating-Point Numbers Between 0.0 and 1.0

**Input array:**  
`[0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]`

**We’ll create 10 buckets for ranges:**  
`[0.0, 0.1), [0.1, 0.2), ..., [0.9, 1.0)`

**Step 1: Create the buckets**  
10 empty lists: `buckets[0], buckets[1], ..., buckets[9]`

**Step 2: Distribute the elements**  
Example:  
```
0.78 -> buckets[7]
0.17 -> buckets[1]
0.39 -> buckets[3]
0.26 -> buckets[2]
0.72 -> buckets[7]
0.94 -> buckets[9]
0.21 -> buckets[2]
0.12 -> buckets[1]
0.23 -> buckets[2]
0.68 -> buckets[6]
```

**Step 3: Sort each bucket (using Insertion Sort or built-in sort)**

- `buckets[1]: [0.12, 0.17]`
- `buckets[2]: [0.21, 0.23, 0.26]`
- `buckets[3]: [0.39]`
- `buckets[6]: [0.68]`
- `buckets[7]: [0.72, 0.78]`
- `buckets[9]: [0.94]`

**Step 4: Concatenate the buckets**  
Merge all buckets in order.

**Result:**  
`[0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]`

---

## ✅ Go Implementation

```go
package main

import (
	"fmt"
	"sort"
)

// bucketSort sorts a list of floating-point numbers between 0.0 and 1.0
func bucketSort(arr []float64, numBuckets int) {
	n := len(arr)
	if n == 0 || numBuckets <= 0 {
		return
	}

	// 1. Create buckets
	buckets := make([][]float64, numBuckets)
	for i := range buckets {
		buckets[i] = []float64{}
	}

	// 2. Distribute elements into buckets
	for _, value := range arr {
		bucketIndex := int(value * float64(numBuckets))
		if bucketIndex == numBuckets {
			bucketIndex--
		}
		if bucketIndex < 0 || bucketIndex >= numBuckets {
			continue
		}
		buckets[bucketIndex] = append(buckets[bucketIndex], value)
	}

	// 3. Sort each bucket and 4. Merge into original array
	k := 0
	for i := 0; i < numBuckets; i++ {
		sort.Float64s(buckets[i])
		for _, value := range buckets[i] {
			arr[k] = value
			k++
		}
	}
}

func main() {
	data := []float64{0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68}
	fmt.Println("Original array (Bucket Sort):", data)
	bucketSort(data, 10)
	fmt.Println("Sorted array (Bucket Sort):", data)

	data2 := []float64{0.5, 0.1, 0.9, 0.3, 0.7, 0.2, 0.8, 0.4, 0.6, 1.0}
	fmt.Println("Original array (Bucket Sort):", data2)
	bucketSort(data2, 10)
	fmt.Println("Sorted array (Bucket Sort):", data2)
}
```

---

## ✅ Python Implementation

```python
def bucket_sort(arr, num_buckets):
    n = len(arr)
    if n == 0 or num_buckets <= 0:
        return

    # 1. Create buckets
    buckets = [[] for _ in range(num_buckets)]

    # 2. Distribute elements into buckets
    for value in arr:
        bucket_index = int(value * num_buckets)
        if bucket_index == num_buckets:
            bucket_index -= 1
        if bucket_index < 0 or bucket_index >= num_buckets:
            continue
        buckets[bucket_index].append(value)

    # 3. Sort each bucket and 4. Merge the buckets
    k = 0
    for i in range(num_buckets):
        buckets[i].sort()
        for value in buckets[i]:
            arr[k] = value
            k += 1

# Examples of using Bucket Sort:
data_bucket = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print("Original list (Bucket Sort):", data_bucket)
bucket_sort(data_bucket, 10)
print("Sorted list (Bucket Sort):", data_bucket)

data_bucket_2 = [0.5, 0.1, 0.9, 0.3, 0.7, 0.2, 0.8, 0.4, 0.6, 1.0]
print("Original list (Bucket Sort):", data_bucket_2)
bucket_sort(data_bucket_2, 10)
print("Sorted list (Bucket Sort):", data_bucket_2)

data_bucket_3 = [0.05, 0.95, 0.001, 0.15, 0.85, 0.25, 0.75, 0.35, 0.65, 0.45]
print("Original list (Bucket Sort):", data_bucket_3)
bucket_sort(data_bucket_3, 5)
print("Sorted list (Bucket Sort):", data_bucket_3)
```

---

## Complexity

- **Average Case:** O(n + k) — where n is the number of elements, k is the number of buckets. (Assumes uniform distribution and small buckets.)
- **Worst Case:** O(n²) — if all elements end up in a single bucket (depends on inner sort).
- **Space Complexity:** O(n + k)

---

## Advantages

- Fast (O(n) average case) when input is uniformly distributed.
- Very efficient for floating-point numbers in a known range.

## Disadvantages

- Performance highly depends on data distribution.
- Additional space required for buckets.
- Needs an extra sorting algorithm for each bucket.

---

> _Bucket Sort is a great illustration of how leveraging properties of your data (like range and distribution) leads to highly efficient sorts in special cases._

---