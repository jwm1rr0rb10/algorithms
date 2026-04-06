# Four Sum — Sorting + Two Pointers Approach

## Problem Description

Given an array `nums` of n integers and an integer `target`, return all unique quadruplets `[a, b, c, d]` such that `a + b + c + d == target`.

You must not return duplicate quadruplets; the order of the quadruplets does not matter.

**Example:**  
Input: nums = [1, 0, -1, 0, -2, 2], target = 0  
Output:  
```
[
  [-2, -1, 1, 2],
  [-2, 0, 0, 2],
  [-1, 0, 0, 1]
]
```

---

## Algorithm Idea and Approach

- Sort the input array to make duplicate handling easier and enable two-pointer techniques.
- Use two nested loops to select the first two numbers (`i` and `j`).
- For each pair, use two pointers (`left` and `right`) to search for pairs whose sum with `nums[i]` and `nums[j]` equals the target.
- Move pointers inward, skipping duplicates, and collect quadruplets that sum to the target.
- Continue until all unique quadruplets are found.

---

## Python Example

```python
def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # skip duplicates for i
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue  # skip duplicates for j
            left, right = j + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if curr_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
    return result

# Example usage:
print(fourSum([1, 0, -1, 0, -2, 2], 0))
# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
```

---

## Complexity Analysis

- **Time:** O(n³), for each pair (i, j), two pointers scan the rest (n² * n).
- **Space:** O(k), where k is the number of unique quadruplets found (not counting input sort).

---

## Real-Life Applications

- Finding sets of four elements that meet a sum constraint in analytics or finance.
- Data mining: discovering groups of records/items matching specified totals.
- Combinatorial problems in optimization, chemistry (e.g., molecular combinations), or cryptography.

---

## Useful Links

- [Four Sum — LeetCode](https://leetcode.com/problems/4sum/)
- [Two Pointers Technique — GeeksforGeeks](https://www.geeksforgeeks.org/two-pointer-technique/)
- [Sorting Algorithm — Wikipedia](https://en.wikipedia.org/wiki/Sorting_algorithm)

---

## LeetCode Practice

| Difficulty | Problem       | Link                                                                    |
|------------|--------------|-------------------------------------------------------------------------|
| Medium     | Four Sum      | [#18 Four Sum](https://leetcode.com/problems/4sum/)                     |
| Medium     | Three Sum     | [#15 Three Sum](https://leetcode.com/problems/3sum/)                    |
| Medium     | Two Sum       | [#1 Two Sum](https://leetcode.com/problems/two-sum/)                    |
| Medium     | Subarray Sum Equals K | [#560 Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) |

---