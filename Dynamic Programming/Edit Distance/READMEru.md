# Edit Distance — Динамическое программирование

## Описание задачи

Даны две строки `word1` и `word2`. Нужно найти минимальное количество операций для преобразования строки `word1` в строку `word2`.  
Допустимые операции:  
- Вставка символа  
- Удаление символа  
- Замена символа  

**Пример:**  
Вход: word1 = "horse", word2 = "ros"  
Выход: 3  
Пояснение:  
"horse" → "rorse" (замена 'h' на 'r')  
"rorse" → "rose" (удаление 'r')  
"rose" → "ros" (удаление 'e')

---

## Идея и подход

- Используем динамическое программирование с таблицей `dp[i][j]`, где dp[i][j] — минимальная стоимость преобразования первых i символов `word1` в первые j символов `word2`.
- Если текущие символы совпадают, операция не требуется.
- Иначе рассматриваем минимум среди операций вставки, удаления и замены.
- Базовые случаи: преобразование пустой строки в префикс другой (только вставки/удаления).

---

## Пример на Python

```python
def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Заполнение базовых случаев
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Основное динамическое программирование
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     # удаление
                    dp[i][j - 1],     # вставка
                    dp[i - 1][j - 1]  # замена
                )
    return dp[m][n]

# Пример использования:
print(minDistance("horse", "ros"))  # Вывод: 3
```

---

## Анализ сложности

- **Время:** O(m * n), где m и n — длины строк.
- **Память:** O(m * n), можно оптимизировать до O(min(m, n)).

---

## Применения

- Проверка орфографии и автокоррекция
- Выравнивание ДНК/белковых последовательностей в биоинформатике
- Проверка на плагиат
- Diff-инструменты и системы контроля версий

---

## Полезные ссылки

- [Edit Distance — LeetCode](https://leetcode.com/problems/edit-distance/)
- [Динамическое программирование — GeeksforGeeks (en)](https://www.geeksforgeeks.org/edit-distance-dp-5/)
- [Wikipedia: Расстояние Левенштейна](https://ru.wikipedia.org/wiki/Расстояние_Левенштейна)

---

## LeetCode — задачи для практики

| Сложность | Задача                                             | Ссылка                                                                                 |
|-----------|----------------------------------------------------|----------------------------------------------------------------------------------------|
| Сложная   | Edit Distance                                      | [#72 Edit Distance](https://leetcode.com/problems/edit-distance/)                      |
| Средняя   | Delete Operation for Two Strings                   | [#583 Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) |
| Средняя   | Minimum ASCII Delete Sum for Two Strings           | [#712 Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) |

---