# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Print the original list
print("Original list of numbers:", numbers)

# Use the copy() method to create a new list 'newNumbers' that is a copy of 'numbers'
newNumbers = numbers.copy()

# Modify the first element of the new list 'newNumbers'
newNumbers[0] = 10

# Print the modified 'newNumbers' list
print("Modified newNumbers list:", newNumbers)

# Print the original 'numbers' list to show it has not been affected
print("Original numbers list after modification:", numbers)


# Define a list of fruit names (strings)
fruits = ["Apple", "Banana", "Cherry", "Mango"]

# Print the original list of fruits
print("Original list of fruits:", fruits)

# Use the copy() method to create a new list 'newFruits' that is a copy of 'fruits'
newFruits = fruits.copy()

# Modify the first element of the new list 'newFruits'
newFruits[0] = "Orange"

# Print the modified 'newFruits' list
print("Modified newFruits list:", newFruits)

# Print the original 'fruits' list to show it has not been affected
print("Original fruits list after modification:", fruits)
