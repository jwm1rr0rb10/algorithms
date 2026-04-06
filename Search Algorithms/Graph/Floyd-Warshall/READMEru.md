# Алгоритм Флойда–Уоршелла (Floyd-Warshall)

## Что это такое?

**Флойд–Уоршелл (Floyd-Warshall)** — алгоритм поиска кратчайших расстояний между всеми парами вершин во взвешенном графе (допускает отрицательные веса рёбер, но не допускает отрицательные циклы).  
Используется, когда нужно знать кратчайшие расстояния между каждой парой точек.

---

## Как работает?

1. **Инициализация:**  
   - Создаётся матрица расстояний `dist[i][j]`: из вершины i в вершину j.
   - Если между i и j есть ребро, то dist[i][j] = вес ребра, иначе бесконечность (`float('inf')`), dist[i][i] = 0.

2. **Основная идея:**  
   - Для каждой промежуточной вершины k обновляем все пары (i, j):
     - `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`
   - Если путь i→k→j короче текущего i→j, обновляем.

3. **Повторяем для всех k.**  
   - В конце dist[i][j] — кратчайшее расстояние от i до j.

---

## Особенности

- Находит кратчайшие расстояния между **всеми парами вершин**.
- Работает с отрицательными весами рёбер (но не с отрицательными циклами).
- Простая реализация: вложенные циклы по всем вершинам.

---

## Сложность

| Сложность   | Значение  |
|:-----------:|:---------:|
| **Время**   | O(V³)     |
| **Память**  | O(V²)     |

- **V** — количество вершин

---

## Применение

- Кратчайшие пути между всеми парами городов (транспортные сети, карты).
- Анализ сетей и задержек (network delays).
- Транзитивное замыкание/достижимость в графах.
- Обнаружение отрицательных циклов (`dist[i][i] < 0` после работы алгоритма).

---

## Пример на Python

```python
def floyd_warshall(graph):
    """
    graph: dict, список смежности, graph[u][v] = вес ребра u->v
    Возвращает: матрицу dist, где dist[i][j] — кратчайшее расстояние от i до j
    """
    nodes = list(graph.keys())
    n = len(nodes)
    index = {node: idx for idx, node in enumerate(nodes)}

    # Инициализация матрицы расстояний
    dist = [[float('inf')] * n for _ in range(n)]
    for u in nodes:
        for v in nodes:
            if u == v:
                dist[index[u]][index[v]] = 0
            elif v in graph[u]:
                dist[index[u]][index[v]] = graph[u][v]

    # Основной алгоритм Флойда–Уоршелла
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist, nodes

# Пример использования
graph = {
    'A': {'B': 3, 'C': 8, 'E': -4},
    'B': {'D': 1, 'E': 7},
    'C': {'B': 4},
    'D': {'A': 2, 'C': -5},
    'E': {'D': 6}
}

dist, nodes = floyd_warshall(graph)
print("Кратчайшие расстояния между всеми парами:")
for i, u in enumerate(nodes):
    for j, v in enumerate(nodes):
        print(f"{u} -> {v}: {dist[i][j]}")
```

---

## Полезные ссылки

- [Wikipedia: Алгоритм Флойда–Уоршелла](https://ru.wikipedia.org/wiki/Алгоритм_Флойда_—_Уоршелла)
- [GeeksforGeeks: Floyd Warshall Algorithm (EN)](https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/)
- [Visualgo: Floyd-Warshall (EN)](https://visualgo.net/en/sssp)

---

## Задачи на LeetCode

|    # | Название                                              | Ссылка                                                                             |
| :--- | :---------------------------------------------------- | :--------------------------------------------------------------------------------- |
| 1334 | Город с наименьшим числом соседей при пороговом расстоянии | [LeetCode 1334](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) |
| 2642 | Конструктор графа с поиском кратчайшего пути          | [LeetCode 2642](https://leetcode.com/problems/design-graph-with-shortest-path-calculator/) |
| 1462 | Расписание курсов IV                                  | [LeetCode 1462](https://leetcode.com/problems/course-schedule-iv/)                  |
| 2045 | Второе минимальное время до точки назначения          | [LeetCode 2045](https://leetcode.com/problems/second-minimum-time-to-reach-destination/) |