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

n = 5
edges = [(0,1), (0,2), (1,3), (1,4)]
values = [1, 2, 3, 4, 5]
print(max_independent_set_sum(n, edges, values))  # Output: 12 (choose nodes 0, 3, 4)