# Поиск наибольшей возрастающей подпоследовательности (Longest Increasing Subsequence, LIS)

## Описание задачи

Дан массив чисел. Найдите длину самой длинной строго возрастающей подпоследовательности (не обязательно подряд идущей).

**Пример:**  
Ввод: [10, 9, 2, 5, 3, 7, 101, 18]  
Вывод: 4  
Пояснение: Одна из LIS — [2, 3, 7, 101].

---

## Идея и подход

- Классическое решение — динамическое программирование:
  - Пусть `dp[i]` — длина LIS, заканчивающейся на i-м элементе.
  - Для каждого i перебираем все j < i, если nums[j] < nums[i]:  
    dp[i] = max(dp[i], dp[j] + 1)
- Можно оптимизировать до O(n log n) с помощью двоичного поиска.

---

## Пример на Python (O(n^2) решение)

```python
def lengthOfLIS(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Пример использования:
print(lengthOfLIS([10,9,2,5,3,7,101,18]))  # Выведет 4
```

---

## Быстрое решение (O(n log n))

```python
import bisect

def lengthOfLIS(nums):
    tails = []
    for num in nums:
        idx = bisect.bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)

# Пример:
print(lengthOfLIS([10,9,2,5,3,7,101,18]))  # Выведет 4
```

---

## Анализ сложности

- **O(n^2)** по времени, **O(n)** по памяти — динамическое программирование.
- **O(n log n)** по времени, **O(n)** по памяти — с помощью двоичного поиска.

---

## Применения

- Анализ последовательностей и трендов
- Распознавание паттернов в данных
- Биоинформатика (выравнивание последовательностей)
- Обработка сигналов, временных рядов

---

## Полезные ссылки

- [LIS — LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/)
- [LIS — GeeksforGeeks](https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/)
- [Wikipedia: LIS](https://ru.wikipedia.org/wiki/Задача_о_наибольшей_возрастающей_подпоследовательности)

---

## Практика на LeetCode

| Сложность | Задача                                 | Ссылка                                                                                      |
|-----------|----------------------------------------|---------------------------------------------------------------------------------------------|
| Средняя   | Longest Increasing Subsequence         | [#300 Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)|
| Средняя   | Russian Doll Envelopes                 | [#354 Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)        |
| Средняя   | Maximum Length of Pair Chain           | [#646 Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/) |