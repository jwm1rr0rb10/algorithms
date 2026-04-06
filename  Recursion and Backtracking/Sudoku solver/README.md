# Sudoku (Sudoku Solver) — Recursive Backtracking Approach

## What is Sudoku?

Sudoku is a logic-based number puzzle. The goal is to fill a 9×9 grid with digits from 1 to 9 so that each digit appears **exactly once** in every row, every column, and each of the nine 3×3 subgrids. Some cells in the grid are initially filled in.

---

## How to Apply Backtracking to Solve Sudoku?

Backtracking is ideal for Sudoku. The algorithm fills empty cells one by one, checking validity at each step and backtracking if a dead end is reached.

### Backtracking Steps

1. **Find an Empty Cell**: Locate the next empty cell (typically scan left-to-right, top-to-bottom).
2. **Base Case**: If there are no empty cells, the board is solved.
3. **Try Digits 1–9**: For each empty cell, try digits 1–9.
   - For each digit, check if it is safe (not already in the same row, column, or 3×3 block).
4. **Explore**: If valid, place the digit and recursively solve the updated board.
5. **Backtrack**: If a choice fails, remove the digit and try the next one.
6. **Failure**: If no digit fits, return failure up the call stack.

---

## Board Representation

Use a 2D array (9×9) where `0` (or `.`) means empty.

---

## Validity Check

A helper function checks if a number can be safely placed in a given cell by checking:
- The row
- The column
- The 3×3 subgrid (top-left corner: `(row//3)*3`, `(col//3)*3`)

---

## Go Example

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

	fmt.Println("Initial Sudoku Board:")
	printBoard(board)

	if SolveSudoku(board) {
		fmt.Println("\nSolved Sudoku Board:")
		printBoard(board)
	} else {
		fmt.Println("\nNo solution exists for the given Sudoku board.")
	}
}
```

---

## Python Example

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

# Example usage:
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

print("Initial Sudoku Board:")
print_board(board)

if solve_sudoku(board):
    print("\nSolved Sudoku Board:")
    print_board(board)
else:
    print("\nNo solution exists for this Sudoku board.")
```

---

## Complexity Analysis

| Metric                | Complexity         | Explanation                                                     |
|:----------------------|:------------------|:----------------------------------------------------------------|
| **Time Complexity**   | Exponential (in # of empty cells) | Worst case O(9^E), E = number of empty cells. Pruning helps a lot. |
| **Space Complexity**  | O(N²)             | Recursion stack and board storage.                              |

---

## Production Applications

- Sudoku solvers/generators (apps, websites)
- **Constraint Satisfaction Problems (CSPs)**:  
  - Graph coloring
  - Product/system configuration
  - Test data generation
  - Resource allocation with discrete choices
  - Other grid-based logic puzzles (Kakuro, Hitori, etc.)

---

## Useful Links

- [Sudoku — Wikipedia](https://en.wikipedia.org/wiki/Sudoku)
- [Sudoku Solver — LeetCode](https://leetcode.com/problems/sudoku-solver/)
- [Backtracking — GeeksforGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [Constraint Satisfaction Problem](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem)

---

## LeetCode Practice

| Difficulty | Problem             | Link                                                               |
|------------|---------------------|--------------------------------------------------------------------|
| Hard       | Sudoku Solver       | [#37 Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)  |
| Medium     | Word Search         | [#79 Word Search](https://leetcode.com/problems/word-search/)      |
| Hard       | Word Search II      | [#212 Word Search II](https://leetcode.com/problems/word-search-ii/)|
| Medium     | N-Queens            | [#51 N-Queens](https://leetcode.com/problems/n-queens/)            |

---