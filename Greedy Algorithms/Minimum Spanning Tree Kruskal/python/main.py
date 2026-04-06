class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        self.parent[yr] = xr
        return True

def kruskal(n, edges):
    # edges: list of (weight, u, v)
    edges.sort()
    dsu = DSU(n)
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        if dsu.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

# Example usage
edges = [(1, 0, 1), (4, 0, 2), (3, 1, 2), (2, 1, 3), (5, 2, 3)]
mst, weight = kruskal(4, edges)
print("MST:", mst)
print("Total Weight:", weight)