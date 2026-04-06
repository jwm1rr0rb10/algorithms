# Rotating Calipers (Convex Polygon Diameter): Explanation and Example

## What is the Rotating Calipers Algorithm?

**Rotating Calipers** is a geometric technique used to solve various problems involving convex polygons.  
It works by simulating a pair of calipers (like a compass) rotating around the polygon to find optimal configurations.

---

## What is the Convex Polygon Diameter?

The **diameter** of a convex polygon is the largest distance between any two of its vertices.  
Rotating Calipers can find this in linear time after computing the convex hull.

---

## How does the algorithm work?

### Step 1: Compute the convex hull
- Use Graham Scan or Jarvis March to get the convex polygon.

### Step 2: Initialize antipodal pairs
- For each edge of the convex hull, find the farthest vertex (antipodal point) in the direction perpendicular to the edge.

### Step 3: Rotate calipers
- Simulate rotating a pair of calipers around the polygon.
- For each position, compute the distance between the current pair of points.
- Track the maximum distance found.

---

## Python Example

```python
from math import hypot

def convex_diameter(points):
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

    def convex_hull(points):
        points = sorted(set(points))
        if len(points) <= 1:
            return points
        lower, upper = [], []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        return lower[:-1] + upper[:-1]

    def distance(p1, p2):
        return hypot(p1[0]-p2[0], p1[1]-p2[1])

    hull = convex_hull(points)
    n = len(hull)
    if n == 1:
        return 0
    if n == 2:
        return distance(hull[0], hull[1])

    max_dist = 0
    j = 1
    for i in range(n):
        while True:
            next_j = (j + 1) % n
            if abs(cross(hull[i], hull[(i+1)%n], hull[next_j])) > abs(cross(hull[i], hull[(i+1)%n], hull[j])):
                j = next_j
            else:
                break
        max_dist = max(max_dist, distance(hull[i], hull[j]))
    return max_dist

# Example usage
points = [(0,0), (1,2), (2,1), (4,4), (0,5), (3,0)]
print(convex_diameter(points))  # Output: maximum distance between any two points on the convex hull
```

---

## Complexity
- Time: O(n log n) for convex hull + O(n) for rotating calipers
- Space: O(n)

---

## Applications
- Finding the diameter of a shape
- Minimum bounding rectangle
- Closest pair of convex polygons
- Shape analysis in computer vision

---

## Summary

- Rotating Calipers is a powerful geometric tool for analyzing convex polygons. It extends the utility of convex hulls to solve more advanced spatial problems efficiently.

---