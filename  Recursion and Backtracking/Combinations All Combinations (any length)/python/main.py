def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(list(path))
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # backtracking

    backtrack(0, [])
    return result

# Example usage:
print(subsets([1, 2, 3]))
# [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]