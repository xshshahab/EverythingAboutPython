# Dictionaries in python

In Python, dictionaries are unordered collections of items that store data in key-value pairs. They are one of Python’s built-in data types and are highly versatile for organizing and manipulating data.

## Key Features of Dictionaries:

1. **Key-Value Pairs:**

- Each item in a dictionary has a key and a corresponding value.
- Example: `{"name": "Alice", "age": 25}` where `"name"` and `"age"` are keys and `"Alice" `and `25` are values.

2. **Unordered:**

- As of Python 3.7, dictionaries maintain the insertion order of keys.

3. **Mutable:**

- You can modify the dictionary (add, update, or remove items).

4. **Keys Must Be Unique and Immutable:**

- Keys cannot be duplicated, and they must be immutable types like strings, numbers, or tuples.

5. **Values Can Be Any Type:**

- Values can be of any data type, including lists, other dictionaries, or custom objects.

---

## Creating a Dictionary:

```python
# Empty dictionary
my_dict = {}

# Dictionary with data
person = {
    "name": "Alice",
    "age": 25,
    "is_student": False
}
```

---

### Accessing Values:

```python
person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice
```

- To avoid errors, use `.get()`:

```python
print(person.get("gender", "Key not found"))  # Output: Key not found
```

## Adding and Updating Items:

```python
person["city"] = "New York"  # Add new key-value pair
person["age"] = 26           # Update existing key
```

---

## Removing Items:

```python
# Using pop()
age = person.pop("age")  # Removes and returns the value
print(age)  # Output: 25

# Using del
del person["city"]

# Clear all items
person.clear()
```

---

## Iterating Over a Dictionary:

```python
person = {"name": "Alice", "age": 25}

# Keys
for key in person:
    print(key)

# Values
for value in person.values():
    print(value)

# Keys and values
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## Dictionary Methods:

- `dict.keys():` Returns all keys.
- `dict.values():` Returns all values.
- `dict.items():` Returns all key-value pairs.
- `dict.update():` Merges another dictionary.
- `dict.pop(key):` Removes a key and returns its value.
- `dict.copy():` Creates a shallow copy of the dictionary.

---

## Nested Dictionaries:

Dictionaries can contain other dictionaries as values.

```python
students = {
    "student1": {"name": "Alice", "age": 25},
    "student2": {"name": "Bob", "age": 22}
}
print(students["student1"]["name"])  # Output: Alice
```
