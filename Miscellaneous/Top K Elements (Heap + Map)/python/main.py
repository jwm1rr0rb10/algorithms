### Example 1: Top K Largest Numbers
 
import heapq

def find_top_k_largest(nums, k):
    if k == 0:
        return []

    # Create a min-heap
    min_heap = []

    for num in nums:
        if len(min_heap) < k:
            # If heap size is less than k, just add the number
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]: # min_heap[0] is the smallest element in the min-heap
            # If current number is larger than the smallest in the heap,
            # remove the smallest and add the current number
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    # The min_heap now contains the k largest elements
    return sorted(min_heap, reverse=True) # Sort for presentation, otherwise just return min_heap

# Test cases
print("--- Top K Largest Numbers ---")
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(f"Nums: {nums1}, k: {k1} -> Top {k1}: {find_top_k_largest(nums1, k1)}") # Expected: [6, 5]

nums2 = [7, 10, 4, 3, 20, 15]
k2 = 3
print(f"Nums: {nums2}, k: {k2} -> Top {k2}: {find_top_k_largest(nums2, k2)}") # Expected: [20, 15, 10]

nums3 = [1, 2, 3, 4, 5]
k3 = 5
print(f"Nums: {nums3}, k: {k3} -> Top {k3}: {find_top_k_largest(nums3, k3)}") # Expected: [5, 4, 3, 2, 1]

nums4 = [10, 10, 10, 9, 9, 8]
k4 = 2
print(f"Nums: {nums4}, k: {k4} -> Top {k4}: {find_top_k_largest(nums4, k4)}") # Expected: [10, 10]


## Example 2: Top K Most Frequent Elements (Heap + Map)

import heapq
from collections import Counter

def find_top_k_frequent(words, k):
    if k == 0:
        return []

    # Step 1: Count frequencies using a hash map (Counter)
    frequency_map = Counter(words)
    print(f"Frequency Map: {frequency_map}")

    # Step 2: Use a min-heap to keep track of the top K elements by frequency
    # We store tuples (frequency, word). Python's heapq is a min-heap,
    # so it will naturally order by frequency (first element of tuple).
    min_heap = []

    for word, freq in frequency_map.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, word))
        elif freq > min_heap[0][0]: # Compare current frequency with the smallest frequency in the heap
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, (freq, word))
        # Optional: Handle ties based on secondary criteria (e.g., alphabetical order if freq is same)
        # elif freq == min_heap[0][0] and word < min_heap[0][1]: # Example for tie-breaking: if current word is smaller alphabetically
        #     heapq.heappop(min_heap)
        #     heapq.heappush(min_heap, (freq, word))


    # Step 3: Extract the elements from the heap
    # The heap contains (freq, word) tuples. We only need the words.
    result = [item[1] for item in min_heap]

    # Optional: Sort the result for consistent output if order matters (e.g., by frequency then alphabetically)
    # The problem usually specifies order. If not, any order of top K is fine.
    # Here, we sort descending by frequency, then ascending by word for ties.
    result.sort(key=lambda word: (-frequency_map[word], word))

    return result

# Test cases
print("\n--- Top K Most Frequent Elements ---")
words1 = ["i", "love", "leetcode", "i", "love", "coding"]
k1 = 2
print(f"Words: {words1}, k: {k1} -> Top {k1}: {find_top_k_frequent(words1, k1)}")
# Expected: ["i", "love"] (or ["love", "i"] depending on tie-breaking/heap internal order)

words2 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k2 = 3
print(f"Words: {words2}, k: {k2} -> Top {k2}: {find_top_k_frequent(words2, k2)}")
# Expected: ["the", "is", "sunny"]

words3 = ["a", "b", "c", "a", "b", "a"]
k3 = 1
print(f"Words: {words3}, k: {k3} -> Top {k3}: {find_top_k_frequent(words3, k3)}")
# Expected: ["a"]