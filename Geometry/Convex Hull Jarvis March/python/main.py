def jarvis_march(points):
    if len(points) < 3:
        return points

    hull = []
    leftmost = min(points, key=lambda p: p[0])
    point_on_hull = leftmost

    while True:
        hull.append(point_on_hull)
        endpoint = points[0]
        for p in points[1:]:
            if endpoint == point_on_hull or cross(point_on_hull, endpoint, p) < 0:
                endpoint = p
        point_on_hull = endpoint
        if endpoint == hull[0]:
            break
    return hull

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

# Example usage
points = [(0,0), (1,1), (2,2), (2,0), (2,4), (3,3), (4,2)]
print(jarvis_march(points))
# Output: [(0, 0), (2, 0), (4, 2), (2, 4)]