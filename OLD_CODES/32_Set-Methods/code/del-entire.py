# Creating a set of numbers
numbers = {1, 2, 3, 4, 5}

# Deleting the entire set
del numbers

# Attempting to print the set after deletion will raise an error
try:
    print(numbers)
except NameError:
    print("The set has been deleted.")
