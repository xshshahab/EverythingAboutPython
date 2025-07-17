# Lists in Python

A **list** in Python is like a collection of items, such as a shopping list or a to-do list. It allows you to store multiple items (like numbers, words, or other objects) in one variable.

### Features of Python Lists:

1. **Flexible:** You can store different types of items, such as numbers, strings, or even other lists.
2. **Ordered:** The items in a list stay in the order you put them.
3. **Changeable:** You can add, remove, or update items in a list.

### Key Points About Python Lists:

- Created using square brackets: `[ ]`
- Can contain any type of data: numbers, strings, or even other lists.
- Supports indexing: You can access items using their position (starting at 0).

---

### Python Code Example: Working with Lists

```python
# Creating a list
my_list = [1, 2, 3, "apple", "banana", [10, 20]]  # List with numbers, strings, and another list

# Accessing items in a list
print(my_list[0])  # Output: 1 (first item)
print(my_list[3])  # Output: "apple" (fourth item)

# Changing an item in the list
my_list[1] = "orange"  # Change second item from 2 to "orange"
print(my_list)  # Output: [1, 'orange', 3, 'apple', 'banana', [10, 20]]

# Adding an item to the list
my_list.append("grape")  # Adds "grape" to the end of the list
print(my_list)  # Output: [1, 'orange', 3, 'apple', 'banana', [10, 20], 'grape']

# Removing an item from the list
my_list.remove("apple")  # Removes "apple" from the list
print(my_list)  # Output: [1, 'orange', 3, 'banana', [10, 20], 'grape']

# Looping through a list
for item in my_list:
    print(item)  # Prints each item in the list
```
