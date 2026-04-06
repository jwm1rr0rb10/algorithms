from math import hypot

def convex_diameter(points):
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

    def convex_hull(points):
        points = sorted(set(points))
        if len(points) <= 1:
            return points
        lower, upper = [], []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        return lower[:-1] + upper[:-1]

    def distance(p1, p2):
        return hypot(p1[0]-p2[0], p1[1]-p2[1])

    hull = convex_hull(points)
    n = len(hull)
    if n == 1:
        return 0
    if n == 2:
        return distance(hull[0], hull[1])

    max_dist = 0
    j = 1
    for i in range(n):
        while True:
            next_j = (j + 1) % n
            if abs(cross(hull[i], hull[(i+1)%n], hull[next_j])) > abs(cross(hull[i], hull[(i+1)%n], hull[j])):
                j = next_j
            else:
                break
        max_dist = max(max_dist, distance(hull[i], hull[j]))
    return max_dist

# Example usage
points = [(0,0), (1,2), (2,1), (4,4), (0,5), (3,0)]
print(convex_diameter(points))  # Output: maximum distance between any two points on the convex hull