# Circle Intersection: Explanation and Example

## What is the Circle Intersection Problem?

The Circle Intersection problem asks:  
Given two circles (each defined by a center point and radius), do they intersect? If so, where?  
You may be asked to:
- Check if circles intersect (touch or overlap)
- Find the intersection points (if any)

---

## How does the Circle Intersection Algorithm work?

Given two circles:
- Circle 1: center (x₁, y₁), radius r₁
- Circle 2: center (x₂, y₂), radius r₂

**Step 1: Calculate Distance Between Centers**
```
d = sqrt((x₂ - x₁)² + (y₂ - y₁)²)
```

**Step 2: Check Intersection Cases**
- **No intersection:** d > r₁ + r₂ (circles are too far apart)
- **One point (touches externally):** d == r₁ + r₂
- **Two points (overlap):** |r₁ - r₂| < d < r₁ + r₂
- **One inside another (no intersection):** d < |r₁ - r₂|
- **Identical circles:** infinite intersection points

**Step 3: Compute Intersection Points (if they exist)**

If circles intersect in one or two points:

Let:
- a = (r₁² - r₂² + d²) / (2d)
- h = sqrt(r₁² - a²)

Then, the intersection points are:
```
P₀ = (x₁ + a*(x₂ - x₁)/d, y₁ + a*(y₂ - y₁)/d)

Intersection points:
(x₃, y₃) = (P₀ₓ ± h*(y₂ - y₁)/d, P₀ᵧ ∓ h*(x₂ - x₁)/d)
```
(“±” gives both intersection points, if two exist.)

---

## Python Example

```python
import math

def circle_intersection(x1, y1, r1, x2, y2, r2):
    dx = x2 - x1
    dy = y2 - y1
    d = math.hypot(dx, dy)

    # No intersection
    if d > r1 + r2 or d < abs(r1 - r2):
        return []

    # Touching (one point)
    if d == 0 and r1 == r2:
        return ["Infinite intersection points (identical circles)"]
    
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(max(0, r1**2 - a**2))

    xm = x1 + a * dx / d
    ym = y1 + a * dy / d

    if h == 0:
        return [(xm, ym)]
    else:
        xs1 = xm + h * dy / d
        ys1 = ym - h * dx / d
        xs2 = xm - h * dy / d
        ys2 = ym + h * dx / d
        return [(xs1, ys1), (xs2, ys2)]

# Example usage:
print(circle_intersection(0, 0, 5, 8, 0, 5))  # Output: [(4.0, 3.0), (4.0, -3.0)]
```

---

## Complexity

- **Time:** O(1)
- **Space:** O(1)

---

## Where is it used?

- Detecting collisions in games and simulations
- Analyzing molecular overlaps in chemistry/biology
- Robotics (obstacle avoidance)
- Computer graphics (clipping, Venn diagrams)

---

## When to use Circle Intersection?

- When you need to check if two circular objects touch or overlap
- When you need the exact intersection points for further processing

---

## Real-life Example

Suppose you have two WiFi routers with a certain range (circle). You want to know if their coverage areas overlap, and if so, where you could place a device to connect to both networks.

---

## Summary

Circle intersection is a fundamental geometry problem with applications in collision detection, graphics, and spatial analysis.