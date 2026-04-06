def can_find_subset_sum_helper(index, current_sum, target_sum, nums):
    # Base case 1: Found the solution - the current sum equals the target
    if current_sum == target_sum:
        return True

    # Base case 2: Failure / Pruning
    # current_sum exceeded the target, OR we have considered all elements
    if current_sum > target_sum or index >= len(nums):
        return False

    # Recursive step: We have two options for nums[index]

    # Option A: Include nums[index] in the subset
    # Make a recursive call for the next element, adding the current one to the sum.
    # If this path leads to a solution, return True.
    if can_find_subset_sum_helper(index + 1, current_sum + nums[index], target_sum, nums):
        return True

    # Option B: Exclude nums[index] from the subset
    # If Option A didn't lead to a solution, try excluding the current element.
    # Make a recursive call for the next element, keeping the current sum.
    if can_find_subset_sum_helper(index + 1, current_sum, target_sum, nums):
        return True

    # If neither Option A nor Option B led to a solution from this state
    return False

# can_subset_sum - main function to check for the existence of a subset with the given sum
def can_subset_sum(nums, target_sum):
    # Start the recursive search from the first element (index 0) with an initial sum of 0.
    return can_find_subset_sum_helper(0, 0, target_sum, nums)

# Example usage:
nums1 = [10, 7, 5, 18, 12, 20, 15]
target1 = 35
print(f"Set: {nums1}, Target: {target1}")
if can_subset_sum(nums1, target1):
    print(f"There exists a subset with sum {target1}")
else:
    print(f"No subset exists with sum {target1}")

nums2 = [1, 2, 3, 4, 5]
target2 = 11
print(f"\nSet: {nums2}, Target: {target2}")
if can_subset_sum(nums2, target2):
    print(f"There exists a subset with sum {target2}")
else:
    print(f"No subset exists with sum {target2}")

nums3 = [1, 2, 3, 4, 5]
target3 = 20  # The sum of all elements = 15
print(f"\nSet: {nums3}, Target: {target3}")
if can_subset_sum(nums3, target3):
    print(f"There exists a subset with sum {target3}")
else:
    print(f"No subset exists with sum {target3}")