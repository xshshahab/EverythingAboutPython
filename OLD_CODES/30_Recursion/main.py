def fibonacci_recursive(num1, num2, n, sequence=None):
    """
    Generate the Fibonacci sequence using recursion.

    :param num1: The first number in the sequence
    :param num2: The second number in the sequence
    :param n: The number of terms to generate
    :param sequence: Used internally to store the sequence during recursion
    :return: A list of Fibonacci sequence numbers
    """
    # Initialize the sequence list on the first call
    if sequence is None:
        sequence = [num1, num2]

    # Base case: stop when the sequence has n terms
    if len(sequence) == n:
        return sequence

    # Recursive case: calculate the next number and add it to the sequence
    next_number = sequence[-1] + sequence[-2]
    sequence.append(next_number)
    return fibonacci_recursive(num1, num2, n, sequence)

# Input from the user
try:
    num1 = int(input("Enter the first number of the sequence: "))
    num2 = int(input("Enter the second number of the sequence: "))
    n = int(input("Enter the number of terms you want in the sequence: "))
    
    if n < 2:
        print("The number of terms should be at least 2.")
    else:
        fibonacci_sequence = fibonacci_recursive(num1, num2, n)
        print("The Fibonacci sequence is:", fibonacci_sequence)

except ValueError:
    print("Please enter valid integers.")

# Example: Generate a Fibonacci sequence starting with 0 and 1, for 10 terms
result = fibonacci_recursive(0, 1, 10)
print(result)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Example: Generate a sequence starting with 2 and 3, for 7 terms
result = fibonacci_recursive(2, 3, 7)
print(result)  # Output: [2, 3, 5, 8, 13, 21, 34]
