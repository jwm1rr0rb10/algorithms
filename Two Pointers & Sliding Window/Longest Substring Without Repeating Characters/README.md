# Longest Substring Without Repeating Characters — Sliding Window Approach

## Problem Description

Given a string, find the length of the longest substring without repeating characters.

**Example:**  
Input: s = "abcabcbb"  
Output: 3  
Explanation: The answer is "abc", with the length of 3.

---

## Algorithm Idea and Approach

- Use the sliding window technique with two pointers (`left` and `right`).
- Maintain a set of unique characters in the current window.
- Move the `right` pointer, expanding the window; if a duplicate is found, move the `left` pointer to shrink the window until there are no duplicates.
- At each step, update the maximum length found.

---

## Python Example

```python
def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

# Example usage:
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
```

---

## Complexity Analysis

- **Time:** O(n), where n is the length of the string. Each character is visited at most twice.
- **Space:** O(min(n, m)), where m is the size of the character set (e.g., 26 for lowercase English letters).

---

## Real-Life Applications

- Finding unique user activity streaks in logs.
- Data stream analysis for unique sequences.
- Detecting unique patterns or substrings in DNA sequences or network traffic.
- Useful as a base for more complex string/windowed algorithms.

---

## Useful Links

- [Longest Substring Without Repeating Characters — LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [Sliding Window Technique — GeeksforGeeks](https://www.geeksforgeeks.org/window-sliding-technique/)
- [Substring — Wikipedia](https://en.wikipedia.org/wiki/Substring)

---

## LeetCode Practice

| Difficulty | Problem                                             | Link                                                                 |
|------------|-----------------------------------------------------|----------------------------------------------------------------------|
| Medium     | Longest Substring Without Repeating Characters      | [#3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)    |
| Medium     | Substring with Concatenation of All Words           | [#30 Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) |
| Medium     | Longest Substring with At Most Two Distinct Chars   | [#159 Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) |
| Medium     | Longest Repeating Character Replacement             | [#424 Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) |

---