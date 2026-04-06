# Rectangle Overlap: Explanation and Example

## What is the Rectangle Overlap Problem?

The **Rectangle Overlap** problem asks:  
Given two axis-aligned rectangles, determine whether they **overlap** (i.e., share any area in common).

---

## Why is it important?

- Used in GUI layout engines (e.g., overlapping windows)
- Collision detection in games and simulations
- Bounding box filtering in computer vision
- Spatial indexing and optimization

---

## How does the algorithm work?

Assume each rectangle is defined by its bottom-left and top-right corners:  
- Rectangle A: (x1_min, y1_min), (x1_max, y1_max)  
- Rectangle B: (x2_min, y2_min), (x2_max, y2_max)

### Overlap condition:
Two rectangles **do not overlap** if one is completely to the left, right, above, or below the other.

So, they **overlap** if:


```text
x1_min < x2_max AND x1_max > x2_min AND
y1_min < y2_max AND y1_max > y2_min
```

## Python example 

```python
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
```

---

## Complexity
- Time: O(1)
- Space: O(1)

---

## Applications
- GUI layout and rendering
- Physics engines
- Object detection (bounding boxes)
- Spatial queries in databases

---

## Summary

- Rectangle Overlap is a fast and essential check in many real-time systems. It’s a simple geometric test that enables efficient filtering and collision detection.

---