# DP on Trees: Maximum Sum of Independent Set

## Problem Description

Given a tree (an undirected acyclic connected graph) with `n` nodes, each node contains an integer value.  
Find the maximum sum by choosing a subset of nodes such that no two chosen nodes are directly connected (no two chosen nodes share an edge).

---

## Idea and Approach

- For each node, compute two values:
    - `take`: the maximum sum if we include this node (then we **cannot** take its immediate children)
    - `not_take`: the maximum sum if we do **not** include this node (then for each child we can take or not take, whichever is better)
- Traverse the tree using DFS (Depth-First Search) starting from the root.

---

## Python Example

```python
from collections import defaultdict

def max_independent_set_sum(n, edges, values):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    def dfs(node, parent):
        take = values[node]
        not_take = 0
        for child in tree[node]:
            if child == parent:
                continue
            child_take, child_not_take = dfs(child, node)
            take += child_not_take
            not_take += max(child_take, child_not_take)
        return take, not_take

    return max(dfs(0, -1))
```

### Example Usage

```python
n = 5
edges = [(0,1), (0,2), (1,3), (1,4)]
values = [1, 2, 3, 4, 5]
print(max_independent_set_sum(n, edges, values))  # Output: 12 (choose nodes 0, 3, 4)
```

---

## Complexity

- **Time:** O(n)
- **Space:** O(n)

---

## Where it's used

- Optimal placement of sensors, cameras, or resources in networks where adjacent locations can't be picked together.
- Bioinformatics, planning, game theory.

---

## Useful Links

- [CP-algorithms — DP on Trees](https://cp-algorithms.com/graph/dp_tree.html)
- [LeetCode 337. House Robber III (binary tree variant)](https://leetcode.com/problems/house-robber-iii/)