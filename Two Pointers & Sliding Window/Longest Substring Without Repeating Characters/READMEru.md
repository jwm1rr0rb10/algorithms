# Самая длинная подстрока без повторяющихся символов — подход скользящего окна

## Описание задачи

Дана строка. Требуется найти длину самой длинной подстроки без повторяющихся символов.

**Пример:**  
Ввод: s = "abcabcbb"  
Вывод: 3  
Пояснение: Ответ — "abc", длина 3.

---

## Идея и подход алгоритма

- Использовать технику скользящего окна с двумя указателями (`left` и `right`).
- Поддерживать множество уникальных символов в текущем окне.
- Расширять окно вправо, двигая `right`; при встрече дубликата сдвигать `left`, удаляя символы до устранения повтора.
- На каждом шаге обновлять максимальную найденную длину.

---

## Пример на Python

```python
def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

# Пример использования:
print(lengthOfLongestSubstring("abcabcbb"))  # Выведет: 3
```

---

## Анализ сложности

- **Время:** O(n), где n — длина строки. Каждый символ рассматривается максимум дважды.
- **Память:** O(min(n, m)), где m — мощность алфавита (например, 26 для строчных английских букв).

---

## Применение в жизни

- Поиск уникальных последовательностей действий пользователя в логах.
- Анализ потоков данных на уникальные сегменты.
- Обнаружение уникальных паттернов или подстрок в ДНК или сетевом трафике.
- Основа для более сложных алгоритмов обработки строк и окон.

---

## Полезные ссылки

- [Longest Substring Without Repeating Characters — LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [Техника скользящего окна — GeeksforGeeks (на англ.)](https://www.geeksforgeeks.org/window-sliding-technique/)
- [Подстрока — Википедия](https://ru.wikipedia.org/wiki/Подстрока)

---

## Задачи для практики на LeetCode

| Сложность | Задача                                            | Ссылка                                                                 |
|-----------|---------------------------------------------------|------------------------------------------------------------------------|
| Средняя   | Самая длинная подстрока без повторяющихся символов | [#3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| Средняя   | Подстрока с конкатенацией всех слов                | [#30 Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) |
| Средняя   | Самая длинная подстрока с не более чем двумя разными символами | [#159 Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) |
| Средняя   | Замена повторяющихся символов                      | [#424 Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) |

---