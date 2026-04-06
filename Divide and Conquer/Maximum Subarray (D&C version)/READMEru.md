# Maximum Subarray — Разделяй и властвуй (Divide & Conquer)

## Описание задачи

Дан массив целых чисел (могут быть отрицательные). Найти непрерывный подмассив с максимальной суммой.

**Пример:**
```python
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Максимальная сумма: 6 ([4, -1, 2, 1])
```

## Алгоритм (Divide & Conquer)

1. Разделить массив на две части.
2. Рекурсивно найти максимум в левой и правой половинах.
3. Найти максимальную сумму, "пересекающую" середину.
4. Вернуть максимум из трёх вариантов.

### Пример кода на Python

```python
def max_crossing_sum(arr, left, mid, right):
    left_sum = float('-inf')
    total = 0
    for i in range(mid, left-1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
    right_sum = float('-inf')
    total = 0
    for i in range(mid+1, right+1):
        total += arr[i]
        if total > right_sum:
            right_sum = total
    return left_sum + right_sum

def max_subarray_sum(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    max_left = max_subarray_sum(arr, left, mid)
    max_right = max_subarray_sum(arr, mid+1, right)
    max_cross = max_crossing_sum(arr, left, mid, right)
    return max(max_left, max_right, max_cross)

# Пример использования:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr, 0, len(arr)-1))  # 6
```

## Временная сложность

- O(n log n)

## Где применять

- Для обучения принципам Divide & Conquer.
- Когда нужно расширить задачу (например, для 2D-массивов).
- В распределённых/параллельных системах.

## Недостатки

- Проигрывает по скорости алгоритму Кадане (O(n)), если задача простая.

---

## Полезные ссылки

- [Разделяй и властвуй — Хабр](https://habr.com/ru/articles/324626/)
- [Задача о максимальной подпоследовательности — Хабр](https://habr.com/ru/articles/346348/)
- [Wikipedia: Задача о максимальной подпоследовательности](https://ru.wikipedia.org/wiki/Задача_о_максимальной_подпоследовательности)

---

## Задачи на LeetCode

- [53. Maximum Subarray (Easy)](https://leetcode.com/problems/maximum-subarray/)
- [918. Maximum Sum Circular Subarray (Medium)](https://leetcode.com/problems/maximum-sum-circular-subarray/)
- [363. Max Sum of Rectangle No Larger Than K (Hard, 2D-версия)](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/)

---