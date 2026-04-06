# Генерация правильных скобочных последовательностей (Generate Parentheses) — Рекурсия и бэктрекинг

## Описание задачи

Дано число **n** — количество пар скобок. Требуется сгенерировать все возможные правильные (валидные) комбинации из n пар круглых скобок.

**Пример:**  
Ввод: n = 3  
Вывод:  
```
["((()))","(()())","(())()","()(())","()()()"]
```

---

## Идея и подход

- У нас есть две операции: добавить открывающую скобку `(` или закрывающую `)`.
- Открывающую скобку можно добавить, если их использовано меньше, чем n.
- Закрывающую — если их меньше, чем открывающих.
- Как только строка длиной 2*n — добавляем комбинацию в результат.

---

## Пример на Python

```python
def generate_parentheses(n):
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append("".join(current))
            return
        if open_count < n:
            current.append("(")
            backtrack(current, open_count + 1, close_count)
            current.pop()
        if close_count < open_count:
            current.append(")")
            backtrack(current, open_count, close_count + 1)
            current.pop()

    backtrack([], 0, 0)
    return result

# Пример использования:
print(generate_parentheses(3))
# ['((()))', '(()())', '(())()', '()(())', '()()()']
```

---

## Сложность

- **Время:** O(4^n / sqrt(n)) — это n-е число Каталана.
- **Память:** O(4^n / sqrt(n)) на хранение всех последовательностей + O(n) глубина рекурсии.

---

## Где применяется

- Парсеры и компиляторы (разбор скобочных выражений).
- Генерация тестов для калькуляторов и парсеров.
- Проверка корректности вложенных структур.
- Моделирование вариантов вложенных действий в программировании и математике.

---

## Полезные ссылки

- [Generate Parentheses — LeetCode (англ.)](https://leetcode.com/problems/generate-parentheses/)
- [Числа Каталана — Википедия](https://ru.wikipedia.org/wiki/Числа_Каталана)
- [Бэктрекинг — GeeksforGeeks (англ.)](https://www.geeksforgeeks.org/backtracking-algorithms/)

---

## Практика на LeetCode

| Сложность | Задача                  | Ссылка                                                                          |
|-----------|-------------------------|---------------------------------------------------------------------------------|
| Средняя   | Generate Parentheses    | [№22 Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)  |
| Средняя   | Letter Combinations     | [№17 Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)|
| Средняя   | Restore IP Addresses    | [№93 Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)  |
| Средняя   | Subsets                 | [№78 Subsets](https://leetcode.com/problems/subsets/)                            |

---