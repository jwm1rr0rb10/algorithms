# Десериализация бинарного дерева (Deserialize Binary Tree)

---

## Описание задачи

Дано строковое представление бинарного дерева (например, в виде списка значений в ширину с использованием `null` для отсутствующих узлов).  
Необходимо восстановить (десериализовать) бинарное дерево.

**Пример входа:**  
```
[1,2,3,null,null,4,5]
```
Это дерево:
```
      1
     / \
    2   3
       / \
      4   5
```

---

## Подход (алгоритм)

1. Преобразуем строку в список значений.
2. Используем очередь для поуровневого восстановления дерева.
3. Для каждого узла из очереди добавляем левого и правого ребёнка, если они есть.

---

## Пример на Python

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(data):
    if not data or data == "[]":
        return None
    # Убираем скобки и разбиваем по запятой
    values = data.strip("[]").split(",")
    values = [val.strip() for val in values]
    if values[0] == "null":
        return None

    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        # Левый ребенок
        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1
        # Правый ребенок
        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1
    return root

# Пример использования:
tree = deserialize("[1,2,3,null,null,4,5]")
# Теперь tree — корень восстановленного бинарного дерева
```

---

## Применение

- Восстановление структуры дерева из сериализованного представления (например, для тестирования, передачи по сети, хранения).
- Часто используется в задачах LeetCode, интервью и олимпиадах.

---

## Когда использовать

- Когда требуется восстановить дерево из строкового/спискового представления (обычно в формате BFS/уровневого обхода).

---

## Когда не стоит использовать

- Если требуется только распарсить дерево в глубину (под другие специфические форматы), алгоритм может быть иным.

---

## Сложность

- **Время:** O(n), где n — число узлов
- **Память:** O(n)

---

## Полезные ссылки

- [LeetCode — Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- [Binary Tree — Википедия](https://ru.wikipedia.org/wiki/Бинарное_дерево)