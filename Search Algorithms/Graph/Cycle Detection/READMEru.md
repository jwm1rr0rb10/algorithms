# Обнаружение циклов в графах

---

## Описание задачи

Дан граф (неориентированный или ориентированный). Определить, содержит ли он хотя бы один цикл.

---

## Подход

### Неориентированный граф

- Используем DFS или BFS.
- Для каждой вершины храним “родителя”, чтобы не считать тривиальные циклы.
- Если находим посещённую вершину, не являющуюся родителем — цикл найден.

### Ориентированный граф

- Используем DFS с “рекурсивным стеком” (или топологическую сортировку).
- Если попадаем в вершину, которая уже “в стеке вызова”, — цикл найден.

---

## Примеры на Python

### Неориентированный граф

```python
def has_cycle_undirected(graph):
    visited = set()
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False
```

### Ориентированный граф

```python
def has_cycle_directed(graph):
    visited = set()
    on_stack = set()
    def dfs(node):
        visited.add(node)
        on_stack.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in on_stack:
                return True
        on_stack.remove(node)
        return False
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False
```

---

## Как это работает

- В неориентированных графах цикл обнаруживается, если из вершины попали в уже посещённую (не родителя).
- В ориентированных — если встретили вершину, находящуюся “в стеке вызова”.

---

## Применение

- Валидация топологического порядка
- Детектирование deadlock-ов
- Анализ зависимостей (build-системы, компиляторы)
- Проверка корректности автоматов состояний

---

## Когда использовать

- Когда нужно узнать, есть ли в графе цикл (например, для задач планирования, разрешения зависимостей и др.)

---

## Когда не стоит использовать

- Если граф гарантированно дерево (циклов нет по определению)
- Если наличие цикла неважно для задачи

---

## Сложность

- **Время:** O(V + E)
- **Память:** O(V)

---

## Полезные ссылки

- [LeetCode — Course Schedule (поиск цикла в ориентированном графе)](https://leetcode.com/problems/course-schedule/)
- [Обнаружение цикла — Википедия](https://ru.wikipedia.org/wiki/Обнаружение_цикла)