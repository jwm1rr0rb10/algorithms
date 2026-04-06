# Восстановление IP-адресов (Restore IP Addresses) — Рекурсия и бэктрекинг

## Описание задачи

Дана строка s, содержащая только цифры. Необходимо вернуть **все возможные действительные IP-адреса**, которые можно получить, расставив три точки так, чтобы получилось четыре сегмента (октета), каждый из которых:
- находится в диапазоне от 0 до 255,
- не содержит лидирующих нулей (например, "01", "001" — некорректно, только "0" допустимо).

**Пример:**  
Ввод: `"25525511135"`  
Вывод:  
```
["255.255.11.135", "255.255.111.35"]
```

---

## Идея и подход

- Всего в IP-адресе четыре сегмента.
- На каждом шаге рекурсивно выбираем сегмент длиной 1, 2 или 3 символа, если он корректен.
- Если сегмент валиден, добавляем его к текущему пути и продолжаем разбиение оставшейся строки.
- Как только выбрали 4 сегмента и дошли до конца строки — собираем валидный IP и сохраняем.
- После рекурсии откатываем последний сегмент (бэктрекинг).

---

## Пример на Python

```python
def restore_ip_addresses(s):
    result = []

    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s):
                result.append(".".join(path))
            return
        for length in range(1, 4):
            if start + length > len(s):
                break
            segment = s[start:start+length]
            if (len(segment) > 1 and segment[0] == '0') or int(segment) > 255:
                continue
            path.append(segment)
            backtrack(start + length, path)
            path.pop()  # Бэктрекинг

    backtrack(0, [])
    return result

# Пример использования:
print(restore_ip_addresses("25525511135"))
# ['255.255.11.135', '255.255.111.35']
```

---

## Сложность

- **Время:** O(1) — число вариантов ограничено длиной IP (4 сегмента × до 3 символов), на практике очень быстро (N ≤ 12).
- **Память:** O(N) — глубина стека рекурсии + место для хранения результата.

---

## Где применяется

- Генерация и валидация IP-адресов из строк (парсинг логов, форм, пользовательских данных).
- Проверка пользовательского ввода и автотестирование сетевых приложений.
- Парсеры и автотесты для сетевых протоколов.
- Поиск всех возможных интерпретаций строки как IP-адреса.

---

## Полезные ссылки

- [Restore IP Addresses — LeetCode (англ.)](https://leetcode.com/problems/restore-ip-addresses/)
- [IPv4 — Википедия](https://ru.wikipedia.org/wiki/IPv4)
- [Бэктрекинг — GeeksforGeeks (англ.)](https://www.geeksforgeeks.org/backtracking-algorithms/)

---

## Практика на LeetCode

| Сложность | Задача                  | Ссылка                                                                        |
|-----------|-------------------------|-------------------------------------------------------------------------------|
| Средняя   | Restore IP Addresses    | [№93 Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)|
| Средняя   | Generate Parentheses    | [№22 Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)|
| Средняя   | Letter Combinations     | [№17 Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)|
| Средняя   | Subsets                 | [№78 Subsets](https://leetcode.com/problems/subsets/)                         |

---