# 🔍 Deque (Double-ended Queue)

## 📌 Problem Description

A Deque (Double-ended Queue) is a linear data structure that generalizes a queue, allowing elements to be added or removed from either the front or the back. Unlike a standard queue (FIFO), where elements are added to the end and removed from the front, and a stack (LIFO), where elements are added and removed from the top, a deque supports operations at both ends.

## 💡 Idea and Approach

The main idea of a deque is to provide **O(1)** time complexity for adding and removing elements from **both ends**. This can be achieved through:

* **Doubly Linked List**: Each node stores references to both the previous and next nodes, allowing quick insertion and deletion at both ends.
* **Circular Array (Dynamic Array with wrapped indices)**: Uses a fixed-size array where indices wrap around. On overflow, the array is resized.

### Key Operations:

* `append()` / `push_back()`: Add to the back.
* `appendleft()` / `push_front()`: Add to the front.
* `pop()` / `pop_back()`: Remove and return from the back.
* `popleft()` / `pop_front()`: Remove and return from the front.
* `peek()` / `front()` / `back()`: Access (without removing) the front or back element.
* `is_empty()`: Check if deque is empty.
* `size()`: Number of elements.

## 🧪 Python Example

```python
from collections import deque

print("--- Deque (Double-ended Queue) Example ---")

# 1. Initialization
my_deque = deque()

# 2. Adding Elements
my_deque.append(10)
my_deque.append(20)
my_deque.appendleft(5)
my_deque.appendleft(1)

print(f"Deque after additions: {my_deque}")
print(f"Size: {len(my_deque)}")

# 3. Access without removing
print(f"First element: {my_deque[0]}")
print(f"Last element: {my_deque[-1]}")

# 4. Removing Elements
removed_right = my_deque.pop()
print(f"Removed from right: {removed_right}, Deque: {my_deque}")

removed_left = my_deque.popleft()
print(f"Removed from left: {removed_left}, Deque: {my_deque}")

# 5. Check if empty
print(f"Is deque empty? {not my_deque}")

# 6. Extend with multiple elements
my_deque.extend([30, 40])
my_deque.extendleft([-1, 0])
print(f"After extend: {my_deque}")

# 7. Rotate
my_deque.rotate(1)
print(f"After rotating right: {my_deque}")

my_deque.rotate(-2)
print(f"After rotating left: {my_deque}")

# 8. Clear
my_deque.clear()
print(f"After clearing: {my_deque}")
```

## ⏱️ Complexity

For efficient implementations like `collections.deque`:

* `append()`, `appendleft()`: `O(1)`
* `pop()`, `popleft()`: `O(1)`
* Access by index (`deque[i]`): `O(n)` (in Python: `O(k)` where `k` is distance from closest end)
* `len()`: `O(1)`
* `rotate(k)`: `O(k)`

**Space Complexity**: `O(n)`

## ⚠️ Considerations

* **Random Access**: Less efficient than lists. Best for frequent front/back operations.
* **Memory**: Unlike arrays, deque (with linked list) may not store data contiguously.
* **Structure Choice**:

  * Frequent insert/remove at both ends → Deque
  * Only one end → Stack/Queue
  * Frequent index access → list/array

## 🧭 Applications

* **Sliding Windows**: Max/min in subarrays.
* **Stack/Queue Simulation**: Fast front/back operations.
* **BFS Variants**: Use `appendleft` in 0-1 BFS.
* **Undo/Redo History**
* **Monotonic Queues/Stacks**: Maintain ordered data efficiently.
* **Browser History Navigation**
* **Work-stealing in Parallel Processing**

## 🔗 Useful Links

* [Python Docs — collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)
* [GeeksForGeeks — Deque](https://www.geeksforgeeks.org/deque-set-1-introduction-applications/)
* [Wikipedia — Deque](https://en.wikipedia.org/wiki/Double-ended_queue)

## 🧩 LeetCode Connection

Deque is a powerful tool for solving medium and hard problems:

* **Sliding Window Maximum** (239)
* **Modified BFS**: `appendleft`
* **Monotonic Stack/Queue**: Next greater/smaller
* **Recent Calls/Bounded Queues**
* **Browser History Simulation**

Deque often allows **O(n)** solutions where naive methods are **O(n²)**.
