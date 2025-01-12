# Define a variable with a single integer value in parentheses (1).
tup1 = (1)

# Print the type and value of tup1.
# Explanation: The parentheses are ignored unless followed by a comma, so tup1 is treated as an integer, not a tuple.
print(type(tup1), tup1)  # Output: <class 'int'> 1


# Define a single-element tuple by including a comma after the value.
tup2 = (1, )

# Print the type and value of tup2.
# Explanation: The comma makes it a tuple, even though there's only one element.
print(type(tup2), tup2)  # Output: <class 'tuple'> (1,)


# Define a tuple with multiple elements.
tup3 = (1, 2, 4, 5, 7)

# Print the type and value of tup3.
# Explanation: Multiple elements separated by commas inside parentheses naturally form a tuple.
print(type(tup3), tup3)  # Output: <class 'tuple'> (1, 2, 4, 5, 7)
