class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)  # 1-based indexing

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i  # move to parent

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i  # move to next ancestor
        return res

    def range_sum(self, l, r):
        return self.query(r) - self.query(l - 1)

# Example usage:
ft = FenwickTree(8)
for idx, val in enumerate([3,2,1,6,5,4,7,8], start=1):
    ft.update(idx, val)

print(ft.range_sum(3, 6))  # Sum from 3 to 6: 1+6+5+4 = 16