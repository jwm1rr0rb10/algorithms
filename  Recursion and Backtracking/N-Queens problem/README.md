# N-Queens Problem — Recursion and Backtracking

## What is the N-Queens problem?

The N-Queens problem asks: How can you place N chess queens on an N×N chessboard so that no two queens threaten each other? Queens attack horizontally, vertically, and diagonally, so no two queens can share a row, column, or diagonal.

The goal is typically to find all possible valid arrangements.

---

## Backtracking and Recursion Approach

This problem is a classic use case for recursion and backtracking. The algorithm incrementally builds a solution row by row, placing queens where they're not under threat and backtracking if a partial solution can't be completed.

### Steps:

1. **Place queens row by row**. Start with row 0, try every column.
2. **For each cell (row, col):**
   - Check if any previously placed queen threatens this position (same column, same main diagonal, or same anti-diagonal).
3. **If safe:**
   - Place the queen.
   - Move to the next row (recursive call).
4. **If not safe or out of options:**
   - Backtrack (remove the queen, try next column).
5. **Base case:** If you successfully place queens in all N rows, record the solution (board configuration).

Efficient conflict checking is done by tracking columns and diagonals with arrays/sets.

---

## Board and Conflict Representation

- **Columns:** `cols[N]`, true if column c is occupied.
- **Main diagonals:** Index is `row - col + (N-1)` (range: 0 to 2N-2).
- **Anti-diagonals:** Index is `row + col` (range: 0 to 2N-2).
- **Board:** A 1D array, where `board[r] = c` means a queen at row r, column c.

---

## Example Implementation — Go

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
	fmt.Printf("Found %d solutions for %d queens:\n", len(solutions), n)
	for i, sol := range solutions {
		fmt.Printf("Solution %d:\n", i+1)
		for _, row := range sol {
			fmt.Println(row)
		}
		fmt.Println()
	}
}
```

---

## Example Implementation — Python

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

# Example usage:
for n in [4, 1]:
    solutions = solve_nqueens(n)
    print(f"Found {len(solutions)} solutions for {n} queens:")
    for i, sol in enumerate(solutions):
        print(f"Solution {i+1}:")
        for row in sol:
            print(row)
        print()
```

---

## Complexity

| Metric             | Complexity                                      | Explanation                                                                                                      |
|--------------------|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| **Time**           | Exponential (better than O(N^N))                | Prunes many branches; exact count is complex, but it's exponential in N.                                         |
| **Space (Auxiliary)** | O(N)                                         | For call stack and board/sets.                                                                                   |
| **Space (Total)**  | O(N + A(N) × N^2)                               | Includes all solutions; A(N) is the number of valid arrangements (grows rapidly with N).                         |

---

## Backtracking with Constraints: Real-World Applications

The backtracking + constraint-checking pattern is fundamental for **Constraint Satisfaction Problems (CSPs)** including:

- **Scheduling & Planning**: Courses, employee shifts, production, resource allocation.
- **Layout & Configuration**: Object placement, system configuration.
- **Simplified Logistics**: Route finding for small N.
- **Game & Puzzle AI**: Sudoku, KenKen, logic puzzles.
- **Parsing & Analysis**: Some parsing algorithms for ambiguous grammars.

Backtracking enables smart exploration: as soon as a partial solution violates constraints, it backtracks immediately, avoiding wasted computation.

---

# Useful Links

- [N-Queens Problem — Wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
- [Backtracking — GeeksforGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [Constraint Satisfaction Problem — Wikipedia](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem)
- [LeetCode Explore Card: Recursion](https://leetcode.com/explore/learn/card/recursion-i/)

---

# LeetCode Practice

| Difficulty | Problem                                              | Link                                                                                 |
|------------|------------------------------------------------------|--------------------------------------------------------------------------------------|
| Medium     | N-Queens                                             | [#51 N-Queens](https://leetcode.com/problems/n-queens/)                              |
| Hard       | N-Queens II (count solutions)                        | [#52 N-Queens II](https://leetcode.com/problems/n-queens-ii/)                        |
| Medium     | Sudoku Solver                                        | [#37 Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)                    |
| Medium     | Word Search                                          | [#79 Word Search](https://leetcode.com/problems/word-search/)                        |
| Hard       | Word Search II                                       | [#212 Word Search II](https://leetcode.com/problems/word-search-ii/)                 |
| Medium     | Combination Sum                                      | [#39 Combination Sum](https://leetcode.com/problems/combination-sum/)                |
| Medium     | Combination Sum II                                   | [#40 Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)          |
| Medium     | Subsets                                              | [#78 Subsets](https://leetcode.com/problems/subsets/)                                |
| Medium     | Subsets II                                           | [#90 Subsets II](https://leetcode.com/problems/subsets-ii/)                          |

---