# 🎯 Top K Elements (Heap + Map Approach)

## 📌 Problem Description

The "Top K Elements" problem asks us to find the `k` largest (or smallest) elements from a given list, array, or stream of data. A common variation also asks for the `k` most frequent elements.

**Examples:**
* Given `[3, 2, 1, 5, 6, 4]` and `k = 2`, find the 2 largest elements. Output: `[5, 6]` (order doesn't usually matter).
* Given `["apple", "banana", "apple", "orange", "banana", "apple"]` and `k = 2`, find the 2 most frequent words. Output: `["apple", "banana"]` (if counts are equal, alphabetical or original order might be specified).

## 💡 Core Idea and Approach

The naive approach would be to sort the entire array and then pick the top `k` elements. This would take $O(N \log N)$ time. We can do better by using a heap.

The core idea is to maintain a heap of size `k` that, at any point, contains the `k` "best" elements seen so far.

### For Top K Largest Elements: Use a Min-Heap

* We want to find the `k` largest elements.
* We use a **Min-Heap** of size `k`.
* Why a Min-Heap? Because the smallest element in our heap (its root) is the `k`-th largest element we've found so far. If we encounter a new element that is *larger* than this `k`-th largest element, it means the new element is one of the true top `k` elements, and the current `k`-th largest element can be discarded.

### For Top K Most Frequent Elements: Use a Map + Min-Heap

This is a two-step process:
1.  **Count Frequencies:** Use a **Map (Hash Table/Dictionary)** to count the occurrences of each unique element in the input. This transforms the problem from "elements" to "element-frequency pairs."
2.  **Find Top K Frequencies:** Now, apply the "Top K Largest Elements" logic to these `(element, frequency)` pairs. We'll use a **Min-Heap** that prioritizes based on frequency. If frequencies are tied, a secondary sorting criterion (e.g., alphabetical order of the element) might be specified.

## 📝 Algorithm Steps (Detailed)

### Case 1: Finding Top K Largest Numbers

1.  **Initialize a Min-Heap:** Create an empty min-heap (priority queue).
2.  **Iterate through Input:** For each `number` in the input array/list:
    * If `min_heap.size() < k`:
        * `min_heap.insert(number)` (Add the number to the heap).
    * Else if `number > min_heap.peek_min()`:
        * `min_heap.extract_min()` (Remove the smallest element from the heap).
        * `min_heap.insert(number)` (Add the current `number` to the heap).
    * Else (`number <= min_heap.peek_min()`):
        * Do nothing. This number is not among the top `k` largest seen so far.
3.  **Result:** After iterating through all numbers, the `min_heap` will contain the `k` largest elements. You can then extract them one by one (`min_heap.extract_min()`) if you need them in sorted order, or just return the heap's contents as a list.

### Case 2: Finding Top K Most Frequent Elements

1.  **Count Frequencies:**
    * Create a `frequency_map` (e.g., Python's `collections.Counter` or a dictionary).
    * Iterate through the input data and populate `frequency_map` where keys are elements and values are their frequencies.
2.  **Initialize a Min-Heap of Tuples:** Create an empty min-heap. This heap will store `(frequency, element)` tuples. The heap will prioritize based on the first element of the tuple (frequency), so it will effectively be a min-heap of frequencies.
3.  **Iterate through `frequency_map`:** For each `(element, frequency)` pair in the `frequency_map`:
    * If `min_heap.size() < k`:
        * `min_heap.insert((frequency, element))`
    * Else if `frequency > min_heap.peek_min().frequency`: (Compare current frequency with the frequency of the smallest element in the heap)
        * `min_heap.extract_min()`
        * `min_heap.insert((frequency, element))`
    * Else (`frequency <= min_heap.peek_min().frequency`):
        * Do nothing.
4.  **Result:** After iterating through all frequency pairs, the `min_heap` will contain `k` tuples, where the elements correspond to the `k` most frequent items. Extract the elements (e.g., the second item of each tuple) to get your result.

---

## ⏱️ Complexity Analysis

* **Time Complexity:**
    * **Counting Frequencies (if applicable):** $O(N)$ for iterating through all `N` elements to build the map.
    * **Heap Operations:** For each of the `M` unique elements (or `N` elements in the first case), we perform at most one heap insertion/deletion. A heap operation takes $O(\log K)$ time because the heap's maximum size is `K`.
    * **Total Time:** $O(N + M \log K)$ when counting frequencies (or $O(N \log K)$ if no frequency counting is needed). Since $M \le N$, this simplifies to **$O(N \log K)$**. This is more efficient than $O(N \log N)$ sorting when `K` is much smaller than `N`.

* **Space Complexity:**
    * **Frequency Map (if applicable):** $O(M)$ where `M` is the number of unique elements. In the worst case, $M=N$, so $O(N)$.
    * **Heap:** $O(K)$ as it stores at most `K` elements.
    * **Total Space:** $O(M + K)$ (or $O(N + K)$ in the worst case for frequencies), which simplifies to **$O(N)$** in the worst case (all unique elements) or **$O(K)$** if elements are not unique (for just finding largest numbers). More precisely, it's $O(\text{unique elements} + K)$.

---

## ⚠️ Variations and Considerations

* **Using a Max-Heap:** You *could* insert all `N` elements into a Max-Heap ($O(N \log N)$) and then extract `k` times ($O(K \log N)$). Total $O(N \log N + K \log N) = O(N \log N)$. This is generally less efficient than the $O(N \log K)$ min-heap approach when $K \ll N$.
* **Tie-breaking:** For "most frequent" problems, if two elements have the same frequency and you need to select `k`, the problem usually specifies a tie-breaking rule (e.g., lexicographical order). You'd handle this by including the tie-breaking criteria in your tuple for the heap, often as a negative value if it should be min-heap behavior for a tie-breaker, or just directly for max-heap behavior.
    * For example, for top K frequent where ties break alphabetically: `(frequency, element_string)` for a min-heap (Python default works since smaller strings come first). If you need reverse alphabetical, it might be `(frequency, -hash(element_string))` or a custom comparator.
* **Small `k` vs. Large `k`:** The heap approach is particularly efficient when `k` is small relative to `N`. If `k` is close to `N`, sorting ($O(N \log N)$) might be competitive or even simpler to implement, depending on the constant factors.

---

## 🧪 Python Examples

### Example 1: Top K Largest Numbers


```python 
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
```

## Example 2: Top K Most Frequent Elements (Heap + Map)

```python
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
```

---

## 🔗 Useful Links

* [**GeeksForGeeks - Priority Queue Introduction**](https://www.geeksforgeeks.org/priority-queue-set-1-introduction/) (Отличное введение)
* [**GeeksForGeeks - Heap Data Structure**](https://www.geeksforgeeks.org/heap-data-structure/) (Подробно о самой куче)
* [**Wikipedia - Priority Queue**](https://en.wikipedia.org/wiki/Priority_queue)
* [**Wikipedia - Heap (data structure)**](https://en.wikipedia.org/wiki/Heap_(data_structure))
* [**Python `heapq` module documentation**](https://docs.python.org/3/library/heapq.html)

---

## 🧩 LeetCode Connection

The "Top K Elements" pattern is extremely popular on LeetCode and in coding interviews. You'll find direct problems like:

* **"Kth Largest Element in an Array"** (Easy/Medium)
* **"Top K Frequent Elements"** (Medium)
* **"Top K Frequent Words"** (Medium)
* **"Find K Closest Elements"** (Medium)
* **"K Closest Points to Origin"** (Medium)
* **"Merge K Sorted Lists"** (Hard, uses a min-heap of list heads)

Mastering the heap-based approach for these types of problems is essential for technical interviews.
