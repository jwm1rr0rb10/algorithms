# Helper function to get the digit at the given place (exp)
def get_digit(number, exp):
    # For example, for number 170 and exp=10: (170 // 10) % 10 = 17 % 10 = 7
    # For number 170 and exp=1: (170 // 1) % 10 = 170 % 10 = 0
    return (number // exp) % 10

# Helper function to perform Counting Sort based on the digit at exp place
# This function must be STABLE.
def count_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n  # Output list
    count = [0] * 10  # Count list for digits 0-9

    # Count occurrences of digits
    for i in range(n):
        digit = get_digit(arr[i], exp)
        count[digit] += 1

    # Compute cumulative counts
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output list in reverse order (to maintain stability)
    for i in range(n - 1, -1, -1):
        digit = get_digit(arr[i], exp)
        position = count[digit] - 1
        output[position] = arr[i]
        count[digit] -= 1

    # Copy sorted elements back to the original list
    # In Python, slicing can also be used, but element-wise copying is more explicit
    for i in range(n):
        arr[i] = output[i]  # or arr[:] = output  # this also works, but less explicit

# Function radix_sort to perform the Radix Sort
def radix_sort(arr):
    n = len(arr)
    if n <= 1:
        return  # A list with 0 or 1 element is already sorted

    # Find the maximum number to determine the number of digits
    max_val = max(arr)

    # Sort by each digit place. exp = current digit place (1, 10, 100, ...)
    exp = 1
    while max_val // exp > 0:
        count_sort_for_radix(arr, exp)
        exp *= 10

# Examples of using Radix Sort:
data_radix = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original list (Radix Sort):", data_radix)
radix_sort(data_radix)
print("Sorted list (Radix Sort):", data_radix)

data_radix_2 = [4, 2, 7, 1, 9, 3, 6, 8, 5]
print("Original list (Radix Sort):", data_radix_2)
radix_sort(data_radix_2)
print("Sorted list (Radix Sort):", data_radix_2)

data_radix_3 = [123, 45, 6, 7890, 1, 555, 10000]
print("Original list (Radix Sort):", data_radix_3)
radix_sort(data_radix_3)
print("Sorted list (Radix Sort):", data_radix_3)