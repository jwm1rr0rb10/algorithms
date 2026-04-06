# Subset Sum Problem — Recursive (Backtracking) Approach

## What is the Subset Sum Problem?

Given a set (or list) of integers and a target sum T, determine if there exists a subset whose elements sum to T. This version checks only for existence, not all such subsets.

**Example:**  
Set: {10, 7, 5, 18, 12, 20, 15}, Target T = 35  
Possible solutions: {10, 5, 20} or {7, 18, 10}

---

## Recursion and Backtracking Approach

For each element, decide to include or exclude it, and recurse on the next element. Backtracking prunes paths that exceed the target or fail.

### Algorithm Outline

Let `canFindSubsetSum(index, current_sum, target_sum, nums)` be our recursive function:
- **Base Case 1 (Success):** If `current_sum == target_sum` ⇒ return `True`.
- **Base Case 2 (Failure/Pruning):** If `current_sum > target_sum` or `index == len(nums)` ⇒ return `False`.
- **Recursive Step:**
  - **Include** `nums[index]` and recurse.
  - **Exclude** `nums[index]` and recurse.
  - Return `True` if either branch succeeds.

Initial call: `canFindSubsetSum(0, 0, target_sum, nums)`

---

## Golang Example

```go
package main

import "fmt"

func canFindSubsetSumHelper(index int, currentSum int, targetSum int, nums []int) bool {
	if currentSum == targetSum {
		return true
	}
	if currentSum > targetSum || index >= len(nums) {
		return false
	}
	if canFindSubsetSumHelper(index+1, currentSum+nums[index], targetSum, nums) {
		return true
	}
	if canFindSubsetSumHelper(index+1, currentSum, targetSum, nums) {
		return true
	}
	return false
}

func CanSubsetSum(nums []int, targetSum int) bool {
	return canFindSubsetSumHelper(0, 0, targetSum, nums)
}

func main() {
	nums1 := []int{10, 7, 5, 18, 12, 20, 15}
	target1 := 35
	fmt.Printf("Set: %v, Target: %d\n", nums1, target1)
	if CanSubsetSum(nums1, target1) {
		fmt.Println("There exists a subset with sum", target1)
	} else {
		fmt.Println("No subset exists with sum", target1)
	}
}
```

---

## Explanation (Go)

- **CanSubsetSum:** Entry point, calls the recursive helper.
- **canFindSubsetSumHelper:**
  - Base cases: found (`currentSum == targetSum`) or failed/pruned path.
  - Recursive: try including and excluding the current element.

---

## Python Example

```python
def can_find_subset_sum_helper(index, current_sum, target_sum, nums):
    if current_sum == target_sum:
        return True
    if current_sum > target_sum or index >= len(nums):
        return False
    if can_find_subset_sum_helper(index + 1, current_sum + nums[index], target_sum, nums):
        return True
    if can_find_subset_sum_helper(index + 1, current_sum, target_sum, nums):
        return True
    return False

def can_subset_sum(nums, target_sum):
    return can_find_subset_sum_helper(0, 0, target_sum, nums)

# Example usage:
nums1 = [10, 7, 5, 18, 12, 20, 15]
target1 = 35
print(f"Set: {nums1}, Target: {target1}")
if can_subset_sum(nums1, target1):
    print(f"There exists a subset with sum {target1}")
else:
    print(f"No subset exists with sum {target1}")
```

---

## Explanation (Python)

- **can_subset_sum:** Entry point.
- **can_find_subset_sum_helper:** Same logic as Go, uses recursion to try including/excluding each element.

---

## Complexity Analysis

| Metric            | Complexity      | Explanation                                                   |
|:------------------|:----------------|:--------------------------------------------------------------|
| **Time**          | O(2^N)          | Each element: include or exclude (worst-case).                |
| **Space**         | O(N)            | Recursion stack up to N deep.                                 |

---

## Practical Notes

- The Subset Sum Problem is **NP-complete**; this approach is only feasible for small N (~20–25).
- For larger N or production, dynamic programming is used (pseudopolynomial time).
- This recursive pattern underlies many combinatorial and optimization problems.

---

## Real-World Applications

- **Knapsack Problem:** Subset sum is a special case.
- **Partition Problem:** Partition a set into two equal-sum subsets.
- **Cryptography:** Some attacks reduce to subset sum.
- **Test Data Generation:** Create sets with specific sums.
- **Finance:** Select assets to match a target cost.

---

## Useful Links

- [Subset Sum Problem — Wikipedia](https://en.wikipedia.org/wiki/Subset_sum_problem)
- [Subset Sum — GeeksforGeeks](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/)
- [Partition Problem](https://en.wikipedia.org/wiki/Partition_problem)
- [Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem)

---

## LeetCode Practice

| Difficulty | Problem                                   | Link                                                                            |
|------------|-------------------------------------------|---------------------------------------------------------------------------------|
| Medium     | Partition Equal Subset Sum                | [#416 Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |
| Medium     | Target Sum                               | [#494 Target Sum](https://leetcode.com/problems/target-sum/)                     |
| Medium     | Subsets                                  | [#78 Subsets](https://leetcode.com/problems/subsets/)                            |
| Medium     | Subsets II                               | [#90 Subsets II](https://leetcode.com/problems/subsets-ii/)                      |
| Medium     | Combination Sum                          | [#39 Combination Sum](https://leetcode.com/problems/combination-sum/)            |

---