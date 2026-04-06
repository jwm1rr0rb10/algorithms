# Count Inversions — Разделяй и властвуй (Divide & Conquer)

## Описание задачи

Вам дан массив целых чисел. Необходимо посчитать количество инверсий в массиве.

**Инверсия** — это пара индексов (i, j), таких что i < j и arr[i] > arr[j].

**Пример:**
```python
arr = [2, 4, 1, 3, 5]
# Инверсии: (2,1), (4,1), (4,3)
# Ответ: 3
```

## Алгоритм (Divide & Conquer)

- Базируется на модифицированном алгоритме сортировки слиянием (Merge Sort).
- При слиянии двух отсортированных половин учитываются случаи, когда левый элемент больше правого — это и есть инверсия.

### Пример кода на Python

```python
def merge_and_count(arr, left, mid, right):
    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]
    i = j = 0
    k = left
    inv_count = 0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
            inv_count += (len(left_part) - i)
        k += 1

    arr[k:right+1] = left_part[i:] + right_part[j:]
    return inv_count

def count_inversions(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += count_inversions(arr, left, mid)
        inv_count += count_inversions(arr, mid+1, right)
        inv_count += merge_and_count(arr, left, mid, right)
    return inv_count

# Пример использования:
arr = [2, 4, 1, 3, 5]
print(count_inversions(arr, 0, len(arr)-1))  # 3
```

## Временная сложность

- O(n log n)

## Где применять

- При анализе “беспорядка” или “рассортированности” в массиве.
- В задачах по теории сортировок, оценке сложности перестановок.
- В биоинформатике, теории информации, анализе социальных сетей.

## Недостатки

- Требует дополнительной памяти для временных массивов.
- Для маленьких массивов проще и быстрее использовать перебор.

---

## Полезные ссылки

- [Инверсии в массиве — Хабр](https://habr.com/ru/articles/282993/)
- [Wikipedia: Инверсия (перестановка)](https://ru.wikipedia.org/wiki/Инверсия_(перестановка))

---

## Задачи на LeetCode

- [315. Count of Smaller Numbers After Self (Hard, вариация)](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
- [327. Count of Range Sum (Hard, вариация)](https://leetcode.com/problems/count-of-range-sum/)
- [493. Reverse Pairs (Hard, вариация)](https://leetcode.com/problems/reverse-pairs/)

---