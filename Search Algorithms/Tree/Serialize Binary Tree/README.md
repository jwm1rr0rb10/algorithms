# Serialize Binary Tree

---

## Problem Description

**Serialize a binary tree** — convert its structure into a string or array so it can be saved or transmitted (e.g., over a network).  
Most commonly, level order (BFS) format is used, inserting `null` for missing children.

---

## Approach (Algorithm)

1. Use breadth-first search (BFS, with a queue).
2. For each visited node:
   - If the node is not `None`, save its value and enqueue its children.
   - If the node is `None`, save `null` in the result.
3. Optionally, remove trailing `null` values from the end.

---

## Python Example

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root:
        return "[]"
    queue = deque([root])
    res = []
    while queue:
        node = queue.popleft()
        if node:
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append("null")
    # Remove trailing nulls (optional)
    while res and res[-1] == "null":
        res.pop()
    return "[" + ",".join(res) + "]"

# Example usage:
# tree = TreeNode(...)
# print(serialize(tree))  # e.g., "[1,2,3,null,null,4,5]"
```

---

## Applications

- Saving/transmitting tree structure between programs, over network, or in tests.
- Often paired with deserialization for verifying tree algorithms.

---

## When to Use

- When you need to save/transmit a tree as a string or array.
- For LeetCode, interview, and algorithm problems.

---

## When Not to Use

- For very large trees (may be memory-inefficient).
- If only values (not structure) are needed.

---

## Complexity

- **Time:** O(n), where n is the number of nodes
- **Space:** O(n)

---

## Useful Links

- [LeetCode — Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- [Binary tree — Wikipedia](https://en.wikipedia.org/wiki/Binary_tree)