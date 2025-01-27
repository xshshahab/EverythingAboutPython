# Create a dictionary
dict2 = {"x": 10, "y": 20}

# Use the del statement to delete the entire dictionary
del dict2

# Trying to print dict2 after deletion will raise a NameError
try:
    print(dict2)
except NameError as e:
    print(f"Error: {e}")
