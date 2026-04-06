package main

import "fmt"

// canFindSubsetSumHelper - recursive helper function to find a subset with the given sum
// index: the index of the current element being considered in nums
// currentSum: the sum of elements included up to the current step
// targetSum: the target sum
// nums: the original set of numbers
func canFindSubsetSumHelper(index int, currentSum int, targetSum int, nums []int) bool {
	// Base case 1: Found a solution - the current sum equals the target
	if currentSum == targetSum {
		return true
	}

	// Base case 2: Failure / Pruning
	// currentSum exceeds the target, OR we have considered all elements
	if currentSum > targetSum || index >= len(nums) {
		return false
	}

	// Recursive step: We have two options for nums[index]

	// Option A: Include nums[index] in the subset
	// Make a recursive call for the next element, adding the current one to the sum.
	// If this path leads to a solution, return true.
	if canFindSubsetSumHelper(index+1, currentSum+nums[index], targetSum, nums) {
		return true
	}

	// Option B: Exclude nums[index] from the subset
	// If Option A did not lead to a solution, try excluding the current element.
	// Make a recursive call for the next element, keeping the current sum.
	if canFindSubsetSumHelper(index+1, currentSum, targetSum, nums) {
		return true
	}

	// If neither Option A nor Option B led to a solution from this state
	return false
}

// CanSubsetSum - main function to check the existence of a subset with the given sum
func CanSubsetSum(nums []int, targetSum int) bool {
	// Start the recursive search from the first element (index 0) with an initial sum of 0.
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

	nums2 := []int{1, 2, 3, 4, 5}
	target2 := 11
	fmt.Printf("\nSet: %v, Target: %d\n", nums2, target2)
	if CanSubsetSum(nums2, target2) {
		fmt.Println("There exists a subset with sum", target2)
	} else {
		fmt.Println("No subset exists with sum", target2)
	}

	nums3 := []int{1, 2, 3, 4, 5}
	target3 := 20 // The sum of all elements = 15
	fmt.Printf("\nSet: %v, Target: %d\n", nums3, target3)
	if CanSubsetSum(nums3, target3) {
		fmt.Println("There exists a subset with sum", target3)
	} else {
		fmt.Println("No subset exists with sum", target3)
	}
}
