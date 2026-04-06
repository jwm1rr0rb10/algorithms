# Bit Manipulation & Bitmasking Algorithms

This collection covers classic and advanced bit manipulation and bitmasking algorithms. Bitwise techniques are essential for high-performance computing, competitive programming, and optimizing space/time in algorithmic challenges.

---

## Why Use Bit Manipulation?

- **Performance:** Bitwise operations are fast—typically O(1) per operation.
- **Space Efficiency:** Enable compact representations (e.g., bitmasks for sets).
- **Expressiveness:** Allow elegant solutions to problems like parity, uniqueness, and subset enumeration.

---

## When to Use and When Not to Use

### Strengths
- **Speed:** Most bitwise operations are constant time.
- **Compactness:** Represent large sets or states in a single integer.
- **Elegant Solutions:** Many problems (e.g., uniqueness, toggling states, subset enumeration) have neat bit tricks.

### Weaknesses
- **Readability:** Bitwise code can be hard to understand or debug.
- **Overflow/Portability:** Must be careful with signedness and integer size.
- **Limited to Integers:** Not directly applicable to floating-point or non-integer data.

**Best used when:**
- Working with small sets, flags, masks, or integers (≤ 32 or 64 bits).
- Solving classic problems: parity, uniqueness, subset DP, low-level optimization.

**Avoid when:**
- Readability and maintainability are a priority for a large team.
- Data is not naturally representable as bits.
- There are clear, simpler alternatives.

---

## Algorithms Overview

| Name                                    | Time Complexity           | Space Complexity | Description / Typical Use                                                               |
|------------------------------------------|--------------------------|------------------|-----------------------------------------------------------------------------------------|
| Bit masking                             | O(1) per op              | O(1)             | Setting, clearing, toggling, or checking specific bits in an integer.                   |
| Bitmask DP (e.g. TSP)                   | O(2^n × n)               | O(2^n)           | Dynamic programming over subsets (e.g., Traveling Salesman Problem).                    |
| Bitwise AND of Numbers Range             | O(1)                     | O(1)             | Efficiently computes AND for a range [m, n].                                            |
| Bitwise Complement (inversion)           | O(1)                     | O(1)             | Inverts all bits of a number.                                                           |
| Clear ith bit                           | O(1)                     | O(1)             | Set bit i to 0.                                                                         |
| Count set bits (Hamming weight)          | O(log n)                 | O(1)             | Counts the number of 1s in the binary representation.                                   |
| Detect opposite signs                    | O(1)                     | O(1)             | Check if two numbers have different signs.                                              |
| Divide Two Integers (bitwise division)   | O(1) (32-bit int)        | O(1)             | Division using only bitwise operations (not `+`, `-`, `/`, `*`).                        |
| Find Missing Number using XOR            | O(n)                     | O(1)             | Find the missing number in a sequence using XOR.                                        |
| Find Rightmost Set Bit                   | O(1)                     | O(1)             | Gets the rightmost 1 in a number.                                                       |
| Get ith bit                             | O(1)                     | O(1)             | Checks if bit i is set.                                                                 |
| Gray Code generation                     | O(2^n)                   | O(2^n)           | Generates all n-bit Gray codes (single bit change per step).                            |
| Hamming Distance                        | O(1)                     | O(1)             | Count the number of differing bits between two numbers.                                 |
| Maximum Product of Word Lengths          | O(n^2)                   | O(n)             | Uses bitmasks to compare character sets of words efficiently.                           |
| Power of Two check                      | O(1)                     | O(1)             | Checks if a number is a power of two.                                                   |
| Reverse bits of an integer               | O(1)                     | O(1)             | Reverses the bits of an integer.                                                        |
| Set ith bit                             | O(1)                     | O(1)             | Sets bit i to 1.                                                                        |
| Single Number I                          | O(n)                     | O(1)             | Finds the unique number when all others appear twice.                                   |
| Single Number II                         | O(n)                     | O(1)             | Finds the unique number when all others appear k times (k=3).                           |
| Single Number III                        | O(n)                     | O(1)             | Finds two unique numbers when all others appear twice.                                  |
| Subsets using bits                       | O(2^n × n)               | O(1)             | Generates all subsets of a set via bitmasking.                                          |
| Sum without '+' (bitwise sum)            | O(1) (32-bit int)        | O(1)             | Adds two numbers without using `+` or `-`.                                              |
| Toggle ith bit                           | O(1)                     | O(1)             | Flips the ith bit.                                                                      |
| XOR tricks single/unique numbers         | O(n) (array)             | O(1)             | XOR-ing to find single or unique numbers in arrays.                                     |
| XOR tricks swap                          | O(n) (array), O(1) swap  | O(1)             | Swap two numbers using XOR, or parity tricks.                                           |

---

## References

- [Bitwise operation — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)
- [Bit Manipulation — LeetCode Tag](https://leetcode.com/tag/bit-manipulation/)
- [Gray code — Wikipedia](https://en.wikipedia.org/wiki/Gray_code)

---