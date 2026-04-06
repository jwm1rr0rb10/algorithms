# Rectangle Intersection: Explanation and Example

## What is the Rectangle Intersection Problem?

The **Rectangle Intersection** problem asks:  
Given two axis-aligned rectangles on a 2D plane, determine whether they intersect.  
Optionally, compute the rectangle of their intersection.

---

## Why is it important?

- Used in GUI layout engines  
- Collision detection in games and simulations  
- Bounding box analysis in computer vision  
- Spatial indexing in databases and GIS

---

## How does the algorithm work?

Assume each rectangle is defined by its bottom-left and top-right corners:  
- Rectangle A: (x1_min, y1_min), (x1_max, y1_max)  
- Rectangle B: (x2_min, y2_min), (x2_max, y2_max)

### Step 1: Check for overlap
- Rectangles intersect if:
  - `x1_min < x2_max` and `x1_max > x2_min`
  - `y1_min < y2_max` and `y1_max > y2_min`

### Step 2: Compute intersection rectangle (optional)
- If they intersect, the overlapping rectangle is:
  - `x_overlap = max(x1_min, x2_min), min(x1_max, x2_max)`
  - `y_overlap = max(y1_min, y2_min), min(y1_max, y2_max)`

---

## Python Example

```python
def rectangles_intersect(a, b):
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b

    if ax1 >= bx2 or bx1 >= ax2:
        return False
    if ay1 >= by2 or by1 >= ay2:
        return False
    return True

def intersection_rectangle(a, b):
    if not rectangles_intersect(a, b):
        return None
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    return (
        max(ax1, bx1),
        max(ay1, by1),
        min(ax2, bx2),
        min(ay2, by2)
    )

# Example usage
rect1 = (1, 1, 5, 5)
rect2 = (3, 3, 6, 6)
print(rectangles_intersect(rect1, rect2))  # True
print(intersection_rectangle(rect1, rect2))  # (3, 3, 5, 5)
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

- Rectangle intersection is a fast and essential geometric operation. It’s used in many real-time systems where performance and accuracy are critical.

---