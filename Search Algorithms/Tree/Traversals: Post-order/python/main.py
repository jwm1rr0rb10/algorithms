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