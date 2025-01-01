# String Methods in Python

String methods in Python are built-in functions that you can use to perform operations on strings. Here's a summary of commonly used string methods with examples and explanations.

## Common String Methods

### 1.**lower()**

Converts all characters of a string to lowercase.

```python
text = "HELLO"
print(text.lower())  # Output: "hello"
```

### 2.**upper()**

Converts all characters of a string to uppercase.

```python
text = "hello"
print(text.upper())  # Output: "HELLO"
```

### 3. **strip()**

Removes leading and trailing spaces (or specified characters).

```python
text = "  hello  "
print(text.strip())  # Output: "hello"
```

### 4. **replace(old, new)**

Replaces all occurrences of a substring with another substring.

```python
text = "hello world"
print(text.replace("world", "Python")) # Output: "hello Python"
```

### 5. **split(separator)**

Splits the string into a list using the specified separator.

```python
text = "apple,banana,grape"
print(text.split(","))  # Output: ["apple", "banana", "grape"]
```

### 6. **join(iterable)**

Joins elements of an iterable (like a list) into a string using a specified separator.

```python
fruits = ["apple", "banana", "grape"]
print(", ".join(fruits))  # Output: "apple, banana, grape"
```

### 7. **find(substring)**

Returns the index of the first occurrence of a substring, or -1 if not found.

```python
text = "hello world"
print(text.find("world")) # Output: 6
```

### 8. **count(substring)**

Counts how many times a substring appears in the string.

```python
text = "banana"
print(text.count("a"))  # Output: 3
```

### 9. **startswith(substring)**

Checks if the string starts with the specified substring.

```python
text = "hello"
print(text.startswith("he"))  # Output: True
```

### 10. **endswith(substring)**

Checks if the string ends with the specified substring.

```python
text = "hello"
print(text.endswith("lo")) # Output: True
```

### 11.**capitalize()**

Converts the first character of the string to uppercase.

```python
text = "hello"
print(text.capitalize()) # Output: "Hello"
```

### 12. **title()**

Converts the first character of each word to uppercase.

```python
text = "hello world"
print(text.title()) # Output: "Hello World"
```

### 13. **isalpha()**

Returns True if all characters are alphabetic.

```python
text = "hello"
print(text.isalpha()) # Output: True
```

### 14. **isdigit()**

Returns True if all characters are digits.

```python
text = "12345"
print(text.isdigit()) # Output: True
```

### 15. **isalnum()**

Returns True if all characters are alphanumeric (letters or numbers).

```python
text = "hello123"
print(text.isalnum()) # Output: True
```

### 16. **rstrip()**

The rstrip() method removes trailing spaces or specified characters from the right end of a string.

```python
text = "hello!!!"
print(text.rstrip("!"))  # Output: "hello"
```

### 17. **lstrip()**

The lstrip() method removes leading spaces or specified characters from the left end of a string.

```python
text = "###hello"
print(text.lstrip("#"))  # Output: "hello"
```

#### **case :** Combination of Characters

```python
text = "123hello"
print(text.lstrip("123"))  # Output: "hello"
```
