# Point in Polygon (Ray Casting): Explanation and Example

## What is the Point in Polygon Problem?

The **Point in Polygon (PIP)** problem asks:  
Given a polygon and a point, determine whether the point lies **inside**, **outside**, or **on the edge** of the polygon.

---

## What is Ray Casting?

**Ray Casting** is a classic algorithm to solve the PIP problem.  
It works by drawing a horizontal ray from the point to the right and counting how many times it intersects the polygon's edges.

- If the number of intersections is **odd**, the point is **inside**.
- If **even**, the point is **outside**.

---

## How does the Ray Casting Algorithm work?

**Step 1: Iterate over each edge of the polygon**  
- For each edge, check if the ray from the point crosses it.

**Step 2: Count intersections**  
- Only count edges that cross the ray from left to right.

**Step 3: Determine result**  
- If the count is odd → inside  
- If even → outside

---

## Python Example

```python
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
```

## Complexity
- Time: O(n), where n is the number of polygon vertices
- Space: O(1)

## Applications
- Hit-testing in GUIs and games
- Geographic Information Systems (GIS)
- Collision detection
- Shape analysis

## Summary

- Ray Casting is a simple and effective algorithm to determine whether a point lies inside a polygon. It’s widely used in graphics, simulations, and spatial analysis.

