# Python Modules and pip - Quick Overview

## What is a Python Module?

- A **module** is a file containing Python code that can define functions, classes, and variables.
- It allows you to organize your code into manageable sections.
- You can import and use modules in other Python programs to reuse code.
- Example: `math`, `os`, `sys` are common built-in modules in Python.

# Types of Modules in Python

In Python, modules can be categorized into different types:

## 1. **Built-in Modules**

- These are modules that come pre-installed with Python.
- You don’t need to install them separately.
- Example modules: `math`, `sys`, `os`, `random`, `time`.

### Example:

```python
import math
print(math.sqrt(16))  # Output: 4.0
```

## 2. Third-party Modules

- These are modules that are not included with Python by default.
- You can install them using pip from the Python Package Index (PyPI).
- Example modules: `requests`, `numpy`, `pandas`, `flask`, `django`.

## 3. Custom Modules

- These are modules that you create yourself.
- You write your own Python code and save it as a `.py` file, which can then be imported into other programs.
- Example: If you create a file named `my_module.py`, you can import it like this:

### Example:

````python
# In my_module.py
def greet():
    return "Hello, World!"

# In another Python file
import my_module
print(my_module.greet())  # Output: Hello, World!



### How to Use a Module:

- To use a module, you **import** it in your Python program.
- Example:
  ```python
  import math
  print(math.sqrt(16))  # Output: 4.0
````

# What is pip?

- **pip** is the Python package installer.
- It allows you to install third-party libraries (packages) that are not part of the standard Python library.
- **pip** can install libraries from the Python Package Index (PyPI), a repository of Python software.
