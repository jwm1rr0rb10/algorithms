# bubble_sort sorts a list using the bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    # Outer loop iterates through all elements
    for i in range(n - 1):
        swapped = False  # Optimization flag

        # Inner loop compares adjacent elements
        # (n - i - 1) because the last i elements are already in place
        for j in range(n - i - 1):
            # If the current element is greater than the next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Mark that a swap occurred

        # If no swaps occurred in this pass, the list is sorted
        if not swapped:
            break

# Example usage of Bubble Sort:
data_bubble = [10, 7, 8, 9, 1, 5]
print("Original list (Bubble Sort):", data_bubble)
bubble_sort(data_bubble)
print("Sorted list (Bubble Sort):", data_bubble)

data_bubble_2 = [1, 2, 3, 4, 5]  # Already sorted
print("Original list (Bubble Sort):", data_bubble_2)
bubble_sort(data_bubble_2)
print("Sorted list (Bubble Sort):", data_bubble_2)
