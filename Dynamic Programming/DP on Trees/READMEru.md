# DP на деревьях: Максимальная сумма независимого множества вершин

## Описание задачи

Дано дерево (неориентированный граф без циклов) из `n` вершин, в каждой вершине записано целое число. Нужно выбрать множество вершин так, чтобы никакие две выбранные не были соединены ребром, и сумма их значений была максимальной.

---

## Идея и подход

- Для каждой вершины считаем два значения:
    - `take`: максимальная сумма, если мы включаем эту вершину в ответ (тогда детей брать нельзя)
    - `not_take`: максимальная сумма, если мы не включаем эту вершину (тогда детей можно брать или не брать — выбираем максимум для каждого)
- Обход выполняем в глубину (DFS) от корня.

---

## Пример на Python

```python
from collections import defaultdict

def max_independent_set_sum(n, edges, values):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    def dfs(node, parent):
        take = values[node]
        not_take = 0
        for child in tree[node]:
            if child == parent:
                continue
            child_take, child_not_take = dfs(child, node)
            take += child_not_take
            not_take += max(child_take, child_not_take)
        return take, not_take

    return max(dfs(0, -1))
```

### Пример использования

```python
n = 5
edges = [(0,1), (0,2), (1,3), (1,4)]
values = [1, 2, 3, 4, 5]
print(max_independent_set_sum(n, edges, values))  # Вывод: 12 (берем вершины 0, 3, 4)
```

---

## Сложность

- **Время:** O(n)
- **Память:** O(n)

---

## Где встречается

- Оптимизация размещения датчиков, камер, ресурсов в сетях, где нельзя брать соседние точки.
- В биоинформатике, планировании, теории игр.

---

## Полезные ссылки

- [CP-algorithms — DP на деревьях (рус)](https://e-maxx.ru/algo/dynamic_programming_on_trees)
- [LeetCode 337. House Robber III (аналог для бин. деревьев)](https://leetcode.com/problems/house-robber-iii/)