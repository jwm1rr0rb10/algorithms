# Обход бинарного дерева: Pre-order (Прямой обход)

---

## Описание задачи

**Pre-order traversal** (прямой обход, "центр-лево-право") — способ пройти по всем узлам бинарного дерева в следующем порядке:  
**корень → левое поддерево → правое поддерево**.

Используется для копирования дерева, сериализации, построения выражений, и других задач.

---

## Подход (алгоритм)

Рекурсивно:
1. Посетить текущий узел (корень).
2. Обойти левое поддерево.
3. Обойти правое поддерево.

Можно реализовать также итеративно с помощью стека.

---

## Пример на Python (рекурсивно и итеративно)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Рекурсивная реализация
def preorder_recursive(root):
    if not root:
        return []
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)

# Итеративная реализация
def preorder_iterative(root):
    result, stack = [], []
    if root:
        stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.val)
        # Сначала добавляем правого, чтобы левый был на вершине
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

# Пример использования:
# tree = TreeNode(...)
# print(preorder_recursive(tree))
# print(preorder_iterative(tree))
```

---

## Применение

- Сериализация/десериализация дерева (например, в LeetCode).
- Копирование дерева.
- Построение префиксных выражений из арифметических деревьев.
- Обработка всех узлов сверху вниз.

---

## Когда использовать

- Когда важен порядок "сверху вниз".
- Для задач на построение новых деревьев по шаблону.

---

## Когда не стоит использовать

- Для обхода графов с циклами (только для деревьев).
- Если нужен другой порядок (in-order, post-order).

---

## Сложность

- **Время:** O(n), где n — количество узлов.
- **Память:** O(h), где h — высота дерева (глубина рекурсии или размер стека).

---

## Полезные ссылки

- [LeetCode — Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [Обход дерева — Википедия](https://ru.wikipedia.org/wiki/Обход_дерева)