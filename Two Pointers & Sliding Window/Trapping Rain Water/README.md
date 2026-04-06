# Trapping Rain Water

## Problem Description

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Example:**  
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]  
Output: 6  
Explanation: The elevation map can trap 6 units of water (see diagram for visual explanation).

---

## Algorithm Idea and Approach

- Use the two pointers technique to efficiently calculate trapped water:
  - Initialize two pointers, `left` and `right`, at the start and end of the array.
  - Maintain `left_max` and `right_max` to keep track of the maximum height to the left and right of each bar.
  - At each step:
    - If `height[left] < height[right]`, move `left` pointer and update `left_max`. Water trapped at `left` is `left_max - height[left]`.
    - Otherwise, move `right` pointer and update `right_max`. Water trapped at `right` is `right_max - height[right]`.
- Add up the trapped water for each position.

---

## Python Example

```python
def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

# Example usage:
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
```

---

## Complexity Analysis

- **Time:** O(n), single pass through the array.
- **Space:** O(1), constant extra space.

---

## Real-Life Applications

- Modeling water flow and accumulation in landscape or architecture.
- Analyzing histograms or 1D sensor data for dips and accumulation.
- Flood simulation and water retention analysis.

---

## Useful Links

- [Trapping Rain Water — LeetCode](https://leetcode.com/problems/trapping-rain-water/)
- [Two Pointer Technique — GeeksforGeeks](https://www.geeksforgeeks.org/two-pointers-technique/)
- [Visualization of Trapping Rain Water](https://www.youtube.com/watch?v=ZI2z5pq0TqA)

---

## LeetCode Practice

| Difficulty | Problem                | Link                                                                             |
|------------|-----------------------|----------------------------------------------------------------------------------|
| Hard       | Trapping Rain Water    | [#42 Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)    |
| Medium     | Container With Most Water | [#11 Container With Most Water](https://leetcode.com/problems/container-with-most-water/) |
| Medium     | Trapping Rain Water II | [#407 Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/) |

---