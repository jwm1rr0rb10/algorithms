# Linear Search

**What it is:**  
Linear Search (also called Sequential Search) is the simplest algorithm for finding an element in a collection. It checks each element in order, one by one, until it finds the target or reaches the end.

---

**How it works:**

1. Start from the first element of the array or list.
2. Compare the current element with the target value.
3. If the element matches the target, return its index (or the element itself).
4. If not, move to the next element.
5. Repeat steps 2–4 until the end of the array is reached.
6. If the target is not found, return a special value (like -1 or None).

---

## Complexity

- **Time Complexity:**  
  - Best case: O(1) (target is at the first position)
  - Average/Worst case: O(n) (may need to scan the entire collection)
- **Space Complexity:**  
  - O(1) (no additional data structures required)

---

## When to Use

- The array or list is **not sorted**.
- The dataset is **small**.
- You need to find **all occurrences** of a value.

## When Not to Use

- The dataset is **large** (inefficient).
- The data is **sorted** (binary search is faster).
- You require **many repeated searches** (other structures like hash tables are better).

---

## Python Example

```python
def linear_search(data, target):
    """
    Returns the index of the first occurrence of target in data,
    or -1 if target is not found.
    """
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1

# Example usage:
numbers = [8, 3, 7, 1, 9, 4]
target1 = 7
target2 = 5

result1 = linear_search(numbers, target1)
print(f"Element {target1} found at index {result1}" if result1 != -1 else f"Element {target1} not found")

result2 = linear_search(numbers, target2)
print(f"Element {target2} found at index {result2}" if result2 != -1 else f"Element {target2} not found")
```

---

## Summary

Linear Search is universal and simple, but slow for large datasets. Use it for unsorted or small collections, or when searching for all matches.