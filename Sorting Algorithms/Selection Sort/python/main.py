# selection_sort sorts a list using the Selection Sort algorithm
def selection_sort(arr):
    n = len(arr)
    # Iterate through the list up to the second-to-last element
    for i in range(n - 1):
        # Assume the current element (arr[i]) is the smallest in the unsorted part
        min_idx = i

        # Find the index of the smallest element in the remaining unsorted part (from i+1 to the end)
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Found a new minimum

        # If the smallest element is not already at the current position i,
        # swap them. The current element (arr[i]) is placed in its correct position.
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Examples of using Selection Sort:
data_selection = [10, 7, 8, 9, 1, 5]
print("\nOriginal list (Selection Sort):", data_selection)
selection_sort(data_selection)
print("Sorted list (Selection Sort):", data_selection)

data_selection_2 = [4, 2, 7, 1, 9, 3, 6, 8, 5]
print("Original list (Selection Sort):", data_selection_2)
selection_sort(data_selection_2)
print("Sorted list (Selection Sort):", data_selection_2)
