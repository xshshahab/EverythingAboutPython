# Create a dictionary
dict1 = {"a": 1, "b": 2, "c": 3}

# Use the pop() method to remove the key "b"
removed_value = dict1.pop("b")

# Result: dict1 now contains {"a": 1, "c": 3}, and removed_value is 2
print(dict1)          # Output: {"a": 1, "c": 3}
print(removed_value)  # Output: 2
