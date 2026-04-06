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