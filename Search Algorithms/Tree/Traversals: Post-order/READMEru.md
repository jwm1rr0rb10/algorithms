# Обход бинарного дерева: Post-order (Обратный обход)

---

## Описание задачи

**Post-order traversal** (обратный обход, "лево-право-центр") — способ пройти по всем узлам бинарного дерева в следующем порядке:  
**левое поддерево → правое поддерево → корень**.

Используется для удаления дерева, вычисления выражений, и во многих задачах на дерево.

---

## Подход (алгоритм)

Рекурсивно:
1. Обойти левое поддерево.
2. Обойти правое поддерево.
3. Посетить текущий узел (корень).

Также можно реализовать итеративно с помощью стека.

---

## Пример на Python (рекурсивно и итеративно)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Рекурсивная реализация
def postorder_recursive(root):
    if not root:
        return []
    return postorder_recursive(root.left) + postorder_recursive(root.right) + [root.val]

# Итеративная реализация
def postorder_iterative(root):
    result, stack = [], []
    last_visited = None
    curr = root
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            peek = stack[-1]
            # Если есть правое поддерево и оно ещё не посещено
            if peek.right and last_visited != peek.right:
                curr = peek.right
            else:
                result.append(peek.val)
                last_visited = stack.pop()
    return result

# Пример использования:
# tree = TreeNode(...)
# print(postorder_recursive(tree))
# print(postorder_iterative(tree))
```

---

## Применение

- Удаление дерева (освобождение памяти).
- Вычисление выражений по дереву выражений (арифметика, логика).
- Построение обратной польской нотации (RPN).
- Задачи на обход и обработку дерева снизу вверх.

---

## Когда использовать

- Когда обработка/удаление/вычисление должно идти снизу вверх.
- Для работы с арифметическими выражениями.

---

## Когда не стоит использовать

- Для обхода графов с циклами (только для деревьев).
- Если нужен другой порядок (in-order, pre-order).

---

## Сложность

- **Время:** O(n), где n — количество узлов.
- **Память:** O(h), где h — высота дерева (глубина рекурсии или размер стека).

---

## Полезные ссылки

- [LeetCode — Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
- [Обход дерева — Википедия](https://ru.wikipedia.org/wiki/Обход_дерева)