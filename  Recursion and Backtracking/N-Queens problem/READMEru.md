# Задача о N-Ферзях — Рекурсия и Бэктрекинг

## Что такое задача о N-ферзях?

В задаче о N-ферзях требуется расставить N шахматных ферзей на шахматной доске N×N так, чтобы ни один ферзь не бил другого. Ферзь угрожает по горизонтали, вертикали и диагоналям, значит, в решении ни в одной строке, столбце или диагонали не может быть двух ферзей.

Обычно задача требует найти все возможные расстановки.

---

## Решение с помощью рекурсии и бэктрекинга

Это классический пример для применения рекурсии и бэктрекинга. Алгоритм поочередно расставляет ферзей по строкам, размещая их только в безопасных клетках и возвращаясь назад (бэктрекинг), если частичное решение нельзя продолжить.

### Основные шаги:

1. **Перебираем строки**. Начинаем с 0-й строки, пробуем все столбцы.
2. **Для каждой клетки (строка, столбец)**:
   - Проверяем, не бьют ли уже расставленные ферзи выбранную позицию (тот же столбец, главная или побочная диагональ).
3. **Если безопасно:**
   - Ставим ферзя.
   - Переходим к следующей строке (рекурсивно).
4. **Если не безопасно или нет вариантов:**
   - Возвращаемся назад (снимаем ферзя, пробуем следующий столбец).
5. **Базовый случай:** Если ферзи расставлены во всех N строках — сохраняем решение.

Для проверки конфликтов используем массивы/множества для столбцов и диагоналей.

---

## Представление доски и конфликтов

- **Столбцы:** `cols[N]`, true если столбец c занят.
- **Главные диагонали:** Индекс `row - col + (N-1)` (от 0 до 2N-2).
- **Побочные диагонали:** Индекс `row + col` (от 0 до 2N-2).
- **Доска:** 1D-массив, где `board[r] = c` — ферзь в строке r, столбце c.

---

## Пример реализации — Go

```go
package main

import "fmt"

func solveNQueensHelper(row int, n int, board []int, colUsed []bool, diag1Used []bool, diag2Used []bool, result *[][]string) {
	if row == n {
		solution := make([]string, n)
		for r := 0; r < n; r++ {
			rowStr := ""
			for c := 0; c < n; c++ {
				if board[r] == c {
					rowStr += "Q"
				} else {
					rowStr += "."
				}
			}
			solution[r] = rowStr
		}
		*result = append(*result, solution)
		return
	}
	for col := 0; col < n; col++ {
		diag1 := row - col + (n - 1)
		diag2 := row + col
		if !colUsed[col] && !diag1Used[diag1] && !diag2Used[diag2] {
			board[row] = col
			colUsed[col], diag1Used[diag1], diag2Used[diag2] = true, true, true
			solveNQueensHelper(row+1, n, board, colUsed, diag1Used, diag2Used, result)
			colUsed[col], diag1Used[diag1], diag2Used[diag2] = false, false, false
		}
	}
}

func SolveNQueens(n int) [][]string {
	var result [][]string
	board := make([]int, n)
	colUsed := make([]bool, n)
	diag1Used := make([]bool, 2*n-1)
	diag2Used := make([]bool, 2*n-1)
	solveNQueensHelper(0, n, board, colUsed, diag1Used, diag2Used, &result)
	return result
}

func main() {
	n := 4
	solutions := SolveNQueens(n)
	fmt.Printf("Найдено %d решений для %d ферзей:\n", len(solutions), n)
	for i, sol := range solutions {
		fmt.Printf("Решение %d:\n", i+1)
		for _, row := range sol {
			fmt.Println(row)
		}
		fmt.Println()
	}
}
```

---

## Пример реализации — Python

```python
def solve_nqueens(n):
    result = []
    board = [-1] * n
    col_used = set()
    diag1_used = set()
    diag2_used = set()

    def backtrack(row):
        if row == n:
            solution = []
            for r in range(n):
                row_str = "".join('Q' if board[r] == c else '.' for c in range(n))
                solution.append(row_str)
            result.append(solution)
            return
        for col in range(n):
            if col in col_used or (row-col) in diag1_used or (row+col) in diag2_used:
                continue
            board[row] = col
            col_used.add(col)
            diag1_used.add(row-col)
            diag2_used.add(row+col)
            backtrack(row+1)
            board[row] = -1
            col_used.remove(col)
            diag1_used.remove(row-col)
            diag2_used.remove(row+col)
    backtrack(0)
    return result

# Пример использования:
for n in [4, 1]:
    solutions = solve_nqueens(n)
    print(f"Найдено {len(solutions)} решений для {n} ферзей:")
    for i, sol in enumerate(solutions):
        print(f"Решение {i+1}:")
        for row in sol:
            print(row)
        print()
```

---

## Сложность

| Метрика           | Сложность                                   | Пояснение                                                                                  |
|-------------------|---------------------------------------------|-------------------------------------------------------------------------------------------|
| **Время**         | Экспоненциальная (лучше, чем O(N^N))        | Благодаря отсечкам не исследуются все варианты; точная формула сложна, но экспоненциально.|
| **Память (стек)** | O(N)                                        | Для стека вызовов и хранения доски/множеств.                                              |
| **Память (итого)**| O(N + A(N) × N^2)                           | С учетом хранения всех решений; A(N) — число валидных расстановок, быстро растет с N.     |

---

## Бэктрекинг с проверкой ограничений: Где применяется

Этот паттерн (поиск с возвратом и проверкой ограничений) лежит в основе **задач удовлетворения ограничений (Constraint Satisfaction Problems, CSP)**:

- **Расписание и планирование:** Учебные расписания, смены сотрудников, производственные процессы, распределение ресурсов.
- **Компоновка и конфигурация:** Размещение объектов, конфигурирование ПО/оборудования.
- **Простая логистика:** Поиск маршрутов для малого N.
- **Игры и головоломки:** Судоку, КенКен, логические игры.
- **Парсинг и анализ:** Некоторые алгоритмы разбора неоднозначных грамматик.

Бэктрекинг с отсечками позволяет эффективно исследовать пространство решений: если частичное решение нарушает ограничения, ветвь сразу отбрасывается.

---

# Полезные ссылки

- [Задача о восьми ферзях — Википедия](https://ru.wikipedia.org/wiki/Задача_о_восьми_ферзях)
- [Бэктрекинг — GeeksforGeeks (англ.)](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [Задача удовлетворения ограничений — Википедия](https://ru.wikipedia.org/wiki/Задача_удовлетворения_ограничений)
- [LeetCode: Курс по рекурсии (англ.)](https://leetcode.com/explore/learn/card/recursion-i/)

---

# Практика на LeetCode

| Сложность | Задача                                  | Ссылка                                                                                  |
|-----------|-----------------------------------------|-----------------------------------------------------------------------------------------|
| Средняя   | N-Queens                               | [№51 N-Queens](https://leetcode.com/problems/n-queens/)                                 |
| Сложная   | N-Queens II (подсчет решений)           | [№52 N-Queens II](https://leetcode.com/problems/n-queens-ii/)                           |
| Средняя   | Sudoku Solver                           | [№37 Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)                       |
| Средняя   | Word Search                             | [№79 Word Search](https://leetcode.com/problems/word-search/)                           |
| Сложная   | Word Search II                          | [№212 Word Search II](https://leetcode.com/problems/word-search-ii/)                    |
| Средняя   | Combination Sum                         | [№39 Combination Sum](https://leetcode.com/problems/combination-sum/)                   |
| Средняя   | Combination Sum II                      | [№40 Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)             |
| Средняя   | Subsets                                 | [№78 Subsets](https://leetcode.com/problems/subsets/)                                   |
| Средняя   | Subsets II                              | [№90 Subsets II](https://leetcode.com/problems/subsets-ii/)                             |

---