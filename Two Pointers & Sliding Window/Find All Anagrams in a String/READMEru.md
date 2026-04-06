# Найти все анаграммы в строке — подход скользящего окна и хэш-карты

## Описание задачи

Даны две строки `s` и `p`. Найдите все индексы начала анаграмм строки `p` в строке `s`. Ответ можно возвращать в любом порядке.

Анаграмма — это перестановка всех символов другой строки.

**Пример:**  
Ввод: s = "cbaebabacd", p = "abc"  
Вывод: [0, 6]  
Пояснение:  
- Подстрока с индекса 0 ("cba") — анаграмма "abc".
- Подстрока с индекса 6 ("bac") — анаграмма "abc".

---

## Идея и подход алгоритма

- Использовать технику скользящего окна длиной, равной длине `p`.
- Хранить количество символов для `p` (в хэш-карте или массиве).
- Для каждого окна в `s` поддерживать количество символов в окне.
- Если счетчики совпадают — текущее окно является анаграммой, записываем его индекс.
- Сдвигая окно, добавляем символ справа и убираем символ слева из счетчика.

---

## Пример на Python

```python
def findAnagrams(s, p):
    from collections import Counter
    
    result = []
    p_count = Counter(p)
    s_count = Counter()
    window = len(p)

    for i, char in enumerate(s):
        s_count[char] += 1
        if i >= window:
            left_char = s[i - window]
            s_count[left_char] -= 1
            if s_count[left_char] == 0:
                del s_count[left_char]
        if s_count == p_count:
            result.append(i - window + 1)
    return result

# Пример использования:
print(findAnagrams("cbaebabacd", "abc"))  # Выведет: [0, 6]
```

---

## Анализ сложности

- **Время:** O(n), где n — длина строки `s` (каждый символ обрабатывается один раз, если алфавит фиксированный).
- **Память:** O(1) при фиксированном алфавите (например, только строчные английские буквы), иначе O(m), где m — размер алфавита.

---

## Применения в жизни

- Поиск плагиата (нахождение перестановок слов/фраз).
- Анализ биологических последовательностей (ДНК/белки — поиск перестановок).
- Детектирование паттернов в сетевом трафике или логах.
- Поиск всех расположений зашифрованного пароля или кода.

---

## Полезные ссылки

- [Find All Anagrams in a String — LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
- [Анаграмма — Википедия](https://ru.wikipedia.org/wiki/Анаграмма)
- [Скользящее окно — GeeksforGeeks (на англ.)](https://www.geeksforgeeks.org/window-sliding-technique/)

---

## Задачи для практики на LeetCode

| Сложность | Задача                                   | Ссылка                                                                               |
|-----------|------------------------------------------|--------------------------------------------------------------------------------------|
| Средняя   | Найти все анаграммы в строке             | [#438 Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) |
| Средняя   | Перестановка в строке                    | [#567 Permutation in String](https://leetcode.com/problems/permutation-in-string/)    |
| Средняя   | Минимальное окно-подстрока               | [#76 Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)|
| Средняя   | Подстрока с конкатенацией всех слов      | [#30 Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) |

---