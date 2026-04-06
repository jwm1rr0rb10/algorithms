# Partition Problem — Recursive (Backtracking) Approach

## Where the Partition Problem is Used

The Partition Problem asks whether a given set of positive integers can be split into two subsets with equal sums. This classic combinatorial problem is a special case of the Subset Sum Problem.

**Examples of application:**
- Balancing workload between two servers or groups.
- Fairly distributing prizes, resources, or items between two participants.
- Optimizing allocation of tasks, memory, or resources.
- Planning and analysis in logistics or project management.

---

## Algorithm Complexity

- **Time complexity:**  
  O(2^N), where N is the number of elements in the input set.  
  Each element can be either included in the first subset or not (and thus belongs to the second subset).

- **Space complexity:**  
  O(N) — recursion stack depth in backtracking.

---

## Python Example

```python
def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False  # If the sum is odd, partition is impossible

    target = total // 2

    def backtrack(i, current_sum):
        # If we've found a subset with the required sum
        if current_sum == target:
            return True
        # If the sum is exceeded or no elements left
        if current_sum > target or i == len(nums):
            return False
        # Try to include or exclude the current element
        return (backtrack(i + 1, current_sum + nums[i]) or
                backtrack(i + 1, current_sum))

    return backtrack(0, 0)

# Example usage
print(can_partition([1, 5, 11, 5]))  # True ([1, 5, 5] and [11])
print(can_partition([1, 2, 3, 5]))   # False
```

### Code Explanation

- First, the total sum of all elements is calculated. If the sum is odd, partition is not possible.
- The recursive `backtrack` function tries to reach half of the total sum.
- At each step, you can either include the current element in the subset or skip it.
- If a subset with the target sum is found, the function returns True.

---

## Real-Life Examples

1. **Load balancing:** Evenly distributing tasks between two servers or employees.
2. **Resource division:** Fairly dividing prizes or items between two people.
3. **Planning:** Assigning tasks to two processors or teams to minimize imbalance.
4. **Game development:** Fair distribution of resources or creating balanced teams.

---

# Useful Links

- [Partition Problem — Wikipedia](https://en.wikipedia.org/wiki/Partition_problem)
- [Subset Sum Problem — GeeksforGeeks](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/)
- [Dynamic Programming vs. Backtracking — LeetCode Discuss](https://leetcode.com/problems/partition-equal-subset-sum/solutions/)
- [Backtracking — GeeksforGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/)

---

# LeetCode Practice

| Difficulty | Problem                                         | Link                                                                              |
|------------|-------------------------------------------------|-----------------------------------------------------------------------------------|
| Medium     | Partition Equal Subset Sum                      | [#416 Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |
| Medium     | Subset Sum                                      | [#494 Target Sum](https://leetcode.com/problems/target-sum/)                      |
| Medium     | Split Array Largest Sum                         | [#410 Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) |
| Medium     | Minimum Subset Sum Difference                   | [#1049 Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/) |
| Easy       | Subsets                                         | [#78 Subsets](https://leetcode.com/problems/subsets/)                             |
| Medium     | Subsets II                                      | [#90 Subsets II](https://leetcode.com/problems/subsets-ii/)                       |
| Medium     | Combination Sum                                 | [#39 Combination Sum](https://leetcode.com/problems/combination-sum/)             |

---