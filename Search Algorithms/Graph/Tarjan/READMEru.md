# Алгоритм Тарьяна (Tarjan's Algorithm)

Алгоритм Тарьяна — это эффективный алгоритм поиска компонент сильной связности (SCC, Strongly Connected Components) в ориентированном графе. Компонента сильной связности — это максимальное множество вершин, из которых достижима любая другая вершина этого множества.

## Краткое описание

1. Использует поиск в глубину (DFS).
2. Для каждой вершины вычисляется два значения: время входа (индекс) и минимальное достижимое значение (lowlink).
3. С помощью стека отслеживаются вершины текущей компоненты.
4. Когда вершина становится “корнем” SCC (index == lowlink), формируется новая компонента.

## Применение

- Анализ графов зависимостей (например, в компиляторах).
- Выявление циклических зависимостей в программном обеспечении.
- Поиск “модулей” в социальных сетях и других сетевых структурах.

## Пример на Python

```python
def tarjans_scc(graph):
    n = len(graph)
    index = 0
    stack = []
    indices = [None] * n
    lowlink = [None] * n
    on_stack = [False] * n
    result = []

    def strongconnect(v):
        nonlocal index
        indices[v] = lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if indices[w] is None:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if indices[v] == lowlink[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            result.append(scc)

    for v in range(n):
        if indices[v] is None:
            strongconnect(v)

    return result

# Пример графа (список смежности)
# Вершины: 0, 1, 2, 3, 4
# Рёбра: 0->1, 1->2, 2->0, 1->3, 3->4
graph = [
    [1],    # 0
    [2,3],  # 1
    [0],    # 2
    [4],    # 3
    []      # 4
]

print("Компоненты сильной связности:", tarjans_scc(graph))
# Вывод: [[4], [3], [0, 2, 1]]
```

## Визуализация

```
0 → 1 → 2
↑    ↓
└─── 3 → 4
```
SCC: [0,1,2], [3], [4]

## Сложность

- Время: O(V + E), где V — количество вершин, E — количество рёбер.
- Память: O(V)

## Полезные ссылки

- [Википедия: Алгоритм Тарьяна](https://ru.wikipedia.org/wiki/Алгоритм_Тарьяна_по_поиску_компонент_сильной_связности)
- [Хабр: Компоненты сильной связности (Тарян и Коса-Раджу)](https://habr.com/ru/articles/212163/)
- [YouTube: Визуализация алгоритма Тарьяна (рус.)](https://www.youtube.com/watch?v=ZeDNSeilf-Y)

## Задачи для практики

- [LeetCode 1192. Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/)
- [LeetCode 323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)