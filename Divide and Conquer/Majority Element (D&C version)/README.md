# Majority Element — Divide & Conquer

## Problem description

Given an array of integers, find the element that appears more than ⌊n/2⌋ times (i.e., more than half the length of the array). It is guaranteed that such an element exists.

**Example:**
```python
arr = [2, 2, 1, 1, 1, 2, 2]
# Output: 2 (appears 4 times out of 7)
```

## Algorithm (Divide & Conquer)

Idea: recursively split the array, find the majority element in each half, then combine the results.

### Steps

1. If the array contains only one element, return it.
2. Split the array into two halves.
3. Recursively find the majority for the left and right halves.
4. If both results are the same, return it as the majority.
5. If not, count each candidate's occurrences in the current range and return the one that appears more often.

### Python code example

```python
def majority_element_rec(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    left_major = majority_element_rec(arr, left, mid)
    right_major = majority_element_rec(arr, mid + 1, right)
    if left_major == right_major:
        return left_major
    left_count = sum(1 for i in range(left, right + 1) if arr[i] == left_major)
    right_count = sum(1 for i in range(left, right + 1) if arr[i] == right_major)
    return left_major if left_count > right_count else right_major

def majority_element(arr):
    return majority_element_rec(arr, 0, len(arr) - 1)
    
# Usage example:
arr = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(arr))  # 2
```

## Time complexity

- O(n log n)

## When to use

- When you need to find a majority element in an array.
- For learning divide and conquer techniques.
- In problems that guarantee the existence of a majority.

## Drawbacks

- There is a faster algorithm (Boyer-Moore, O(n)), but D&C is useful for learning and generalization.

---

## Useful links

- [GeeksforGeeks: Majority Element](https://www.geeksforgeeks.org/majority-element/)
- [Wikipedia: Majority element](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)
- [LeetCode Discuss: Majority Element](https://leetcode.com/problems/majority-element/solutions/)

---

## LeetCode Problems

- [169. Majority Element (Easy)](https://leetcode.com/problems/majority-element/)
- [229. Majority Element II (Medium)](https://leetcode.com/problems/majority-element-ii/)

---