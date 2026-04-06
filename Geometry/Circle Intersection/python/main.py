import math

def circle_intersection(x1, y1, r1, x2, y2, r2):
    dx = x2 - x1
    dy = y2 - y1
    d = math.hypot(dx, dy)

    # No intersection
    if d > r1 + r2 or d < abs(r1 - r2):
        return []

    # Touching (one point)
    if d == 0 and r1 == r2:
        return ["Infinite intersection points (identical circles)"]
    
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(max(0, r1**2 - a**2))

    xm = x1 + a * dx / d
    ym = y1 + a * dy / d

    if h == 0:
        return [(xm, ym)]
    else:
        xs1 = xm + h * dy / d
        ys1 = ym - h * dx / d
        xs2 = xm - h * dy / d
        ys2 = ym + h * dx / d
        return [(xs1, ys1), (xs2, ys2)]

# Example usage:
print(circle_intersection(0, 0, 5, 8, 0, 5))  # Output: [(4.0, 3.0), (4.0, -3.0)]