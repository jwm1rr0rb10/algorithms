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