# Union-Find (DSU, Система непересекающихся множеств)

**Union-Find** (или **DSU** — Disjoint Set Union, система непересекающихся множеств) — это структура данных, предназначенная для эффективного объединения множеств и проверки принадлежности элементов одному множеству.

## Краткое описание

- Поддерживает операции:
    - **find(x)** — определить, в каком множестве находится элемент x (найти “корень”).
    - **union(x, y)** — объединить множества, содержащие x и y.
- Использует оптимизации:
    - **Сжатие пути** (path compression) — ускоряет find.
    - **Объединение по размеру или рангу** — ускоряет union.
- Амортизированная сложность операций — почти O(1).

## Применение

- Построение минимального остовного дерева (алгоритм Краскала).
- Определение компонент связности в графе.
- Поиск циклов в неориентированном графе.
- Сети, кластеры, динамические задачи на объединение.

## Пример на Python

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Сжатие пути
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # Уже в одном множестве
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
        return True

# Пример использования:
uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
print(uf.find(0) == uf.find(2))  # True
print(uf.find(0) == uf.find(3))  # False
```

## Визуализация

```
До объединения:
0  1  2  3  4

После union(0, 1):
0-1  2  3  4

После union(1, 2):
0-1-2  3  4
```

## Сложность

- **Время:** O(α(n)) — почти константа (где α — обратная функция Аккермана).
- **Память:** O(n)

## Полезные ссылки

- [Википедия: Система непересекающихся множеств](https://ru.wikipedia.org/wiki/Система_непересекающихся_множеств)
- [Хабр: Union-Find](https://habr.com/ru/articles/182463/)
- [YouTube: DSU за 15 минут (рус.)](https://www.youtube.com/watch?v=F6k8lTrAE2g)

## Задачи для практики

- [LeetCode 547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)
- [LeetCode 684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)
- [LeetCode 990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/)