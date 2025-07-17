def square():
    """
        Take a number as input and return its square.
    """
    num = int(input("Enter a number: "))
    return num ** 2

value = square()
print("Result :", value)

print(square.__doc__)