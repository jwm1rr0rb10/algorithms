# Kth Element (QuickSelect) — Разделяй и властвуй (Divide & Conquer)

## Описание задачи

Вам дан неотсортированный массив и число k. Требуется найти k-й по величине элемент (k начинается с 1, то есть 1-й — минимальный, n-й — максимальный).

**Пример:**
```python
arr = [7, 10, 4, 3, 20, 15]
k = 3
# Ответ: 7 (третий по величине элемент после сортировки: [3, 4, 7, 10, 15, 20])
```

## Алгоритм (QuickSelect)

- QuickSelect — это модификация быстрой сортировки (QuickSort) для поиска k-го по величине элемента.
- В среднем работает за O(n), в худшем случае — O(n^2) (но на практике почти всегда быстрее сортировки).

### Шаги алгоритма

1. Выбрать опорный элемент (pivot).
2. Разделить массив на элементы меньше и больше опорного (partition).
3. Если индекс опорного элемента совпадает с (k-1), найден нужный элемент.
4. Если индекс больше (k-1), повторить для левой части; если меньше — для правой.

### Пример кода на Python

```python
def quickselect(arr, k):
    def partition(left, right):
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i

    def select(left, right, k_smallest):
        if left == right:
            return arr[left]
        pivot_index = partition(left, right)
        if k_smallest == pivot_index:
            return arr[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)

    return select(0, len(arr) - 1, k - 1)

# Пример использования:
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(quickselect(arr, k))  # 7
```

## Временная сложность

- Среднее время: O(n)
- Худший случай: O(n^2) (если всегда неудачно выбирается опорный элемент)

## Где применять

- Быстрый поиск k-го минимального/максимального элемента без полной сортировки.
- Задачи на медиану, персентиль, статистику порядка.
- Большие массивы, где сортировка слишком затратна.

## Недостатки

- Неустойчив во времени в худших случаях (можно улучшить случайным выбором pivot).
- Не возвращает отсортированный массив — только искомый элемент.

---

## Полезные ссылки

- [QuickSelect на Хабре](https://habr.com/ru/articles/346782/)
- [Wikipedia: Quickselect (рус)](https://ru.wikipedia.org/wiki/Quickselect)
- [Wikipedia: Алгоритмы поиска статистики порядка](https://ru.wikipedia.org/wiki/Статистика_порядка)

---

## Задачи на LeetCode

- [215. Kth Largest Element in an Array (Medium)](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [703. Kth Largest Element in a Stream (Easy/Medium)](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [347. Top K Frequent Elements (Medium)](https://leetcode.com/problems/top-k-frequent-elements/)

---