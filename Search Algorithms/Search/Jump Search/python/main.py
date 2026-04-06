import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Jump ahead in blocks
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search within the block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 13, 17, 21, 29, 35, 42, 56]
print(jump_search(arr, 21))  # Output: 7
print(jump_search(arr, 6))   # Output: -1