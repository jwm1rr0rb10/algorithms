# 🔍 Hashing (HashMap / HashSet Usage)

## 📌 Problem Description

Hashing is a fundamental concept in computer science that involves mapping data of arbitrary size to a fixed-size value, typically an integer, called a hash code or hash value. This hash code is then used to quickly locate or store data.

HashMap (also known as a hash table or dictionary) and HashSet are data structures that implement the hashing concept to provide highly efficient average-case performance for common operations like insertion, deletion, and lookup.

- **HashMap**: Stores key-value pairs. Given a key, it allows for very fast retrieval of its associated value. Keys must be unique, but values can be duplicated.
- **HashSet**: Stores unique elements. It's essentially a HashMap where only the keys are stored, and the values are typically dummy objects. It's used to quickly check for the presence of an element.

---

## 💡 Idea and Approach

The core idea behind HashMaps and HashSets is to use a hash function to transform a key (or element) into an index in an underlying array (often called a "bucket array" or "table").

---

### How It Works

1. **Hash Function**: Computes an integer hash code from a key. A good hash function distributes keys uniformly to minimize collisions.
2. **Index Calculation**: The hash code is usually moduloed by the array size to determine the target bucket.
3. **Collision Resolution**:
   - **Separate Chaining**: Each bucket holds a list or tree of items.
   - **Open Addressing**: Uses probing (e.g., linear, quadratic) to find an empty slot.

When retrieving a value (or checking for presence), the same hash function and index calculation are used.

---

## 🧪 Python Example

```python
# --- HashMap (Python Dictionary) Example ---
print("--- HashMap Example ---")
my_map = {}

my_map["apple"] = 10
my_map["banana"] = 20
my_map["cherry"] = 30
my_map["date"] = 10  # Duplicate value

print(f"Map after insertions: {my_map}")

print(f"Value for 'banana': {my_map['banana']}")
print(f"Value for 'apple': {my_map.get('apple', 'Not Found')}")
print(f"Value for 'grape': {my_map.get('grape', 'Not Found')}")

print(f"'cherry' in map: {'cherry' in my_map}")
print(f"'fig' in map: {'fig' in my_map}")

del my_map["banana"]
print(f"Map after deleting 'banana': {my_map}")

for key in my_map:
    print(f"Key: {key}, Value: {my_map[key]}")

for key, value in my_map.items():
    print(f"Key: {key}, Value: {value}")

# --- HashSet (Python Set) Example ---
print("\n--- HashSet Example ---")
my_set = set()

my_set.add("red")
my_set.add("green")
my_set.add("blue")
my_set.add("red")  # Duplicate ignored

print(f"Set after additions: {my_set}")

print(f"'green' in set: {'green' in my_set}")
print(f"'yellow' in set: {'yellow' in my_set}")

my_set.remove("blue")
print(f"Set after removing 'blue': {my_set}")

my_set.discard("yellow")
print(f"Set after discarding 'yellow': {my_set}")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Union: {set1.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")
print(f"Difference: {set1.difference(set2)}")
print(f"Symmetric Difference: {set1.symmetric_difference(set2)}")

print("Iterating through set elements:")
for item in my_set:
    print(item)
```

---

## ⏱️ Complexity

### Time Complexity (Average Case):

- Insertion: `O(1)`
- Deletion: `O(1)`
- Lookup: `O(1)`

### Time Complexity (Worst Case):

- All operations: `O(n)`

### Space Complexity:

- `O(n)` for storing `n` elements.

---

## ⚠️ Considerations

- **Mutable Keys**: Only immutable types (int, str, tuple) are hashable in Python.
- **Hash Function**: Should be fast and uniformly distributed.
- **Load Factor**: A high load factor can degrade performance, triggering resizing and rehashing.
- **Worst Case**: Be aware of `O(n)` worst-case scenarios due to hash collisions.

---

## 🧭 Applications

- **Databases**: Indexing
- **Caching**: LRU Cache
- **Compilers**: Symbol Tables
- **Duplicate Detection**
- **Frequency Counting**
- **Graph Traversal**
- **Cryptography**: Hash-based structures
- **Routing Tables**

---

## 🔗 Useful Links

- [Wikipedia - Hash Table](https://en.wikipedia.org/wiki/Hash_table)
- [GeeksForGeeks - Hashing](https://www.geeksforgeeks.org/hashing-data-structure/)
- [Python Docs - dict](https://docs.python.org/3/library/stdtypes.html#dict)
- [Python Docs - set](https://docs.python.org/3/library/stdtypes.html#set)

---

## 🧩 LeetCode Connection

HashMaps and HashSets are extremely common in LeetCode problems:

- **Two Sum / Pair Sum**
- **Frequency Counting**
- **Duplicate Detection**
- **Longest Unique Substring**
- **LRU Cache**
- **Group Anagrams**
- **Subarray Sum / Prefix Sum**
- **Intersection / Union Problems**

---

They are efficient tools to solve problems requiring fast membership checks, counting, grouping, and mapping.
