# Minimum Window Substring

## Problem Description

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return an empty string `""`.

**Example:**  
Input: s = "ADOBECODEBANC", t = "ABC"  
Output: "BANC"  
Explanation: The minimum window substring in `s` that contains all the characters of `t` is "BANC".

---

## Algorithm Idea and Approach

- Use the Sliding Window (two pointers) technique with hash maps or arrays to track character counts.
- Create a dictionary `need` with counts of each character from `t`.
- Expand the right end of the window to include characters from `s` until all needed characters are in the window.
- Once all characters are included, try to shrink the window from the left to find the minimal window.
- Track the minimum length and starting position of the window.

---

## Python Example

```python
from collections import Counter, defaultdict

def minWindow(s, t):
    if not t or not s:
        return ""
    need = Counter(t)
    window = defaultdict(int)
    have, need_count = 0, len(need)
    res, res_len = [-1, -1], float('inf')
    l = 0

    for r, c in enumerate(s):
        window[c] += 1
        if c in need and window[c] == need[c]:
            have += 1

        while have == need_count:
            # Update result
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1
            # Pop from the left
            window[s[l]] -= 1
            if s[l] in need and window[s[l]] < need[s[l]]:
                have -= 1
            l += 1

    l, r = res
    return s[l:r+1] if res_len != float('inf') else ""

# Example usage:
print(minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
```

---

## Complexity Analysis

- **Time:** O(m + n), where m = len(s), n = len(t) (each character is processed at most twice).
- **Space:** O(1) if the alphabet is fixed (e.g., ASCII); otherwise, O(k) where k is the unique characters in `t`.

---

## Real-Life Applications

- DNA sequence analysis: finding the shortest segment containing all required nucleotides.
- Text mining: extracting the shortest context containing key terms.
- Data stream processing: identifying minimal segments meeting constraints.
- Information retrieval: document highlighting for all keywords.

---

## Useful Links

- [Minimum Window Substring — LeetCode](https://leetcode.com/problems/minimum-window-substring/)
- [Sliding Window Technique — GeeksforGeeks](https://www.geeksforgeeks.org/window-sliding-technique/)
- [Hash Table — Wikipedia](https://en.wikipedia.org/wiki/Hash_table)

---

## LeetCode Practice

| Difficulty | Problem                          | Link                                                                             |
|------------|----------------------------------|----------------------------------------------------------------------------------|
| Hard       | Minimum Window Substring         | [#76 Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) |
| Medium     | Longest Substring Without Repeating Characters | [#3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| Hard       | Sliding Window Maximum           | [#239 Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) |
| Medium     | Permutation in String            | [#567 Permutation in String](https://leetcode.com/problems/permutation-in-string/) |

---