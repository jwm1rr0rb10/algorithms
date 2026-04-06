# Замена символов для наибольшей повторяющейся подстроки — Два указателя / Sliding Window

## Описание задачи

Дана строка `s` и целое число `k`. Нужно определить максимальную длину подстроки, которую можно получить, если выполнить не более `k` замен символов, чтобы все символы в этой подстроке были одинаковыми (можно заменить до `k` символов на любые другие заглавные буквы английского алфавита).

**Пример:**  
Вход: s = "AABABBA", k = 1  
Выход: 4  
Пояснение: Можно изменить одну 'A' в середине на 'B', чтобы получить "AABBBBA" (или одну 'B' на 'A', чтобы получить "AAAAAAA").

---

## Идея и подход

- Используем sliding window (два указателя — левый и правый), чтобы поддерживать текущую подстроку.
- Храним частоты символов в окне.
- Следим за количеством самого частого символа внутри окна.
- Если размер окна минус количество самого частого символа превышает `k`, сдвигаем левый указатель вправо.
- Ответ — максимальный размер окна, удовлетворяющего условию.

---

## Пример на Python

```python
def characterReplacement(s: str, k: int) -> int:
    from collections import defaultdict

    count = defaultdict(int)
    max_count = 0
    left = 0
    result = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_count = max(max_count, count[s[right]])

        # Если нужно заменить больше k символов, сдвигаем левую границу окна
        if (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result

# Пример использования:
print(characterReplacement("AABABBA", 1))  # Вывод: 4
```

---

## Анализ сложности

- **Время:** O(n), где n — длина строки.
- **Память:** O(1), так как в окне максимум 26 возможных символов.

---

## Применения в реальной жизни

- Поиск почти однородных подстрок в текстах и ДНК-цепочках.
- Анализ ошибок и коррекция в потоковых данных.
- Детектирование плагиата и нестрогий поиск подстрок.
- Анализ пользовательского ввода с ограничением на количество опечаток.

---

## Полезные ссылки

- [Longest Repeating Character Replacement — LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [Sliding Window Technique — GeeksforGeeks](https://www.geeksforgeeks.org/window-sliding-technique/)
- [Two Pointers Technique — Wikipedia](https://ru.wikipedia.org/wiki/Два_указателя_(метод))

---

## Задачи для практики на LeetCode

| Сложность | Задача                                              | Ссылка                                                                                    |
|-----------|-----------------------------------------------------|-------------------------------------------------------------------------------------------|
| Средняя   | Longest Repeating Character Replacement             | [#424 Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) |
| Средняя   | Longest Substring with At Most K Distinct Chars     | [#340 Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) |
| Средняя   | Minimum Window Substring                            | [#76 Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) |
| Средняя   | Longest Substring Without Repeating Characters      | [#3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |

---