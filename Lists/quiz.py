# A list of user names is created and assigned to the variable `users`
users = ["rahul", "komal", "priya", "john", "pritam"]

# Printing the entire list `users`
print(users)  # Output: ['rahul', 'komal', 'priya', 'john', 'pritam']

# Printing the entire list using slicing syntax
print(users[:])  # Output: ['rahul', 'komal', 'priya', 'john', 'pritam']
# `[:]` means slicing from the start to the end of the list, which results in the whole list

# Printing the list starting from the second element (index 1) to the end
print(users[1:])  # Output: ['komal', 'priya', 'john', 'pritam']
# `[1:]` starts slicing from index 1 (second element) to the last element

# Printing the list starting from the second element (index 1) up to the second-to-last element (excluding the last one)
print(users[1:-1])  # Output: ['komal', 'priya', 'john']
# `[1:-1]` means start from index 1 (second element) and stop before the last element
