# 🔍 Ordered Map/Set (TreeMap/TreeSet)

## 📌 Problem Description

**Ordered Map** (often called `TreeMap` in Java, or `std::map` in C++, or `SortedDict` in some Python libraries like `sortedcontainers`) and **Ordered Set** (`TreeSet` in Java, `std::set` in C++, or `SortedList` in `sortedcontainers`) are data structures that store key-value pairs (for maps) or unique elements (for sets) while maintaining their elements in **sorted order based on the keys (or elements themselves).**

Unlike `HashMap` / `HashSet`, which provide average $O(1)$ lookup but no inherent order, Ordered Maps/Sets guarantee that elements are always iterated in a sorted sequence. This ordered property comes at the cost of slightly higher time complexity for insertions, deletions, and lookups compared to hash-based structures.

---

## 💡 Idea and Approach

The core idea behind Ordered Maps and Sets is that they are typically implemented using **self-balancing binary search trees (BSTs)**. Common types of self-balancing BSTs include:

* **Red-Black Trees:** A popular choice (used by Java's `TreeMap/TreeSet`, C++'s `std::map/std::set`). They ensure that the tree remains balanced (height is `O(logn)`) by applying rotations and color changes during insertions and deletions, guaranteeing logarithmic time complexity for operations.

* **AVL Trees:** Another type of self-balancing BST, known for being strictly balanced.

* **Treaps:** A randomized data structure that combines properties of binary search trees and heaps.

Regardless of the specific self-balancing BST, the fundamental principles are:

1. **Binary Search Tree Property:** For any node, all keys in its left subtree are less than its key, and all keys in its right subtree are greater than its key.

2. **Self-Balancing Property:** After any insertion or deletion, the tree automatically performs operations (rotations, recoloring) to maintain a balanced structure, preventing the tree from degenerating into a linked list (which would lead to O(n) worst-case time complexity).

3. **In-order Traversal:** An in-order traversal of a BST always visits the nodes in sorted order of their keys. This property is what allows Ordered Maps/Sets to provide sorted iteration.

## Key Operations:

* `put(key, value)` / `add(element)`: Inserts a new key-value pair (or element) while maintaining sorted order and balance.

* `get(key)` / `contains(element)`: Retrieves the value associated with a key (or checks for element presence) by traversing the tree based on key comparisons.

* `remove(key)` / `remove(element)`: Deletes a key-value pair (or element) while maintaining order and balance.

* `first_key()` / `last_key()`: Get the smallest/largest key in the map/set.

* `lower_bound(key)` / `upper_bound(key)`: Find the smallest key greater than/equal to (or strictly greater than) a given key. (C++ `std::map` features)

* `floor_key(key)` / `ceiling_key(key)`: Find the largest key less than/equal to (or smallest key greater than/equal to) a given key. (Java `TreeMap` features)

* `iterate()`: Traverse elements in sorted order.

---

## 🧪 Python Example

Python's built-in `dict` and `set` are hash-based and do not maintain insertion order (for `dict` before Python 3.7, after 3.7 insertion order is preserved but it's still hash-based). For truly sorted maps and sets (based on key values, not insertion order), you typically rely on external libraries or implement a BST yourself.

The `sortedcontainers` library is a popular choice in Python for this functionality.

```python
# You might need to install it: pip install sortedcontainers
from sortedcontainers import SortedDict, SortedList

print("--- Ordered Map (SortedDict) Example ---")
my_map = SortedDict()

# 1. Insertion
my_map[5] = "apple"
my_map[2] = "banana"
my_map[8] = "cherry"
my_map[1] = "date"
my_map[5] = "grape" # Updates value for key 5

print(f"Map after insertions (sorted by key): {my_map}")
# Output will show elements sorted by key: SortedDict({1: 'date', 2: 'banana', 5: 'grape', 8: 'cherry'})

# 2. Lookup
print(f"Value for key 2: {my_map.get(2, 'Not Found')}") # Output: banana
print(f"Value for key 7: {my_map.get(7, 'Not Found')}") # Output: Not Found

# 3. Check for key existence
print(f"Is key 8 in map? {8 in my_map}") # Output: True

# 4. Deletion
del my_map[2]
print(f"Map after deleting key 2: {my_map}")
# Output: SortedDict({1: 'date', 5: 'grape', 8: 'cherry'})

# 5. Iteration (always sorted by key)
print("Iterating through map keys:")
for key in my_map:
    print(f"Key: {key}, Value: {my_map[key]}")

# 6. Ordered specific operations (example with SortedDict)
print(f"Smallest key: {my_map.keys()[0]}")   # Or my_map.peekitem(0)[0]
print(f"Largest key: {my_map.keys()[-1]}")   # Or my_map.peekitem(-1)[0]
print(f"Keys less than or equal to 5: {my_map.bisect_right(5)}") # Returns index where 5 could be inserted to maintain order (first index > 5)
                                                                 # Correct usage for range: my_map.irange(None, 5)

print("\n--- Ordered Set (SortedList) Example ---")
my_set = SortedList()

# 1. Insertion (adding unique elements, sorted)
my_set.add(50)
my_set.add(20)
my_set.add(80)
my_set.add(10)
my_set.add(50) # Duplicates are ignored

print(f"Set after additions (sorted): {my_set}")
# Output: SortedList([10, 20, 50, 80])

# 2. Check for element existence
print(f"Is 20 in set? {20 in my_set}") # Output: True
print(f"Is 70 in set? {70 in my_set}") # Output: False

# 3. Deletion
my_set.remove(20)
print(f"Set after removing 20: {my_set}")
# Output: SortedList([10, 50, 80])

# 4. Iteration (always sorted)
print("Iterating through set elements:")
for item in my_set:
    print(item)

# 5. Ordered specific operations (example with SortedList)
print(f"Smallest element: {my_set[0]}")
print(f"Largest element: {my_set[-1]}")
print(f"Count of 50: {my_set.count(50)}")
print(f"Index of 50: {my_set.index(50)}")
```

---

## ⏱️ Complexity

The time complexity for Ordered Maps/Sets, when implemented with self-balancing BSTs, is logarithmic.

    Time Complexity (Average & Worst Case):

        Insertion (put/add): O(logn)

        Deletion (remove): O(logn)

        Lookup (get/contains): O(logn)

        Finding min/max (first/last): O(logn) (or O(1) if the implementation keeps direct pointers to min/max nodes, which is common).

        Range queries/Iteration: O(k+logn), where k is the number of elements in the range. The logn is for finding the start of the range, and k for traversing the elements.

    Space Complexity:

        O(n)
        The data structure needs to store all n key-value pairs (or elements). Each node in the tree typically requires more memory than an entry in a hash table due to pointers (left, right, parent, color).

⚠️ Considerations

* **Performance Trade-offs:** Ordered Maps/Sets offer guaranteed sorted order and O(logn) worst-case performance, which is better than `HashMap`'s $O(n)$ worst-case. However, their O(logn) average-case is typically slower than `HashMap`'s $O(1)$ average-case due to the overhead of tree traversals and balancing operations. Choose based on whether sorted order or raw speed for isolated operations is more critical.

* **Key/Element Comparability:** Keys (or elements) must be comparable (implement `__lt__` or similar in Python) so that the tree can correctly order them.

* **Memory Overhead:** Nodes in a tree-based structure often consume more memory than entries in a hash table due to the need for pointers to children and possibly parent nodes, as well as balance-related metadata.

* **Range Queries:** One of the strongest advantages of ordered maps/sets is their ability to perform efficient range queries (e.g., "find all items between key X and key Y"), which is not efficiently possible with hash-based structures.

---

## 🧭 Applications

Ordered Maps and Sets are indispensable when the order of elements or efficient range-based queries are crucial.

* Databases (Indexing): B-trees (a generalization of BSTs) are commonly used for database indexing, allowing for efficient sorted retrieval and range queries on large datasets.

* **Scheduling/Event Management:** Storing events or tasks ordered by time or priority.

* **Custom Sorting:** Maintaining a collection of items that always need to be presented or accessed in a sorted manner.

* **Finding Closest Elements:** Efficiently finding the element immediately greater or smaller than a given value.

* **Range Queries:** Any scenario where you need to retrieve all items within a specific range of keys/values (e.g., "find all users whose score is between 100 and 200").

* **Implementing Other Data Structures:** They can be used as building blocks for more complex data structures.

* **Autocompletion/Dictionary Lookups:** Can be efficient for partial matches or prefix-based searches.

* **Order Statistics (K-th smallest/largest):** While not direct, a balanced BST can be augmented to find the K-th smallest/largest element efficiently.

---

## 🔗 Useful Links

* [**GeeksForGeeks - TreeMap in Java**](https://www.geeksforgeeks.org/treemap-in-java/) (Good conceptual overview, even if not Python specific)

* [**GeeksForGeeks - TreeSet in Java**](https://www.geeksforgeeks.org/java/treeset-in-java/)

* [**Wikipedia - Self-balancing binary search tree**](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree)

* [**Python sortedcontainers library documentation**](https://grantjenks.com/docs/sortedcontainers/sorteddict.html) (If using Python)

---

## 🧩 LeetCode Connection

Ordered Maps and Sets, or the underlying concept of balanced BSTs, are frequently encountered in LeetCode problems, particularly when:

* You need to maintain data in sorted order.

* You need to find elements that are "just greater than" or "just less than" a given value (`ceiling, floor`).

* You need to perform efficient range queries.

* The problem constraints involve `log n` complexity, suggesting tree-based solutions.

* You are asked to implement a data structure that needs to maintain order (e.g., a custom data stream where elements are processed in order).

* Problems like "Skyline Problem," "Count of Smaller Numbers After Self," or "Data Stream as Disjoint Intervals" might be solved using `TreeMap` or `TreeSet` (or similar structures like segment trees/Fenwick trees for some).

* When a simple `heap` (priority queue) doesn't offer enough flexibility (e.g., you need to remove arbitrary elements, not just the min/max, while maintaining order).

While Python's standard library doesn't have a direct `TreeMap/TreeSet`, understanding their principles is crucial for solving many algorithmic problems efficiently, and you might use them in other languages or rely on `sortedcontainers` for competitive programming in Python.

---

