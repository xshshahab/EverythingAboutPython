
# Define three lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Use list comprehension to concatenate the lists
result = [item for sublist in [list1, list2, list3] for item in sublist]

# Print the concatenated list
print("Concatenated list using list comprehension:", result)
