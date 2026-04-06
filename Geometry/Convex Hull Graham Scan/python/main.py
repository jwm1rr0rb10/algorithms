def graham_scan(points):
    points = sorted(set(points))  # Remove duplicates and sort
    if len(points) <= 1:
        return points

    # Helper: cross product of OA and OB vectors
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    # Concatenate (excluding the last point of each half because it's repeated)
    return lower[:-1] + upper[:-1]

# Example usage
points = [(0,0), (1,1), (2,2), (2,0), (2,4), (3,3), (4,2)]
print(graham_scan(points))
# Output: [(0, 0), (2, 0), (4, 2), (2, 4)]