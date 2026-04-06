# Letter Combinations of a Phone Number — Recursion & Backtracking

## Problem Description

Given a string containing digits from 2 to 9, return all possible letter combinations that the number could represent. This is based on the mapping of digits to letters on a telephone keypad.

**Example:**  
Input: `"23"`  
Output:  
```
["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

---

## Algorithm Idea and Approach

- Each digit maps to a set of letters, just like on classic phone keypads.
- To find all combinations:
  - For each digit, try every possible letter.
  - Build up the combination recursively, one letter at a time.
  - When the current combination reaches the length of the input digits, add it to the result.
  - Use backtracking: after exploring a path, remove the last letter and try the next option.

---

## Python Example

```python
def letter_combinations(digits):
    if not digits:
        return []

    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    result = []

    def backtrack(index, path):
        if len(path) == len(digits):
            result.append("".join(path))
            return
        for letter in phone[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()  # Backtracking

    backtrack(0, [])
    return result

# Example usage:
print(letter_combinations("23"))
# Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
```

---

## Complexity Analysis

- **Time Complexity:** O(3^N * 4^M), where N is the number of digits with 3 letters (2,3,4,5,6,8) and M is the number with 4 letters (7,9).
- **Space Complexity:** O(N) for recursion stack + space for storing results.

---

## Real-Life Applications

- Generating vanity phone numbers or memorable codes.
- Predictive text input (T9) for mobile devices.
- Generating test cases for forms or number-to-word systems.
- Searching for possible letter-based representations of numeric codes.

---

## Useful Links

- [Letter Combinations of a Phone Number — LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [Classic Phone Keypad — Wikipedia](https://en.wikipedia.org/wiki/Telephone_keypad)
- [Backtracking Algorithms — GeeksforGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/)

---

## LeetCode Practice

| Difficulty | Problem                                 | Link                                                                                   |
|------------|-----------------------------------------|----------------------------------------------------------------------------------------|
| Medium     | Letter Combinations of a Phone Number   | [#17 Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) |
| Medium     | Generate Parentheses                    | [#22 Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)         |
| Medium     | Combination Sum                         | [#39 Combination Sum](https://leetcode.com/problems/combination-sum/)                   |
| Medium     | Subsets                                 | [#78 Subsets](https://leetcode.com/problems/subsets/)                                   |

---