# Word Break — Dynamic Programming

## Problem Description

Given a string `s` and a dictionary of strings `wordDict`, determine if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Variants:
- Decide if such segmentation is possible (True/False).
- Sometimes: Output the segmentation.

---

## Algorithm Idea and Approach

- Use dynamic programming:
  - Let `dp[i]` be True if `s[:i]` can be segmented into dictionary words.
  - Initialize `dp[0] = True` (empty string is segmentable).
  - For each position `i` from 1 to `len(s)`:
    - For each `j` from 0 to `i`:
      - If `dp[j]` is True and `s[j:i]` in `wordDict`, set `dp[i] = True`.
      - Break inner loop if `dp[i]` is set True.

---

## Python Example: Word Break

```python
def word_break(s, wordDict):
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]

# Example usage:
s = "leetcode"
wordDict = ["leet", "code"]
print(word_break(s, wordDict))  # Output: True
```

---

## Complexity Analysis

- **Time:** O(n²)
- **Space:** O(n)
  - n = length of the string

---

## Applications

- Natural language processing (word segmentation)
- Spell checking and corrections
- Password validation

---

## Useful Links

- [LeetCode #139: Word Break](https://leetcode.com/problems/word-break/)
- [GeeksforGeeks: Word Break Problem](https://www.geeksforgeeks.org/word-break-problem-dp-32/)

---

## LeetCode Practice

| Difficulty | Problem      | Link                                                                  |
|------------|--------------|-----------------------------------------------------------------------|
| Medium     | Word Break   | [#139 Word Break](https://leetcode.com/problems/word-break/)           |