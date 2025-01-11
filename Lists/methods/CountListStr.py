# Define a list of fruits
fruits = ["Orange", "Papaya", "Coconut", "Banana", "Papaya", "Papaya"]

# Print the original list of fruits
print("Original list:", fruits)

# Use the 'count()' method to count the number of times "Papaya" appears in the list
count_of_papaya = fruits.count("Papaya")

# Print the count of "Papaya" in the list
print("Count of 'Papaya':", count_of_papaya)

# You can also count other items, like "Orange"
count_of_orange = fruits.count("Orange")

# Print the count of "Orange" in the list
print("Count of 'Orange':", count_of_orange)

# If an item is not in the list, the count() method will return 0
count_of_apple = fruits.count("Apple")
print("Count of 'Apple':", count_of_apple)
