# Create a dictionary
dict1 = {"a": 1, "b": 2, "c": 3}

# Use the popitem() method to remove the last key-value pair
removed_item = dict1.popitem()

# Result: dict1 now contains {"a": 1, "b": 2}, and removed_item is ("c", 3)
print(dict1)          # Output: {"a": 1, "b": 2}
print(removed_item)   # Output: ("c", 3)
