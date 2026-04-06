def next_greater_element(nums):
    """
    Finds the next greater element for each element in the input list.
    If no greater element exists to the right, -1 is used.

    Uses a Monotonic Decreasing Stack.
    The stack stores indices of elements in decreasing order of their values.
    When a new element `nums[i]` is processed, any element on top of the stack
    that is smaller than `nums[i]` has found its next greater element.
    """
    n = len(nums)
    # Initialize result array with -1 (default for no next greater element)
    result = [-1] * n
    # Stack stores indices
    stack = [] # Monotonic Decreasing Stack (stores indices of elements in decreasing order of value)

    for i in range(n):
        # While stack is not empty AND the element at the top of the stack
        # is LESS THAN the current element (nums[i]):
        # This means nums[i] is the Next Greater Element for stack.top()
        while stack and nums[stack[-1]] < nums[i]:
            idx_to_update = stack.pop()
            result[idx_to_update] = nums[i]

        # Push the current element's index onto the stack.
        # It's a candidate for being the Next Greater Element for future elements.
        stack.append(i)

    # After iterating, any elements remaining in the stack do not have a next greater element
    # in the array (or we're done processing the current pass for circular array problems).
    # They will remain -1 in the result, as initialized.

    return result

# Example Usage:
nums1 = [4, 5, 2, 10, 8]
print(f"Nums: {nums1} -> Next Greater Elements: {next_greater_element(nums1)}")
# Expected: [5, 10, 10, -1, -1]
# Explanation:
# 4 -> 5
# 5 -> 10
# 2 -> 10
# 10 -> -1
# 8 -> -1

nums2 = [1, 3, 2, 4]
print(f"Nums: {nums2} -> Next Greater Elements: {next_greater_element(nums2)}")
# Expected: [3, 4, 4, -1]

nums3 = [13, 7, 6, 12]
print(f"Nums: {nums3} -> Next Greater Elements: {next_greater_element(nums3)}")
# Expected: [-1, 12, 12, -1]