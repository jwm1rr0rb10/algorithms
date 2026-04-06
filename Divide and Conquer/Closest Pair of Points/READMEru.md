# Closest Pair of Points — Алгоритм «Разделяй и властвуй»

## Где применяется Closest Pair of Points

Алгоритм Closest Pair of Points находит две точки с минимальным евклидовым расстоянием между ними среди множества точек на плоскости. Это классическая задача вычислительной геометрии и частый вопрос на собеседованиях.

**Примеры применения:**
- Геоаналитика (поиск ближайших объектов, вышек, магазинов и т.д.)
- Робототехника и обнаружение коллизий (поиск возможных столкновений)
- Кластеризация и анализ данных (выделение плотных кластеров)
- Компьютерная графика (оптимизация рендеринга, работа с мешами)
- Логистика (поиск ближайших складов, ресурсов и пр.)

---

## Сложность алгоритма

- **Временная сложность:**  
  O(n log n), где n — количество точек.

- **По памяти:**  
  O(n), в основном на сортировку и временные структуры.

---

## Пример на Python

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

# Пример использования
points = [(2,3), (12,30), (40,50), (5,1), (12,10), (3,4)]
min_dist, pair = closest_pair(points)
print("Минимальное расстояние:", min_dist)
print("Пара точек:", pair)
```

---

### Объяснение кода

- Алгоритм рекурсивно делит множество точек на две половины.
- Находит минимум в каждой половине и сравнивает с минимумом через "полосу" (strip).
- В полосе рассматриваются только точки, у которых разница по y меньше d (не более 7 пар на точку).
- В итоге возвращается ближайшая пара и расстояние между ними.

---

## Примеры из жизни

1. **Геоинформационные системы:** Поиск ближайших городов или объектов.
2. **Обнаружение коллизий:** Роботы или автомобили — определение возможных столкновений.
3. **Кластеризация:** Определение плотности распределения, построение кластеров.
4. **Логистика:** Быстрый поиск ближайшего склада или точки доставки.

---

## Полезные ссылки

- [Closest Pair of Points — GeeksforGeeks (на англ.)](https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/)
- [Wikipedia — Closest pair of points problem (на англ.)](https://en.wikipedia.org/wiki/Closest_pair_of_points_problem)
- [Computational Geometry — MIT OCW (на англ.)](https://ocw.mit.edu/courses/6-838-computational-geometry-fall-2002/resources/lecture-4-closest-pair-of-points/)

---

## Задачи для практики

| Сложность | Задача                   | Ссылка                                                                              |
|-----------|--------------------------|-------------------------------------------------------------------------------------|
| Сложная   | Closest Pair of Points   | [GeeksforGeeks задача](https://practice.geeksforgeeks.org/problems/closest-pair-of-points1736/1) |
| Сложная   | Minimum Distance Pair    | [LeetCode #532 K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/) |
| Сложная   | Number of Boomerangs     | [LeetCode #447 Number of Boomerangs](https://leetcode.com/problems/number-of-boomerangs/)         |

---