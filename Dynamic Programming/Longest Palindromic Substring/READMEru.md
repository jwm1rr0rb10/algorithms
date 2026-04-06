# Поиск самой длинной палиндромной подстроки (Longest Palindromic Substring, LPS)

## Описание задачи

Дана строка, требуется найти её самую длинную подстроку, которая является палиндромом (читается одинаково слева направо и справа налево).

**Пример:**  
Ввод: "babad"  
Вывод: "bab"  
Пояснение: "aba" тоже является правильным ответом (оба длиной 3).

---

## Идея и подход

- Классический способ — динамическое программирование:
  - Пусть `dp[i][j]` — является ли подстрока s[i:j+1] палиндромом.
  - База: все строки длины 1 — палиндромы, и длины 2 — если s[i] == s[j].
  - Для большей длины:  
    s[i] == s[j] и dp[i+1][j-1] == True.
- Также возможно решение "расширением вокруг центра" (expand around center), работает быстрее и проще реализуется.

---

## Пример на Python (расширение вокруг центра)

```python
def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    start, max_len = 0, 1
    n = len(s)
    for i in range(n):
        # Odd length palindrome
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                start, max_len = l, r - l + 1
            l -= 1
            r += 1
        # Even length palindrome
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                start, max_len = l, r - l + 1
            l -= 1
            r += 1
    return s[start:start + max_len]

# Пример использования:
print(longestPalindrome("babad"))  # Выведет "bab" или "aba"
```

---

## Анализ сложности

- **Время:** O(n^2)
- **Память:** O(1) (expand around center), O(n^2) (динамическое программирование)

---

## Применения

- Обработка строк и поиск паттернов
- Проверка симметрии в данных
- Задачи на анализ текста

---

## Полезные ссылки

- [Longest Palindromic Substring — LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)
- [LPS — GeeksforGeeks](https://www.geeksforgeeks.org/longest-palindromic-substring/)
- [Wikipedia: Palindrome](https://ru.wikipedia.org/wiki/Палиндром)

---

## Практика на LeetCode

| Сложность | Задача                        | Ссылка                                                                                      |
|-----------|-------------------------------|---------------------------------------------------------------------------------------------|
| Средняя   | Longest Palindromic Substring | [#5 Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)|
| Средняя   | Palindromic Substrings        | [#647 Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)        |