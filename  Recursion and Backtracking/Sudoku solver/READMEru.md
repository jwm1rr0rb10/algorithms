# Судоку (Sudoku Solver) — Решение с помощью рекурсивного бэктрекинга

## Что такое Судоку?

Судоку — это логическая числовая головоломка. Цель — заполнить сетку 9×9 цифрами от 1 до 9 так, чтобы каждая цифра встречалась **ровно один раз** в каждой строке, каждом столбце и каждом из девяти 3×3 блоков. Некоторые клетки изначально заполнены.

---

## Как применять бэктрекинг для решения Судоку?

Бэктрекинг идеально подходит для Судоку. Алгоритм поочередно заполняет пустые клетки, проверяя корректность каждого шага и возвращаясь назад, если выбранный путь ведет к тупику.

### Шаги бэктрекинга

1. **Найти пустую клетку:** Найти следующую пустую клетку (обычно сканирование слева направо, сверху вниз).
2. **Базовый случай:** Если пустых клеток не осталось — доска решена.
3. **Пробовать цифры 1–9:** Для каждой пустой клетки попробовать цифры 1–9.
   - Для каждой цифры проверить, можно ли ее поставить (нет ли уже такой цифры в строке, столбце или 3×3 блоке).
4. **Исследование:** Если цифра допустима, поставить ее и рекурсивно решать обновленную доску.
5. **Откат (бэктрекинг):** Если вариант не сработал — стереть цифру и попробовать следующую.
6. **Неудача:** Если ни одна цифра не подходит — возвращаем неудачу на уровень выше.

---

## Представление доски

Используется двумерный массив (9×9), где `0` (или `'.'`) означает пустую клетку.

---

## Проверка допустимости

Вспомогательная функция проверяет, можно ли поставить число в клетку:
- В строке
- В столбце
- В 3×3 блоке (верхний левый угол: `(row//3)*3`, `(col//3)*3`)

---

## Пример на Go

```go
package main

import "fmt"

func isSafe(board [][]int, row, col, num int) bool {
	n := len(board)
	for c := 0; c < n; c++ {
		if board[row][c] == num {
			return false
		}
	}
	for r := 0; r < n; r++ {
		if board[r][col] == num {
			return false
		}
	}
	startRow := (row / 3) * 3
	startCol := (col / 3) * 3
	for r := startRow; r < startRow+3; r++ {
		for c := startCol; c < startCol+3; c++ {
			if board[r][c] == num {
				return false
			}
		}
	}
	return true
}

func findEmptyLocation(board [][]int) (bool, int, int) {
	n := len(board)
	for r := 0; r < n; r++ {
		for c := 0; c < n; c++ {
			if board[r][c] == 0 {
				return true, r, c
			}
		}
	}
	return false, -1, -1
}

func SolveSudoku(board [][]int) bool {
	found, row, col := findEmptyLocation(board)
	if !found {
		return true
	}
	for num := 1; num <= 9; num++ {
		if isSafe(board, row, col, num) {
			board[row][col] = num
			if SolveSudoku(board) {
				return true
			}
			board[row][col] = 0
		}
	}
	return false
}

func printBoard(board [][]int) {
	n := len(board)
	for r := 0; r < n; r++ {
		for c := 0; c < n; c++ {
			fmt.Printf("%d ", board[r][c])
			if (c+1)%3 == 0 && c < n-1 {
				fmt.Print("| ")
			}
		}
		fmt.Println()
		if (r+1)%3 == 0 && r < n-1 {
			fmt.Println("----------------------")
		}
	}
}

func main() {
	board := [][]int{
		{5, 3, 0, 0, 7, 0, 0, 0, 0},
		{6, 0, 0, 1, 9, 5, 0, 0, 0},
		{0, 9, 8, 0, 0, 0, 0, 6, 0},
		{8, 0, 0, 0, 6, 0, 0, 0, 3},
		{4, 0, 0, 8, 0, 3, 0, 0, 1},
		{7, 0, 0, 0, 2, 0, 0, 0, 6},
		{0, 6, 0, 0, 0, 0, 2, 8, 0},
		{0, 0, 0, 4, 1, 9, 0, 0, 5},
		{0, 0, 0, 0, 8, 0, 0, 7, 9},
	}

	fmt.Println("Исходная доска Судоку:")
	printBoard(board)

	if SolveSudoku(board) {
		fmt.Println("\nРешенная доска Судоку:")
		printBoard(board)
	} else {
		fmt.Println("\nДля этой доски решения не существует.")
	}
}
```

---

## Пример на Python

```python
def is_safe(board, row, col, num):
    n = len(board)
    for c in range(n):
        if board[row][c] == num:
            return False
    for r in range(n):
        if board[r][col] == num:
            return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True

def find_empty_location(board):
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == 0:
                return True, r, c
    return False, -1, -1

def solve_sudoku(board):
    found, row, col = find_empty_location(board)
    if not found:
        return True
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def print_board(board):
    n = len(board)
    for r in range(n):
        for c in range(n):
            print(board[r][c], end=" ")
            if (c + 1) % 3 == 0 and c < n - 1:
                print("| ", end="")
        print()
        if (r + 1) % 3 == 0 and r < n - 1:
            print("----------------------")

# Пример использования:
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

print("Исходная доска Судоку:")
print_board(board)

if solve_sudoku(board):
    print("\nРешенная доска Судоку:")
    print_board(board)
else:
    print("\nДля этой доски решения не существует.")
```

---

## Анализ сложности

| Метрика           | Сложность           | Пояснение                                         |
|:------------------|:-------------------|:--------------------------------------------------|
| **Время**         | Экспоненциальная (по числу пустых клеток) | В худшем случае O(9^E), где E — число пустых клеток. Благодаря отсечкам работает гораздо быстрее на реальных задачах. |
| **Память**        | O(N²)              | Стек рекурсии и сама доска.                       |

---

## Применение в продакшене

- Решатели/генераторы судоку (мобильные приложения, сайты).
- **Задачи удовлетворения ограничений (CSP):**
  - Раскраска графа
  - Конфигурирование продуктов/систем
  - Генерация тестовых данных
  - Дискретное распределение ресурсов
  - Другие головоломки на сетке (Какуро, Хитори и др.)

---

## Полезные ссылки

- [Судоку — Википедия](https://ru.wikipedia.org/wiki/Судоку)
- [Sudoku Solver — LeetCode (англ.)](https://leetcode.com/problems/sudoku-solver/)
- [Бэктрекинг — GeeksforGeeks (англ.)](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [Задача удовлетворения ограничений — Википедия](https://ru.wikipedia.org/wiki/Задача_удовлетворения_ограничений)

---

## Практика на LeetCode

| Сложность | Задача               | Ссылка                                                                   |
|-----------|----------------------|--------------------------------------------------------------------------|
| Сложная   | Sudoku Solver        | [№37 Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)        |
| Средняя   | Word Search          | [№79 Word Search](https://leetcode.com/problems/word-search/)            |
| Сложная   | Word Search II       | [№212 Word Search II](https://leetcode.com/problems/word-search-ii/)     |
| Средняя   | N-Queens             | [№51 N-Queens](https://leetcode.com/problems/n-queens/)                  |

---