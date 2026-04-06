# Binary Search Tree Search

## What is a Binary Search Tree (BST)?

A **Binary Search Tree (BST)** is a type of binary tree where, for every node:
- All values in the left subtree are **less than** the node’s value.
- All values in the right subtree are **greater than** the node’s value.
- This property holds recursively for all descendants.

Example BST:
```
      8
     / \
    3   10
   / \    \
  1   6    14
     / \   /
    4   7 13
```

---

## How BST Search Works

BST search uses the tree's ordering property to find a value efficiently:

1. **Start at the root node.**
2. If the current node’s value equals the target — you found it.
3. If the target value is **less** than the current node’s value, search the left subtree.
4. If the target value is **greater**, search the right subtree.
5. Repeat steps 2–4 until you find the value or reach a null pointer (the value is not present).

---

## Time and Space Complexity

- **Time Complexity:**
    - **Best/Average (balanced tree):** O(log n)
    - **Worst case (degenerated tree):** O(n)
- **Space Complexity:**
    - Iterative search: O(1)
    - Recursive search: O(h), where h is the tree height

---

## When to Use

- Data is dynamic (frequent insertions, deletions, searches)
- You want to maintain sorted order and support efficient range queries

## When Not to Use

- The tree is unbalanced (can degrade to a linked list, losing efficiency)
- If you only need fast search, and no dynamic updates, sorted arrays with binary search may be better

---

## Python Example

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bst_search(root, target):
    current = root
    while current:
        if current.val == target:
            return current
        elif target < current.val:
            current = current.left
        else:
            current = current.right
    return None

# Example usage
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

result = bst_search(root, 6)
print("Found!" if result else "Not found.")
```

---

## Summary

BST search is an efficient way to find elements in a dynamic, sorted structure—**as long as the tree remains balanced**. For optimal performance, consider using self-balancing BSTs (like AVL or Red-Black trees).