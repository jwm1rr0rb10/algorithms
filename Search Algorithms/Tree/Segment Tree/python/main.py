class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)
        # Fill leaves
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        # Build the tree
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    # Query sum in [l, r)
    def query(self, l, r):
        res = 0
        l += self.size
        r += self.size
        while l < r:
            if l % 2:
                res += self.tree[l]
                l += 1
            if r % 2:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res

    # Update element at idx to value
    def update(self, idx, value):
        idx += self.size
        self.tree[idx] = value
        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

# Example usage:
arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)
print(st.query(1, 5))  # Sum from 1 to 4: 3+5+7+9 = 24
st.update(3, 10)       # arr[3] = 10
print(st.query(1, 5))  # 3+5+10+9 = 27