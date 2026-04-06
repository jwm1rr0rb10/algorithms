# Deserialize Binary Tree

---

## Problem Description

Given a string representation of a binary tree (typically as a level-order list with `null` for missing nodes),  
reconstruct (deserialize) the binary tree.

**Example input:**  
```
[1,2,3,null,null,4,5]
```
This represents the tree:
```
      1
     / \
    2   3
       / \
      4   5
```

---

## Approach (Algorithm)

1. Convert the string to a list of values.
2. Use a queue to rebuild the tree in level order.
3. For each node dequeued, add left and right children if present.

---

## Python Example

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(data):
    if not data or data == "[]":
        return None
    values = data.strip("[]").split(",")
    values = [val.strip() for val in values]
    if values[0] == "null":
        return None

    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        # Left child
        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1
        # Right child
        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1
    return root

# Example usage:
tree = deserialize("[1,2,3,null,null,4,5]")
# Now tree is the root of the reconstructed binary tree
```

---

## Applications

- Reconstructing tree structure from serialized form (for testing, network transmission, storage).
- Frequently used in LeetCode, interviews, and algorithm competitions.

---

## When to Use

- When you need to reconstruct a tree from its string/list (typically BFS/level order) representation.

---

## When Not to Use

- If you need to parse the tree in depth-first (or another custom) format, a different algorithm may be required.

---

## Complexity

- **Time:** O(n), where n is the number of nodes
- **Space:** O(n)

---

## Useful Links

- [LeetCode — Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- [Binary Tree — Wikipedia](https://en.wikipedia.org/wiki/Binary_tree)