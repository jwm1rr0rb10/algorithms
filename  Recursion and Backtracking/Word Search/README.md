# Word Search Algorithm — Recursion and Backtracking

## Where Word Search is Used

The Word Search algorithm is used to find a given word in a 2D grid of characters (like in a crossword puzzle). It's a classic interview and competitive programming task. It's applied in text processing, games, AI, and data analysis.

**Examples of application:**
- Finding words in crosswords and puzzles
- Verifying the presence of a word in a letter grid in games
- Automating crossword creation and solving
- Pattern search in data (e.g., bioinformatics)

---

## Algorithm Complexity

- **Time Complexity:**  
  O(N * M * 4^L), where N and M are grid sizes, L is the word length  
  (since search can start from each cell, and at each step we can go in 4 directions).

- **Space Complexity:**  
  O(L) — recursion depth (or O(N * M) if we keep a separate visited matrix).

---

## Python Example

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

# Example usage
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

### Code Explanation

- The `backtrack` function recursively searches for the word's letters in the grid.
- Temporarily replaces the character with `#` to avoid revisiting.
- Searches in all four directions.
- Returns True if the whole word is found.

---

## Real-Life Examples

1. **Crosswords and Games:** Validating found words.
2. **OCR and Image Processing:** Finding sequences of letters.
3. **Bioinformatics:** Searching for patterns in DNA/protein sequences.
4. **Education:** Automatically generating word search exercises.

---

## Useful Links

- [Word Search — LeetCode](https://leetcode.com/problems/word-search/)
- [Backtracking — GeeksforGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [Crossword Puzzle — Wikipedia](https://en.wikipedia.org/wiki/Crossword)

---

## LeetCode Practice

| Difficulty | Problem            | Link                                                            |
|------------|--------------------|-----------------------------------------------------------------|
| Medium     | Word Search        | [#79 Word Search](https://leetcode.com/problems/word-search/)   |
| Hard       | Word Search II     | [#212 Word Search II](https://leetcode.com/problems/word-search-ii/) |
| Medium     | N-Queens           | [#51 N-Queens](https://leetcode.com/problems/n-queens/)         |
| Hard       | Sudoku Solver      | [#37 Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)|

---