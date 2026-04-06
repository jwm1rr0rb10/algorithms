# Convex Hull — Алгоритм «Разделяй и властвуй»

## Где применяется Convex Hull

Алгоритм Convex Hull (выпуклая оболочка) находит наименьший выпуклый многоугольник, содержащий все заданные точки на плоскости. Это классическая задача вычислительной геометрии, широко используемая в различных сферах.

**Примеры применения:**
- Компьютерная графика и робототехника (поиск границ, детектирование коллизий)
- Анализ данных и кластеризация (поиск выбросов, визуализация)
- Картография и ГИС (поиск границ городов, кластеров объектов)
- Обработка изображений (обводка объектов)
- Маршрутизация и планирование движения

---

## Сложность алгоритма

- **Временная сложность:**  
  O(n log n), где n — количество точек.

- **По памяти:**  
  O(n), в основном на сортировки и временные структуры.

---

## Пример на Python (Divide and Conquer Convex Hull)

> Примечание: На практике чаще используют алгоритмы Грэхема или монотонную цепь Эндрю (оба O(n log n)), но вариант «разделяй и властвуй» теоретически столь же быстрый и интересен для глубокого понимания темы.

```python
def cross(o, a, b):
    """Векторное произведение OA и OB (O — начало координат)."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def merge(left, right):
    # Объединение двух выпуклых оболочек (left и right) в одну
    points = left + right
    points = sorted(set(points))
    # Монотонная цепь Эндрю на объединённом множестве
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

def convex_hull(points):
    n = len(points)
    if n <= 1:
        return points
    if n == 2:
        return points if points[0] != points[1] else [points[0]]
    if n <= 5:
        # Для малых наборов — простое построение выпуклой оболочки
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
    # Разделяем
    points = sorted(points)
    mid = n // 2
    left = convex_hull(points[:mid])
    right = convex_hull(points[mid:])
    # Объединяем
    return merge(left, right)

# Пример использования
points = [(0,0), (1,1), (2,2), (2,0), (2,4), (3,3), (0,3), (4,2)]
hull = convex_hull(points)
print("Выпуклая оболочка:", hull)
```

---

### Объяснение кода

- Алгоритм рекурсивно делит множество точек пополам.
- Для малых наборов строит оболочку простым алгоритмом (монотонная цепь).
- В функции merge объединяет две выпуклые оболочки в одну.
- В результате — список точек выпуклой оболочки в порядке обхода.

---

## Примеры из жизни

1. **Картография:** Определение границы кластера GPS-точек (например, город).
2. **Обработка изображений:** Поиск контура объекта или кластера на плоскости.
3. **Робототехника:** Выделение области препятствий.
4. **Анализ данных:** Выделение выбросов, визуализация.

---

## Полезные ссылки

- [Convex Hull — GeeksforGeeks (на англ.)](https://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/)
- [Wikipedia — Convex hull (на англ.)](https://en.wikipedia.org/wiki/Convex_hull)
- [Computational Geometry — MIT OCW (на англ.)](https://ocw.mit.edu/courses/6-838-computational-geometry-fall-2002/resources/lecture-5-convex-hulls/)

---

## Задачи для практики

| Сложность | Задача                   | Ссылка                                                                              |
|-----------|--------------------------|-------------------------------------------------------------------------------------|
| Средняя   | Convex Hull              | [LeetCode #587 Erect the Fence](https://leetcode.com/problems/erect-the-fence/)     |
| Средняя   | Convex Polygon           | [GeeksforGeeks задача](https://practice.geeksforgeeks.org/problems/convex-hull/1)   |

---