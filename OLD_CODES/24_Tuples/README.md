# What is a Tuple?

A tuple is an **immutable (unchangeable)** sequence type in Python that can store multiple items. Tuples are defined using parentheses `()` and can hold elements of different data types.

## **Defining Tuples**

### **1. Empty Tuple**

```python
empty_tuple = ()
print(type(empty_tuple))  # Output: <class 'tuple'>
```

### **2. Single-Element Tuple**

To define a single-element tuple, a comma is required after the element:

```python
single_element_tuple = (1,)
print(type(single_element_tuple)) # Output: <class 'tuple'>
```

Without the comma, it will be considered an integer:

```python
not_a_tuple = (1)
print(type(not_a_tuple)) # Output: <class 'int'>
```

### **3. Multi-Element Tuple**

Tuples with multiple elements are created by separating values with commas:

```python
multi_element_tuple = (1, 2, 3, 4)
print(type(multi_element_tuple))  # Output: <class 'tuple'>
```

## Tuple Characteristics

- **Immutable:** Once created, the elements of a tuple cannot be changed.
- **Ordered:** Elements have a defined order and can be accessed by index.
- **Allows Duplicates:** Tuples can contain duplicate values.

---

## Tuple Operations

### **Accessing Elements**

```python
tup = (10, 20, 30)
print(tup[0])  # Output: 10
```

### **Tuple Length**

```python
print(len(tup)) # Output: 3
```

### **Tuple Concatenation**

```python
tup1 = (1, 2)
tup2 = (3, 4)
print(tup1 + tup2) # Output: (1, 2, 3, 4)
```

### **Tuple Slicing**

```python
print(tup[1:3]) # Output: (20, 30)
```

---

## Why Use Tuples?

- Tuples are faster than lists due to their immutability.
- Useful when you want to ensure data remains unchanged.
- Can be used as keys in dictionaries because they are hashable.
