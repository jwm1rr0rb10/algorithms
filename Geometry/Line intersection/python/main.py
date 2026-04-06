def line_intersection(p1, p2, p3, p4):
    # Line 1: p1 to p2
    A1 = p2[1] - p1[1]
    B1 = p1[0] - p2[0]
    C1 = A1 * p1[0] + B1 * p1[1]

    # Line 2: p3 to p4
    A2 = p4[1] - p3[1]
    B2 = p3[0] - p4[0]
    C2 = A2 * p3[0] + B2 * p3[1]

    # Determinant
    det = A1 * B2 - A2 * B1

    if det == 0:
        return None  # Lines are parallel or coincident

    # Cramer's Rule
    x = (C1 * B2 - C2 * B1) / det
    y = (A1 * C2 - A2 * C1) / det
    return (x, y)

# Example usage
A = (1, 1)
B = (4, 4)
C = (1, 4)
D = (4, 1)
print(line_intersection(A, B, C, D))  # Output: (2.5, 2.5)