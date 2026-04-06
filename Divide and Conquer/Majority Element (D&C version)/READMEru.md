# Majority Element — Разделяй и властвуй (Divide & Conquer)

## Описание задачи

Дан массив целых чисел. Требуется найти элемент, который встречается в массиве более ⌊n/2⌋ раз (т.е. больше половины длины массива). Гарантируется, что такой элемент существует.

**Пример:**
```python
arr = [2, 2, 1, 1, 1, 2, 2]
# Ответ: 2 (встречается 4 раза из 7)
```

## Алгоритм (Divide & Conquer)

Идея: рекурсивно разделить массив пополам, найти мажоритарный элемент в каждой половине, а затем объединить результаты.

### Шаги

1. Если массив состоит из одного элемента, вернуть его.
2. Разделить массив пополам.
3. Рекурсивно найти majority для левой и правой части.
4. Если оба результата совпадают — это majority для всего массива.
5. Если нет, посчитать количество каждого кандидата во всём диапазоне и вернуть тот, кто встречается чаще.

### Пример кода на Python

```python
def majority_element_rec(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    left_major = majority_element_rec(arr, left, mid)
    right_major = majority_element_rec(arr, mid + 1, right)
    if left_major == right_major:
        return left_major
    left_count = sum(1 for i in range(left, right + 1) if arr[i] == left_major)
    right_count = sum(1 for i in range(left, right + 1) if arr[i] == right_major)
    return left_major if left_count > right_count else right_major

def majority_element(arr):
    return majority_element_rec(arr, 0, len(arr) - 1)
    
# Пример использования:
arr = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(arr))  # 2
```

## Временная сложность

- O(n log n)

## Где применять

- Когда нужно найти элемент-множитель в массиве.
- Для изучения методов "разделяй и властвуй".
- В задачах, где гарантируется существование majority.

## Недостатки

- Существует более быстрый алгоритм (Boyer-Moore, O(n)), но подход D&C полезен для обучения и обобщения.

---

## Полезные ссылки

- [Majority Element — Хабр](https://habr.com/ru/articles/349860/)
- [Wikipedia: Мажоритарный элемент](https://ru.wikipedia.org/wiki/Задача_о_мажоритарном_элементе)
- [LeetCode Discuss: Majority Element](https://leetcode.com/problems/majority-element/solutions/)

---

## Задачи на LeetCode

- [169. Majority Element (Easy)](https://leetcode.com/problems/majority-element/)
- [229. Majority Element II (Medium)](https://leetcode.com/problems/majority-element-ii/)

---