# Поиск наибольшей общей подпоследовательности (Longest Common Subsequence, LCS)

## Описание задачи

Даны две строки, требуется найти длину наибольшей общей подпоследовательности (LCS) — такую последовательность символов, которая встречается в обеих строках в том же порядке (но не обязательно подряд).

**Пример:**  
Ввод:  
A = "ABCBDAB"  
B = "BDCAB"  
Вывод: 4  
Пояснение: Одна из LCS — "BCAB" (или "BDAB").

---

## Идея и подход

- Используется динамическое программирование:
  - Пусть `dp[i][j]` — длина LCS для первых `i` символов строки A и первых `j` символов строки B.
  - Если A[i-1] == B[j-1]:  
    dp[i][j] = dp[i-1][j-1] + 1
  - Иначе:  
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

---

## Пример на Python

```python
def lcs(a: str, b: str) -> int:
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

# Пример использования:
a = "ABCBDAB"
b = "BDCAB"
print(lcs(a, b))  # Выведет 4
```

---

## Восстановление самой подпоследовательности

```python
def lcs_restore(a: str, b: str) -> str:
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    res = []
    i, j = n, m
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            res.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(res))

# Пример:
print(lcs_restore(a, b))  # Например, "BCAB"
```

---

## Анализ сложности

- **Время:** O(n * m)
- **Память:** O(n * m), можно оптимизировать до O(min(n, m)), если нужна только длина.

---

## Применения

- Сравнение файлов и текстов (diff, git)
- Биоинформатика (сравнение ДНК/РНК)
- Поиск схожих паттернов в данных
- Проверка на плагиат и автокоррекция текстов

---

## Полезные ссылки

- [LCS — LeetCode](https://leetcode.com/problems/longest-common-subsequence/)
- [LCS — GeeksforGeeks](https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/)
- [Wikipedia: LCS](https://ru.wikipedia.org/wiki/Задача_о_наибольшей_общей_подпоследовательности)

---

## Практика на LeetCode

| Сложность | Задача                            | Ссылка                                                                                      |
|-----------|-----------------------------------|---------------------------------------------------------------------------------------------|
| Средняя   | Longest Common Subsequence        | [#1143 Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)|
| Средняя   | Delete Operation for Two Strings  | [#583 Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) |
| Средняя   | Uncrossed Lines                   | [#1035 Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines/)                     |