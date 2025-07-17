s1 = {1, 2, 5, 6}
s2 = {7, 6, 4, 3}

s3 = s1.union(s2)
print("Union :", s3)

print(s1, s2)


# --------------------- Remove() ---------------------
# Creating a set
fruits = {"apple", "banana", "cherry", "orange"}

# Removing an element
fruits.remove("banana")

# Printing the updated set
print(fruits)


# --------------------- Discard() ---------------------

# Creating a set of numbers
numbers = {1, 2, 3, 4, 5}

# Trying to remove an element that doesn't exist using discard()
numbers.discard(6)

# Printing the updated set
print(numbers)
