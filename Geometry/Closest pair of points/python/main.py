import math

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def closest_pair(points):
    points = sorted(points)
    def rec(pts):
        n = len(pts)
        if n <= 3:
            return min((distance(pts[i], pts[j]), (pts[i], pts[j])) for i in range(n) for j in range(i+1, n))
        mid = n // 2
        xmid = pts[mid][0]
        left = pts[:mid]
        right = pts[mid:]
        d1, pair1 = rec(left)
        d2, pair2 = rec(right)
        d, pair = (d1, pair1) if d1 < d2 else (d2, pair2)
        strip = [p for p in pts if abs(p[0] - xmid) < d]
        strip.sort(key=lambda p: p[1])
        for i in range(len(strip)):
            for j in range(i+1, min(i+7, len(strip))):
                d_strip = distance(strip[i], strip[j])
                if d_strip < d:
                    d, pair = d_strip, (strip[i], strip[j])
        return d, pair
    return rec(points)

# Example usage
points = [(0,0), (2,2), (3,1), (5,5), (1,1)]
print(closest_pair(points))  # Output: (1.4142..., ((0,0), (1,1)))