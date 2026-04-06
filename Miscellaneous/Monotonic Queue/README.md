# 🔍 Monotonic Queue

## 📌 Problem Description

A **Monotonic Queue** (also known as a "sliding window minimum/maximum deque") is a specialized data structure that maintains elements in a **strictly increasing** or **strictly decreasing** order. It's not a standalone structure, but a pattern that uses a double-ended queue (`deque`) to solve sliding window problems efficiently.

This technique allows **O(1)** access to the minimum or maximum in a sliding window, leading to an overall **O(N)** solution for problems that would otherwise be **O(N·K)** or **O(N·logK)**.

---

## 💡 Idea and Approach

### Core Concepts:

- Use a `deque` to store **indices**, not values.
- Maintain **monotonic order**:
  - Decreasing for **maximum**
  - Increasing for **minimum**
- Proactively remove elements that are no longer useful.

### Monotonic Decreasing Queue (for maximum):

```text
1. Remove elements from the back that are <= current element.
2. Add current element's index to the back.
3. Remove front if it's outside the sliding window.
4. The front always holds the max for the current window.
```
---

## #Monotonic Increasing Queue (for minimum):

```text
1. Remove elements from the back that are >= current element.
2. Add current element's index to the back.
3. Remove front if it's outside the sliding window.
4. The front always holds the min for the current window.
```

## 🧪 Python Example
### Maximum in Sliding Window
```python
from collections import deque

def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []

    dq = deque()
    result = []

    for i in range(len(nums)):
        if dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Examples
print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
print(max_sliding_window([1], 1))                        # [1]
print(max_sliding_window([9, 11], 2))                    # [11]
print(max_sliding_window([7, 2, 4], 2))                  # [7, 4]
```

### Minimum in Sliding Window
```python
def min_sliding_window(nums, k):
    if not nums or k == 0:
        return []

    dq = deque()
    result = []

    for i in range(len(nums)):
        if dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] >= nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Example
print(min_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [-1, -3, -3, -3, 3, 3]
```

## ⏱️ Complexity
|Operation       | Time Complexity | Space Complexity |
|:---------------|:----------------|:-----------------|
|Total Runtime	 | O(N)	           | O(K)             |
|Deque Operations| O(1) per op	   | Up to K elements |

* Each element is added and removed from the deque at most once.

* `deque` ensures constant-time insertions/removals from both ends.

---

## ⚠️ Considerations

* **Store Indices, Not Values**: Easier to check window bounds.
* **Strict vs Non-Strict Monotonicity**: Use `<, <=, > or >=` based on whether duplicates should be kept.
* **Deque Empty Checks**: Always check before accessing `dq[0]`.
* **Result Collection**: Only collect after full window has formed `(i >= k - 1)`.

---

## 🧭 Applications
* **Sliding Window Min/Max:** Most common use case.
* **Next Greater/Smaller Elements:** Related concept using stacks.
* **Dynamic Programming Optimization:** Convert `O(N²)` DP to `O(N)` using Monotonic Queues.
* **Subarray Range Queries:** When conditions rely on min/max.
* **Scheduling & Greedy Algorithms:** Find best candidates efficiently in a changing range.

---

## 🔗 Useful Links

* [**GeeksForGeeks – Sliding Window Maximum**](https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/) 
* [**CP Algorithms – Sliding Window**](https://cp-algorithms.com/data_structures/sliding_window_minimum.html)
* [**LeetCode 239: Sliding Window Maximum**](https://leetcode.com/problems/sliding-window-maximum/)    

---

## 🧩 LeetCode Connection
1. Core Problems:
    * 239. Sliding Window Maximum
    * Offer II 59. Sliding Window Maximum

2. Related Variants:

    * Sum of minimums/maximums of all subarrays

    * K-th min/max in a window

    * Subarray problems with dynamic constraints

Understanding and implementing the Monotonic Queue pattern is crucial for solving high-performance sliding window problems in interviews and contests.
