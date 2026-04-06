# 🔍 Monotonic Stack

## 📌 Problem Description

* A **Monotonic Stack** is a stack data structure where the elements are kept in a strictly increasing or strictly decreasing order. It's not a standalone data structure, but rather a technique or pattern of using a standard stack (LIFO) to efficiently solve problems that involve finding the "next greater element," "next smaller element," or related concepts within an array or sequence.

* The core idea is to process elements one by one and use the stack to maintain a subset of previously processed elements that are "candidates" for fulfilling certain monotonic conditions for future elements. By keeping the stack monotonic, we can perform these lookups and updates in an amortized `O(1)` time per element.

## 💡 Idea and Approach

The general approach for using a Monotonic Stack involves iterating through the input array (usually from left to right, but sometimes right to left depending on the problem) and performing specific actions based on the current element and the top of the stack.

### For a Monotonic Increasing Stack:

(Used to find the **next smaller element** or **previous smaller element** for elements)
The stack stores elements (or their indices) in increasing order from bottom to top.

1. **Iterate through the array (e.g., `nums[i]`):**

2. **While the stack is not empty AND the element at the top of the stack (`nums[stack.top()]`) is greater than or equal to `nums[i]`:**

    * This means `nums[i]` is a smaller element that has "found" its next smaller element (if processing left-to-right) or will be `nums[i]`'s previous smaller element.

    * pop elements from the stack. For each popped element, `nums[i]` is its "next smaller element."

3. **Push `i` onto the stack:** `nums[i]` is now a candidate for being the "next smaller element" for future elements.


### Key Benefits:

* **Linear Time:** Each element is pushed onto the stack at most once and popped from the stack at most once, leading to an overall `O(N)` time complexity.

* **Efficient Lookups:** Allows constant-time access to the most recently relevant element (top of the stack) that maintains the monotonicity.

---

## 🧪 Python Example

A classic problem solved with a monotonic stack is "Next Greater Element I" (LeetCode 496) or "Next Greater Element II" (LeetCode 503 for circular arrays), and "Largest Rectangle in Histogram" (LeetCode 84).

Here's an example for finding the "Next Greater Element" for each element in an array using a Monotonic Decreasing Stack:

```python 
def next_greater_element(nums):
    """
    Finds the next greater element for each element in the input list.
    If no greater element exists to the right, -1 is used.

    Uses a Monotonic Decreasing Stack.
    The stack stores indices of elements in decreasing order of their values.
    When a new element `nums[i]` is processed, any element on top of the stack
    that is smaller than `nums[i]` has found its next greater element.
    """
    n = len(nums)
    # Initialize result array with -1 (default for no next greater element)
    result = [-1] * n
    # Stack stores indices
    stack = [] # Monotonic Decreasing Stack (stores indices of elements in decreasing order of value)

    for i in range(n):
        # While stack is not empty AND the element at the top of the stack
        # is LESS THAN the current element (nums[i]):
        # This means nums[i] is the Next Greater Element for stack.top()
        while stack and nums[stack[-1]] < nums[i]:
            idx_to_update = stack.pop()
            result[idx_to_update] = nums[i]

        # Push the current element's index onto the stack.
        # It's a candidate for being the Next Greater Element for future elements.
        stack.append(i)

    # After iterating, any elements remaining in the stack do not have a next greater element
    # in the array (or we're done processing the current pass for circular array problems).
    # They will remain -1 in the result, as initialized.

    return result

# Example Usage:
nums1 = [4, 5, 2, 10, 8]
print(f"Nums: {nums1} -> Next Greater Elements: {next_greater_element(nums1)}")
# Expected: [5, 10, 10, -1, -1]
# Explanation:
# 4 -> 5
# 5 -> 10
# 2 -> 10
# 10 -> -1
# 8 -> -1

nums2 = [1, 3, 2, 4]
print(f"Nums: {nums2} -> Next Greater Elements: {next_greater_element(nums2)}")
# Expected: [3, 4, 4, -1]

nums3 = [13, 7, 6, 12]
print(f"Nums: {nums3} -> Next Greater Elements: {next_greater_element(nums3)}")
# Expected: [-1, 12, 12, -1]
```

---

## ⏱️ Complexity

The monotonic stack technique offers efficient performance.

* **Time Complexity:** `O(N)`, where `N` is the number of elements in the input array.

    * Each element is pushed onto the stack at most once.

    * Each element is popped from the stack at most once.

    * Therefore, the total number of push and pop operations is proportional to N.

* **Space Complexity:** `O(N)` in the worst case.

    * If the input array is strictly monotonic (e.g., `[1, 2, 3, 4, 5]` for a decreasing stack, or `[5, 4, 3, 2, 1]` for an increasing stack), all elements might be pushed onto the stack before any are popped, leading to the stack holding up to N elements.

---

## ⚠️ Considerations

* **Empty Stack Check:** Always check if the stack is empty before attempting to access `stack[-1]` (top element).

* **Iterating Direction:** The direction of iteration (left-to-right vs. right-to-left) and the type of monotonic stack (increasing vs. decreasing) depend on whether you're looking for the "next" or "previous" element and "greater" or "smaller." It's often helpful to draw out small examples to determine the correct setup.

    * To find **Next Greater Element:** Iterate L->R, Monotonic Decreasing Stack.

    * To find **Previous Greater Element:** Iterate L->R, Monotonic Increasing Stack (pop if current >= stack.top(), result for current is stack.top()).

    * And so on.

    * **Handling Duplicates:** Depending on the problem, you might need to adjust the comparison (e.g., `>` vs. `>=`) to include or exclude elements equal to the current one.

    * **Circular Arrays:** For problems involving circular arrays, you often iterate through the array twice (e.g., `nums + nums` or `range(2 * n)`) to simulate the circularity.

    ---

    ## 🧭 Applications

    Monotonic Stacks are a specialized but very powerful technique for solving a range of problems where you need to find elements related to "next/previous greater/smaller":

    * **Next Greater/Smaller Element:** Finding the first element to the right (or left) that is greater than (or smaller than) the current element.

    * **Largest Rectangle in Histogram:** Finding the maximum area of a rectangle that can be formed within a histogram. This is a classic application where a monotonic stack is used to efficiently find the left and right boundaries for each bar.

    * **Sum of Subarray Minimums/Maximums:** Calculating the sum of minimums (or maximums) of all possible contiguous subarrays.

    * **Trapping Rain Water:** While solvable with two pointers, a monotonic stack can also be used.

    * **Removing K Digits to Get Smallest Number:** Used to find the lexicographically smallest number after removing k digits.

    * **Valid Parentheses / Longest Valid Parentheses:** While primarily stack problems, some variations might use monotonicity.

    * **Stock Span Problem:** Calculating the span for each day's stock price (number of consecutive days before the current day that the price was less than or equal to the current day's price).

    ---

## 🔗 Useful Links
- [**GeeksForGeeks - Monotonic Stack**](https://www.geeksforgeeks.org/dsa/introduction-to-monotonic-stack-2/) 
- [**CP Algorithms - Monotonic Stack**](https://cp-algorithms.com/index.html)(Part of a broader discussion on stacks with min/max operations)
- [**LeetCode Problem 84: Largest Rectangle in Histogram**](https://leetcode.com/problems/largest-rectangle-in-histogram/)
- [**LeetCode Problem 496: Next Greater Element I**](https://leetcode.com/problems/next-greater-element-i/)
- [**LeetCode Problem 503: Next Greater Element II**](https://leetcode.com/problems/next-greater-element-ii/)

---

## 🧩 LeetCode Connection

Monotonic Stack problems are very common in interviews and competitive programming, often falling into the "medium" to "hard" difficulty categories because they require a conceptual leap from basic stack usage.

* **Direct Application:** Problems like "Next Greater Element" (I & II), "Next Smaller Element," "Previous Greater/Smaller Element."

* **Advanced Applications:** "Largest Rectangle in Histogram" (a must-know for this pattern), "Trapping Rain Water" (alternative solution), "Sum of Subarray Minimums."

* **Pattern Recognition:** The key is to recognize when a problem asks you to find the "first element to the left/right that satisfies a certain condition (greater/smaller)." If the condition involves relative values and order, a monotonic stack is often the optimal solution.

Mastering the monotonic stack technique is a significant step in expanding your algorithmic problem-solving toolkit beyond basic data structures.

---