def solve_nqueens(n):
    result = []
    # board[i] = j means that the queen in row i is in column j
    # board represents the current configuration of queens
    board = [-1] * n  # We use -1 to denote an empty row or column for the queen

    # Using sets to simplify tracking occupied positions
    col_used = set()
    diag1_used = set()  # Main diagonal: r - c
    diag2_used = set()  # Secondary diagonal: r + c

    def backtrack(row):
        # Base case: if we have successfully placed queens in all N rows
        if row == n:
            # We found one solution. Convert the board to a list of strings
            solution = []
            for r in range(n):
                row_str = ""
                for c in range(n):
                    if board[r] == c:
                        row_str += "Q"
                    else:
                        row_str += "."
                solution.append(row_str)
            # Add a copy of the solution to the result
            result.append(solution)
            return

        # Recursive step: trying to place a queen in the current row 'row'
        # Iterate through all possible columns 'col'
        for col in range(n):
            # Check if the cell (row, col) is safe
            if col not in col_used and \
               (row - col) not in diag1_used and \
               (row + col) not in diag2_used:

                # 1. Choice: place the queen at (row, col) and mark it as used
                board[row] = col
                col_used.add(col)
                diag1_used.add(row - col)
                diag2_used.add(row + col)

                # 2. Exploration: recursively call for the next row
                backtrack(row + 1)

                # 3. Undo choice (Backtracking): remove the queen and mark it as unused
                board[row] = -1  # This can be reset or left, as it will be overwritten
                col_used.remove(col)
                diag1_used.remove(row - col)
                diag2_used.remove(row + col)

    backtrack(0)  # Start from the first row (index 0)
    return result

# Example usage:
n1 = 4
solutions1 = solve_nqueens(n1)
print(f"Found {len(solutions1)} solutions for {n1} queens:")
for i, sol in enumerate(solutions1):
    print(f"Solution {i+1}:")
    for row in sol:
        print(row)
    print()

n2 = 1
solutions2 = solve_nqueens(n2)
print(f"Found {len(solutions2)} solutions for {n2} queen:")
for i, sol in enumerate(solutions2):
    print(f"Solution {i+1}:")
    for row in sol:
        print(row)
    print()