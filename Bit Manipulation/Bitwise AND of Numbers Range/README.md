# Bitwise AND of Numbers Range

## Problem Description

Given two integers `left` and `right`, compute the bitwise AND of all numbers in the range `[left, right]` (inclusive).

**Example:**  
Input: `left = 5`, `right = 7`  
Numbers: 5 (101), 6 (110), 7 (111)  
Bitwise AND: 101 & 110 & 111 = 100  
Output: 4

---

## Idea and Approach

- The bitwise AND of all numbers in a range "zeroes out" any bit that flips at least once in that range.
- As soon as the range crosses a boundary where a bit changes, that bit and all lower bits become zero in the result.
- The solution is to find the common prefix (identical leading bits) of `left` and `right`.
- Approach: Shift both numbers right until they are equal, counting the number of shifts. Then shift the result back left.

---

## Python Example

```python
def rangeBitwiseAnd(left, right):
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift

# Example usage:
print(rangeBitwiseAnd(5, 7))  # 4
```

---

## How It Works

1. Find how many times you need to shift both numbers right until they are equal (this is the common prefix).
2. Only the bits that remain the same in all numbers in the range are preserved.
3. All lower bits become zero.

---

## Table: Binary Representation of Numbers (1-8)

| Decimal | Binary  |
|---------|---------|
| 1       | 1       |
| 2       | 10      |
| 3       | 11      |
| 4       | 100     |
| 5       | 101     |
| 6       | 110     |
| 7       | 111     |
| 8       | 1000    |

---

## ASCII Table (Key Symbols)

| Symbol  | Dec | Hex   | Binary     |
|---------|-----|-------|------------|
|   A     | 65  | 0x41  | 01000001   |
|   a     | 97  | 0x61  | 01100001   |
|   0     | 48  | 0x30  | 00110000   |
|   !     | 33  | 0x21  | 00100001   |
|   @     | 64  | 0x40  | 01000000   |
|   z     | 122 | 0x7A  | 01111010   |
| space   | 32  | 0x20  | 00100000   |

---

## Quick Symbol Code Lookup in Python

```python
c = 'A'
print(ord(c), bin(ord(c)))
```

---

## Complexity

- **Time:** O(1) — at most 32 (or 64) steps, as the number of bits is fixed for an integer.
- **Space:** O(1)

---

## Applications

- Fast filtering and masking of number ranges.
- Low-level computation optimization.
- Working with bit masks and access rights.

---

## Useful Links

- [Bitwise AND of Numbers Range — LeetCode #201](https://leetcode.com/problems/bitwise-and-of-numbers-range/)
- [Bitwise operations — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)
- [ASCII Table](https://www.asciitable.com/)

---

## LeetCode Practice

| Difficulty | Problem                             | Link                                                      |
|------------|-------------------------------------|-----------------------------------------------------------|
| Medium     | Bitwise AND of Numbers Range        | [#201](https://leetcode.com/problems/bitwise-and-of-numbers-range/) |
| Easy       | Number of 1 Bits                   | [#191](https://leetcode.com/problems/number-of-1-bits/)   |
| Medium     | Counting Bits                      | [#338](https://leetcode.com/problems/counting-bits/)      |

---