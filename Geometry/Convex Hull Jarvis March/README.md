# Convex Hull (Jarvis March): Explanation and Example

## What is the Convex Hull Problem?

The **Convex Hull** problem asks:  
Given a set of points on a plane, find the smallest convex polygon that encloses all the points.

Imagine stretching a rubber band around the outermost points — the band forms the convex hull.

---

## What is Jarvis March?

**Jarvis March** (also known as the "Gift Wrapping" algorithm) is a simple algorithm to compute the convex hull in **O(nh)** time, where:
- *n* — number of input points
- *h* — number of points on the convex hull

---

## How does the Jarvis March Algorithm work?

**Step 1: Start from the leftmost point**  
- This point is guaranteed to be on the convex hull.

**Step 2: Wrap around the set**  
- From the current point, choose the point that is the most counterclockwise relative to all others.
- Repeat until you return to the starting point.

---

## Python Example

```python
def jarvis_march(points):
    if len(points) < 3:
        return points

    hull = []
    leftmost = min(points, key=lambda p: p[0])
    point_on_hull = leftmost

    while True:
        hull.append(point_on_hull)
        endpoint = points[0]
        for p in points[1:]:
            if endpoint == point_on_hull or cross(point_on_hull, endpoint, p) < 0:
                endpoint = p
        point_on_hull = endpoint
        if endpoint == hull[0]:
            break
    return hull

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

# Example usage
points = [(0,0), (1,1), (2,2), (2,0), (2,4), (3,3), (4,2)]
print(jarvis_march(points))
# Output: [(0, 0), (2, 0), (4, 2), (2, 4)]
```

---

## Complexity

- Time: O(nh) — good for small h
- Space: O(h)

---

## Where is it used?

- Computer graphics
- Pattern recognition
- Robotics
- GIS systems
- Collision detection

---

## When to use Jarvis March?
- When the number of hull points (h) is small
- When simplicity is more important than speed
- For educational or illustrative purposes

--- 

## Real-life Example

- Given GPS coordinates of weather stations, find the minimal convex area that encloses them.

---

## Summary

- Jarvis March is a simple and intuitive algorithm for computing the convex hull. Though not the fastest, it’s easy to implement and understand — perfect for small datasets or teaching purposes.

---