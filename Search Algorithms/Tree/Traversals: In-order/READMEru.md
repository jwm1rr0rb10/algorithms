# Обход бинарного дерева: In-order (Симметричный обход)

---

## Описание задачи

**In-order traversal** (симметричный обход) — это способ пройти по всем узлам бинарного дерева в порядке:  
**левый поддерево → корень → правое поддерево**.

Для бинарного дерева поиска (BST) in-order обход возвращает элементы в отсортированном порядке.

---

## Подход (алгоритм)

Рекурсивно:
1. Обойти левое поддерево.
2. Посетить текущий узел (корень).
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
def inorder_recursive(root):
    if not root:
        return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)

# Итеративная реализация
def inorder_iterative(root):
    result, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result

# Пример использования:
# tree = TreeNode(...)
# print(inorder_recursive(tree))  # [отсортированный список для BST]
# print(inorder_iterative(tree))
```

---

## Применение

- Получение отсортированного списка из BST.
- Копирование дерева, поиск k-го по величине элемента, задачи на обходы.
- Построение выражений из арифметических деревьев.

---

## Когда использовать

- Когда нужна обработка всех элементов дерева в определённом порядке.
- Для получения отсортированного результата из BST.

---

## Когда не стоит использовать

- Для обхода графа с циклами (In-order — только для деревьев).
- Если важен другой порядок (pre-order, post-order).

---

## Сложность

- **Время:** O(n), где n — количество узлов.
- **Память:** O(h), где h — высота дерева (глубина рекурсии или размер стека).

---

## Полезные ссылки

- [LeetCode — Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [Обход дерева — Википедия](https://ru.wikipedia.org/wiki/Обход_дерева)