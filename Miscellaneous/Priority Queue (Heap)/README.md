# 🔍 Priority Queue (Heap)

## 📌 Problem Description

Imagine a queue that isn't just "first-in, first-out" (FIFO), but one where **priority matters**. For example, in an emergency room, a patient with a heart attack is treated before a patient with a broken finger, regardless of who arrived first.

A **Priority Queue** is an abstract data type that maintains a collection of elements, each with an associated priority. Unlike a regular queue, elements are retrieved not in the order they were added, but **in order of their priority**.

The primary operation of a priority queue is to extract the element with the highest (or lowest) priority.

---

## 💡 Idea and Approach

The most common and efficient implementation of a priority queue is using a **heap**. A heap is a specialized tree-based data structure that satisfies the "heap property."

### What is a Heap?

A heap is a **Complete Binary Tree** that satisfies the heap property.

* **Complete Binary Tree:** This is a binary tree in which all levels, except possibly the last, are completely filled, and all nodes on the last level are as far left as possible. This property is crucial because it allows the heap to be efficiently stored in an **array**, without using explicit pointers, saving memory and improving data locality.

* **Heap Property:** Defines the ordering of elements within the tree:

    * **Max-Heap:** For every node `N`, the value of `N` is **greater than or equal to** the values of its child nodes. Consequently, the largest element is always at the root of the heap.

    * **Min-Heap:** For every node `N`, the value of `N` is **less than or equal to** the values of its child nodes. Consequently, the smallest element is always at the root of the heap.

### How does a Heap (and Priority Queue) work?

A heap uses two main operations to maintain its property after insertion or deletion:

1. **"Heapify-Up" (Sift-Up / Bubble-Up):**

    * Used after **inserting** a new element. The new element is added to the first available spot at the end of the array (the last leaf in the tree).

    * If this new element violates the heap property (e.g., in a Min-Heap, the new element is smaller than its parent), it **swaps places with its parent** until the heap property is restored, or until it reaches the root.

2. **"Heapify-Down" (Sift-Down / Bubble-Down):**

    * Used after **removing** an element (typically the root). The root is removed, and its place is taken by the last element in the heap (the last element of the array).

    * If this element violates the heap property (e.g., in a Min-Heap, it's larger than its children), it **swaps places with its smallest (in Min-Heap) or largest (in Max-Heap) child** until the heap property is restored, or until it becomes a leaf.

These "heapify-up" and "heapify-down" operations ensure that the heap always remains balanced (height is $O(logN)$) and the heap property is maintained.

### Array Representation:

Due to the complete binary tree property, a heap can be stored very efficiently in an array. For a node at index `i` (in a 0-indexed array):

* **Left Child:** `2 * i + 1`

* **Right Child:** `2 * i + 2`

* **Parent:** `(i - 1) // 2` (using integer division)

This avoids the need to store pointers, making the implementation simpler and memory more efficient.

---

## 🧪 Python Example (Min-Heap)

In Python, the `heapq` module implements a min-heap algorithm. C++ STL's `priority_queue` is a max-heap by default. Java's `java.util.PriorityQueue` is a min-heap by default.

```Python

import heapq

print("--- Priority Queue (Min-Heap) Example ---")

# Initialize an empty min-heap (a list in Python that heapq functions operate on)
min_heap = []

# 1. Inserting elements (heappush):
# heapq.heappush(heap, item) inserts an item while maintaining the min-heap property
print("Inserting elements:")
heapq.heappush(min_heap, 10) # [10]
print(f"After 10: {min_heap}")

heapq.heappush(min_heap, 30) # [10, 30]
print(f"After 30: {min_heap}")

heapq.heappush(min_heap, 20) # [10, 30, 20] -> Python's internal representation might be slightly different, but the heap property holds
print(f"After 20: {min_heap}")

heapq.heappush(min_heap, 5) # [5, 10, 20, 30] (internally balanced)
print(f"After 5: {min_heap}")

heapq.heappush(min_heap, 25)
print(f"After 25: {min_heap}")

print(f"\nCurrent Min-Heap state (internal representation): {min_heap}")
# Note: the array won't be fully sorted, but the root (index 0) will always be the smallest.

# 2. Extracting the smallest element (heappop):
# heapq.heappop(heap) extracts and returns the smallest item, then re-balances the heap.
print("\nExtracting elements:")
smallest = heapq.heappop(min_heap) # Extracts 5
print(f"Extracted smallest element: {smallest}")
print(f"Heap after extraction: {min_heap}") # [10, 25, 20, 30] (internal representation)

smallest = heapq.heappop(min_heap) # Extracts 10
print(f"Extracted smallest element: {smallest}")
print(f"Heap after extraction: {min_heap}") # [20, 25, 30]

# 3. Peeking at the smallest element (peek/top):
# In Python's heapq, there's no direct peek/top function, but it's always the element at index 0
if min_heap:
    print(f"\nSmallest element (without removal): {min_heap[0]}")
else:
    print("\nHeap is empty.")

# 4. Building a heap from an existing list (heapify):
print("\nBuilding a heap from an existing list:")
my_list = [9, 1, 7, 3, 5]
heapq.heapify(my_list) # Transforms the list into a min-heap "in-place"
print(f"List after heapify: {my_list}") # [1, 3, 7, 9, 5] (internal min-heap representation)

# Extracting from the newly created heap
print(f"Extracted first: {heapq.heappop(my_list)}") # Extracts 1
print(f"Extracted second: {heapq.heappop(my_list)}") # Extracts 3

# Example of Max-Heap (not direct, but can be simulated by storing negative values)
print("\n--- Simulating a Max-Heap (using a Min-Heap) ---")
max_heap_simulated = []

heapq.heappush(max_heap_simulated, -10)
heapq.heappush(max_heap_simulated, -30)
heapq.heappush(max_heap_simulated, -20)
heapq.heappush(max_heap_simulated, -5)

print(f"Simulated Max-Heap (negative values): {max_heap_simulated}")

# Extract the "smallest" negative, which corresponds to the "largest" positive
largest_simulated = -heapq.heappop(max_heap_simulated)
print(f"Extracted largest element (simulated): {largest_simulated}") # 30
print(f"Simulated Max-Heap after extraction: {max_heap_simulated}")
```

---

## ⏱️ Complexity

The main advantage of a heap is its logarithmic time complexity for key operations.

* **Time Complexity (Average & Worst Case):**

    * **Insertion** (`push/add`): $O(logn)$ - due to the "heapify-up" operation, which traverses the height of the tree.

    * **Deletion** (`pop/extract_min/max`): $O(logn)$ - due to the "heapify-down" operation, which also traverses the height of the tree.

    * **Peeking at the highest/lowest element** (`peek/top`): $O(1)$ - the element is always at the root.

    * **Building a heap from an array (heapify):** $O(n)$ - although it seems like each element might take $O(logn)$, the aggregated cost of all "heapify-down" operations during heap construction is $O(n)$.

    * **Changing priority** (`decrease_key/increase_key`): $O(logn)$ - finding the element is $O(n)$ (without an auxiliary hash table), then "heapify-up" or "heapify-down." If we have direct access to the element (e.g., via an index or pointer), it's $O(logn)$.

* **Space Complexity:**

    * $O(n)$
        The heap stores all n elements. If implemented in an array, it is very memory efficient as there's no overhead for pointers like in general tree structures.

---

## ⚠️ Considerations

* **Arbitrary Element Access:** Unlike sorted arrays or lists, direct access to an element by its value or an arbitrary index (other than the root) is not efficient ($O(N)$ in the worst case), as a heap is "partially ordered" rather than fully sorted.

* **Flexibility:** Priority queues are ideal when you only need access to the highest/lowest priority element, not a fully sorted list of all elements.

* **Simulating Max-Heap:** In languages where only Min-Heap is available by default (like Python's `heapq`), a Max-Heap can be easily simulated by inserting elements with an inverted sign (e.g., `-value`) and then inverting the sign upon extraction.

* **Min-Heap vs. Max-Heap Choice:** Depends on whether you need to extract the smallest or largest element as the priority.

---

## 🧭 Applications

Priority queues (and heaps) are fundamental to a multitude of algorithms and systems:

* **Graph Algorithms:**

    * **Dijkstra's Algorithm:** Finding the shortest path from a single source to all other vertices in a graph with non-negative edge weights. A priority queue is used to efficiently select the next vertex with the smallest current distance.

    * **Prim's Algorithm** and **Kruskal's Algorithm:** Finding the minimum spanning tree in a graph. A priority queue helps select edges with the smallest weight.

* **Operating Systems:**

    * **Task/Process Scheduling:** Managing a queue of processes waiting to execute, where higher-priority tasks (e.g., system tasks) are run before lower-priority ones (e.g., background tasks).

    * **Interrupt Handling:** Processing system interrupts based on their priority.

* **Event Simulation:** In discrete-event simulations, events are stored in a priority queue, ordered by their occurrence time, allowing them to be processed in the correct chronological sequence.

* **Data Compression:**

    * **Huffman Coding:** Uses a min-heap to build an optimal prefix code by repeatedly merging the two smallest frequency symbols.

* **Sorting:**

    * **Heapsort:** An efficient sorting algorithm based on the heap data structure, with $O(NlogN)$ complexity.

* **Artificial Intelligence Systems:**

    * **A* Search Algorithm:** A pathfinding algorithm that uses a priority queue to store nodes ordered by their estimated total path cost.

* **Network Equipment:** Managing packet queues in routers, where high-priority traffic (e.g., voice data) needs to be forwarded faster.

* **Finding the Kth Largest/Smallest Element:** Can use a min-heap or max-heap to efficiently find the Kth largest or smallest element in a data stream or a large dataset.

---

## 🔗 Useful Links

* [**GeeksForGeeks - Priority Queue Introduction**](https://www.geeksforgeeks.org/priority-queue-set-1-introduction/) (Excellent introduction)

* [**GeeksForGeeks - Heap Data Structure**](https://www.geeksforgeeks.org/heap-data-structure/) (Detailed on the heap itself)

* [**Wikipedia - Priority Queue**](https://en.wikipedia.org/wiki/Priority_queue)  

* [**Wikipedia - Heap (data structure)**](https://en.wikipedia.org/wiki/Heap_(data_structure))

* [**Python `heapq` module documentation**](https://docs.python.org/3/library/heapq.html)  
     
---

## 🧩 LeetCode Connection

Priority queues and heaps are among the most frequently used data structures in LeetCode and competitive programming. They are indispensable in problems where:

* You constantly need to **extract the highest/lowest priority element.**

* You're dealing with a **stream of data**, and you need to maintain a sorted subset (e.g., the k largest/smallest elements).

* You need to implement algorithms based on **greedy strategies** or **shortest paths/minimum spanning trees.**

* Problems involving **sliding window median, merging K sorted lists, task scheduling**, or topological sort often require priority queues.

* Time constraints ($O(NlogN)$ or $O(logN)$ per operation) often hint at a heap as a suitable solution.

Understanding and effectively using heaps is a key skill for solving a wide range of algorithmic problems.