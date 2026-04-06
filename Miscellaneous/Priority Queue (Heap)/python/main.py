
import heapq

print("--- Priority Queue (Min-Heap) Example ---")

# Initialize an empty min-heap (a list in Python that heapq functions operate on)
min_heap = []

# 1. Inserting elements (heappush):
# heapq.heappush(heap, item) inserts an item while maintaining the min-heap property
print("Inserting elements:")
heapq.heappush(min_heap, 10) # [10]
print(f"After 10: {min_heap}")

heapq.heappush(min_heap, 30) # [10, 30]
print(f"After 30: {min_heap}")

heapq.heappush(min_heap, 20) # [10, 30, 20] -> Python's internal representation might be slightly different, but the heap property holds
print(f"After 20: {min_heap}")

heapq.heappush(min_heap, 5) # [5, 10, 20, 30] (internally balanced)
print(f"After 5: {min_heap}")

heapq.heappush(min_heap, 25)
print(f"After 25: {min_heap}")

print(f"\nCurrent Min-Heap state (internal representation): {min_heap}")
# Note: the array won't be fully sorted, but the root (index 0) will always be the smallest.

# 2. Extracting the smallest element (heappop):
# heapq.heappop(heap) extracts and returns the smallest item, then re-balances the heap.
print("\nExtracting elements:")
smallest = heapq.heappop(min_heap) # Extracts 5
print(f"Extracted smallest element: {smallest}")
print(f"Heap after extraction: {min_heap}") # [10, 25, 20, 30] (internal representation)

smallest = heapq.heappop(min_heap) # Extracts 10
print(f"Extracted smallest element: {smallest}")
print(f"Heap after extraction: {min_heap}") # [20, 25, 30]

# 3. Peeking at the smallest element (peek/top):
# In Python's heapq, there's no direct peek/top function, but it's always the element at index 0
if min_heap:
    print(f"\nSmallest element (without removal): {min_heap[0]}")
else:
    print("\nHeap is empty.")

# 4. Building a heap from an existing list (heapify):
print("\nBuilding a heap from an existing list:")
my_list = [9, 1, 7, 3, 5]
heapq.heapify(my_list) # Transforms the list into a min-heap "in-place"
print(f"List after heapify: {my_list}") # [1, 3, 7, 9, 5] (internal min-heap representation)

# Extracting from the newly created heap
print(f"Extracted first: {heapq.heappop(my_list)}") # Extracts 1
print(f"Extracted second: {heapq.heappop(my_list)}") # Extracts 3

# Example of Max-Heap (not direct, but can be simulated by storing negative values)
print("\n--- Simulating a Max-Heap (using a Min-Heap) ---")
max_heap_simulated = []

heapq.heappush(max_heap_simulated, -10)
heapq.heappush(max_heap_simulated, -30)
heapq.heappush(max_heap_simulated, -20)
heapq.heappush(max_heap_simulated, -5)

print(f"Simulated Max-Heap (negative values): {max_heap_simulated}")

# Extract the "smallest" negative, which corresponds to the "largest" positive
largest_simulated = -heapq.heappop(max_heap_simulated)
print(f"Extracted largest element (simulated): {largest_simulated}") # 30
print(f"Simulated Max-Heap after extraction: {max_heap_simulated}")