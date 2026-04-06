# Сравнение строк с учётом backspace — подход двух указателей

## Описание задачи

Даны две строки `s` и `t`. Вернуть `true`, если они равны после набора в пустом текстовом редакторе, где символ `#` означает backspace (удаление предыдущего символа).

**Пример:**  
Ввод: s = "ab#c", t = "ad#c"  
Вывод: true  
Пояснение: Обе строки преобразуются в "ac".

---

## Идея и подход алгоритма

- Использовать два указателя, начиная с конца каждой строки.
- Перебирать строки справа налево, пропуская символы, которые должны быть удалены из-за backspace (`#`).
- Для каждой строки использовать счётчик пропусков/backspace.
- Сравнивать текущие валидные символы обеих строк; если они не совпадают, вернуть `false`.
- Если оба указателя дошли до начала строки и все символы совпали, вернуть `true`.

---

## Пример на Python

```python
def backspaceCompare(s: str, t: str) -> bool:
    def next_valid_char(string, index):
        skip = 0
        while index >= 0:
            if string[index] == '#':
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                return index
            index -= 1
        return -1

    i, j = len(s) - 1, len(t) - 1
    while i >= 0 or j >= 0:
        i = next_valid_char(s, i)
        j = next_valid_char(t, j)
        if i >= 0 and j >= 0:
            if s[i] != t[j]:
                return False
        elif i >= 0 or j >= 0:
            return False
        i -= 1
        j -= 1
    return True

# Пример использования:
print(backspaceCompare("ab#c", "ad#c"))  # Выведет: True
```

---

## Анализ сложности

- **Время:** O(n + m), где n и m — длины двух строк.
- **Память:** O(1), используются только указатели и счётчики.

---

## Применение в жизни

- Симуляция поведения backspace в текстовых редакторах.
- Сравнение пользовательского ввода с учётом исправлений и удалений.
- Анализ и обработка командных строк, чатов, форм ввода.

---

## Полезные ссылки

- [Backspace String Compare — LeetCode](https://leetcode.com/problems/backspace-string-compare/)
- [Стек — GeeksforGeeks (на англ.)](https://www.geeksforgeeks.org/stack-data-structure/)
- [Два указателя — Википедия (на англ.)](https://en.wikipedia.org/wiki/Two-pointer_technique)

---

## Задачи для практики на LeetCode

| Сложность | Задача                      | Ссылка                                                                 |
|-----------|-----------------------------|------------------------------------------------------------------------|
| Лёгкая    | Сравнение строк с backspace | [#844 Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) |
| Средняя   | Расстояние редактирования   | [#72 Edit Distance](https://leetcode.com/problems/edit-distance/)      |
| Средняя   | Самая длинная валидная скобочная последовательность | [#32 Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) |
| Лёгкая    | Валидные скобки             | [#20 Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) |

---