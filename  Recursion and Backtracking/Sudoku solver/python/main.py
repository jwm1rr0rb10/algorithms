def is_safe(board, row, col, num):
    n = len(board)

    # Check the row
    for c in range(n):
        if board[row][c] == num:
            return False

    # Check the column
    for r in range(n):
        if board[r][col] == num:
            return False

    # Check the 3x3 block
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True  # No conflicts found

def find_empty_location(board):
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == 0:  # We assume 0 means an empty cell
                return True, r, c
    return False, -1, -1  # No empty cells found

def solve_sudoku(board):
    # 1. Find the next empty cell
    found, row, col = find_empty_location(board)

    # 2. Base case: if no empty cells, the board is solved
    if not found:
        return True

    # 3. Try digits 1 through 9
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            # 4. Make a choice
            board[row][col] = num

            # 5. Explore further with recursion
            if solve_sudoku(board):
                return True  # Success

            # 6. Undo the choice (backtracking)
            board[row][col] = 0

    # 7. No valid number found for this cell
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

# Example of an unsolvable board (for demonstration)
# board_unsolvable = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 5],  # Changed 9 to 5 to make it unsolvable
# ]
# print("\nUnsolvable Sudoku Board:")
# print_board(board_unsolvable)
# if solve_sudoku(board_unsolvable):
#     print("\nSolved Unsolvable Board:")
#     print_board(board_unsolvable)
# else:
#     print("\nNo solution exists for this unsolvable board.")