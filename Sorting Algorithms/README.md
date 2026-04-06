# Overview of Sorting Algorithms

Sorting algorithms are fundamental in computer science, impacting everything from database indexing to data visualization. Each algorithm has its own strengths and weaknesses depending on data type, size, and constraints. Below is a comprehensive comparison and practical guidance for common sorting algorithms.

---

## Algorithm Comparison Table

| Algorithm        | Time Complexity (Best / Avg / Worst) | Space Complexity | Stable | In-Place | Notes |
|:-----------------|:-------------------------------------:|:----------------:|:------:|:--------:|:------|
| **Bubble Sort**      | O(n) / O(n²) / O(n²)               | O(1)             | Yes    | Yes      | Simple, rarely used in practice. Good for nearly-sorted data. |
| **Bucket Sort**      | O(n + k) (avg), O(n²) (worst)      | O(n + k)         | Yes    | No       | Fast for uniformly distributed data; good for decimal/floating-point. |
| **Counting Sort**    | O(n + k)                           | O(k)             | Yes    | No       | Only for integer or limited range keys. Linear time, very fast. |
| **Heap Sort**        | O(n log n) / O(n log n) / O(n log n) | O(1)           | No     | Yes      | Always O(n log n), not stable, good for limited memory. |
| **Insertion Sort**   | O(n) / O(n²) / O(n²)               | O(1)             | Yes    | Yes      | Great for small/nearly sorted arrays. |
| **Merge Sort**       | O(n log n) / O(n log n) / O(n log n) | O(n)           | Yes    | No       | Stable, works well for linked lists and external sorting. |
| **Quick Sort**       | O(n log n) / O(n log n) / O(n²)    | O(log n)         | No     | Yes      | Fastest in practice for large arrays, but worst case O(n²) unless randomized. |
| **Radix Sort**       | O(nk)                              | O(n + k)         | Yes    | No       | Non-comparative, best for integers/strings, k = key length/range. |
| **Selection Sort**   | O(n²) / O(n²) / O(n²)              | O(1)             | No     | Yes      | Simple but almost always outperformed by insertion sort. |

---

## Algorithm Summaries

### **Bubble Sort**
- **Description:** Repeatedly steps through the list, compares adjacent elements, and swaps them if out of order.
- **Best Use:** Educational purposes, very small or nearly sorted datasets.
- **Pitfalls:** Very slow for large arrays.

### **Bucket Sort**
- **Description:** Distributes elements into buckets, sorts each bucket, then concatenates.
- **Best Use:** Uniformly distributed or floating-point data.
- **Pitfalls:** Not suitable for data with uneven distribution.

### **Counting Sort**
- **Description:** Counts occurrences of each unique element, then calculates positions.
- **Best Use:** Integers or objects with small, known key ranges.
- **Pitfalls:** Large range of elements leads to high memory use.

### **Heap Sort**
- **Description:** Turns array into a heap, repeatedly extracts the max/min.
- **Best Use:** In-place sorting where O(n log n) is required and stability is not.
- **Pitfalls:** Not stable. Slower than quicksort in practice on modern hardware.

### **Insertion Sort**
- **Description:** Builds sorted array one item at a time by inserting in correct position.
- **Best Use:** Small or nearly sorted arrays, online sorting.
- **Pitfalls:** Poor performance on large/random data.

### **Merge Sort**
- **Description:** Recursively divides and merges lists in sorted order.
- **Best Use:** Linked lists, external sorting, stable sorting needed.
- **Pitfalls:** Not in-place (O(n) space).

### **Quick Sort**
- **Description:** Divides and conquers by partitioning around a pivot.
- **Best Use:** General-purpose; fastest for large in-memory arrays.
- **Pitfalls:** Not stable, worst case O(n²) (mitigated by randomization).

### **Radix Sort**
- **Description:** Sorts by processing individual digits.
- **Best Use:** Large lists of integers, strings, or keys with bounded length/range.
- **Pitfalls:** Not comparison-based; not for floating points without tweaks.

### **Selection Sort**
- **Description:** Repeatedly selects the minimum (or maximum) element and moves it to sorted part.
- **Best Use:** Small arrays, educational.
- **Pitfalls:** Inefficient for large data, not stable.

---

## Practical Tips

- **Small or Nearly Sorted Arrays:** Use Insertion Sort.
- **Large, Random Arrays:** Use Quick Sort or Merge Sort (if stability needed).
- **Stable Sort Needed:** Use Merge, Bubble, Counting, or Radix Sort.
- **Limited Memory:** Heap Sort, Insertion, or Selection Sort.
- **Keys are Integers/Fixed Range:** Use Counting or Radix Sort.
- **Linked Lists:** Use Merge Sort.

---

## Useful Links

- [Sorting Algorithms (Visualgo)](https://visualgo.net/en/sorting)
- [GeeksforGeeks: Sorting Algorithms](https://www.geeksforgeeks.org/sorting-algorithms/)
- [Sorting Algorithm Animations](https://www.toptal.com/developers/sorting-algorithms)

---