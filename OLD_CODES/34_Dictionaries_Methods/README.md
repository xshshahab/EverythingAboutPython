# Python Dictionary Methods

A dictionary in Python is a collection of key-value pairs, where each key is unique. Python provides several built-in methods to work with dictionaries. Below is a summary of commonly used dictionary methods with examples.

---

## 1. `dict.clear()`

Removes all items from the dictionary.

```python
my_dict = {"a": 1, "b": 2, "c": 3}
my_dict.clear()
print(my_dict)  # Output: {}
```

---

## 2. `dict.copy()`

Returns a shallow copy of the dictionary.

```python
original = {"x": 10, "y": 20}
copy_dict = original.copy()
print(copy_dict)  # Output: {'x': 10, 'y': 20}
```

---

## 3. `dict.fromkeys(iterable, value=None)`

Creates a new dictionary with keys from the given iterable and sets all values to the specified value (default is `None`).

```python
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}
```

---

## 4. `dict.get(key, default=None)`

Returns the value for the specified key. If the key is not found, it returns the default value.

```python
person = {"name": "Alice", "age": 25}
print(person.get("name"))       # Output: Alice
print(person.get("gender", "N/A"))  # Output: N/A
```

---

## 5. `dict.items()`

Returns a view object of dictionary’s key-value pairs.

```python
data = {"x": 1, "y": 2}
print(data.items())  # Output: dict_items([('x', 1), ('y', 2)])
```

---

## 6. `dict.keys()`

Returns a view object of dictionary’s keys.

```python
data = {"x": 1, "y": 2}
print(data.keys())  # Output: dict_keys(['x', 'y'])
```

---

## 7. `dict.values()`

Returns a view object of dictionary’s values.

```python
data = {"x": 1, "y": 2}
print(data.values())  # Output: dict_values([1, 2])
```

---

## 8. `dict.pop(key, default=None)`

Removes the specified key and returns its value. If the key is not found, it returns the default value.

```python
data = {"x": 1, "y": 2}
print(data.pop("x"))  # Output: 1
print(data)           # Output: {'y': 2}
```

---

## 9. `dict.popitem()`

Removes and returns the last key-value pair as a tuple. Raises a KeyError if the dictionary is empty.

```python
data = {"x": 1, "y": 2}
print(data.popitem())  # Output: ('y', 2)
print(data)            # Output: {'x': 1}
```

---

## 10. `dict.setdefault(key, default=None)`

Returns the value of the specified key. If the key does not exist, it inserts the key with the specified default value.

```python
data = {"x": 1}
print(data.setdefault("x", 0))  # Output: 1
print(data.setdefault("y", 2))  # Output: 2
print(data)                     # Output: {'x': 1, 'y': 2}
```

---

## 11. `dict.update([other])`

Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.

```python
data = {"a": 1}
data.update({"b": 2, "c": 3})
print(data)  # Output: {'a': 1, 'b': 2, 'c': 3}
```

---

## 12. `dict.__contains__(key)`

Checks if a key exists in the dictionary. This is equivalent to using the in operator.

```python
data = {"x": 1, "y": 2}
print("x" in data)  # Output: True
```

---

### Example Summary

Below is a code block combining some of the methods for reference:

```python
# Example of dictionary methods
my_dict = {"a": 1, "b": 2}

# Add new key
my_dict["c"] = 3

# Use update method
my_dict.update({"d": 4})

# Check keys and values
print(my_dict.keys())     # dict_keys(['a', 'b', 'c', 'd'])
print(my_dict.values())   # dict_values([1, 2, 3, 4])

# Get and remove values
print(my_dict.get("a"))   # 1
print(my_dict.pop("a"))   # 1

# Final dictionary
print(my_dict)            # {'b': 2, 'c': 3, 'd': 4}
```
