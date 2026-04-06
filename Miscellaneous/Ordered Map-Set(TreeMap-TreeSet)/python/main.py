# You might need to install it: pip install sortedcontainers
from sortedcontainers import SortedDict, SortedList

print("--- Ordered Map (SortedDict) Example ---")
my_map = SortedDict()

# 1. Insertion
my_map[5] = "apple"
my_map[2] = "banana"
my_map[8] = "cherry"
my_map[1] = "date"
my_map[5] = "grape" # Updates value for key 5

print(f"Map after insertions (sorted by key): {my_map}")
# Output will show elements sorted by key: SortedDict({1: 'date', 2: 'banana', 5: 'grape', 8: 'cherry'})

# 2. Lookup
print(f"Value for key 2: {my_map.get(2, 'Not Found')}") # Output: banana
print(f"Value for key 7: {my_map.get(7, 'Not Found')}") # Output: Not Found

# 3. Check for key existence
print(f"Is key 8 in map? {8 in my_map}") # Output: True

# 4. Deletion
del my_map[2]
print(f"Map after deleting key 2: {my_map}")
# Output: SortedDict({1: 'date', 5: 'grape', 8: 'cherry'})

# 5. Iteration (always sorted by key)
print("Iterating through map keys:")
for key in my_map:
    print(f"Key: {key}, Value: {my_map[key]}")

# 6. Ordered specific operations (example with SortedDict)
print(f"Smallest key: {my_map.keys()[0]}")   # Or my_map.peekitem(0)[0]
print(f"Largest key: {my_map.keys()[-1]}")   # Or my_map.peekitem(-1)[0]
print(f"Keys less than or equal to 5: {my_map.bisect_right(5)}") # Returns index where 5 could be inserted to maintain order (first index > 5)
                                                                 # Correct usage for range: my_map.irange(None, 5)

print("\n--- Ordered Set (SortedList) Example ---")
my_set = SortedList()

# 1. Insertion (adding unique elements, sorted)
my_set.add(50)
my_set.add(20)
my_set.add(80)
my_set.add(10)
my_set.add(50) # Duplicates are ignored

print(f"Set after additions (sorted): {my_set}")
# Output: SortedList([10, 20, 50, 80])

# 2. Check for element existence
print(f"Is 20 in set? {20 in my_set}") # Output: True
print(f"Is 70 in set? {70 in my_set}") # Output: False

# 3. Deletion
my_set.remove(20)
print(f"Set after removing 20: {my_set}")
# Output: SortedList([10, 50, 80])

# 4. Iteration (always sorted)
print("Iterating through set elements:")
for item in my_set:
    print(item)

# 5. Ordered specific operations (example with SortedList)
print(f"Smallest element: {my_set[0]}")
print(f"Largest element: {my_set[-1]}")
print(f"Count of 50: {my_set.count(50)}")
print(f"Index of 50: {my_set.index(50)}")