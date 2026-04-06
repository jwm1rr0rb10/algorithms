# Permutations — Recursive (Backtracking) Approach

## What is a permutation?
* A permutation of a set of elements is an ordered arrangement of those elements.
* For example, for the set `{1, 2, 3}`, the possible permutations are:
  `{1,2,3}, {1,3,2}, {2,1,3}, {2,3,1}, {3,1,2}, {3,2,1}`
* The number of permutations of a set of n distinct elements is `n!` (n factorial).

---

## How to use recursion and backtracking to generate permutations?

* Build each permutation one element at a time.
* Use a recursive function that, at each step, picks one of the remaining elements and adds it to the current partial permutation.
* When the length of the current permutation equals the number of elements, we have a complete permutation.

### Backtracking approach:
* **Choice:** Pick an unused element from the input.
* **Explore:** Add the chosen element to the current permutation and recursively generate the remaining.
* **Undo choice (Backtrack):** Remove the element and mark it as available again.
* Use a boolean array or set to track used elements.

---

## Complexity Analysis

### Time Complexity:
* There are exactly `N!` unique permutations for `N` elements.
* Each is constructed in `O(N)` time (copying or building).
* **Total:** `O(N! × N)`

### Space Complexity:
* **Auxiliary:** `O(N)` for recursion stack, current permutation, and used tracker.
* **Total:** `O(N! × N)` to store all permutations.

---

## Go Example

```go
package main

import "fmt"

func generatePermutationsHelper(nums []int, currentPermutation []int, used []bool, result *[][]int) {
	if len(currentPermutation) == len(nums) {
		permutationCopy := make([]int, len(currentPermutation))
		copy(permutationCopy, currentPermutation)
		*result = append(*result, permutationCopy)
		return
	}
	for i := 0; i < len(nums); i++ {
		if !used[i] {
			currentPermutation = append(currentPermutation, nums[i])
			used[i] = true
			generatePermutationsHelper(nums, currentPermutation, used, result)
			currentPermutation = currentPermutation[:len(currentPermutation)-1]
			used[i] = false
		}
	}
}

func Permute(nums []int) [][]int {
	var result [][]int
	used := make([]bool, len(nums))
	generatePermutationsHelper(nums, []int{}, used, &result)
	return result
}

func main() {
	nums := []int{1, 2, 3}
	permutations := Permute(nums)
	fmt.Println("Permutations for", nums, ":")
	for _, p := range permutations {
		fmt.Println(p)
	}
}
```

---

## Go Code Explanation

* **Permute** initializes the result and used tracker and calls the helper.
* **generatePermutationsHelper** recursively builds up permutations:
  * **Base case:** If current permutation length equals input length, copy and store it.
  * **Recursive step:** For each unused element, try it, recurse, then backtrack (unmark and remove).

---

## Python Example

```python
def solve_permutations(nums):
    result = []
    n = len(nums)
    used = [False] * n

    def backtrack(current_permutation):
        if len(current_permutation) == n:
            result.append(list(current_permutation))
            return
        for i in range(n):
            if not used[i]:
                current_permutation.append(nums[i])
                used[i] = True
                backtrack(current_permutation)
                current_permutation.pop()
                used[i] = False

    backtrack([])
    return result

# Example usage:
nums1 = [1, 2, 3]
permutations1 = solve_permutations(nums1)
print(f"Permutations for {nums1}:")
for p in permutations1:
    print(p)
```

---

## Python Code Explanation

* `solve_permutations` initializes result and used tracker, then calls `backtrack`.
* `backtrack`:
  * **Base case:** If permutation is full, copy and store.
  * **Recursive step:** For each unused element, pick, recurse, backtrack.

---

## Useful Links

- [Permutation — Wikipedia](https://en.wikipedia.org/wiki/Permutation)
- [Permutations — LeetCode](https://leetcode.com/problems/permutations/)
- [Backtracking — GeeksforGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [Combinatorics — Brilliant.org](https://brilliant.org/wiki/permutations/)

---

## LeetCode Practice

| Difficulty | Problem                       | Link                                                            |
|------------|-------------------------------|-----------------------------------------------------------------|
| Medium     | Permutations                  | [#46 Permutations](https://leetcode.com/problems/permutations/) |
| Medium     | Permutations II (with duplicates) | [#47 Permutations II](https://leetcode.com/problems/permutations-ii/) |
| Medium     | Next Permutation              | [#31 Next Permutation](https://leetcode.com/problems/next-permutation/) |
| Medium     | Letter Tile Possibilities     | [#1079 Letter Tile Possibilities](https://leetcode.com/problems/letter-tile-possibilities/) |
| Medium     | Generate Parentheses          | [#22 Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) |
| Medium     | Subsets                       | [#78 Subsets](https://leetcode.com/problems/subsets/)           |

---