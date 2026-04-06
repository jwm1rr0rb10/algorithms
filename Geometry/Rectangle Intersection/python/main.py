def rectangles_intersect(a, b):
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b

    if ax1 >= bx2 or bx1 >= ax2:
        return False
    if ay1 >= by2 or by1 >= ay2:
        return False
    return True

def intersection_rectangle(a, b):
    if not rectangles_intersect(a, b):
        return None
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    return (
        max(ax1, bx1),
        max(ay1, by1),
        min(ax2, bx2),
        min(ay2, by2)
    )

# Example usage
rect1 = (1, 1, 5, 5)
rect2 = (3, 3, 6, 6)
print(rectangles_intersect(rect1, rect2))  # True
print(intersection_rectangle(rect1, rect2))  # (3, 3, 5, 5)