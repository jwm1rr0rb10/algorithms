# Binary Tree Traversal: Post-order

---

## Problem Description

**Post-order traversal** is a method to visit all nodes of a binary tree in the order:  
**left subtree → right subtree → root**.

Used for deleting trees, evaluating expressions, and various bottom-up tree algorithms.

---

## Approach (Algorithm)

Recursive:
1. Traverse the left subtree.
2. Traverse the right subtree.
3. Visit the current node (root).

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
def postorder_recursive(root):
    if not root:
        return []
    return postorder_recursive(root.left) + postorder_recursive(root.right) + [root.val]

# Iterative implementation
def postorder_iterative(root):
    result, stack = [], []
    last_visited = None
    curr = root
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            peek = stack[-1]
            # If right child exists and hasn't been visited
            if peek.right and last_visited != peek.right:
                curr = peek.right
            else:
                result.append(peek.val)
                last_visited = stack.pop()
    return result

# Example usage:
# tree = TreeNode(...)
# print(postorder_recursive(tree))
# print(postorder_iterative(tree))
```

---

## Applications

- Deleting/freeing memory of a tree.
- Evaluating arithmetic or logic expressions (expression trees).
- Building Reverse Polish Notation (RPN).
- Any bottom-up tree processing.

---

## When to Use

- When processing/evaluating/deleting must go bottom-up.
- For working with arithmetic/logic expression trees.

---

## When Not to Use

- For traversing graphs with cycles (post-order is for trees).
- If another traversal order (in-order, pre-order) is needed.

---

## Complexity

- **Time:** O(n), where n is the number of nodes.
- **Space:** O(h), where h is the height of the tree (recursion depth or stack size).

---

## Useful Links

- [LeetCode — Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
- [Tree traversal — Wikipedia](https://en.wikipedia.org/wiki/Tree_traversal)