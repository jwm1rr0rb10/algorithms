# --- HashMap (Python Dictionary) Example ---
print("--- HashMap Example ---")
my_map = {}

my_map["apple"] = 10
my_map["banana"] = 20
my_map["cherry"] = 30
my_map["date"] = 10  # Duplicate value

print(f"Map after insertions: {my_map}")

print(f"Value for 'banana': {my_map['banana']}")
print(f"Value for 'apple': {my_map.get('apple', 'Not Found')}")
print(f"Value for 'grape': {my_map.get('grape', 'Not Found')}")

print(f"'cherry' in map: {'cherry' in my_map}")
print(f"'fig' in map: {'fig' in my_map}")

del my_map["banana"]
print(f"Map after deleting 'banana': {my_map}")

for key in my_map:
    print(f"Key: {key}, Value: {my_map[key]}")

for key, value in my_map.items():
    print(f"Key: {key}, Value: {value}")

# --- HashSet (Python Set) Example ---
print("\n--- HashSet Example ---")
my_set = set()

my_set.add("red")
my_set.add("green")
my_set.add("blue")
my_set.add("red")  # Duplicate ignored

print(f"Set after additions: {my_set}")

print(f"'green' in set: {'green' in my_set}")
print(f"'yellow' in set: {'yellow' in my_set}")

my_set.remove("blue")
print(f"Set after removing 'blue': {my_set}")

my_set.discard("yellow")
print(f"Set after discarding 'yellow': {my_set}")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Union: {set1.union(set2)}")
print(f"Intersection: {set1.intersection(set2)}")
print(f"Difference: {set1.difference(set2)}")
print(f"Symmetric Difference: {set1.symmetric_difference(set2)}")

print("Iterating through set elements:")
for item in my_set:
    print(item)