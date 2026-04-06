# Convex Hull (Graham Scan): Explanation and Example

## What is the Convex Hull Problem?

The **Convex Hull** problem asks:  
Given a set of points on a plane, find the smallest convex polygon (the "convex hull") that encloses all the points.

Imagine stretching a rubber band around the outside points — the band forms the convex hull.

---

## What is Graham Scan?

**Graham Scan** is a classic efficient algorithm for finding the convex hull of a set of points in O(n log n) time.

---

## How does the Graham Scan Algorithm work?

**Step 1: Find the starting point**  
- Choose the point with the lowest y-coordinate (if tie, lowest x).

**Step 2: Sort points by polar angle**  
- Sort all points by the angle they and the starting point make with the x-axis.

**Step 3: Traverse the sorted points**  
- Start from the first point.
- For each point, check if moving from the two previous points to this point makes a "left turn" or "right turn".
  - If it's a **right turn** (not part of the convex hull), remove the previous point from the hull.
  - Repeat until the last three points make a "left turn".
- Add the current point to the hull.
- Continue until all points are processed.

---

## Python Example

```python
def graham_scan(points):
    points = sorted(set(points))  # Remove duplicates and sort
    if len(points) <= 1:
        return points

    # Helper: cross product of OA and OB vectors
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    # Concatenate (excluding the last point of each half because it's repeated)
    return lower[:-1] + upper[:-1]

# Example usage
points = [(0,0), (1,1), (2,2), (2,0), (2,4), (3,3), (4,2)]
print(graham_scan(points))
# Output: [(0, 0), (2, 0), (4, 2), (2, 4)]
```

---

## Complexity

- **Time:** O(n log n) (because of sorting)
- **Space:** O(n)

---

## Where is it used?

- Computer vision (object shape detection)
- Robot navigation / collision avoidance
- GIS (geographic information systems)
- Pattern recognition
- Game development (bounding shapes)

---

## When to use Convex Hull?

- When you need the minimal enclosing convex polygon for a point set
- For shape analysis, collision detection, clustering

---

## Real-life Example

Given GPS locations of cell towers, find the minimal area that covers all towers (the convex hull).

---

## Summary

Graham Scan is a fast and reliable algorithm to find the convex hull of a point set, with applications in computer vision, GIS, and robotics.