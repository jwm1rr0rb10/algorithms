# Find All Anagrams in a String — Sliding Window + Hash Map Approach

## Problem Description

Given two strings `s` and `p`, return all starting indices of `p`'s anagrams in `s`. You may return the answer in any order.

An anagram is a permutation of all the characters in another string.

**Example:**  
Input: s = "cbaebabacd", p = "abc"  
Output: [0, 6]  
Explanation:  
- The substring starting at index 0 ("cba") is an anagram of "abc".
- The substring starting at index 6 ("bac") is an anagram of "abc".

---

## Algorithm Idea and Approach

- Use the sliding window technique to traverse `s` with a window of length equal to `p`.
- Maintain a count of characters for `p` (using a hash map or array).
- For each window in `s`, maintain a count of the characters in the current window.
- If the counts match, the current window is an anagram — record the starting index.
- Move the window by adding the next character and removing the leftmost character from the count.

---

## Python Example

```python
def findAnagrams(s, p):
    from collections import Counter
    
    result = []
    p_count = Counter(p)
    s_count = Counter()
    window = len(p)

    for i, char in enumerate(s):
        s_count[char] += 1
        if i >= window:
            left_char = s[i - window]
            s_count[left_char] -= 1
            if s_count[left_char] == 0:
                del s_count[left_char]
        if s_count == p_count:
            result.append(i - window + 1)
    return result

# Example usage:
print(findAnagrams("cbaebabacd", "abc"))  # Output: [0, 6]
```

---

## Complexity Analysis

- **Time:** O(n), where n is the length of `s` (each character processed once, assuming fixed alphabet).
- **Space:** O(1) if the alphabet is fixed (e.g., lowercase English letters), otherwise O(m) where m is the alphabet size.

---

## Real-Life Applications

- Plagiarism detection (finding rearranged words/phrases).
- DNA/protein sequence analysis (finding permutations).
- Detecting patterns in network traffic or logs.
- Finding all locations of a scrambled password or code.

---

## Useful Links

- [Find All Anagrams in a String — LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
- [Anagram — Wikipedia](https://en.wikipedia.org/wiki/Anagram)
- [Sliding Window Technique — GeeksforGeeks](https://www.geeksforgeeks.org/window-sliding-technique/)

---

## LeetCode Practice

| Difficulty | Problem                             | Link                                                                           |
|------------|-------------------------------------|--------------------------------------------------------------------------------|
| Medium     | Find All Anagrams in a String       | [#438 Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) |
| Medium     | Permutation in String               | [#567 Permutation in String](https://leetcode.com/problems/permutation-in-string/) |
| Medium     | Minimum Window Substring            | [#76 Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) |
| Medium     | Substring with Concatenation of All Words | [#30 Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) |

---