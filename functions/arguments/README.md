# Functions arguments and return statements in python :

- Arguments are the values that are passed to a function when it is called.
- Return statements are used to return a value from a function.
- In python, arguments are passed by object reference, which means that if you pass a mutable object (like a list or a dictionary) to a function, you can modify the object inside the function and see the changes outside the function.

- If you pass an immutable object (like an integer or a string) to a function, you cannot modify the object inside the function. Return statements are used to return a value from a function. The return statement can be used with or without an argument. If the return statement is used with an argument, the function will return that argument. If the return statement is used without an argument, the function will return None.

---

## 1. **Function Arguments**

Arguments are the values you pass to a function when calling it. Functions can accept arguments to process data.

### Types of Function Arguments:

#### 1. Positional Arguments

Passed in order and matched with parameters in the function definition.

```python
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8
```

#### 2. Default Arguments

Parameters can have default values, which are used if no value is passed.

```python
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
print(greet())         # Output: Hello, Guest!
```

#### 3. Keyword Arguments in Python

You can pass arguments by explicitly specifying parameter names. This is especially useful when a function has multiple parameters, and you want to avoid ambiguity.

### Example:

```python
def introduce(name, age):
    return f"My name is {name} and I am {age} years old."

# Calling the function using keyword arguments
print(introduce(age=25, name="Bob"))  # Output: My name is Bob and I am 25 years old.
```

#### 4. Variable-Length Arguments in Python

In Python, you can use `*args` and `**kwargs` to pass a variable number of arguments to a function:

- **`*args`**: Allows passing multiple positional arguments as a tuple.
- **`**kwargs`\*\*: Allows passing multiple keyword arguments as a dictionary.

### Example:

```python
def show_items(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Calling the function with positional and keyword arguments
show_items(1, 2, 3, item1="Book", item2="Pen")
```

---

# Return Statements in Python

The `return` statement is used to send a result back to the caller of the function. It can be used to return a single value, multiple values, or nothing.

---

## Examples:

### 1. Returning a Single Value

```python
def square(number):
    return number * number

result = square(4)
print(result)  # Output: 16
```

# Returning Multiple Values in Python

In Python, a function can return multiple values. These values are usually returned as a tuple, which can then be unpacked into individual variables.

---

### Example:

```python
def calculate(a, b):
    return a + b, a - b, a * b

# Assigning the returned values to variables
sum_, diff, product = calculate(5, 3)
print(sum_, diff, product)  # Output: 8 2 15
```

---

## Combining Arguments and Return Statements

Here’s a complete example:

```python
def calculate_area(length, width=1):  # Default width is 1
    """
    This function calculates the area of a rectangle.
    """
    area = length * width
    return area

# Example Usage:
print(calculate_area(5, 4))  # Output: 20
print(calculate_area(7))     # Output: 7 (uses default width)
```
