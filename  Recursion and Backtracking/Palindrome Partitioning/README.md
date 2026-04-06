# Palindrome Partitioning — Recursion & Backtracking

## Problem Description

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitionings.

**Example:**  
s = "aab"  
Output:  
```
[
  ["a","a","b"],
  ["aa","b"]
]
```

---

## Algorithm Idea and Approach

The task is to split the string into substrings so that each substring is a palindrome.

To solve this:
- Use recursion and backtracking.
- At each step, try every possible prefix that is a palindrome.
- If the current prefix is a palindrome, recursively partition the remaining suffix.
- When you reach the end of the string, add the current partition to the result.

---

## Python Example

```python
def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def backtrack(s, start, path, result):
    if start == len(s):
        result.append(list(path))
        return
    for end in range(start, len(s)):
        if is_palindrome(s, start, end):
            path.append(s[start:end+1])
            backtrack(s, end + 1, path, result)
            path.pop()

def partition(s):
    result = []
    backtrack(s, 0, [], result)
    return result

# Example usage:
s = "aab"
print(partition(s))
# Output: [['a', 'a', 'b'], ['aa', 'b']]
```

---

## Complexity Analysis

- **Time Complexity:** Exponential in the length of s (worst case: O(2^n)), as each character can be a cut.  
- **Space Complexity:** O(n) for recursion stack, plus O(number of partitions × average length of partition) for result storage.

---

## Real-Life Applications

- Generating all palindromic decompositions for test cases.
- Bioinformatics: searching for palindromic motifs in DNA/RNA sequences.
- Text analysis: identifying symmetrical patterns in strings.
- As a subroutine in dynamic programming/string analysis problems.

---

## Useful Links

- [Palindrome Partitioning — LeetCode](https://leetcode.com/problems/palindrome-partitioning/)
- [Palindrome — Wikipedia](https://en.wikipedia.org/wiki/Palindrome)
- [Backtracking Algorithms — GeeksforGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [String Partitioning — Brilliant.org](https://brilliant.org/wiki/partitions-of-a-set/)

---

## LeetCode Practice

| Difficulty | Problem                   | Link                                                                           |
|------------|---------------------------|--------------------------------------------------------------------------------|
| Medium     | Palindrome Partitioning   | [#131 Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) |
| Hard       | Palindrome Partitioning II| [#132 Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) |
| Medium     | Palindromic Substrings    | [#647 Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) |
| Medium     | Partition Labels          | [#763 Partition Labels](https://leetcode.com/problems/partition-labels/)        |

---