package main

import "fmt"

// isSafe - checks whether it's safe to place `num` in board[row][col]
func isSafe(board [][]int, row, col, num int) bool {
	n := len(board)

	// Check the row
	for c := 0; c < n; c++ {
		if board[row][c] == num {
			return false
		}
	}

	// Check the column
	for r := 0; r < n; r++ {
		if board[r][col] == num {
			return false
		}
	}

	// Check the 3x3 subgrid
	startRow := (row / 3) * 3
	startCol := (col / 3) * 3
	for r := startRow; r < startRow+3; r++ {
		for c := startCol; c < startCol+3; c++ {
			if board[r][c] == num {
				return false
			}
		}
	}

	return true // No conflicts found
}

// findEmptyLocation - finds the next empty cell (denoted by 0)
// Returns true and coordinates if found, false and (-1, -1) if not found
func findEmptyLocation(board [][]int) (bool, int, int) {
	n := len(board)
	for r := 0; r < n; r++ {
		for c := 0; c < n; c++ {
			if board[r][c] == 0 {
				return true, r, c
			}
		}
	}
	return false, -1, -1 // No empty cells left
}

// SolveSudoku - the main recursive function to solve the Sudoku puzzle
// Returns true if a solution is found; false otherwise (and the board will be modified)
func SolveSudoku(board [][]int) bool {
	// 1. Find the next empty cell
	found, row, col := findEmptyLocation(board)

	// 2. Base case: if no empty cells, the puzzle is solved
	if !found {
		return true
	}

	// 3. Try digits from 1 to 9
	for num := 1; num <= 9; num++ {
		if isSafe(board, row, col, num) {
			// 4. Make a choice: place the digit
			board[row][col] = num

			// 5. Recursively attempt to solve the updated board
			if SolveSudoku(board) {
				return true // If recursion succeeds, return true
			}

			// 6. Undo the choice (Backtracking): if recursion failed,
			// reset the cell and try the next digit
			board[row][col] = 0
		}
	}

	// 7. If no digit from 1 to 9 leads to a solution, return false
	return false
}

// printBoard - helper function to print the board
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
