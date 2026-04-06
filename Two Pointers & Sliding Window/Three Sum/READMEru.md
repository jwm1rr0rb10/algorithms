# 3Sum (Три числа в сумме дают ноль)

## Описание задачи

Дан массив целых чисел `nums`. Необходимо найти все уникальные триплеты `[nums[i], nums[j], nums[k]]`, такие что `i != j != k`, и сумма `nums[i] + nums[j] + nums[k] == 0`.  
В результате не должно быть повторяющихся троек.

**Пример:**  
Вход: nums = [-1,0,1,2,-1,-4]  
Выход: [[-1,-1,2], [-1,0,1]]  
Пояснение: Триплеты [-1,-1,2] и [-1,0,1] дают в сумме ноль. Дубликаты не учитываются.

---

## Идея алгоритма и подход

- Сортируем массив для удобного поиска и пропуска дубликатов.
- Проходим по массиву индексом `i`:
  - Для каждого `i` используем два указателя (`left = i+1`, `right = len(nums)-1`), чтобы найти пары, удовлетворяющие условию.
  - Сравниваем сумму и двигаем указатели.
  - Не забываем пропускать дубликаты для всех указателей.

---

## Пример на Python

```python
def threeSum(nums):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, n-1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return res

# Пример использования:
print(threeSum([-1,0,1,2,-1,-4]))  # Вывод: [[-1, -1, 2], [-1, 0, 1]]
```

---

## Анализ сложности

- **Время:** O(n^2), где n — длина массива (из-за вложенных циклов).
- **Память:** O(1) (не считая списка результата).

---

## Применение в жизни

- Поиск нулевых сумм в финансовых данных.
- Химия: подбор устойчивых троек элементов.
- Компьютерное зрение: наборы признаков, удовлетворяющие определённому условию.

---

## Полезные ссылки

- [3Sum — LeetCode](https://leetcode.com/problems/3sum/)
- [Техника двух указателей — GeeksforGeeks (RU)](https://www.geeksforgeeks.org/two-pointers-technique/)
- [Сортировка — Википедия](https://ru.wikipedia.org/wiki/Сортировка)

---

## Практика на LeetCode

| Сложность | Задача         | Ссылка                                                                               |
|-----------|----------------|--------------------------------------------------------------------------------------|
| Средняя   | 3Sum           | [#15 3Sum](https://leetcode.com/problems/3sum/)                                      |
| Средняя   | 3Sum Closest   | [#16 3Sum Closest](https://leetcode.com/problems/3sum-closest/)                      |
| Средняя   | 4Sum           | [#18 4Sum](https://leetcode.com/problems/4sum/)                                      |
| Средняя   | Two Sum II     | [#167 Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) |

---