# Разбиение на палиндромы (Palindrome Partitioning) — Рекурсия и бэктрекинг

## Описание задачи

Дана строка s. Требуется разбить строку на подстроки так, чтобы каждая подстрока была палиндромом. Вернуть все возможные варианты такого разбиения.

**Пример:**  
s = "aab"  
Ответ:  
```
[
  ["a","a","b"],
  ["aa","b"]
]
```

---

## Идея и подход

Задача — разбить строку на такие сегменты, чтобы каждый из них был палиндромом.

Для решения:
- Используем рекурсию и бэктрекинг.
- На каждом шаге пробуем все возможные префиксы, которые являются палиндромами.
- Если текущий префикс — палиндром, рекурсивно разбиваем оставшуюся часть строки.
- Как только дошли до конца строки, добавляем текущий путь в результат.

---

## Пример на Python

```python
def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def backtrack(s, start, path, result):
    if start == len(s):
        result.append(list(path))
        return
    for end in range(start, len(s)):
        if is_palindrome(s, start, end):
            path.append(s[start:end+1])
            backtrack(s, end + 1, path, result)
            path.pop()

def partition(s):
    result = []
    backtrack(s, 0, [], result)
    return result

# Пример использования:
s = "aab"
print(partition(s))
# Вывод: [['a', 'a', 'b'], ['aa', 'b']]
```

---

## Сложность

- **Время:** экспоненциальная по длине строки (в худшем случае O(2^n)), так как каждый символ может быть точкой разреза.
- **Память:** O(n) на стек рекурсии + O(число разбиений × средняя длина разбиения) на хранение результата.

---

## Где применяется

- Генерация всех палиндромных разбиений для автотестов.
- Биоинформатика: поиск палиндромных мотивов в последовательностях ДНК/РНК.
- Лингвистика и анализ текста: поиск симметричных структур в строках.
- Вспомогательный алгоритм в задачах динамического программирования по строкам.

---

## Полезные ссылки

- [Palindrome Partitioning — LeetCode (англ.)](https://leetcode.com/problems/palindrome-partitioning/)
- [Палиндром — Википедия](https://ru.wikipedia.org/wiki/Палиндром)
- [Бэктрекинг — GeeksforGeeks (англ.)](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [Разбиения множества — Brilliant.org (англ.)](https://brilliant.org/wiki/partitions-of-a-set/)

---

## Практика на LeetCode

| Сложность | Задача                      | Ссылка                                                                         |
|-----------|-----------------------------|--------------------------------------------------------------------------------|
| Средняя   | Palindrome Partitioning     | [№131 Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) |
| Сложная   | Palindrome Partitioning II  | [№132 Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) |
| Средняя   | Palindromic Substrings      | [№647 Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) |
| Средняя   | Partition Labels            | [№763 Partition Labels](https://leetcode.com/problems/partition-labels/)        |

---