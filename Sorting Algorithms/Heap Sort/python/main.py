# Function to restore the max-heap property for a subtree rooted at index i.
# n - size of the heap.
def heapify(arr, n, i):
    largest = i        # Initialize largest as root
    left = 2 * i + 1   # Left child = 2*i + 1
    right = 2 * i + 2  # Right child = 2*i + 2

    # If the left child exists (left < n) and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If the right child exists (right < n) and is greater than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root
    if largest != i:
        # Swap arr[i] and arr[largest]
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

# Main function for heap sort
def heapsort(arr):
    n = len(arr)

    # Phase 1: Build a max-heap from the array.
    # Start from the last parent node (n//2 - 1) and move to the root (0).
    # Use integer division '//' in Python.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Phase 2: Extract elements from the heap one by one.
    # Swap the last element of the heap with the root (the largest).
    # Reduce the heap size and restore the heap property for the new root.
    for i in range(n - 1, 0, -1):
        # Move the current root (largest element) to the end of the array
        arr[0], arr[i] = arr[i], arr[0]

        # Call heapify on the reduced heap of size i
        heapify(arr, i, 0)

# Usage examples:
data = [10, 7, 8, 9, 1, 5]
print("Original list:", data)
heapsort(data)
print("Sorted list:", data)

data2 = [4, 2, 7, 1, 9, 3, 6, 8, 5]
print("Original list:", data2)
heapsort(data2)
print("Sorted list:", data2)
