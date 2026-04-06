# Палиндромные подмассивы (подстроки) — Динамическое программирование

## Описание задачи

Дан массив (или строка). Найдите самые длинные (или количество) непрерывных подмассивов (подстрок), которые являются палиндромами.  
Палиндром — это последовательность, которая читается одинаково слева направо и справа налево.

Варианты:
- Найти самую длинную палиндромную подстроку.
- Посчитать количество палиндромных подстрок.

---

## Идея алгоритма и подход

### 1. Расширение вокруг центра (для строк)

- Для каждого индекса пробуем расширяться влево и вправо как для палиндромов нечетной, так и четной длины.
- Время: O(n²), Память: O(1)

### 2. Таблица динамического программирования

- Пусть `dp[i][j]` — True, если подстрока/подмассив от i до j — палиндром.
- Заполняем таблицу для всех подстрок длины 1 (True), 2 (проверяем равенство), и больше (проверяем края и dp[i+1][j-1]).
- Время: O(n²), Память: O(n²)

---

## Пример на Python: количество палиндромных подстрок

```python
def count_palindromic_substrings(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    count = 0
    for l in range(1, n+1):  # длина подстроки
        for i in range(n - l + 1):
            j = i + l - 1
            if l == 1:
                dp[i][j] = True
            elif l == 2:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
            if dp[i][j]:
                count += 1
    return count

# Пример использования:
s = "abba"
print(count_palindromic_substrings(s))  # Вывод: 6
# ("a", "b", "b", "a", "bb", "abba")
```

---

## Пример на Python: самая длинная палиндромная подстрока

```python
def longest_palindrome(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    start, maxlen = 0, 1
    for i in range(n):
        dp[i][i] = True
    for l in range(2, n+1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j]:
                if l == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if l > maxlen:
                        start, maxlen = i, l
    return s[start:start+maxlen]

# Пример использования:
s = "babad"
print(longest_palindrome(s))  # Вывод: "bab" или "aba"
```

---

## Анализ сложности

- **Время:** O(n²)
- **Память:** O(n²)

---

## Применения

- Обработка и поиск в строках
- Анализ ДНК-последовательностей
- Распознавание паттернов

---

## Полезные ссылки

- [LeetCode #5: Longest Palindromic Substring (англ.)](https://leetcode.com/problems/longest-palindromic-substring/)
- [LeetCode #647: Palindromic Substrings (англ.)](https://leetcode.com/problems/palindromic-substrings/)
- [GeeksforGeeks: Count Palindromic Substrings (англ.)](https://www.geeksforgeeks.org/count-palindrome-sub-strings-string/)

---

## Практика на LeetCode

| Сложность  | Задача                       | Ссылка                                                                        |
|------------|-----------------------------|-------------------------------------------------------------------------------|
| Средняя    | Longest Palindromic Substring | [#5 Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) |
| Средняя    | Palindromic Substrings        | [#647 Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)             |