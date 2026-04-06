# Generate Parentheses — Recursion & Backtracking

## Problem Description

Given an integer **n** representing the number of pairs of parentheses, generate all combinations of well-formed (valid) parentheses.

**Example:**  
Input: n = 3  
Output:  
```
["((()))","(()())","(())()","()(())","()()()"]
```

---

## Algorithm Idea and Approach

- You can add an opening parenthesis `(` if you haven't used up all n openings.
- You can add a closing parenthesis `)` if there are more openings than closings in the current string.
- When the current string reaches length 2*n, add it to the results.

---

## Python Example

```python
def generate_parentheses(n):
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append("".join(current))
            return
        if open_count < n:
            current.append("(")
            backtrack(current, open_count + 1, close_count)
            current.pop()
        if close_count < open_count:
            current.append(")")
            backtrack(current, open_count, close_count + 1)
            current.pop()

    backtrack([], 0, 0)
    return result

# Example usage:
print(generate_parentheses(3))
# ['((()))', '(()())', '(())()', '()(())', '()()()']
```

---

## Complexity Analysis

- **Time:** O(4^n / sqrt(n)) — the nth Catalan number.
- **Space:** O(4^n / sqrt(n)) to store all sequences + O(n) recursion depth.

---

## Real-Life Applications

- Parsers and compilers (parsing parenthetical expressions).
- Generating tests for calculators and parsers.
- Validating nested structures.
- Modeling possible nested actions in programming and mathematics.

---

## Useful Links

- [Generate Parentheses — LeetCode](https://leetcode.com/problems/generate-parentheses/)
- [Catalan numbers — Wikipedia](https://en.wikipedia.org/wiki/Catalan_number)
- [Backtracking Algorithms — GeeksforGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/)

---

## LeetCode Practice

| Difficulty | Problem                | Link                                                                         |
|------------|------------------------|------------------------------------------------------------------------------|
| Medium     | Generate Parentheses   | [#22 Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)|
| Medium     | Letter Combinations    | [#17 Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)|
| Medium     | Restore IP Addresses   | [#93 Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)|
| Medium     | Subsets                | [#78 Subsets](https://leetcode.com/problems/subsets/)                         |

---