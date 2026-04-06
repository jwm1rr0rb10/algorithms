### Maximum in Sliding Window
from collections import deque

def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []

    dq = deque()
    result = []

    for i in range(len(nums)):
        if dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Examples
print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
print(max_sliding_window([1], 1))                        # [1]
print(max_sliding_window([9, 11], 2))                    # [11]
print(max_sliding_window([7, 2, 4], 2))                  # [7, 4]

### Minimum in Sliding Window
def min_sliding_window(nums, k):
    if not nums or k == 0:
        return []

    dq = deque()
    result = []

    for i in range(len(nums)):
        if dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] >= nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Example
print(min_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [-1, -3, -3, -3, 3, 3]