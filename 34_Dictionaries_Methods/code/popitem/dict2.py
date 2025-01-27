# NOTE : In this example we don't know try except just for an understanding of how to use it.

# Create an empty dictionary
dict2 = {}

# Attempt to use popitem() on an empty dictionary
try:
    dict2.popitem()
except KeyError as e:
    print(f"Error: {e}")

# Output: Error: 'popitem(): dictionary is empty'
