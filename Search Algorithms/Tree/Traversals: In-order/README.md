# Binary Tree Traversal: In-order

---

## Problem Description

**In-order traversal** is a method to visit all nodes of a binary tree in the order:  
**left subtree → root → right subtree**.

For a Binary Search Tree (BST), in-order traversal returns elements in sorted order.

---

## Approach (Algorithm)

Recursive:
1. Traverse the left subtree.
2. Visit the current node (root).
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
def inorder_recursive(root):
    if not root:
        return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)

# Iterative implementation
def inorder_iterative(root):
    result, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result

# Example usage:
# tree = TreeNode(...)
# print(inorder_recursive(tree))  # [sorted list for BST]
# print(inorder_iterative(tree))
```

---

## Applications

- Getting a sorted list from a BST.
- Copying a tree, finding the k-th smallest element, or other tree traversal tasks.
- Building expressions from arithmetic expression trees.

---

## When to Use

- When you need to process all nodes in a specific order.
- To obtain a sorted result from a BST.

---

## When Not to Use

- For traversing graphs with cycles (in-order is for trees only).
- If you need a different order (pre-order, post-order).

---

## Complexity

- **Time:** O(n), where n is the number of nodes.
- **Space:** O(h), where h is the height of the tree (recursion depth or stack size).

---

## Useful Links

- [LeetCode — Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [Tree traversal — Wikipedia](https://en.wikipedia.org/wiki/Tree_traversal)