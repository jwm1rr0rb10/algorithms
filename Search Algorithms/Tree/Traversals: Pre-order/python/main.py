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