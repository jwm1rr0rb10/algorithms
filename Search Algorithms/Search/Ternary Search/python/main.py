# Ternary Search (rare, but useful in optimization problems)

def ternary_search(data, target):
    """
    Searches for target in a sorted list data using ternary search.
    Returns the index of target if found, otherwise -1.
    This is an example for searching an element, not for function optimization.
    """
    low = 0              # Lower bound
    high = len(data) - 1 # Upper bound

    # While the search interval is valid
    while high >= low:
        # Calculate two points dividing the interval into approximately three parts
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        # Check if target is equal to elements at mid1 or mid2
        if data[mid1] == target:
            return mid1 # Element found
        if data[mid2] == target:
            return mid2 # Element found

        # Determine which of the three parts the target might be in
        if target < data[mid1]:
            # Target is in the left third [low, mid1 - 1]
            high = mid1 - 1
        elif target > data[mid2]:
            # Target is in the right third [mid2 + 1, high]
            low = mid2 + 1
        else:
            # Target is in the middle third [mid1 + 1, mid2 - 1]
            low = mid1 + 1
            high = mid2 - 1

    # Element not found
    return -1

# Examples of usage
sorted_data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target1 = 38
target2 = 10

# Search for target1
index1 = ternary_search(sorted_data, target1)
if index1 != -1:
    print(f"Element {target1} found at index {index1}")
else:
    print(f"Element {target1} not found")

# Search for target2
index2 = ternary_search(sorted_data, target2)
if index2 != -1:
    print(f"Element {target2} found at index {index2}")
else:
    print(f"Element {target2} not found")