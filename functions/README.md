## Defining a Function

A function is defined using the `def` keyword, followed by the function name, parentheses `( )`, and a colon `:`.

### **Syntax:**

```python
def function_name(parameters):
"""
Optional docstring (describes what the function does).
""" # Function body
return value # (Optional)
```

### **Example:**

```python
def greet(name):
    """This function greets the person whose name is passed as an argument."""
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

### Calling a Function

You invoke a function by using its name followed by parentheses.

##### **Example:**

```python
def add(a, b):
    return a + b

result = add(3, 5)  # Calling the function
print(result)       # Output: 8
```
