# Define a list of fruits
fruits = ["Apple", "Banana", "Cherry"]

# Define another list of fruits to extend the first list
more_fruits = ["Orange", "Mango", "Pineapple"]

# Print the original list of fruits
print("Original list of fruits:", fruits)

# Use the extend() method to add all elements of more_fruits to the fruits list
fruits.extend(more_fruits)

# Print the extended list of fruits
print("List after extending:", fruits)
