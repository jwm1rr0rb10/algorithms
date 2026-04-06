# Поиск слова (Word Search) — Рекурсия и бэктрекинг

## Где используется поиск слова

Алгоритм поиска слова применяется для поиска заданного слова в двумерной сетке символов (как в кроссворде). Это классическая задача для собеседований и олимпиад. Используется в текстовой обработке, играх, ИИ и анализе данных.

**Примеры применения:**
- Поиск слов в кроссвордах и головоломках
- Проверка наличия слова в поле игры
- Автоматизация создания и решения кроссвордов
- Поиск паттернов в данных (например, биоинформатика)

---

## Сложность алгоритма

- **Временная сложность:**  
  O(N * M * 4^L), где N и M — размеры сетки, L — длина слова  
  (поиск может начинаться с каждой клетки, на каждом шаге 4 направления).

- **Пространственная сложность:**  
  O(L) — глубина рекурсии (или O(N * M) при отдельной visited-матрице).

---

## Пример на Python

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, index):
        if index == len(word):
            return True
        if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]):
            return False

        temp = board[r][c]
        board[r][c] = "#"

        found = (backtrack(r + 1, c, index + 1) or
                 backtrack(r - 1, c, index + 1) or
                 backtrack(r, c + 1, index + 1) or
                 backtrack(r, c - 1, index + 1))

        board[r][c] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                return True
    return False

# Пример использования
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
print(exist(board, "ABCCED"))  # True
print(exist(board, "SEE"))     # True
print(exist(board, "ABCB"))    # False
```

---

### Пояснение к коду

- Функция `backtrack` рекурсивно ищет буквы слова в сетке.
- Временно заменяет символ на `#`, чтобы не посещать клетку повторно.
- Ищет во всех четырех направлениях.
- Возвращает True, если найдено всё слово.

---

## Примеры из жизни

1. **Кроссворды и игры:** Проверка найденных слов.
2. **OCR и обработка изображений:** Поиск последовательностей букв.
3. **Биоинформатика:** Поиск паттернов в ДНК/белках.
4. **Образование:** Автоматическая генерация упражнений на поиск слов.

---

## Полезные ссылки

- [Word Search — LeetCode (англ.)](https://leetcode.com/problems/word-search/)
- [Бэктрекинг — GeeksforGeeks (англ.)](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [Кроссворд — Википедия](https://ru.wikipedia.org/wiki/Кроссворд)

---

## Практика на LeetCode

| Сложность | Задача             | Ссылка                                                                  |
|-----------|--------------------|-------------------------------------------------------------------------|
| Средняя   | Word Search        | [№79 Word Search](https://leetcode.com/problems/word-search/)           |
| Сложная   | Word Search II     | [№212 Word Search II](https://leetcode.com/problems/word-search-ii/)    |
| Средняя   | N-Queens           | [№51 N-Queens](https://leetcode.com/problems/n-queens/)                 |
| Сложная   | Sudoku Solver      | [№37 Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)       |

---