# 📐 Line Intersection: Explanation and Example

## What is the Line Intersection Problem?

The **Line Intersection** problem asks:  
Given two infinite lines in a 2D plane, determine whether they intersect.  
If they do, compute the exact point of intersection.

Unlike line segments, lines extend infinitely in both directions, so intersection is always defined unless the lines are parallel or coincident.

---

## 📌 Why is it Important?

- Used in ray tracing, rendering, and geometric modeling  
- Fundamental in analytical geometry and linear algebra  
- Applied in robotics, physics engines, and CAD systems

---

## ⚙️ How Does the Algorithm Work?

### Step 1: Represent Lines in General Form

Each line is defined by two points:  
- Line 1: (x₁, y₁) to (x₂, y₂)  
- Line 2: (x₃, y₃) to (x₄, y₄)

Convert each line to the form:  
**Ax + By = C**

### Step 2: Solve the System of Equations

Use the determinant method (Cramer’s Rule) to solve:

- `A1 * x + B1 * y = C1 A2 * x + B2 * y = C2`


- If the determinant is zero → lines are parallel or coincident  
- Otherwise → compute the intersection point (x, y)

---

## 🧪 Python Example

```python
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
```

---

## ⏱️ Complexity
- Time: O(1)
- Space: O(1)

---

## 🧭 Applications
- Ray tracing and rendering
- Analytical geometry
- Intersection of roads, paths, or trajectories
- Solving systems of linear equations

---

## ✅ Summary
- Line intersection computes the exact point where two infinite lines cross.
- It uses the general form of a line and Cramer’s Rule to solve the system.
- It does not check whether the intersection lies within any segment — it assumes lines are infinite.

---
