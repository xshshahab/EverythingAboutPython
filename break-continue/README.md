**`break` and `continue` in Python**

**`break` Statement:**

- **Purpose:** Exits the current loop immediately.
- **Example:**

```python
for i in range(10):
    if i == 5:
        break  # Exit the loop when i reaches 5
    print(i)
```

**`continue` Statement:**

- **Purpose:** Skips the current iteration of the loop.

- Execution jumps back to the beginning of the loop for the next iteration.

- **Example:**

```python
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
```
