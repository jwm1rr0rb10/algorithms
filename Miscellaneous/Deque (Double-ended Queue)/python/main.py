from collections import deque

print("--- Deque (Double-ended Queue) Example ---")

# 1. Initialization
my_deque = deque()

# 2. Adding Elements
my_deque.append(10)
my_deque.append(20)
my_deque.appendleft(5)
my_deque.appendleft(1)

print(f"Deque after additions: {my_deque}")
print(f"Size: {len(my_deque)}")

# 3. Access without removing
print(f"First element: {my_deque[0]}")
print(f"Last element: {my_deque[-1]}")

# 4. Removing Elements
removed_right = my_deque.pop()
print(f"Removed from right: {removed_right}, Deque: {my_deque}")

removed_left = my_deque.popleft()
print(f"Removed from left: {removed_left}, Deque: {my_deque}")

# 5. Check if empty
print(f"Is deque empty? {not my_deque}")

# 6. Extend with multiple elements
my_deque.extend([30, 40])
my_deque.extendleft([-1, 0])
print(f"After extend: {my_deque}")

# 7. Rotate
my_deque.rotate(1)
print(f"After rotating right: {my_deque}")

my_deque.rotate(-2)
print(f"After rotating left: {my_deque}")

# 8. Clear
my_deque.clear()
print(f"After clearing: {my_deque}")