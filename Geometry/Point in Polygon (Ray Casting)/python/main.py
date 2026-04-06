def is_point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False

    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i + 1) % n]

        if ((yi > y) != (yj > y)):
            x_intersect = (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi
            if x < x_intersect:
                inside = not inside

    return inside

# Example usage
polygon = [(0,0), (4,0), (4,4), (0,4)]
point1 = (2,2)
point2 = (5,5)
print(is_point_in_polygon(point1, polygon))  # True
print(is_point_in_polygon(point2, polygon))  # False