def cross(o, a, b):
    """Cross product of OA and OB vectors (O — origin)."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def merge(left, right):
    # Merge two convex hulls (left and right) into one. Simplified for clarity.
    points = left + right
    points = sorted(set(points))
    # Use Andrew's monotone chain on the merged set
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    # Concatenate lower and upper to get full hull, removing duplicates
    return lower[:-1] + upper[:-1]

def convex_hull(points):
    n = len(points)
    if n <= 1:
        return points
    if n == 2:
        return points if points[0] != points[1] else [points[0]]
    if n <= 5:
        # For small sets, use brute force (Andrew's monotone chain)
        points = sorted(set(points))
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        return lower[:-1] + upper[:-1]
    # Divide
    points = sorted(points)
    mid = n // 2
    left = convex_hull(points[:mid])
    right = convex_hull(points[mid:])
    # Conquer (merge hulls)
    return merge(left, right)

# Example usage
points = [(0,0), (1,1), (2,2), (2,0), (2,4), (3,3), (0,3), (4,2)]
hull = convex_hull(points)
print("Convex hull:", hull)