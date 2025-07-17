## Match case in python

The match...case statement, introduced in Python 3.10, provides a powerful and expressive way to perform pattern matching, allowing for more readable and concise code when handling multiple conditions.

```python
match variable:
    case pattern1:
        # Code block for pattern1
    case pattern2:
        # Code block for pattern2
    case _:
        # Default case if no patterns match
```

#### Example:

```python
def http_status(status_code):
    match status_code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown Status"

print(http_status(200))  # Output: OK
print(http_status(404))  # Output: Not Found
print(http_status(123))  # Output: Unknown Status
```

In this example, the `http_status` function uses a `match` statement to compare the `status_code` against specific patterns (200, 404, 500). If a match is found, the corresponding message is returned. The underscore `_` serves as a wildcard pattern, matching any value not explicitly handled by the previous cases.

##### Using Guards for Additional Conditions:

You can add conditions to patterns using "guard" clauses with the `if` keyword:

```python
def number_type(num):
    match num:
        case x if x < 0:
            return "Negative"
        case 0:
            return "Zero"
        case x if x > 0:
            return "Positive"

print(number_type(-5))  # Output: Negative
print(number_type(0))   # Output: Zero
print(number_type(7))   # Output: Positive
```
