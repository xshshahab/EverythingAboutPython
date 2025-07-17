# Define a list of numbers
numbers = [1, 2, 3]

# Define a tuple of numbers to extend the list
more_numbers = (4, 5, 6)

# Print the original list of numbers
print("Original list of numbers:", numbers)

# Use the extend() method to add all elements of more_numbers to the numbers list
numbers.extend(more_numbers)

# Print the extended list of numbers
print("List after extending:", numbers)
