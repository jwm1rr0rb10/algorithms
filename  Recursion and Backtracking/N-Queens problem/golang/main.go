package main

import "fmt"

// solveNQueensHelper - recursive helper function
// row: the current row where we are trying to place a queen
// n: the size of the board
// board: a one-dimensional array, board[r] = c means the queen is at row r, column c
// colUsed: boolean array for tracking occupied columns
// diag1Used: boolean array for tracking occupied main diagonals (r - c)
// diag2Used: boolean array for tracking occupied anti-diagonals (r + c)
// result: a slice of slices of strings, where all found solutions are stored
func solveNQueensHelper(row int, n int, board []int, colUsed []bool, diag1Used []bool, diag2Used []bool, result *[][]string) {
	// Base case: if we've successfully placed queens in all N rows
	if row == n {
		// We found one solution. Convert board to a []string format
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
		// Add a copy of the solution to the result
		*result = append(*result, solution)
		return
	}

	// Recursive step: try to place a queen in the current row 'row'
	// Iterate over all possible columns 'col'
	for col := 0; col < n; col++ {
		// Check if the cell (row, col) is safe
		diag1Index := row - col + (n - 1) // Offset for the main diagonal
		diag2Index := row + col           // Index for the anti-diagonal

		if !colUsed[col] && !diag1Used[diag1Index] && !diag2Used[diag2Index] {
			// 1. Choice: place the queen at (row, col) and mark it as used
			board[row] = col
			colUsed[col] = true
			diag1Used[diag1Index] = true
			diag2Used[diag2Index] = true

			// 2. Explore: recursively call for the next row
			solveNQueensHelper(row+1, n, board, colUsed, diag1Used, diag2Used, result)

			// 3. Undo the choice (Backtracking): remove the queen and mark as unused
			// (No need to reset board[row], as the next iteration will overwrite it)
			colUsed[col] = false
			diag1Used[diag1Index] = false
			diag2Used[diag2Index] = false
		}
	}
}

// SolveNQueens - main function to solve the N-Queens problem
func SolveNQueens(n int) [][]string {
	var result [][]string
	// board[i] = j means the queen in row i is at column j
	board := make([]int, n)
	// Arrays to track occupied columns and diagonals
	colUsed := make([]bool, n)
	diag1Used := make([]bool, 2*n-1) // r - c + (n - 1) -> range [0, 2n-2]
	diag2Used := make([]bool, 2*n-1) // r + c -> range [0, 2n-2]

	solveNQueensHelper(0, n, board, colUsed, diag1Used, diag2Used, &result)
	return result
}

func main() {
	n := 4
	solutions := SolveNQueens(n)
	fmt.Printf("Found %d solutions for %d queens:\n", len(solutions), n)
	for i, sol := range solutions {
		fmt.Printf("Solution %d:\n", i+1)
		for _, row := range sol {
			fmt.Println(row)
		}
		fmt.Println()
	}

	n2 := 1
	solutions2 := SolveNQueens(n2)
	fmt.Printf("Found %d solutions for %d queen:\n", len(solutions2), n2)
	for i, sol := range solutions2 {
		fmt.Printf("Solution %d:\n", i+1)
		for _, row := range sol {
			fmt.Println(row)
		}
		fmt.Println()
	}
}
