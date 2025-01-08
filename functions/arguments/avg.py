# Define a function named calcAvg that takes a variable number of arguments using *numbers.
def calcAvg(*numbers):
    # Initialize a variable 'sum' to 0. This will hold the sum of all numbers passed to the function.
    sum = 0

    # Loop through each number in the 'numbers' tuple (variable-length arguments are stored as a tuple).
    for i in numbers:
        # Add each number to the 'sum' variable.
        sum += i

    # Calculate the average by dividing the 'sum' by the total number of arguments passed.
    # Use len(numbers) to get the count of the numbers in the tuple.
    print("Average is :", sum / len(numbers))

# Call the calcAvg function with three numbers: 3, 4, and 5.
calcAvg(3, 4, 5)
