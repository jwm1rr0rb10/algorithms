# Задача о разбиении множества — Динамическое программирование (Табуляция)

## Описание задачи

Дано множество (или массив) положительных целых чисел. Определить, можно ли разбить его на два подмножества с равной суммой.

Варианты:
- Просто ответить, существует ли такое разбиение (True/False).
- Иногда: найти само разбиение.

---

## Идея алгоритма и подход

- Задача сводится к поиску подмножества с суммой, равной половине общей суммы.
- Если общая сумма нечётная — ответ False.
- Используем динамическое программирование (табуляция, bottom-up):
  - Пусть `dp[i][j]` — можно ли получить сумму `j`, используя первые `i` чисел.
  - Для каждого числа заполняем DP-таблицу, рассматривая включение и исключение текущего числа.
  - `dp[0][0] = True` (пустое подмножество даёт сумму 0).
  - Для каждого `i` от 1 до n и для каждого `j` от 0 до target:
    - Если `j < nums[i-1]`, то `dp[i][j] = dp[i-1][j]`
    - Иначе: `dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]`

---

## Пример на Python: Partition Equal Subset Sum (Табуляция)

```python
def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True  # сумма 0 возможна всегда
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < nums[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
    return dp[n][target]

# Пример использования:
nums = [1, 5, 11, 5]
print(can_partition(nums))  # Вывод: True ([1, 5, 5] и [11])
```

---

## Анализ сложности

- **Время:** O(n * sum/2)
- **Память:** O(n * sum/2)
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