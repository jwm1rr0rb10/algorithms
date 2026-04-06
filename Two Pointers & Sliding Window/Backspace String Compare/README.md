# Backspace String Compare — Two Pointers Approach

## Problem Description

Given two strings, `s` and `t`, return `true` if they are equal when both are typed into empty text editors. `#` means a backspace character.

**Example:**  
Input: s = "ab#c", t = "ad#c"  
Output: true  
Explanation: Both become "ac".

---

## Algorithm Idea and Approach

- Use two pointers starting from the end of each string.
- Traverse each string from right to left, skipping characters that should be erased due to backspaces (`#`).
- For each string, keep a counter for the number of backspaces to apply.
- Compare the current valid characters from both strings; if they mismatch, return `false`.
- If both pointers reach the start and all compared characters match, return `true`.

---

## Python Example

```python
def backspaceCompare(s: str, t: str) -> bool:
    def next_valid_char(string, index):
        skip = 0
        while index >= 0:
            if string[index] == '#':
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                return index
            index -= 1
        return -1

    i, j = len(s) - 1, len(t) - 1
    while i >= 0 or j >= 0:
        i = next_valid_char(s, i)
        j = next_valid_char(t, j)
        if i >= 0 and j >= 0:
            if s[i] != t[j]:
                return False
        elif i >= 0 or j >= 0:
            return False
        i -= 1
        j -= 1
    return True

# Example usage:
print(backspaceCompare("ab#c", "ad#c"))  # Output: True
```

---

## Complexity Analysis

- **Time:** O(n + m), where n and m are the lengths of the two strings.
- **Space:** O(1), using only pointers and counters.

---

## Real-Life Applications

- Text editor undo/backspace simulation.
- Comparing typed user inputs that may include corrections.
- Useful in command-line input processing and chat applications.

---

## Useful Links

- [Backspace String Compare — LeetCode](https://leetcode.com/problems/backspace-string-compare/)
- [Stack Data Structure — GeeksforGeeks](https://www.geeksforgeeks.org/stack-data-structure/)
- [Two Pointers Technique — Wikipedia](https://en.wikipedia.org/wiki/Two-pointer_technique)

---

## LeetCode Practice

| Difficulty | Problem                     | Link                                                                |
|------------|-----------------------------|---------------------------------------------------------------------|
| Easy       | Backspace String Compare    | [#844 Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) |
| Medium     | Edit Distance               | [#72 Edit Distance](https://leetcode.com/problems/edit-distance/)    |
| Medium     | Longest Valid Parentheses   | [#32 Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) |
| Easy       | Valid Parentheses           | [#20 Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) |

---