# Function to check if the first number is greater than the second
def isGreater(a, b):
    if a > b:  # If 'a' is greater than 'b'
        print("First number is greater")
    else:  # If 'a' is less than or equal to 'b'
        print("Second number is greater or equal")

# Function to check if the first number is lesser than the second
# Currently not implemented
def isLesser(a, b):
    pass  # Placeholder for future implementation

# Main code starts here
a = 10  # First number
b = 91  # Second number

# Call the function to compare 'a' and 'b'
isGreater(a, b)
