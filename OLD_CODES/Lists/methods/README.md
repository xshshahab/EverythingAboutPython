# List Methods

Python provides a variety of built-in methods to manipulate lists. Below are some commonly used list methods:

## 1. `append():`

- Adds an element to the end of the list.
- Syntax: `list.append(item)`
- **Example**

```python
my_list = [1, 2, 3]
my_list.append(4)  # Output: [1, 2, 3, 4]
```

## 2. `extend():`

- Adds multiple elements to the end of the list.
- Syntax: `list.extend(iterable)`
- **Example**

```python
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])  # Output: [1, 2, 3, 4, 5, 6]
```

## 3. `insert():`

- Inserts an element at a specified position in the list.
- Syntax: `list.insert(index, item)`
- **Example**

```python
my_list = [1, 2, 3]
my_list.insert(1, 4)  # Output: [1, 4, 2, 3]
```

## 4. `remove():`

- Removes the first occurrence of an element in the list.
- Syntax: `list.remove(item)`
- **Example**

```python
my_list = [1, 2, 3]
my_list.remove(2)  # Output: [1, 3]
```

- **Note:** If the element is not found, it raises a `ValueError`.

## 5. `pop():`

- **Usage:** Removes and returns an item at the given index (or the last item if index is not provided).
- Syntax: `list.pop(index)`
- **Example:**

```python
my_list = [1, 2, 3]
my_list.pop(1)  # Output: 2, list becomes [1, 3]
```

- **Note:** If the index is not provided, it removes and returns the last item.

## 6. `clear()`

- **Usage:** Removes all items from the list.
- **Syntax:** `list.clear()`
- **Example:**

```python
my_list = [1, 2, 3]
my_list.clear()  # Output: []
```

- **Note:** This method does not return anything.
