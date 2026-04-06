# Closest Pair of Points — Divide and Conquer Algorithm

## Where Closest Pair is Used

The Closest Pair of Points algorithm finds the two points with the smallest Euclidean distance between them in a set of points on a plane. It's a classic computational geometry problem and a well-known interview question.

**Example applications:**
- Geographic data analysis (finding nearest facilities, cell towers, etc.)
- Robotics and collision detection (finding potential object collisions)
- Clustering and data mining (finding dense clusters)
- Computer graphics (optimizing rendering, mesh processing)
- Logistics (locating nearest resources or hubs)

---

## Algorithm Complexity

- **Time Complexity:**  
  O(n log n), where n is the number of points.

- **Space Complexity:**  
  O(n), mainly for sorting and temporary storage.

---

## Python Example

```python
import math

def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def brute_force(points):
    min_dist = float('inf')
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return min_dist, pair

def strip_closest(strip, d_min):
    min_dist = d_min
    pair = None
    n = len(strip)
    strip.sort(key=lambda p: p[1])
    for i in range(n):
        j = i + 1
        while j < n and (strip[j][1] - strip[i][1]) < min_dist:
            d = dist(strip[i], strip[j])
            if d < min_dist:
                min_dist = d
                pair = (strip[i], strip[j])
            j += 1
    return min_dist, pair

def closest_util(px, py):
    n = len(px)
    if n <= 3:
        return brute_force(px)
    mid = n // 2
    Qx = px[:mid]
    Rx = px[mid:]
    midpoint = px[mid][0]
    Qy = list(filter(lambda p: p[0] <= midpoint, py))
    Ry = list(filter(lambda p: p[0] > midpoint, py))

    (dl, pair_left) = closest_util(Qx, Qy)
    (dr, pair_right) = closest_util(Rx, Ry)

    if dl < dr:
        d_min = dl
        pair_min = pair_left
    else:
        d_min = dr
        pair_min = pair_right

    strip = [p for p in py if abs(p[0] - midpoint) < d_min]
    (ds, pair_strip) = strip_closest(strip, d_min)
    if ds < d_min:
        return ds, pair_strip
    else:
        return d_min, pair_min

def closest_pair(points):
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    return closest_util(px, py)

# Example usage
points = [(2,3), (12,30), (40,50), (5,1), (12,10), (3,4)]
min_dist, pair = closest_pair(points)
print("Minimum distance:", min_dist)
print("Closest pair:", pair)
```

---

### Code Explanation

- The algorithm recursively divides the set of points into halves.
- Finds the minimal distance in each half and compares with the minimal distance across the split (the "strip").
- In the strip, only points within `d` distance in the y-direction are checked (at most 7 checks per point).
- Returns the closest pair and their distance.

---

## Real-Life Examples

1. **Mapping and GIS:** Finding which two cities or facilities are closest.
2. **Collision detection:** Robots or vehicles identifying imminent collisions.
3. **Cluster Analysis:** Used in density-based clustering as a primitive operation.
4. **Logistics:** Quickly finding the nearest depot or delivery location.

---

## Useful Links

- [Closest Pair of Points — GeeksforGeeks](https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/)
- [Wikipedia — Closest pair of points problem](https://en.wikipedia.org/wiki/Closest_pair_of_points_problem)
- [Computational Geometry — MIT OpenCourseWare](https://ocw.mit.edu/courses/6-838-computational-geometry-fall-2002/resources/lecture-4-closest-pair-of-points/)

---

## LeetCode/Practice

| Difficulty | Problem                   | Link                                                                          |
|------------|---------------------------|-------------------------------------------------------------------------------|
| Hard       | Closest Pair of Points    | [GeeksforGeeks Problem](https://practice.geeksforgeeks.org/problems/closest-pair-of-points1736/1) |
| Hard       | Minimum Distance Pair     | [LeetCode #532 K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/) |
| Hard       | Number of Boomerangs      | [LeetCode #447 Number of Boomerangs](https://leetcode.com/problems/number-of-boomerangs/)         |

---