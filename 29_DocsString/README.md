# What is a Docstring in Python?

A **docstring** is a special string used to document a Python function, class, or module. It helps explain what the code does.

## How to Write a Docstring

1. Place it right after the function, class, or module declaration.
2. Use triple double quotes (`"""`) to enclose the docstring.

### Example for a Function

```python
def greet(name):
    """
    This function greets the person whose name is passed as a parameter.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"
```

### Example for a Class

```python
class Person:
    """
    A class to represent a person.

    Attributes:
    name (str): Name of the person.
    age (int): Age of the person.
    """

    def __init__(self, name, age):
        """
        Constructs all the necessary attributes for the person object.

        Parameters:
        name (str): Name of the person.
        age (int): Age of the person.
        """
        self.name = name
        self.age = age
```

## Why Use Docstrings?

- Helps understand the purpose of code.
- Useful for generating documentation automatically.
- Makes code easier to maintain and share.

---

# What is PEP 8 in Python?

**PEP 8** stands for **Python Enhancement Proposal 8**. It is a set of guidelines and best practices for writing clean, readable, and consistent Python code.

## Key Guidelines of PEP 8

1. **Indentation:** Use **4 spaces** per indentation level.

   ```python
   def example_function():
       if True:
           print("Follow PEP 8!")
   ```

2. **Line Length:** Limit lines to **79 characters**.

   ```python
   # Good:
   greeting = "Hello, welcome to the Python PEP 8 example."

   # Bad:
   long_greeting = "Hello, this line is too long and does not follow PEP 8 guidelines for length."
   ```

3. **Blank Lines:**

   - Use 2 blank lines between functions or classes.
   - Use 1 blank line between methods inside a class.

   ```python
   def function_one():
       pass


   def function_two():
       pass
   ```

4. **Imports:** Place imports at the top of the file.

   - Use separate lines for different imports.

   ```python
   # Good:
   import os
   import sys

   # Bad:
   import os, sys
   ```

5. **Spaces Around Operators and After Commas:**

   ```python
   # Good:
   x = 1 + 2
   y = [1, 2, 3]

   # Bad:
   x=1+2
   y=[1,2,3]
   ```

6. **Naming Conventions:** Use meaningful and descriptive names.

   - Variables and functions: snake_case (`example_variable`)
   - Classes: PascalCase (`ExampleClass`)

   ```python
   # Good:
   def calculate_sum():
       pass

   # Bad:
   def CalculateSum():
       pass
   ```

## Why Follow PEP 8?

- Increases code readability and maintainability.
- Helps developers collaborate easily.
- Makes code look consistent and professional.
