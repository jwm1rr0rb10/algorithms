# Lowest Common Ancestor (LCA)

---

## Problem Description

**Lowest Common Ancestor (LCA)** of two nodes in a tree is the deepest node that is an ancestor of both nodes.

Task: Given the root of a tree and two nodes, find their LCA.

---

## Approaches

### 1. Recursive Approach for a Binary Tree

Works for any binary tree (not just BST):

- If the current node matches either node, return it.
- Recursively search for LCA in the left and right subtrees.
- If both subtrees return non-None results, the current node is the LCA.

### Python Example

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right

# Usage:
# p and q are pointers to nodes in the tree (not just values!)
```

---

## Advanced Methods

- For many LCA queries, use preprocessing: binary lifting, RMQ on Euler tour.
- For BST, can use value comparisons to speed up search.

---

## Applications

- Hierarchies, genealogies, file systems, segment tree queries.
- Used in graph/tree algorithms for path and distance queries.

---

## When to Use

- When you need to efficiently find LCAs for node pairs in a tree.

---

## When Not to Use

- Not for graphs with cycles (only trees).
- For many queries, use an O(n) preprocessing method.

---

## Complexity

- **Time:** O(n) per query in general tree, O(log n) with preprocessing.
- **Space:** O(n)

---

## Useful Links

- [LeetCode — Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- [LCA — Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor)