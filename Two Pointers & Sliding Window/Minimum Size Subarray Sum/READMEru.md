# Минимальная длина подмассива с суммой ≥ S

## Описание задачи

Дан массив положительных целых чисел `nums` и целое число `target`. Необходимо найти минимальную длину непрерывного подмассива, сумма которого больше либо равна `target`. Если такого подмассива не существует — вернуть 0.

**Пример:**  
Вход: nums = [2,3,1,2,4,3], target = 7  
Выход: 2  
Пояснение: Подмассив [4,3] минимальной длины, удовлетворяющий условию задачи.

---

## Идея алгоритма и подход

- Используется техника скользящего окна (два указателя) для эффективного поиска минимальной длины.
- Инициализируем два указателя:  
  - `start` — левая граница окна.
  - `end` — правая граница окна.
- Используем переменную `window_sum` для хранения суммы текущего окна.
- Расширяем окно, двигая `end` и добавляя значения к `window_sum`.
- Как только `window_sum` становится больше либо равен `target`, двигаем `start` вправо для минимизации размера окна и обновляем ответ.
- Продолжаем до конца массива.

---

## Пример на Python

```python
def minSubArrayLen(target, nums):
    n = len(nums)
    min_length = float('inf')
    window_sum = 0
    start = 0

    for end in range(n):
        window_sum += nums[end]
        while window_sum >= target:
            min_length = min(min_length, end - start + 1)
            window_sum -= nums[start]
            start += 1
    return 0 if min_length == float('inf') else min_length

# Пример использования:
print(minSubArrayLen(7, [2,3,1,2,4,3]))  # Вывод: 2
```

---

## Анализ сложности

- **Время:** O(n), где n — количество элементов в массиве (каждый элемент посещается максимум дважды).
- **Память:** O(1), используется только несколько переменных.

---

## Применение в жизни

- Поиск минимального периода, за который достигается заданный порог (например, минимальное количество подряд идущих дней с продажами выше цели).
- Оптимизация распределения ресурсов по временным окнам.
- Анализ временных рядов для быстрого достижения пороговых значений.

---

## Полезные ссылки

- [Minimum Size Subarray Sum — LeetCode (RU)](https://leetcode.com/problems/minimum-size-subarray-sum/)
- [Скользящее окно — GeeksforGeeks (RU)](https://www.geeksforgeeks.org/window-sliding-technique/)
- [Массив — Википедия](https://ru.wikipedia.org/wiki/Массив_(структура_данных))

---

## Практика на LeetCode

| Сложность | Задача                                      | Ссылка                                                                                  |
|-----------|---------------------------------------------|-----------------------------------------------------------------------------------------|
| Средняя   | Минимальная длина подмассива с суммой ≥ S   | [#209 Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) |
| Средняя   | Самая длинная подстрока без повторов        | [#3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| Средняя   | Подмассивы с произведением меньше K         | [#713 Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) |
| Средняя   | Максимальное среднее подмассива I           | [#643 Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) |

---