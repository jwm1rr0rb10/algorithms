# Longest Repeating Character Replacement — Two Pointers / Sliding Window

## Problem Description

Given a string `s` and an integer `k`, return the length of the longest substring containing the same letter you can get after performing at most `k` character replacements (i.e., change up to `k` characters to any other uppercase English letter).

**Example:**  
Input: s = "AABABBA", k = 1  
Output: 4  
Explanation: Replace one 'A' in the middle with 'B' to get "AABBBBA" (or one 'B' to 'A' to get "AAAAAAA").

---

## Algorithm Idea and Approach

- Use a sliding window with two pointers (`left` and `right`) to represent the current substring.
- Keep a frequency count of characters within the window.
- Track the count of the most frequent character within the current window.
- If the window size minus the count of the max character is greater than `k`, shrink the window from the left.
- Update the result with the maximum window size found.

---

## Python Example

```python
def characterReplacement(s: str, k: int) -> int:
    from collections import defaultdict

    count = defaultdict(int)
    max_count = 0
    left = 0
    result = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_count = max(max_count, count[s[right]])

        # If more than k replacements needed, shrink window from left
        if (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result

# Example usage:
print(characterReplacement("AABABBA", 1))  # Output: 4
```

---

## Complexity Analysis

- **Time:** O(n), where n is the length of the string.
- **Space:** O(1) (since there are at most 26 uppercase English letters in the window).

---

## Real-Life Applications

- Detecting/allowing near-uniform substrings in text analysis.
- Rate limiting and error correction in streaming data.
- DNA sequence analysis (finding uniform segments with limited mutations).
- Plagiarism detection and fuzzy string matching.

---

## Useful Links

- [Longest Repeating Character Replacement — LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [Sliding Window Technique — GeeksforGeeks](https://www.geeksforgeeks.org/window-sliding-technique/)
- [Two Pointers Technique — Wikipedia](https://en.wikipedia.org/wiki/Two-pointer_technique)

---

## LeetCode Practice

| Difficulty | Problem                                      | Link                                                                          |
|------------|----------------------------------------------|-------------------------------------------------------------------------------|
| Medium     | Longest Repeating Character Replacement      | [#424 Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) |
| Medium     | Longest Substring with At Most K Distinct Chars | [#340 Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) |
| Medium     | Minimum Window Substring                     | [#76 Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) |
| Medium     | Longest Substring Without Repeating Characters| [#3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |

---