# Search Algorithms Summary

This summary covers key search algorithms, their time and space complexities, best use cases, and limitations.

---

## Comparison Table

| Algorithm                                                                                                   | Time Complexity         | Space Complexity | When to Use                                                                                                       | Limitations / When Not to Use                        |
|-------------------------------------------------------------------------------------------------------------|------------------------|------------------|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| [**Linear Search**](https://github.com/jwm1rr0rb/leetcode/tree/main/Search%20Algorithms/Search/Linear%20Search)                    | O(n)                   | O(1)             | Unsorted/small lists, or when random access is not possible                                                       | Inefficient for large/ordered data                   |
| [**Binary Search**](https://github.com/jwm1rr0rb/leetcode/tree/main/Search%20Algorithms/Search/Binary%20Search)        | O(log n)               | O(1)             | Sorted arrays with fast random access                                                                             | Not for unsorted data, linked lists                  |
| [**Ternary Search**](https://github.com/jwm1rr0rb/leetcode/tree/main/Search%20Algorithms/Search/Ternary%20Search)           | O(log₃ n)              | O(1)             | Rare; unimodal functions, specialized cases                                                                       | Usually not faster than binary search                |
| [**Jump Search**](https://github.com/jwm1rr0rb/leetcode/tree/main/Search%20Algorithms/Search/Jump%20Search)                      | O(√n)                  | O(1)             | Sorted arrays; when jumping saves time over linear search                                                          | Not ideal for random access or unsorted data         |
| [**Exponential Search**](https://github.com/jwm1rr0rb/leetcode/tree/main/Search%20Algorithms/Search/Exponential%20Search)               | O(log i)               | O(1)             | Very large or unbounded sorted arrays, or when target is near the start                                            | Only for sorted data with cheap random access        |
| [**Binary Search Tree Search**](https://github.com/jwm1rr0rb/leetcode/tree/main/Search%20Algorithms/Search/Binary%20Search%20Tree%20Search)        | O(h) (O(log n) balanced) | O(1)          | Dynamic sorted data with frequent insertion/deletion                                                              | Tree must be balanced; poor for degenerate trees     |
| [**Search in Rotated Sorted Array**](https://github.com/jwm1rr0rb/leetcode/tree/main/Search%20Algorithms/Search/Search%20in%20Rotated%20Sorted%20Array)   | O(log n)               | O(1)             | Rotated sorted arrays (interview problems)                                                                        | Rare in practice; not for unsorted or unrotated data |
| [**Search in 2D Matrix**](https://github.com/jwm1rr0rb/leetcode/tree/main/Search%20Algorithms/Search/Search%20in%202D%20Matrix)              | O(m + n) or O(log(mn)) | O(1)             | Special 2D matrices where each row is sorted and next row starts above previous row's max                         | Not for arbitrary or unsorted matrices               |

---

## Key Takeaways

- **Linear Search** is universal but slow for large datasets. Use only when data is unsorted or small.
- **Binary Search** is fast and efficient on sorted arrays and is a must-know. It does not work on unsorted data.
- **Ternary Search** is a rarely-used variant for unimodal functions, very niche.
- **Jump Search** offers a compromise between linear and binary search for sorted arrays, but is rarely used in real-world work.
- **Exponential Search** shines when the data is sorted and the target is likely near the start, or in streams/unbounded arrays.
- **BST Search** is essential for dynamic datasets that need to stay sorted, but only if the tree is balanced.
- **Search in Rotated Sorted Array** is mainly an interview problem; practical uses are rare.
- **Search in 2D Matrix** is applicable only for matrices with special sorting properties.

---

## When **Not** to Use

- If data is unsorted and you need frequent search: **prefer hash tables (O(1))**.
- If you require frequent insertions and deletions in a sorted container: use self-balancing BSTs or skip lists.
- If the structure doesn't allow random access (e.g., linked list), avoid binary, jump, exponential, and similar searches.
- For very large/range queries, consider interval trees or advanced data structures.

---

## Typical Bottlenecks

- **Unsorted data:** All search methods except linear search fail or are suboptimal.
- **Unbalanced BST:** Search degrades to O(n).
- **Large datasets:** Linear and jump searches become slow.
- **Poor data structure choice:** Using a search algorithm that doesn't fit the structure (e.g., binary search on a linked list).

---

## Summary

Choose the search algorithm based on:
- **Data ordering** (sorted/unsorted)
- **Data structure** (array, tree, matrix, etc.)
- **Operation needs** (static data, dynamic updates)
- **Performance requirements** (speed, memory)

For most practical applications, binary search and hash-based lookups are the most useful. The more exotic algorithms (ternary, exponential, rotated, 2D matrix search) are great for interviews, algorithm study, and niche problems.