class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        self.parent[yr] = xr
        return True

def kruskal(n, edges):
    """
    n: number of vertices (vertices are 0...n-1)
    edges: list of (weight, u, v)
    Returns: list of edges in the MST, total weight
    """
    edges.sort()
    dsu = DSU(n)
    mst = []
    total_weight = 0

    for w, u, v in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == n - 1:
                break

    return mst, total_weight

# Example usage
edges = [
    (1, 0, 1),
    (3, 0, 2),
    (2, 1, 2),
    (4, 1, 3),
    (5, 2, 3),
]
n = 4
mst, total = kruskal(n, edges)
print("Edges in MST:", mst)
print("Total weight:", total)