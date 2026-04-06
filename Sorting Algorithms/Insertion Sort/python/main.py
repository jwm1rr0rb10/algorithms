# insertion_sort sorts a list using the insertion sort algorithm
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Examples of using Insertion Sort:
data_insertion = [10, 7, 8, 9, 1, 5]
print("\nOriginal list (Insertion Sort):", data_insertion)
insertion_sort(data_insertion)
print("Sorted list (Insertion Sort):", data_insertion)

data_insertion_2 = [4, 2, 7, 1, 9, 3, 6, 8, 5]
print("Original list (Insertion Sort):", data_insertion_2)
insertion_sort(data_insertion_2)
print("Sorted list (Insertion Sort):", data_insertion_2)