# Area of a Polygon: Explanation and Example

## What is the Area of a Polygon Problem?

The Area of a Polygon problem asks:  
Given the coordinates of the vertices of a simple polygon (not self-intersecting), how do you calculate its area?

---

## How does the Area of a Polygon Algorithm work?

The standard method to solve this is the **Shoelace Formula** (also known as Gauss's area formula).

For a polygon with vertices (x₁, y₁), (x₂, y₂), ..., (xₙ, yₙ) listed in order (clockwise or counterclockwise), the area is:

```
Area = 0.5 * |(x₁y₂ + x₂y₃ + ... + xₙy₁) - (y₁x₂ + y₂x₃ + ... + yₙx₁)|
```

**Step-by-step:**
1. List all vertices in order and repeat the first at the end.
2. Multiply each x-coordinate by the next y-coordinate and add up these products.
3. Multiply each y-coordinate by the next x-coordinate and add up these products.
4. Subtract the second sum from the first.
5. Take the absolute value and divide by 2.

---

## Python Example

```python
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
```

---

## Complexity

- **Time:** O(n), where n is the number of vertices
- **Space:** O(1) (ignoring input storage)

---

## Where is it used?

- Computer graphics and modeling
- Geographic Information Systems (GIS)
- Robotics and navigation
- Image processing

---

## When to use the Shoelace Formula?

- When you know the coordinates of all polygon vertices
- The polygon is simple (not self-intersecting)
- You do not want to break the polygon into triangles

---

## Real-life Example

Suppose you need to calculate the area of a plot of land defined by GPS points. The Shoelace Formula allows you to easily compute the area just by plugging in the coordinates of the corners of the plot.

---

## Summary

The Shoelace Formula is a fast and easy way to compute the area of any simple polygon given the vertex coordinates.