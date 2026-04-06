# Count Inversions — Divide & Conquer

## Problem description

Given an array of integers, count the number of inversions in the array.

**An inversion** is a pair of indices (i, j) such that i < j and arr[i] > arr[j].

**Example:**
```python
arr = [2, 4, 1, 3, 5]
# Inversions: (2,1), (4,1), (4,3)
# Output: 3
```

## Algorithm (Divide & Conquer)

- Based on a modified merge sort algorithm.
- While merging two sorted halves, count cases where a left element is greater than a right element — these are inversions.

### Python code example

```python
def merge_and_count(arr, left, mid, right):
    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]
    i = j = 0
    k = left
    inv_count = 0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
            inv_count += (len(left_part) - i)
        k += 1

    arr[k:right+1] = left_part[i:] + right_part[j:]
    return inv_count

def count_inversions(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += count_inversions(arr, left, mid)
        inv_count += count_inversions(arr, mid+1, right)
        inv_count += merge_and_count(arr, left, mid, right)
    return inv_count

# Usage example:
arr = [2, 4, 1, 3, 5]
print(count_inversions(arr, 0, len(arr)-1))  # 3
```

## Time complexity

- O(n log n)

## When to use

- To analyze the “disorder” or “unsortedness” of an array.
- In sorting theory, permutation complexity analysis.
- Applications in bioinformatics, information theory, social network analysis.

## Drawbacks

- Needs extra memory for temporary arrays.
- For small arrays, brute-force may be simpler and faster.

---

## Useful links

- [GeeksforGeeks: Count Inversions in an array](https://www.geeksforgeeks.org/counting-inversions/)
- [Wikipedia: Inversion (permutation)](https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics))

---

## LeetCode Problems

- [315. Count of Smaller Numbers After Self (Hard, variant)](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
- [327. Count of Range Sum (Hard, variant)](https://leetcode.com/problems/count-of-range-sum/)
- [493. Reverse Pairs (Hard, variant)](https://leetcode.com/problems/reverse-pairs/)

---