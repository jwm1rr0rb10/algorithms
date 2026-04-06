# Bitwise Complement

## Problem Description

Given an integer `n`, find its bitwise complement.  
The bitwise complement of a number is the number you get by inverting (flipping) all its bits: 0 becomes 1, 1 becomes 0.  
The result should only consider all **significant bits** of the original number (ignore leading zeros).

**Example:**  
Input: `n = 5`  
Binary: `101`  
Bitwise complement: `010`  
Output: `2`

---

## Idea and Approach

- The bitwise complement operation flips all bits of a number.
- For a given integer, we only want to flip the bits up to its most significant 1 (ignore leading zeros).
- To achieve this, we create a mask with the same number of bits as `n` (all set to 1).
- The complement is then `n ^ mask`.

---

## Python Example

```python
def bitwiseComplement(n):
    if n == 0:
        return 1
    mask = (1 << n.bit_length()) - 1
    return n ^ mask

# Example usage:
print(bitwiseComplement(5))  # 2
```

---

## How It Works

1. If `n` is zero, its complement is `1` (as a single bit).
2. Find the length of the binary representation (excluding leading zeros).
3. Build a mask of all ones with that length.
4. XOR the original number with the mask to flip only significant bits.

---

## Table: Bitwise Complement for Numbers 0–8

| Decimal | Binary | Complement (bin) | Output |
|---------|--------|------------------|--------|
| 0       | 0      | 1                | 1      |
| 1       | 1      | 0                | 0      |
| 2       | 10     | 01               | 1      |
| 3       | 11     | 00               | 0      |
| 4       | 100    | 011              | 3      |
| 5       | 101    | 010              | 2      |
| 6       | 110    | 001              | 1      |
| 7       | 111    | 000              | 0      |
| 8       | 1000   | 0111             | 7      |

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

- Bitmasking and toggling flags.
- Data obfuscation and low-level data manipulation.
- Image processing (inverting pixel values).
- Simplified logic for communication protocols.

---# Bitwise Complement — Python Example

Given an integer `n`, find its bitwise complement (invert all bits up to the most significant 1).

## Python Implementation

```python
def bitwiseComplement(n):
    if n == 0:
        return 1
    mask = (1 << n.bit_length()) - 1
    return n ^ mask

# Example usage:
print(bitwiseComplement(5))   # Output: 2
print(bitwiseComplement(0))   # Output: 1
print(bitwiseComplement(8))   # Output: 7
```

## Step-by-Step Explanation

1. **Special case for zero:**  
   The complement of 0 is 1 (since for a single bit, 0 -> 1).

2. **Find number of significant bits:**  
   `n.bit_length()` gives the number of bits needed for `n`.

3. **Create a mask:**  
   `(1 << n.bit_length()) - 1` gives a mask where all significant bits are set to 1.  
   E.g., for `n = 5 (101)`, mask is `111` (7).

4. **XOR with mask:**  
   `n ^ mask` flips all bits in the mask range.  
   For `n = 5 (101)` and mask `111`, result is `010` (2).

---

## Table: Bitwise Complement for Numbers 0–8

| n | bin(n) | mask | n ^ mask | Output |
|---|--------|------|----------|--------|
| 0 | 0      | 1    | 1        | 1      |
| 1 | 1      | 1    | 0        | 0      |
| 2 | 10     | 11   | 01       | 1      |
| 3 | 11     | 11   | 00       | 0      |
| 4 | 100    | 111  | 011      | 3      |
| 5 | 101    | 111  | 010      | 2      |
| 6 | 110    | 111  | 001      | 1      |
| 7 | 111    | 111  | 000      | 0      |
| 8 | 1000   | 1111 | 0111     | 7      |

---

## Fun: Invert ASCII in Python

```python
c = 'A'
ascii_code = ord(c)
print("Original:", bin(ascii_code))
mask = (1 << ascii_code.bit_length()) - 1
print("Complement:", bin(ascii_code ^ mask))
```

---

## Useful Links

- [Bitwise Complement — LeetCode #1009](https://leetcode.com/problems/complement-of-base-10-integer/)
- [Bitwise operations — Wikipedia](https://en.wikipedia.org/wiki/Bitwise_operation)
- [ASCII Table](https://www.asciitable.com/)

---

## LeetCode Practice

| Difficulty | Problem                       | Link                                                      |
|------------|-------------------------------|-----------------------------------------------------------|
| Easy       | Complement of Base 10 Integer | [#1009](https://leetcode.com/problems/complement-of-base-10-integer/) |
| Easy       | Number of 1 Bits              | [#191](https://leetcode.com/problems/number-of-1-bits/)   |
| Medium     | Bitwise AND of Numbers Range  | [#201](https://leetcode.com/problems/bitwise-and-of-numbers-range/) |

---