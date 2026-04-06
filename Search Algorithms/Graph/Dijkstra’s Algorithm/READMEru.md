# Алгоритм Дейкстры (Dijkstra’s Algorithm)

## Что это такое?

**Алгоритм Дейкстры** — классический алгоритм поиска кратчайших путей от одной вершины ко всем остальным в графе с неотрицательными весами рёбер. Очень популярен в задачах маршрутизации, навигации и оптимизации.

---

## Как работает?

1. **Инициализация:**  
   - Расстояние до старта — 0, до остальных вершин — бесконечность.
   - Все вершины считаются необработанными.
   - Используется приоритетная очередь (например, min-heap), чтобы быстро выбирать вершину с минимальным текущим расстоянием.

2. **Главный цикл:**  
   - Пока есть необработанные вершины:
     - Выбираем вершину с минимальным расстоянием.
     - Для каждого соседа:
       - Если путь через эту вершину короче, обновляем расстояние до соседа.
     - Помечаем вершину как обработанную.

3. **Завершение:**  
   - Когда все вершины обработаны, получаем кратчайшие расстояния от источника до всех вершин.
   - Можно восстановить маршруты, если сохранять "предков" (предыдущие вершины).

---

## Особенности

- **Не работает** с отрицательными весами рёбер.
- Эффективен при использовании кучи (min-heap).
- Позволяет находить не только длины путей, но и сами маршруты.

---

## Сложность

| Сложность        | Значение                    |
|:----------------:|:--------------------------:|
| **Время**        | O((V + E) log V)           |
| **Память**       | O(V)                       |

- **V** — количество вершин  
- **E** — количество рёбер

---

## Применение

- Навигаторы и маршрутизация на картах (например, Google Maps, Яндекс.Карты).
- Сетевые протоколы маршрутизации (OSPF, IS-IS).
- Поиск пути для ИИ в играх.
- Оптимизация логистики и цепочек поставок.
- Городское планирование (кратчайшие пути по дорогам).

---

## Пример на Python

```python
import heapq

def dijkstra(graph, start):
    """
    graph: dict, список смежности (вершина: список (сосед, вес))
    start: стартовая вершина
    Возвращает: (расстояния, предки)
    """
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

    return distances, predecessors

def reconstruct_path(predecessors, start, target):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = predecessors[node]
    path.reverse()
    if path[0] == start:
        return path
    else:
        return []

# Пример использования
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

distances, predecessors = dijkstra(graph, 'A')
print("Кратчайшие расстояния:", distances)
print("Путь от A до D:", reconstruct_path(predecessors, 'A', 'D'))
```

---

## Полезные ссылки

- [Wikipedia: Алгоритм Дейкстры](https://ru.wikipedia.org/wiki/Алгоритм_Дейкстры)
- [GeeksforGeeks: Dijkstra’s Shortest Path Algorithm (EN)](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
- [Visualgo: Dijkstra (EN)](https://visualgo.net/en/sssp)
- [Brilliant.org: Dijkstra’s Algorithm (EN)](https://brilliant.org/wiki/dijkstras-short-path-finder/)

---

## Практика на LeetCode

|    # | Название                               | Ссылка                                                                              |
| :--- | :--------------------------------------| :---------------------------------------------------------------------------------- |
|  743 | Network Delay Time                     | [LeetCode 743](https://leetcode.com/problems/network-delay-time/)                   |
| 1631 | Path With Minimum Effort               | [LeetCode 1631](https://leetcode.com/problems/path-with-minimum-effort/)            |
| 1514 | Path with Maximum Probability          | [LeetCode 1514](https://leetcode.com/problems/path-with-maximum-probability/)       |
|  787 | Cheapest Flights Within K Stops        | [LeetCode 787](https://leetcode.com/problems/cheapest-flights-within-k-stops/)      |
|  882 | Reachable Nodes In Subdivided Graph    | [LeetCode 882](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/)  |
|  399 | Evaluate Division (вариация, BFS)      | [LeetCode 399](https://leetcode.com/problems/evaluate-division/)                    |