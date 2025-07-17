# Python Variables and Data Types

This guide covers the basics of variables and data types in Python.

## What are Variables?

Variables are used to store data in Python. You can assign values to variables using the `=` operator.

### Example:

```python
name = "Alice"
age = 25
height = 5.8
is_student = True
```

### Rules for Naming Variables

- Start with a letter or an underscore \_.
- Cannot start with a number.
- Can contain letters, numbers, and underscores.
- Case-sensitive.

# Data Types in Python

Python provides several built-in data types to handle different types of data efficiently. Below is a categorized list of these data types with a brief description.

## Numeric Types

- **`int`**: Used to store whole numbers (e.g., `10`, `-5`).
- **`float`**: Used to store decimal numbers (e.g., `3.14`, `-0.001`).
- **`complex`**: Used to store complex numbers (e.g., `1 + 2j`).

## Text Type

- **`str`**: Used to store sequences of characters (e.g., `"Hello, World!"`).

## Boolean Type

- **`bool`**: Represents two possible values: `True` or `False`.

## Sequence Types

- **`list`**: Ordered, mutable (changeable) collections (e.g., `[1, 2, 3]`).
- **`tuple`**: Ordered, immutable collections (e.g., `(1, 2, 3)`).
- **`range`**: Represents a sequence of numbers (e.g., `range(5)`).

## Mapping Type

- **`dict`**: Represents key-value pairs (e.g., `{"key": "value", "name": "Alice"}`).

## Set Types

- **`set`**: Unordered collection of unique elements (e.g., `{1, 2, 3}`).
- **`frozenset`**: Immutable version of a set (e.g., `frozenset([1, 2, 3])`).

## None Type

- **`None`**: Represents the absence of a value or a null value.

---

## Example Code

Here’s an example demonstrating these data types in Python:

```python
# Numeric Types
x = 10           # int
y = 3.14         # float
z = 1 + 2j       # complex

# Text Type
text = "Hello, World!"

# Boolean Type
is_active = True

# Sequence Types
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_range = range(5)

# Mapping Type
my_dict = {"key": "value", "name": "Alice"}

# Set Types
my_set = {1, 2, 3}
my_frozenset = frozenset([1, 2, 3])

# None Type
nothing = None

# Print the data types
print(type(x))           # <class 'int'>
print(type(text))        # <class 'str'>
print(type(is_active))   # <class 'bool'>
print(type(my_list))     # <class 'list'>
print(type(my_dict))     # <class 'dict'>
print(type(my_frozenset)) # <class 'frozenset'>
print(type(nothing))     # <class 'NoneType'>

```
