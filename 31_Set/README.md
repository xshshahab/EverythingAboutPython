# Sets in Python

A set in Python is a collection of `unique` items. It is `unordered` (`no defined order`) and does not allow `duplicate` values.

Think of it as a bag of items where:

1. **Order doesn't matter.**
2. **Duplicates are automatically removed.**

### Key Features of Sets

1. **Unordered:** Items in a set do not have a specific position.
2. **Unique Elements:** Duplicate items are automatically removed.
3. **Mutable:** You can add or remove items from a set.
4. **Set Operations:** Sets support mathematical operations like union, intersection, and difference.

### `Syntax`

You create a set using curly braces {} or the set() function.

```python
# Example 1: Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Example 2: Using set() function
another_set = set([1, 2, 2, 3, 4])
print(another_set)  # Output: {1, 2, 3, 4}
```

## **Set Operations**

Sets are very powerful because of their built-in operations.

```python
# Define two sets
A = {1, 2, 3}
B = {3, 4, 5}

# Union: Combines elements from both sets
print(A | B)  # Output: {1, 2, 3, 4, 5}

# Intersection: Common elements in both sets
print(A & B)  # Output: {3}

# Difference: Elements in A but not in B
print(A - B)  # Output: {1, 2}

# Symmetric Difference: Elements in A or B, but not both
print(A ^ B)  # Output: {1, 2, 4, 5}
```

## **Adding and Removing Elements**

You can modify a set using `add()` and `remove()`.

```python
# Create a set
fruits = {"apple", "banana", "cherry"}

# Add an element
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# Remove an element
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

# Discard removes an item, but doesn't throw an error if it doesn't exist
fruits.discard("mango")  # No error
```

## Checking Membership

You can check if an item exists in a set using the in keyword.

```python
# Check membership
numbers = {1, 2, 3, 4, 5}
print(3 in numbers)  # Output: True
print(6 in numbers)  # Output: False
```

### **Why Use Sets?**

- **Avoid duplicates:** If you want only unique items, sets are the perfect choice.
- **Fast membership tests:** Checking if an item exists is faster in sets compared to lists.
- **Mathematical operations:** Easily handle tasks like finding common elements or differences between datasets.
