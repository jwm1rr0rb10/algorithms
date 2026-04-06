# Binary Tree Traversal: Pre-order

---

## Problem Description

**Pre-order traversal** is a method to visit all nodes of a binary tree in the order:  
**root → left subtree → right subtree**.

Used for copying trees, serialization, building prefix expressions, etc.

---

## Approach (Algorithm)

Recursive:
1. Visit the current node (root).
2. Traverse the left subtree.
3. Traverse the right subtree.

It can also be implemented iteratively using a stack.

---

## Python Example (Recursive and Iterative)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive implementation
def preorder_recursive(root):
    if not root:
        return []
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)

# Iterative implementation
def preorder_iterative(root):
    result, stack = [], []
    if root:
        stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.val)
        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

# Example usage:
# tree = TreeNode(...)
# print(preorder_recursive(tree))
# print(preorder_iterative(tree))
```

---

## Applications

- Tree serialization/deserialization (e.g., in LeetCode).
- Copying a tree.
- Building prefix expressions from expression trees.
- Top-down tree processing.

---

## When to Use

- When "top-down" order is important.
- For building new trees from templates.

---

## When Not to Use

- For traversing graphs with cycles (pre-order is for trees).
- If a different order (in-order, post-order) is needed.

---

## Complexity

- **Time:** O(n), where n is the number of nodes.
- **Space:** O(h), where h is the height of the tree (recursion depth or stack size).

---

## Useful Links

- [LeetCode — Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [Tree traversal — Wikipedia](https://en.wikipedia.org/wiki/Tree_traversal)