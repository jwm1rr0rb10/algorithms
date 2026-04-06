# Function to perform partitioning
# Takes the last element as pivot, places it
# at its correct position, and places all smaller elements before it,
# and larger elements after it.
def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1      # Index of smaller element

    # Iterate through elements from low to high-1
    for j in range(low, high):
        # If the current element is less than or equal to the pivot
        if arr[j] <= pivot:
            i += 1  # Increment index of smaller element
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element (arr[high])
    # with the element at index i+1.
    # The element at index i+1 is now in its correct position.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1 # Return the partitioning index

# Main recursive Quick Sort function
# arr[] --> Array to be sorted
# low  --> Starting index
# high --> Ending index
def quicksort(arr, low, high):
    if low < high:
        # pi is the partitioning index after partition call
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Auxiliary function to call quicksort with initial parameters
def sort_quick(arr):
    quicksort(arr, 0, len(arr) - 1)

# Usage examples:
data = [10, 7, 8, 9, 1, 5]
print("Original array:", data)
sort_quick(data)
print("Sorted array:", data)

data2 = [4, 2, 7, 1, 9, 3, 6, 8, 5]
print("Original array:", data2)
sort_quick(data2)
print("Sorted array:", data2)