# Introduction

This guide explains how to take user input in Python. User input is essential for interactive programs where the user provides data during the program's execution.

## 1. **What is User Input?**

User input is when a program asks the user to type something (e.g., their name, age, or a number) while it runs. Python collects this input using the input() function.

## 2. **How to Take Input?**

The input() function is used to take input from the user. It pauses the program and waits for the user to type something.

### Example:

```python

name = input("What is your name? ")
print("Hello, " + name)
```

## 3. **Important Points About input()**

- Always Returns a String:

- Whatever the user types is treated as a string.

### Example:

```python
data = input("Type something: ")
print(type(data)) # Output: <class 'str'>
```

Convert Input for Other Data Types:
If you need a number (e.g., integer or float), you must convert the input.

## 4. **Converting Input**

- To convert input into different data types, use these functions:

- To Integer: int()
- To Float: float()

### Example:

```python
# Take an integer input

age = int(input("How old are you? "))
print(f"You are {age} years old!")

# Take a decimal/float input

price = float(input("Enter the price: "))
print(f"The price is {price}")
```

## 5. **Steps to Take Input**

- Use the input() function to ask the user a question.
- Store the input in a variable.
- Convert the input to the required data type if necessary.
- Use the input in your program. 6. Full Example
- Here’s a complete program that takes multiple inputs:

```python
# Ask for user's name

name = input("What is your name? ")

# Ask for user's age and convert it to an integer

age = int(input("How old are you? "))

# Ask for a favorite number and convert it to a float

favorite_number = float(input("What is your favorite number? "))

# Display a summary

print(f"Hello {name}, you are {age} years old.")
print(f"Your favorite number is {favorite_number}.")
```

## 7. **Output Example**

- When the program runs, the output might look like this:

```bash
What is your name? Alex
How old are you? 25
What is your favorite number? 7.5
Hello Alex, you are 25 years old.
Your favorite number is 7.5.
```

8. Common Errors
   i. **Not Converting Input:**
   Forgetting to convert input to the required data type will result in errors when performing calculations.

### Example:

```python

number = input("Enter a number: ") # This is a string

print(number \* 2) # Will repeat the string instead of doubling the number
```

Fix:

```python

number = int(input("Enter a number: ")) # Convert to integer
print(number \* 2) # Now it doubles the number
```

ii. **Invalid Input:**

- If the user types something that can’t be converted, Python will raise an error.

### Example:

```python
age = int(input("Enter your age: ")) # If the user types "twenty", an error occurs
```

Fix: Use try and except to handle errors:

```python

try:
age = int(input("Enter your age: "))
print(f"You are {age} years old!")
except ValueError:
print("Please enter a valid number!")
```

## 9. **Practice Problems**

- Write a program to ask the user for their name and birth year, then calculate and display their age.
- Create a program that takes two numbers as input, adds them, and prints the result.
- Write a program to take a sentence as input and print the number of characters in it.
