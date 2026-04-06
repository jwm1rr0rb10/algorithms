# Overview of Two Pointers / Sliding Window Algorithms

## Introduction

Algorithms using the **Two Pointers** and **Sliding Window** techniques are powerful tools for efficiently solving problems on arrays and strings. They allow processing data in linear or nearly linear time, often with minimal extra space.

---

## Quick Comparison of Problems

| Problem                                      | Time      | Space    | Approach                        |
|-----------------------------------------------|-----------|----------|---------------------------------|
| Backspace String Compare                      | O(n)      | O(1)     | Two Pointers                    |
| Container With Most Water                     | O(n)      | O(1)     | Two Pointers                    |
| Find All Anagrams in a String                 | O(n)      | O(1)/O(k) | Sliding Window                  |
| Four Sum                                      | O(n²/n³)  | O(n)     | Two Pointers + Hash             |
| Longest Repeating Character Replacement       | O(n)      | O(1)     | Sliding Window                  |
| Longest Substring Without Repeating Characters| O(n)      | O(n)     | Sliding Window + Set            |
| Maximum Subarray (Kadane’s Algorithm)         | O(n)      | O(1)     | Sliding Window                  |
| Minimum Size Subarray Sum                     | O(n)      | O(1)     | Sliding Window                  |
| Minimum Window Substring                      | O(n)      | O(n)     | Sliding Window + Map            |
| Move Zeroes                                   | O(n)      | O(1)     | Two Pointers                    |
| Remove Duplicates from Sorted Array           | O(n)      | O(1)     | Two Pointers                    |
| Sort Colors (Dutch National Flag)             | O(n)      | O(1)     | Two Pointers                    |
| Three Sum                                     | O(n²/n³)  | O(n)     | Two Pointers + Sort             |
| Trapping Rain Water                           | O(n)      | O(1)     | Two Pointers                    |
| Two Sum                                       | O(n²/n³)  | O(n)     | Hash Map / Two Pointers         |
| **Sliding Window Max Sum (example below)**    | O(n)      | O(1)     | Sliding Window                  |

---

## Sliding Window Example

**Problem:** Find the maximum sum of a subarray of length `k` in an array.

```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

## When and Where to Apply

### Two Pointers

- **Best suited for:**  
  - Problems involving finding pairs/groups with certain properties.
  - Processing sorted arrays (e.g., removing duplicates, sorting, sum problems).
  - Compressing or expanding intervals without brute-forcing all combinations.
  - Problems where minimal extra space is desirable (usually O(1)).

- **Typical examples:**  
  - Container With Most Water, Move Zeroes, Remove Duplicates, Sort Colors, Three/Four Sum, Trapping Rain Water.

- **Limitations:**  
  - Less effective for unsorted arrays unless combined with extra data structures.
  - Sometimes requires sorting first (extra time cost).
  - Not suitable for problems where the order of elements is crucial and you can't move from both ends.

### Sliding Window

- **Best suited for:**  
  - Finding substrings/subarrays with certain properties (max length, sum, number of unique characters, etc.).
  - Problems with a dynamic window: "expand to the right", "shrink from the left" while maintaining invariants.
  - Processing large data with linear time complexity.

- **Typical examples:**  
  - Longest Substring Without Repeating Characters, Minimum Window Substring, Maximum Subarray, Minimum Size Subarray Sum, Find All Anagrams, Sliding Window Max Sum.

- **Limitations:**  
  - Not applicable if the problem can't be reduced to a window of fixed or variable size.
  - For complex window rules (e.g., counting occurrences), needs extra structures (arrays/maps).
  - May require more memory (e.g., to store frequency counts).

---

## When NOT to Use

- If you must brute-force all combinations without any optimization via window or pointers.
- If the data is highly unstructured and it's hard to define invariants for moving the window.
- If the problem requires nested windows or multiple passes over the same data (then DP or greedy is often better).

---

## Approach Limitations

- **Two Pointers** is not always effective if you need to keep extra information about visited elements or if the array/string structure doesn't fit the requirements.
- **Sliding Window** is less effective if you can't maintain fast updates to the window's state (e.g., complex counts or costly recalculations).

---

## General Advice on Choosing an Approach

1. **Analyze problem constraints** — if linear time is needed and there is a "moving window" or "two ends", you can likely apply one of these techniques.
2. **Check if you can decompose the problem into subproblems using a window or pointers** — e.g., finding boundaries where an invariant holds.
3. **Consider sorting the data to enable Two Pointers if appropriate.**
4. **Don’t be afraid to combine approaches:** Sliding Window + Hash Map, Two Pointers + Sort, etc.

---

## Sample Practice Problems

- [LeetCode Two Pointer Problems](https://leetcode.com/tag/two-pointers/)
- [LeetCode Sliding Window Problems](https://leetcode.com/tag/sliding-window/)

---

## Conclusion

Two Pointers and Sliding Window algorithms are powerful for optimizing search and analysis in linear or nearly linear time. Choosing the right approach depends on the problem's properties, data structure, and space/time constraints.