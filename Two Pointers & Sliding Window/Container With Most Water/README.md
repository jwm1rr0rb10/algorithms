# Container With Most Water — Two Pointers Approach

## Problem Description

Given an array of integers `height` where each element represents the height of a vertical line on the x-axis, find two lines that together with the x-axis form a container such that the container contains the most water. Return the maximum amount of water a container can store.

**Example:**  
Input: height = [1,8,6,2,5,4,8,3,7]  
Output: 49  
Explanation: The two lines at indices 1 and 8 (heights 8 and 7) form a container with area 7 * 7 = 49 (width 7, height 7).

---

## Algorithm Idea and Approach

- Use two pointers, one at the beginning (`left`) and one at the end (`right`) of the array.
- At each step, calculate the area formed by the lines at `left` and `right`.
- The area is determined by the shorter of the two heights and the distance between the pointers:  
  Area = min(height[left], height[right]) * (right - left)
- Update the maximum area found so far.
- Move the pointer that points to the shorter line inward, aiming to find a taller line that could increase the area.
- Continue until the two pointers meet.

---

## Python Example

```python
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        h = min(height[left], height[right])
        w = right - left
        max_area = max(max_area, h * w)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

# Example usage:
print(maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
```

---

## Complexity Analysis

- **Time:** O(n), where n is the number of elements in the array (each pointer moves at most n times).
- **Space:** O(1), only a few variables are used.

---

## Real-Life Applications

- Finding the maximum area between lines or boundaries (e.g., water storage between barriers, maximizing land or fence placement).
- Used in optimization and engineering problems involving distances and heights.
- Base for advanced interval and windowed search algorithms.

---

## Useful Links

- [Container With Most Water — LeetCode](https://leetcode.com/problems/container-with-most-water/)
- [Two Pointer Technique — GeeksforGeeks](https://www.geeksforgeeks.org/two-pointer-technique/)
- [Maximum Area Problem — Wikipedia](https://en.wikipedia.org/wiki/Maximum_area_problem)

---

## LeetCode Practice

| Difficulty | Problem                        | Link                                                                |
|------------|-------------------------------|---------------------------------------------------------------------|
| Medium     | Container With Most Water      | [#11 Container With Most Water](https://leetcode.com/problems/container-with-most-water/) |
| Medium     | Trapping Rain Water            | [#42 Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) |
| Medium     | Max Consecutive Ones III       | [#1004 Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) |
| Medium     | Largest Rectangle in Histogram | [#84 Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) |

---