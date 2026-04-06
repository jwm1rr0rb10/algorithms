# Двунаправленный поиск в ширину (Bidirectional BFS)

## Что это такое?

**Двунаправленный BFS** — это эффективный алгоритм поиска кратчайшего пути между двумя вершинами в невзвешенном графе.  
В отличие от обычного BFS, двунаправленный поиск запускает два одновременных обхода: один от начальной вершины, другой — от целевой.  
Поиск заканчивается, когда два фронта поиска встречаются.

---

## Когда применять

- Когда известны стартовая и целевая вершины.
- Когда граф очень большой, и обычный BFS слишком медленный.
- Полезен в задачах навигации, социальных сетях, играх и там, где требуется быстро найти путь между двумя точками.

---

## Сложность

| Сложность        | Значение                         |
|:----------------:|:--------------------------------:|
| **Время**        | O(b^{d/2})                       |
| **Память**       | O(b^{d/2})                       |

- **b** — средняя степень вершины (число соседей)
- **d** — длина кратчайшего пути

---

## Как работает

- Одновременно запускаем BFS из start и goal.
- Поочерёдно расширяем поиски с каждой стороны.
- Как только фронты пересеклись — восстанавливаем путь.

---

## Пример на Python

```python
from collections import deque

def bidirectional_bfs(graph, start, goal):
    if start == goal:
        return [start]
    
    queue_start = deque([start])
    queue_goal = deque([goal])
    visited_start = {start: None}
    visited_goal = {goal: None}

    while queue_start and queue_goal:
        # Шаг со стороны start
        if queue_start:
            current = queue_start.popleft()
            for neighbor in graph.get(current, []):
                if neighbor not in visited_start:
                    visited_start[neighbor] = current
                    queue_start.append(neighbor)
                    if neighbor in visited_goal:
                        return reconstruct_path(visited_start, visited_goal, neighbor)
        # Шаг со стороны goal
        if queue_goal:
            current = queue_goal.popleft()
            for neighbor in graph.get(current, []):
                if neighbor not in visited_goal:
                    visited_goal[neighbor] = current
                    queue_goal.append(neighbor)
                    if neighbor in visited_start:
                        return reconstruct_path(visited_start, visited_goal, neighbor)
    return None  # Путь не найден

def reconstruct_path(visited_start, visited_goal, meeting_point):
    path = []
    node = meeting_point
    while node is not None:
        path.append(node)
        node = visited_start[node]
    path = path[::-1]
    node = visited_goal[meeting_point]
    while node is not None:
        path.append(node)
        node = visited_goal[node]
    return path

# Пример графа
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

path = bidirectional_bfs(graph, 0, 5)
print("Путь от 0 до 5:", path)
```

---

## Где применяется двунаправленный BFS на практике

1. **Поиск кратчайшего пути между двумя точками на карте (навигация, игры)**

    **Пример:**  
    В навигаторе (Google Maps, Яндекс.Карты) нужно найти кратчайший маршрут от точки А до точки Б.  
    Если карта очень большая, обычный BFS просмотрит огромное число улиц, а двунаправленный будет одновременно искать путь от обоих точек — это ускоряет работу почти вдвое.  
    **В играх:** В стратегиях, где карта большая, и юниту нужно быстро найти путь к цели.

2. **Социальные сети — поиск кратчайшей цепочки между людьми (friend-of-a-friend)**

    **Пример:**  
    На Facebook можно узнать, через каких друзей связаны два пользователя (“6 рукопожатий”).  
    Двунаправленный BFS быстро найдёт кратчайшую цепочку знакомств между двумя людьми.

3. **Сетевые протоколы и роутинг (поиск оптимального маршрута передачи данных)**

    **Пример:**  
    В больших компьютерных сетях (например, в дата-центрах) нужно найти кратчайший путь между двумя серверами для передачи данных.  
    Двунаправленный BFS экономит ресурсы при построении маршрута.

4. **Решение головоломок, лабиринтов, кубика Рубика и т.д.**

    **Пример:**  
    Если есть начальное и целевое состояния (например, позиции в головоломке), можно искать путь от обоих состояний — это существенно ускоряет поиск решения.

5. **Поиск в огромных графах, где полный обход невозможен**

    **Пример:**  
    В рекомендательных системах (“люди, которых вы можете знать”, “фильмы, похожие на этот”) — поиск минимального количества переходов между двумя элементами в огромном графе.

## Полезные ссылки

- [Wikipedia: Двунаправленный поиск](https://ru.wikipedia.org/wiki/Двунаправленный_поиск)
- [GeeksforGeeks: Bidirectional Search (EN)](https://www.geeksforgeeks.org/bidirectional-search/)
- [LeetCode: Shortest Path in Binary Matrix (BFS)](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
