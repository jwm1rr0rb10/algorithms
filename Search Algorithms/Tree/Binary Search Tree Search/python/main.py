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