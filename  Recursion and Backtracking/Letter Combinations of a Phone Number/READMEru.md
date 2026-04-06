# Буквенные комбинации телефонного номера (Letter Combinations of a Phone Number) — Рекурсия и бэктрекинг

## Описание задачи

Дана строка из цифр от 2 до 9. Требуется вернуть все возможные комбинации букв, которые может представлять этот номер, согласно телефонной клавиатуре.

**Пример:**  
Ввод: `"23"`  
Вывод:  
```
["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

---

## Идея и подход

- Каждая цифра соответствует набору букв, как на старых мобильных телефонах.
- Для поиска всех комбинаций:
  - Для каждой цифры перебираем все возможные буквы.
  - Рекурсивно строим комбинацию, добавляя по одной букве за раз.
  - Как только длина комбинации достигает длины исходной строки — добавляем её в результат.
  - Используем бэктрекинг: после рассмотрения варианта убираем последнюю букву и пробуем следующий вариант.

---

## Пример на Python

```python
def letter_combinations(digits):
    if not digits:
        return []

    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    result = []

    def backtrack(index, path):
        if len(path) == len(digits):
            result.append("".join(path))
            return
        for letter in phone[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()  # Бэктрекинг

    backtrack(0, [])
    return result

# Пример использования:
print(letter_combinations("23"))
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
```

---

## Сложность

- **Время:** O(3^N * 4^M), где N — число цифр с 3 буквами (2,3,4,5,6,8), M — с 4 буквами (7,9).
- **Память:** O(N) — глубина стека рекурсии + место для хранения результата.

---

## Где применяется

- Подбор красивых или запоминающихся телефонных номеров (vanity numbers).
- Предиктивный набор (T9) на мобильных устройствах.
- Генерация тестовых кейсов для номеров и систем ввода.
- Поиск возможных слов по цифровому коду.

---

## Полезные ссылки

- [Letter Combinations of a Phone Number — LeetCode (англ.)](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [Телефонная клавиатура — Википедия](https://ru.wikipedia.org/wiki/Телефонная_клавиатура)
- [Бэктрекинг — GeeksforGeeks (англ.)](https://www.geeksforgeeks.org/backtracking-algorithms/)

---

## Практика на LeetCode

| Сложность | Задача                                  | Ссылка                                                                              |
|-----------|-----------------------------------------|-------------------------------------------------------------------------------------|
| Средняя   | Letter Combinations of a Phone Number   | [№17 Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) |
| Средняя   | Generate Parentheses                    | [№22 Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)      |
| Средняя   | Combination Sum                         | [№39 Combination Sum](https://leetcode.com/problems/combination-sum/)                |
| Средняя   | Subsets                                 | [№78 Subsets](https://leetcode.com/problems/subsets/)                                |

---