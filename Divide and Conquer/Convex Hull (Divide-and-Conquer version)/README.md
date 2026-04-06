# Convex Hull — Divide and Conquer Algorithm

## Where Convex Hull is Used

The Convex Hull algorithm finds the smallest convex polygon that contains all given points in the plane. It's a classic problem in computational geometry and is widely used in various fields.

**Example applications:**
- Collision detection in robotics and computer graphics
- Pattern recognition and image processing (e.g., object outline detection)
- GIS and mapping (finding boundaries of point clusters)
- Data clustering, outlier detection
- Path planning and navigation

---

## Algorithm Complexity

- **Time Complexity:**  
  O(n log n), where n is the number of points.

- **Space Complexity:**  
  O(n), mainly for sorting and temporary arrays.

---

## Python Example (Divide and Conquer Convex Hull)

> Note: The most common convex hull algorithms are Graham's scan and Andrew's monotone chain (both O(n log n)).  
> The Divide and Conquer convex hull is theoretically the same complexity, but is more advanced and less used in practice.  
> Here is a simple version that recursively divides points and merges hulls.

```python
def cross(o, a, b):
    """Cross product of OA and OB vectors (O — origin)."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def merge(left, right):
    # Merge two convex hulls (left and right) into one. Simplified for clarity.
    points = left + right
    points = sorted(set(points))
    # Use Andrew's monotone chain on the merged set
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    # Concatenate lower and upper to get full hull, removing duplicates
    return lower[:-1] + upper[:-1]

def convex_hull(points):
    n = len(points)
    if n <= 1:
        return points
    if n == 2:
        return points if points[0] != points[1] else [points[0]]
    if n <= 5:
        # For small sets, use brute force (Andrew's monotone chain)
        points = sorted(set(points))
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        return lower[:-1] + upper[:-1]
    # Divide
    points = sorted(points)
    mid = n // 2
    left = convex_hull(points[:mid])
    right = convex_hull(points[mid:])
    # Conquer (merge hulls)
    return merge(left, right)

# Example usage
points = [(0,0), (1,1), (2,2), (2,0), (2,4), (3,3), (0,3), (4,2)]
hull = convex_hull(points)
print("Convex hull:", hull)
```

---

### Code Explanation

- The algorithm recursively divides the set of points into halves.
- For small sets (base cases), it uses a simple convex hull construction (Andrew's chain).
- The `merge` step combines two hulls into one, removing inner points.
- The final result is a list of points forming the convex hull in counter-clockwise order.

---

## Real-Life Examples

1. **Mapping:** Determining the boundary of a set of GPS coordinates (e.g., the outer edge of a city).
2. **Image processing:** Finding the outline of a shape or cluster of points in an image.
3. **Robotics:** Obstacle boundary detection.
4. **Data science:** Outlier detection and clustering visualization.

---

## Useful Links

- [Convex Hull — GeeksforGeeks](https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/)
- [Wikipedia — Convex hull](https://en.wikipedia.org/wiki/Convex_hull)
- [Computational Geometry — MIT OpenCourseWare](https://ocw.mit.edu/courses/6-838-computational-geometry-fall-2002/resources/lecture-5-convex-hulls/)

---

## LeetCode/Practice

| Difficulty | Problem                   | Link                                                                          |
|------------|---------------------------|-------------------------------------------------------------------------------|
| Medium     | Convex Hull               | [LeetCode #587 Erect the Fence](https://leetcode.com/problems/erect-the-fence/) |
| Medium     | Convex Polygon            | [GeeksforGeeks Problem](https://practice.geeksforgeeks.org/problems/convex-hull/1) |

---