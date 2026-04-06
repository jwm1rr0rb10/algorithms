def solve_permutations(nums):
    result = []
    n = len(nums)
    used = [False] * n # Boolean list to track used elements

    def backtrack(current_permutation):
        # Base case: if the length of the current permutation equals the length of the original list
        if len(current_permutation) == n:
            # Add a copy of the current permutation to the result
            result.append(list(current_permutation))
            return

        # Recursive step: iterate through all elements of the original list
        for i in range(n):
            # If the element is not yet used
            if not used[i]:
                # 1. Choose: add the element to the current permutation
                current_permutation.append(nums[i])
                used[i] = True

                # 2. Explore: make the recursive call
                backtrack(current_permutation)

                # 3. Unchoose (Backtrack): remove the last element
                # and mark it as unused
                current_permutation.pop()
                used[i] = False

    backtrack([]) # Start with an empty current permutation
    return result

# Example usage:
nums1 = [1, 2, 3]
permutations1 = solve_permutations(nums1)
print(f"Permutations for {nums1}:")
for p in permutations1:
    print(p)

nums2 = [4, 5]
permutations2 = solve_permutations(nums2)
print(f"\nPermutations for {nums2}:")
for p in permutations2:
    print(p)