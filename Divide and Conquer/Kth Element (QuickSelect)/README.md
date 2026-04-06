# Kth Element (QuickSelect) — Divide & Conquer

## Problem description

Given an unsorted array and an integer k, find the k-th smallest element in the array (k is 1-based: 1st = minimum, n-th = maximum).

**Example:**
```python
arr = [7, 10, 4, 3, 20, 15]
k = 3
# Output: 7 (the 3rd smallest element after sorting: [3, 4, 7, 10, 15, 20])
```

## Algorithm (QuickSelect)

- QuickSelect is a modification of QuickSort for finding the k-th smallest element.
- Average-case time complexity is O(n); worst-case is O(n^2) (rare in practice).

### Algorithm steps

1. Choose a pivot element.
2. Partition the array into elements less than and greater than the pivot.
3. If the pivot index is (k-1), the answer is found.
4. If the pivot index is greater, repeat for the left; if less, for the right subarray.

### Python code example

```python
def quickselect(arr, k):
    def partition(left, right):
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i

    def select(left, right, k_smallest):
        if left == right:
            return arr[left]
        pivot_index = partition(left, right)
        if k_smallest == pivot_index:
            return arr[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)

    return select(0, len(arr) - 1, k - 1)

# Usage example:
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(quickselect(arr, k))  # 7
```

## Time complexity

- Average: O(n)
- Worst-case: O(n^2) (can be improved with random pivot selection)

## When to use

- Quick search for the k-th smallest/largest element without full sorting.
- Median, percentile, order statistics problems.
- Large arrays where sorting is too costly.

## Drawbacks

- Worst-case can be slow (use random pivot for mitigation).
- Does not return a sorted array, only the answer.

---

## Useful links

- [GeeksforGeeks: QuickSelect Algorithm](https://www.geeksforgeeks.org/quickselect-algorithm/)
- [Wikipedia: Quickselect](https://en.wikipedia.org/wiki/Quickselect)
- [Order Statistic Algorithms](https://en.wikipedia.org/wiki/Order_statistic)

---

## LeetCode Problems

- [215. Kth Largest Element in an Array (Medium)](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [703. Kth Largest Element in a Stream (Easy/Medium)](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [347. Top K Frequent Elements (Medium)](https://leetcode.com/problems/top-k-frequent-elements/)

---