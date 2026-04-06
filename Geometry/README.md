# 📐 Geometry Algorithms Overview

Geometry algorithms are essential for solving problems involving shapes, distances, intersections, and spatial relationships. These algorithms are widely used in computational geometry, computer graphics, robotics, GIS, and collision detection systems.

This section summarizes key geometry algorithms, their time and space complexities, and guidance on when and how to apply them effectively.

---

## 📊 Algorithm Complexity Table

| Algorithm                                | Time Complexity | Space Complexity |
|:------------------------------------------|:------------------|:------------------|
| Area of Polygon                          | O(n)             | O(1)             |
| Circle Intersection                      | O(1)             | O(1)             |
| Closest Pair of Points                   | O(n log n)       | O(n)             |
| Convex Hull (Graham Scan)                | O(n log n)       | O(n)             |
| Convex Hull (Jarvis March)               | O(nh)            | O(1)             |
| Line Intersection                        | O(1)             | O(1)             |
| Line Segment Intersection                | O(1)             | O(1)             |
| Point in Polygon (Ray Casting)           | O(n)             | O(1)             |
| Rectangle Intersection                   | O(1)             | O(1)             |
| Rectangle Overlap                        | O(1)             | O(1)             |
| Rotating Calipers (Convex Polygon Diameter) | O(n)          | O(1)             |

---

## 🧭 When to Use These Algorithms

- **Collision Detection**:  
  Use Rectangle Overlap, Line Segment Intersection, and Circle Intersection in physics engines, UI layout, and robotics.

- **Shape Analysis**:  
  Area of Polygon, Convex Hull, and Rotating Calipers are useful in computer vision, pattern recognition, and robotics.

- **Geospatial Systems**:  
  Point in Polygon and Closest Pair of Points are foundational in GIS, mapping, and spatial indexing.

- **Optimization & Planning**:  
  Convex Hull and Rotating Calipers help in route planning, bounding box minimization, and shape fitting.

---

## ⚠️ Where to Be Cautious

- Convex Hull (Jarvis March) can degrade to O(n²) when the number of hull points h ≈ n.
- Closest Pair of Points requires careful divide-and-conquer implementation to maintain O(n log n) time.
- Ray Casting assumes a simple polygon and may fail with self-intersections unless handled explicitly.
- Floating-point precision errors can affect intersection and orientation tests — use robust geometric predicates when needed.

---

## 🛠️ Practical Tips

- Preprocess input: remove duplicate points and sort if needed (e.g., for Convex Hull).
- Cache convex hulls for static objects to avoid recomputation.
- Combine with spatial data structures (e.g., Quadtrees, KD-Trees) for large-scale or real-time applications.
- Use integer coordinates when possible to avoid floating-point instability.

---

## 📚 Further Reading

- [Computational Geometry Algorithms Library (CGAL)](https://www.cgal.org/)
- [Geometry Problems on LeetCode](https://leetcode.com/tag/geometry/)
- [Real-Time Collision Detection by Christer Ericson](https://www.amazon.com/Real-Time-Collision-Detection-Interactive-Technology/dp/1558607323)

---

## ✅ Conclusion

Geometry algorithms are compact, efficient, and foundational for spatial reasoning. Mastering them enables you to build systems that understand and interact with the physical world — from autonomous vehicles to 3D engines and beyond.
