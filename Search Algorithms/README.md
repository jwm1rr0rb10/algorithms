# Search Algorithms

## Summary of the Four Key Search Algorithms:

### [Binary Search](https://github.com/jwm1rr0rb/leetcode/tree/main/Search%20Algorithms/Binary%20Search):
* Fast search in sorted arrays/lists.
* Time complexity: O(log n).
* Divides the search space in half each time.

---

### [Ternary Search](https://github.com/jwm1rr0rb/leetcode/tree/main/Search%20Algorithms/Ternary%20Search):
* Similar to binary, but divides into three parts.
* Mainly used for optimization in unimodal functions (functions with a single peak or trough).
* Time complexity: O(log n), but typically slower than binary search for finding a specific element.

---

### [Depth-First Search (DFS)](https://github.com/jwm1rr0rb/leetcode/tree/main/Search%20Algorithms/Depth-First%20Search):
* Explores as deep as possible along each branch before backtracking.
* Uses a stack or recursion.
* Time complexity: O(V + E), where V is the number of vertices and E is Tree Search
Algorithm 	Time Complexity 	Space Complexity
Binary Search Tree Search 	O(h) (O(log n) for balanced) 	O(1)
Deserialize Binary Tree 		O(n)
Fenwick Tree (Binary Indexed Tree) 	O(log n) 	O(n)
Lowest Common Ancestor 		O(n)
Segment Tree 	O(log n) 	O(n)
Serialize Binary Tree 		O(n)
Traversals: In-order 	O(n) 	O(n)
Traversals: Post-order 	O(n) 	O(h)
Traversals: Pre-order 	O(n) 	O(h)
Trie(Prefix Tree) 	O(L) 	O(N*L)the number of edges.

--- 

### [Breadth-First Search (BFS)](https://github.com/jwm1rr0rb/leetcode/tree/main/Search%20Algorithms/Breadth-First%20Search):
* Explores the graph level by level.
* Uses a queue.
* Time complexity: O(V + E).
* Guarantees the shortest path in unweighted graphs.

## Key Differences from DFS:
| Aspect           | BFS                                 | DFS                                           |
|:---------------- |:----------------------------------- |:--------------------------------------------- |
| Data Structure   | Queue                               | Stack (explicit or recursion)                 |
| Traversal Style  | Level-by-level (wide)               | Deep branch exploration                       |
| Typical Use Case | Shortest paths in unweighted graphs | Structure analysis (cycles, components, etc.) |


    e8e46-75a0b75f73-60e3d8b6a4-0feedb1192-59ad9c3974-8e1e8bccf3-6b8a0b4454-6e6e689c30-3b360a510d-6547165353-cb8e1ce0b3-d804088efa-9256f2ff00-bb121ea61a-9722727380-497b7e7aa1-4ee48