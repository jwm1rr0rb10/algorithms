# Топологическая сортировка (Topological Sort)

**Топологическая сортировка** — это упорядочивание вершин ориентированного ациклического графа (DAG), при котором для каждого ребра `u → v` вершина `u` располагается раньше вершины `v`. Такой порядок позволяет учитывать зависимости между задачами, модулями, процессами и т.д.

## Краткое описание

- Работает только для ориентированных ациклических графов (DAG).
- Находит порядок выполнения задач с зависимостями.
- Если в графе есть цикл — топологическая сортировка невозможна.

## Применение

- Сборка проектов (build systems).
- Разрешение зависимостей между модулями.
- Планирование задач и курсов (что учить или делать раньше).
- Компиляторы и анализ кода.

## Пример на Python (алгоритм Кана через входные степени)

```python
from collections import deque

def topological_sort(graph):
    n = len(graph)
    in_degree = [0] * n
    for u in range(n):
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([u for u in range(n) if in_degree[u] == 0])
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(order) != n:
        raise ValueError("Граф содержит цикл, топологическая сортировка невозможна.")
    return order

# Пример графа:
# 0 -> 2
# 1 -> 2
# 2 -> 3
# 3 -> 4
graph = [
    [2],    # 0
    [2],    # 1
    [3],    # 2
    [4],    # 3
    []      # 4
]

print("Топологический порядок:", topological_sort(graph))
# Вывод: [0, 1, 2, 3, 4] или [1, 0, 2, 3, 4]
```

## Визуализация

```
0   1
 \ /
  2
  |
  3
  |
  4
```

## Сложность

- **Время:** O(V + E), где V — количество вершин, E — количество рёбер.
- **Память:** O(V + E)

## Полезные ссылки

- [Википедия: Топологическая сортировка](https://ru.wikipedia.org/wiki/Топологическая_сортировка)
- [Хабр: Топологическая сортировка](https://habr.com/ru/articles/260821/)
- [YouTube: Топологическая сортировка (рус.)](https://www.youtube.com/watch?v=eL-KzMXSXXI)

## Задачи для практики

- [LeetCode 207. Course Schedule](https://leetcode.com/problems/course-schedule/)
- [LeetCode 210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
- [LeetCode 269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)