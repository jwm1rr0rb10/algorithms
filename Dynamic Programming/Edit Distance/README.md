# Edit Distance — Dynamic Programming

## Problem Description

Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` into `word2`.  
Allowed operations are:  
- Insert a character  
- Delete a character  
- Replace a character  

**Example:**  
Input: word1 = "horse", word2 = "ros"  
Output: 3  
Explanation:  
"horse" → "rorse" (replace 'h' with 'r')  
"rorse" → "rose" (remove 'r')  
"rose" → "ros" (remove 'e')

---

## Algorithm Idea and Approach

- Use dynamic programming with a DP table `dp[i][j]` representing the minimum edit distance between `word1[:i]` and `word2[:j]`.
- If the current characters are equal, no operation is needed.
- Otherwise, consider the minimum among insert, delete, or replace.
- Base cases: transforming an empty string to a prefix (deletes/inserts).

---

## Python Example

```python
def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # DP computation
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     # delete
                    dp[i][j - 1],     # insert
                    dp[i - 1][j - 1]  # replace
                )
    return dp[m][n]

# Example usage:
print(minDistance("horse", "ros"))  # Output: 3
```

---

## Complexity Analysis

- **Time:** O(m * n), where m and n are the lengths of the two words.
- **Space:** O(m * n), but can be optimized to O(min(m, n)).

---

## Applications

- Spell checking and autocorrect
- DNA/protein sequence alignment in bioinformatics
- Plagiarism detection
- Diff tools and version control

---

## Useful Links

- [Edit Distance — LeetCode](https://leetcode.com/problems/edit-distance/)
- [Dynamic Programming — GeeksforGeeks](https://www.geeksforgeeks.org/edit-distance-dp-5/)
- [Wikipedia: Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance)

---

## LeetCode Practice

| Difficulty | Problem           | Link                                                                 |
|------------|-------------------|----------------------------------------------------------------------|
| Hard       | Edit Distance     | [#72 Edit Distance](https://leetcode.com/problems/edit-distance/)    |
| Medium     | Delete Operation for Two Strings | [#583 Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) |
| Medium     | Minimum ASCII Delete Sum for Two Strings | [#712 Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) |

---