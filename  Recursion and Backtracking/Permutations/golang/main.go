package main

import "fmt"

// generatePermutationsHelper - recursive helper function
// nums: the original set of numbers
// currentPermutation: the current permutation being formed
// used: boolean array to track which elements have been used
// result: slice of slices to store all generated permutations
func generatePermutationsHelper(nums []int, currentPermutation []int, used []bool, result *[][]int) {
	// Base case: if the current permutation has the same length as the original set,
	// we've found a complete permutation. Make a copy and add it to the result.
	if len(currentPermutation) == len(nums) {
		// Important to make a copy of currentPermutation, as it will change
		// during backtracking.
		permutationCopy := make([]int, len(currentPermutation))
		copy(permutationCopy, currentPermutation)
		*result = append(*result, permutationCopy)
		return
	}

	// Recursive step: iterate over all elements in the original set
	for i := 0; i < len(nums); i++ {
		// If the element hasn't been used in the current permutation yet
		if !used[i] {
			// 1. Choice: add the element to the current permutation
			currentPermutation = append(currentPermutation, nums[i])
			used[i] = true

			// 2. Explore: make a recursive call
			generatePermutationsHelper(nums, currentPermutation, used, result)

			// 3. Undo choice (Backtracking): remove the element from the current permutation
			// and mark it as unused.
			currentPermutation = currentPermutation[:len(currentPermutation)-1]
			used[i] = false
		}
	}
}

// Permute - main function to generate all permutations
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

	nums2 := []int{4, 5}
	permutations2 := Permute(nums2)
	fmt.Println("\nPermutations for", nums2, ":")
	for _, p := range permutations2 {
		fmt.Println(p)
	}
}
