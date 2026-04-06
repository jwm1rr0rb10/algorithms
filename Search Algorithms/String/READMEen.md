# Substring Search Algorithm Comparison: Boyer-Moore vs Rabin-Karp vs KMP vs Z-Algorithm vs Manacher’s vs Naive

## Main Differences

| Algorithm                | Time Complexity                  | Space Complexity | Applicability & Notes |
|:------------------------:|:-------------------------------:|:----------------:|:---------------------|
| Naive Substring Search   | O((n−m+1)m)                     | O(1)             | Very simple, no extra memory, but slow on large data. Good for learning and small tasks. |
| Rabin-Karp               | O(n + m) (avg) / O(nm) (worst)  | O(1)             | Fast on average thanks to hashing, easy to extend for multiple patterns. Can degrade to naive in worst case. |
| KMP (Knuth-Morris-Pratt) | O(n + m)                        | O(m)             | Always fast, needs prefix function memory (lps). Great for large texts and patterns if memory is not tight. |
| Boyer-Moore              | O(n + m) (worst), O(n/m) (avg)  | O(m + k)         | Extremely fast in practice for long patterns and large alphabets. Uses extra memory for preprocessing. Best for single-pattern searches in large texts. |
| Z-Algorithm              | O(n)                            | O(n)             | Excellent for pattern matching when you need all occurrences. Useful for string preprocessing and some advanced string problems. |
| Manacher’s Algorithm     | O(n)                            | O(n)             | Specialized for finding all palindromic substrings in linear time. Not a general substring search algorithm. |

*Here, n = length of the text, m = length of the pattern, k = alphabet size.*

---

## More on the Algorithms

- **Naive Substring Search**:
    - Compares the pattern at every position in the text.
    - No preprocessing or extra memory.
    - Slow on large texts or patterns.
    - Useful for learning, testing, or very small/one-off tasks.

- **Rabin-Karp**:
    - Uses hashing for fast average-case search. Very fast in practice if few hash collisions.
    - Hashes may collide even when strings differ, so sometimes character-by-character comparison is needed.
    - Easily adapted for searching multiple patterns at once (multi-pattern search).
    - Requires almost no extra memory, just for hashes.
    - Works well on large texts/patterns, but if hash collisions are frequent, can degrade to naive.
    - Worst case: O(nm) if all hashes collide.

- **KMP (Knuth-Morris-Pratt)**:
    - No hashing, builds a prefix function (lps) for the pattern only.
    - Never does redundant comparisons, never moves backwards in text, always O(n + m).
    - Needs O(m) memory for lps (can be a limit if pattern is huge).
    - Not ideal for searching many patterns without modifications.
    - Excellent for large repetitive texts.

- **Boyer-Moore**:
    - Preprocesses the pattern to build "bad character" and "good suffix" tables.
    - Compares pattern from right to left, allowing for large jumps in the text.
    - Extremely fast in practice, especially for long patterns and large alphabets.
    - Extra memory used for tables: O(m + k), where m = pattern length, k = alphabet size.
    - Best suited for searching a single pattern in large texts.
    - Widely used in text editors, search engines, and system utilities.
    - Loses advantage for very short patterns or small alphabets.

- **Z-Algorithm**:
    - Preprocesses the string to compute Z-values (lengths of substrings matching the prefix).
    - Useful for finding all pattern occurrences at once.
    - Excellent for building advanced string algorithms (e.g., for multiple pattern searches, string factorization).
    - Linear time and space, but not directly used for single pattern search in practice as often as KMP/Boyer-Moore.

- **Manacher’s Algorithm**:
    - Specialized algorithm for finding all palindromic substrings in linear time.
    - Not a standard substring search algorithm, but invaluable for palindrome-related problems.
    - Useful for problems like "Longest Palindromic Substring".

---

## Where and How Algorithms Can "Break" (Reach Worst Case or Lose Efficiency)

- **Naive Algorithm**
    - "Breaks" (becomes very slow) on long texts and/or long patterns, especially if the text contains many repeating characters matching the start of the pattern.
    - Example: searching for `"aaaaab"` in the text `"aaaaaaaaaaaaaaaaaaaab"`.

- **Rabin-Karp**
    - Worst case occurs when there are many hash collisions. For example, if all substrings of the text have the same hash but do not match the pattern character by character.
    - In this case, a full comparison is needed for each occurrence, and the complexity becomes O(n·m).
    - Also, with a very large alphabet or a poor hash function, the probability of collisions increases.

- **KMP**
    - Practically never breaks in terms of time, but can require a lot of memory for long patterns (O(m)).
    - Inefficient for searching many different patterns — you need to build a separate prefix function for each pattern.
    - Also, offers little advantage for very short patterns (e.g., a single character).

- **Boyer-Moore**
    - Breaks (loses its main advantage) on very short patterns and/or very small alphabets (for example, only using "A" and "B").
    - Worst case: both text and pattern consist of repeating characters matching the end of the pattern. In this scenario, shifts are minimal, and comparisons happen at almost every position.
    - Complicated and resource-intensive for searching many patterns at once (not natively supported).

- **Z-Algorithm**
    - Not ideal for searching a single pattern in extremely large texts due to its O(n) space.
    - Mostly efficient and robust for its use-cases.

- **Manacher’s Algorithm**
    - Only useful for palindromic substring problems; not applicable for general substring searching.

---

## Summary

- **Limited memory?** — Rabin-Karp or Naive is preferable, needs almost no extra space.
- **Guaranteed speed?** — KMP is good, especially for repetitive texts.
- **Many patterns?** — Rabin-Karp (with set), Z-Algorithm (for advanced multi-pattern usage).
- **Single long pattern, large text, need blazing speed?** — Boyer-Moore is usually the best choice.
- **Need all palindromic substrings?** — Manacher’s Algorithm (unique, nothing else matches it).
- **Naive** — only for demonstration and very small data.

---

## String Search Algorithm Comparison Table

| Algorithm                | Time Complexity                  | Space Complexity |
|:------------------------:|:-------------------------------:|:----------------|
| Boyer-Moore              | O(n + m) (worst), O(n/m) (avg)  | O(m + k)        |
| KMP (Knuth-Morris-Pratt) | O(n + m)                        | O(m)            |
| Manacher’s Algorithm     | O(n)                            | O(n)            |
| Naive Substring Search   | O((n−m+1)m)                     | O(1)            |
| Rabin-Karp               | O(n + m) (avg) / O(nm) (worst)  | O(1)            |
| Z-Algorithm              | O(n)                            | O(n)            |

---