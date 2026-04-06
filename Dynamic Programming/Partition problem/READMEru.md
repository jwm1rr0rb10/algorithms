# Задача о разбиении множества (Partition Problem) — Динамическое программирование

## Описание задачи

Дано множество (или массив) положительных целых чисел. Определить, можно ли разбить его на два подмножества с равной суммой.

Варианты:
- Просто ответить, существует ли такое разбиение (True/False).
- Иногда: найти само разбиение.

---

## Идея алгоритма и подход

- Задача сводится к поиску подмножества с суммой, равной половине общей суммы.
- Если общая сумма нечётная — ответ False.
- Используем динамическое программирование (аналогично задаче о подмножестве с заданной суммой):
  - Пусть `dp[i]` — можно ли получить сумму `i` каким-то подмножеством.
  - Для каждого числа обновляем DP-массив с конца к началу.

---

## Пример на Python: Partition Equal Subset Sum

```python
def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]

# Пример использования:
nums = [1, 5, 11, 5]
print(can_partition(nums))  # Вывод: True ([1, 5, 5] и [11])
```

---

## Анализ сложности

- **Время:** O(n * sum/2)
- **Память:** O(sum/2)
  - n — количество элементов, sum — общая сумма элементов

---

## Применения

- Распределение ресурсов
- Планирование и балансировка нагрузки
- Задачи справедливого деления

---

## Полезные ссылки

- [LeetCode #416: Partition Equal Subset Sum (англ.)](https://leetcode.com/problems/partition-equal-subset-sum/)
- [GeeksforGeeks: Partition Problem (англ.)](https://www.geeksforgeeks.org/partition-problem-dp-18/)

---

## Практика на LeetCode

| Сложность  | Задача                        | Ссылка                                                                          |
|------------|-------------------------------|---------------------------------------------------------------------------------|
| Средняя    | Partition Equal Subset Sum    | [#416 Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |