# Jump Index in List Slicing `(Step or Stride)`

In Python, you can use a step (jump index) in list slicing to skip items in a sequence. The syntax is:

```python
list[start:end:step]
```

- `start`: The index where the slicing starts (default is 0).
- `end`: The index where the slicing ends (default is the end of the list).
- `step`: The interval between each index (default is 1).

If the `step` is positive, slicing moves forward; if it's negative, slicing moves backward.

### Examples of Jump Index in Slicing:

```python
# Creating a list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 1: Jump index of 2 (every second element)
print(numbers[::2])  # Output: [0, 2, 4, 6, 8]
# Explanation: Starts from the beginning, skips every second element.

# Example 2: Jump index of 3 (every third element)
print(numbers[::3])  # Output: [0, 3, 6, 9]
# Explanation: Starts from the beginning, skips every two elements.

# Example 3: Negative jump index (reverse the list)
print(numbers[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# Explanation: The step `-1` starts from the last element and goes backward.

# Example 4: Using start, end, and jump index together
print(numbers[1:8:2])  # Output: [1, 3, 5, 7]
# Explanation: Starts at index 1, stops before index 8, skips every second element.

# Example 5: Reverse with jump index of -2 (every second element in reverse)
print(numbers[8:1:-2])  # Output: [8, 6, 4, 2]
# Explanation: Starts at index 8, goes backward to index 1 (exclusive), skips every second element.

```
