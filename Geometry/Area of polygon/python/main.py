def polygon_area(vertices):
    """
    vertices: List of (x, y) tuples, ordered around the polygon.
    """
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2
        area -= y1 * x2
    return abs(area) / 2

# Example usage
polygon = [(0, 0), (4, 0), (4, 3)]
print(polygon_area(polygon))  # Output: 6.0 (area of triangle)