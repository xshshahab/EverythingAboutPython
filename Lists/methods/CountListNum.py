# Define a list of numbers
numbers = [1, 2, 3, 4, 1, 5, 1, 6, 7, 8, 1]

# Print the original list of numbers
print("Original list of numbers:", numbers)

# Use 'count()' to count how many times the number 1 appears in the list
count_of_one = numbers.count(1)

# Print the count of 1
print("Count of 1 in the list:", count_of_one)

# Count the occurrences of the number 3
count_of_three = numbers.count(3)
print("Count of 3 in the list:", count_of_three)

# Count an item not in the list (e.g., 10)
count_of_ten = numbers.count(10)
print("Count of 10 in the list:", count_of_ten)
