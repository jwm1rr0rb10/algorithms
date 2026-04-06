def linear_search(data, target):
    """
    Returns the index of the first occurrence of target in data,
    or -1 if target is not found.
    """
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1

# Example usage:
numbers = [8, 3, 7, 1, 9, 4]
target1 = 7
target2 = 5

result1 = linear_search(numbers, target1)
print(f"Element {target1} found at index {result1}" if result1 != -1 else f"Element {target1} not found")

result2 = linear_search(numbers, target2)
print(f"Element {target2} found at index {result2}" if result2 != -1 else f"Element {target2} not found")