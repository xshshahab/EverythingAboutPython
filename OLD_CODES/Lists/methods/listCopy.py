# Define a list of numbers
numbers = [1, 2, 3, 4, 1, 5, 1, 6, 7, 8, 1]

# Print the original list of numbers
print("Original list (numbers):", numbers)

# Create a new reference 'newNumbers' that points to the same list as 'numbers'
newNumbers = numbers

# Modify the first element (index 0) of the 'newNumbers' list to 10
newNumbers[0] = 10

# Print the modified 'newNumbers' list
print("Modified list (newNumbers):", newNumbers)

# Print the original 'numbers' list to show that it is also affected
print("Original list (numbers) after modification:", numbers)
