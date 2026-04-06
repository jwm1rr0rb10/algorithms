# Сочетания (Combinations) — Рекурсия и бэктрекинг

## Описание задачи

Даны два числа: **n** и **k**.  
Требуется вернуть все возможные сочетания из k различных чисел из диапазона от 1 до n включительно (без повторений, порядок внутри комбинации не важен).

**Пример:**  
Ввод: n = 4, k = 2  
Вывод:  
```
[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4]
]
```

---

## Идея и подход

- Формируем частичную комбинацию (path).
- На каждом шаге добавляем следующее число от текущего start до n.
- Как только длина комбинации становится равной k — сохраняем результат.
- После возврата из рекурсии убираем последний элемент (бэктрекинг).

---

## Пример на Python

```python
def combine(n, k):
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(list(path))
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result

# Пример использования:
print(combine(4, 2))
# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
```

---

## Сложность

- **Время:** O(C(n, k) * k), где C(n, k) — биномиальный коэффициент, число вариантов сочетаний.
- **Память:** O(k) — глубина рекурсии + место для хранения результата.

---

## Где применяется

- Генерация вариантов для поиска, перебора, тестирования.
- Задачи оптимизации, динамическое программирование.
- Математика и комбинаторика (сочетания без повторений).
- Составление команд, выборка данных, генерация вариантов.

---

## Полезные ссылки

- [Combinations — LeetCode (англ.)](https://leetcode.com/problems/combinations/)
- [Сочетания — Википедия](https://ru.wikipedia.org/wiki/Сочетание)
- [Бэктрекинг — GeeksforGeeks (англ.)](https://www.geeksforgeeks.org/backtracking-algorithms/)

---

## Практика на LeetCode

| Сложность | Задача           | Ссылка                                                              |
|-----------|------------------|---------------------------------------------------------------------|
| Средняя   | Combinations     | [№77 Combinations](https://leetcode.com/problems/combinations/)      |
| Средняя   | Combination Sum  | [№39 Combination Sum](https://leetcode.com/problems/combination-sum/)|
| Средняя   | Subsets          | [№78 Subsets](https://leetcode.com/problems/subsets/)                |
| Средняя   | Permutations     | [№46 Permutations](https://leetcode.com/problems/permutations/)      |

---