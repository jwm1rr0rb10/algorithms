# Line Segment Intersection: Explanation and Example

## What is the Line Intersection Problem?

The **Line Intersection** problem asks:  
Given two line segments on a 2D plane, determine whether they intersect.  
If they do, find the point of intersection.

---

## Why is it important?

- Used in computer graphics (e.g., rendering, clipping)
- Essential in computational geometry
- Applied in GIS, CAD, robotics, and game development

---

## How does the algorithm work?

### Step 1: Orientation function
- For three points (p, q, r), compute the orientation:
  - 0 → colinear
  - 1 → clockwise
  - 2 → counterclockwise

### Step 2: General case
- Two segments (p1, q1) and (p2, q2) intersect if:
  - orientations of (p1, q1, p2) and (p1, q1, q2) differ
  - and orientations of (p2, q2, p1) and (p2, q2, q1) differ

### Step 3: Special cases (colinear overlap)
- Check if any endpoint lies on the other segment

---

## Python Example

```python
def on_segment(p, q, r):
    return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and \
           min(p[1], r[1]) <= q[1] <= max(p[1], r[1])

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # colinear
    return 1 if val > 0 else 2  # clockwise or counterclockwise

def do_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    # Special cases
    if o1 == 0 and on_segment(p1, p2, q1): return True
    if o2 == 0 and on_segment(p1, q2, q1): return True
    if o3 == 0 and on_segment(p2, p1, q2): return True
    if o4 == 0 and on_segment(p2, q1, q2): return True

    return False

# Example usage
A = (1, 1)
B = (4, 4)
C = (1, 4)
D = (4, 1)
print(do_intersect(A, B, C, D))  # Output: True
```

---

## Complexity
- Time: O(1) per pair of segments
- Space: O(1)

---

## Applications
- Collision detection
- Map overlay in GIS
- Ray casting
- Path planning


--- 

## Summary

- Line segment intersection is a fundamental geometric operation with wide applications. The orientation method is efficient and handles both general and edge cases.

---
