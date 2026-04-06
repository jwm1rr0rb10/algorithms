# Function to merge two sorted lists
def merge(left, right):
    result = []
    i, j = 0, 0  # Pointers for the left and right lists

    # While there are elements in both lists, compare and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from the left list (if any)
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add remaining elements from the right list (if any)
    while j < len(right):
        result.append(right[j])
        j += 1

    return result  # Return the merged sorted list

# Main recursive Merge Sort function
def mergesort(arr):
    # Base case: a list with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  # Find the middle of the list (integer division)
    left = mergesort(arr[:mid])  # Recursively sort the left half
    right = mergesort(arr[mid:])  # Recursively sort the right half

    # Merge the two sorted halves
    return merge(left, right)

# Usage examples:
data = [10, 7, 8, 9, 1, 5]
print("Original list:", data)
sorted_data = mergesort(data)
print("Sorted list:", sorted_data)

data2 = [4, 2, 7, 1, 9, 3, 6, 8, 5]
print("Original list:", data2)
sorted_data2 = mergesort(data2)
print("Sorted list:", sorted_data2)
