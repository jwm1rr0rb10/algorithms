# 🔍 LRU Cache (Least Recently Used Cache)

## 📌 Problem Description

An LRU (Least Recently Used) Cache is a cache eviction policy that removes the item that has not been used for the longest period of time when the cache is full and a new item needs to be added. The core principle is that if an item was recently used, it is likely to be used again soon. Conversely, if an item hasn't been used for a while, it's a good candidate for eviction.

Implementing an LRU Cache efficiently requires tracking both the keys and their "recency" of access.

---

## 💡 Idea and Approach

The key to an efficient LRU Cache is to combine two data structures:

* A **HashMap** (or `dict` in Python): Maps keys to their corresponding nodes in the list.
* A **Doubly Linked List**: Maintains access order.

### How it Works

* **get(key)**:

  * If key not found, return -1.
  * Otherwise, move the node to the head (most recently used).

* **put(key, value)**:

  * If key exists, update and move to head.
  * If key doesn't exist:

    * If cache is full, remove from tail (least recently used).
    * Insert new node at head.

 ---   

## 🧪 Python Example

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove_node(node)
        self._add_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_head(node)
        else:
            if self.size == self.capacity:
                lru = self.tail.prev
                self._remove_node(lru)
                del self.cache[lru.key]
                self.size -= 1
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            self.size += 1

# --- Example ---
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # 1
lru.put(3, 3)       # Removes 2
print(lru.get(2))  # -1
lru.put(4, 4)       # Removes 1
print(lru.get(1))  # -1
print(lru.get(3))  # 3
print(lru.get(4))  # 4
```

---

## ⏱️ Complexity

* **Time**:

  * `get()`, `put()` — O(1)
* **Space**:

  * O(N), where N = cache capacity

---  

## ⚠️ Considerations

* Dummy head/tail simplify list operations.
* Keys must be immutable/hashable.
* In multithreaded apps, synchronization may be needed.

---

## 🧭 Applications

* CPU cache
* Web browsers
* OS page replacement
* Database caching
* CDN content
* API gateway response caching
* File system block caching

---

## 🔗 Useful Links

* [GeeksForGeeks - LRU Cache](https://www.geeksforgeeks.org/lru-cache-implementation/)
* [LeetCode 146 - LRU Cache](https://leetcode.com/problems/lru-cache/)
* [Wikipedia - Cache Replacement Policies](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_%28LRU%29)
* [Python functools.lru\_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)

---

## 🧩 LeetCode Connection

LeetCode 146 — **LRU Cache** — is a popular and fundamental problem that tests your ability to:

- Combine a **HashMap** with a **Doubly Linked List**.
- Manage **pointers** effectively in linked data structures.
- Meet strict **time complexity** requirements (O(1) for `get()` and `put()`).
- Handle various **edge cases**, such as cache capacity limits and repeated keys.

This is a core design problem every developer should know how to solve.

