# Create a dictionary
dict2 = {"x": 10, "y": 20}

# Try to remove a key that doesn't exist, with a default value provided
removed_value = dict2.pop("z", "Not Found")

# Result: dict2 remains unchanged, and removed_value is "Not Found"
print(dict2)          # Output: {"x": 10, "y": 20}
print(removed_value)  # Output: "Not Found"
