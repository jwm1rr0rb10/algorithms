# Binary Search (must-know)

def binary_search(data, target):
    """
    Searches for target in a sorted list data using binary search.
    Returns the index of target if found, otherwise -1.
    """
    low = 0              # Lower bound of the current search segment
    high = len(data) - 1 # Upper bound of the current search segment

    # While the lower bound has not exceeded the upper bound
    while low <= high:
        # Find the index of the middle element
        mid = (low + high) // 2 # In Python, there is no overflow risk with standard int

        # Compare the middle element with the target value
        if data[mid] == target:
            return mid # Element found, return its index
        elif data[mid] < target:
            # If the middle element is less than the target, it can only be to the right of mid
            low = mid + 1 # Shift the lower bound to the right
        else: # data[mid] > target
            # If the middle element is greater than the target, it can only be to the left of mid
            high = mid - 1 # Shift the upper bound to the left

    # If the loop ends, the element was not found
    return -1

# Example usage
sorted_data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target1 = 23
target2 = 10

# Search for target1
index1 = binary_search(sorted_data, target1)
if index1 != -1:
    print(f"Element {target1} found at index {index1}")
else:
    print(f"Element {target1} not found")

# Search for target2
index2 = binary_search(sorted_data, target2)
if index2 != -1:
    print(f"Element {target2} found at index {index2}")
else:
    print(f"Element {target2} not found")
