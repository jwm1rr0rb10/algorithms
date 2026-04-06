def is_rectangle_overlap(a, b):
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b

    return ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1

# Example usage
rect1 = (1, 1, 4, 4)
rect2 = (2, 2, 5, 5)
rect3 = (5, 5, 7, 7)

print(is_rectangle_overlap(rect1, rect2))  # True
print(is_rectangle_overlap(rect1, rect3))  # False