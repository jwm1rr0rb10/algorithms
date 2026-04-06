# Restore IP Addresses — Recursion & Backtracking

## Problem Description

Given a string s containing only digits, return **all possible valid IP addresses** that can be obtained by inserting three dots so that the string is split into four segments (octets), each of which:
- is in the range 0 to 255,
- does not have leading zeros (e.g., "01", "001" are invalid, only "0" is allowed).

**Example:**  
Input: `"25525511135"`  
Output:  
```
["255.255.11.135", "255.255.111.35"]
```

---

## Algorithm Idea and Approach

- There are four segments in an IP address.
- At each recursion step, try to take a segment of length 1, 2 or 3, if it is valid.
- If the segment is valid, add it to the current path and recursively partition the remaining string.
- When four segments are chosen and the string is fully consumed, join the path into an IP and add it to the result.
- After recursion, remove the last segment (backtracking) to try other options.

---

## Python Example

```python
def restore_ip_addresses(s):
    result = []

    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s):
                result.append(".".join(path))
            return
        for length in range(1, 4):
            if start + length > len(s):
                break
            segment = s[start:start+length]
            if (len(segment) > 1 and segment[0] == '0') or int(segment) > 255:
                continue
            path.append(segment)
            backtrack(start + length, path)
            path.pop()  # Backtracking

    backtrack(0, [])
    return result

# Example usage:
print(restore_ip_addresses("25525511135"))
# ['255.255.11.135', '255.255.111.35']
```

---

## Complexity Analysis

- **Time:** O(1) — number of options is bounded (4 segments × up to 3 digits), practically very fast (N ≤ 12).
- **Space:** O(N) — recursion stack depth + space for results.

---

## Real-Life Applications

- Automatic generation and validation of IP addresses from strings (log parsing, forms, user data).
- User input validation and network application testing.
- Parsers and test suites for network protocols.
- Finding all possible interpretations of a string as an IP address.

---

## Useful Links

- [Restore IP Addresses — LeetCode](https://leetcode.com/problems/restore-ip-addresses/)
- [IPv4 — Wikipedia](https://en.wikipedia.org/wiki/IPv4)
- [Backtracking Algorithms — GeeksforGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/)

---

## LeetCode Practice

| Difficulty | Problem                | Link                                                                       |
|------------|------------------------|----------------------------------------------------------------------------|
| Medium     | Restore IP Addresses   | [#93 Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)|
| Medium     | Generate Parentheses   | [#22 Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)|
| Medium     | Letter Combinations    | [#17 Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)|
| Medium     | Subsets                | [#78 Subsets](https://leetcode.com/problems/subsets/)                      |

---