# Typecasting in python

Typecasting in Python in a simple and easy-to-understand way. It covers both **implicit** and **explicit** typecasting, with examples and common functions.

---

## What is Typecasting?

Typecasting is the process of converting one data type into another. It is useful when you need to perform operations that require specific data types.

---

## Types of Typecasting

### 1. Implicit Typecasting

- **Performed automatically by Python.**
- Converts smaller data types to larger ones safely.

#### Example:

```python
x = 10       # Integer
y = 5.5      # Float
z = x + y    # Python converts 'x' to float automatically
print(z)     # Output: 15.5
```

### 2. Explicit Typecasting

- **Manually performed by the programmer.**
- Requires the use of built-in functions to specify the target data type.

#### Example:

```python
x = "123"    # String
y = int(x)   # Explicitly converting 'x' to integer
print(y)     # Output: 123
```

### Common Typecasting Functions

- Here is a list of commonly used typecasting functions:

#### 1. **int()**

- **Converts data to an integer.**
- Removes the decimal part if the input is a float.

#### Example:

```python
print(int(4.8))       # Output: 4
print(int("123"))     # Output: 123
```

#### 2. **float()**

- Converts data to a float (decimal number).

#### Example:

```python
print(float(10))      # Output: 10.0
print(float("5.67"))  # Output: 5.67
```

#### 3. **str()**

- Converts data to a string.

#### Example:

```python
print(str(100))       # Output: "100"
print(str(10.5))      # Output: "10.5"
```

#### 4. **list()**

- Converts data to a list.

#### Example:

```python
print(list("hello"))  # Output: ['h', 'e', 'l', 'l', 'o']

```

#### 5. **tuple()**

- Converts data to a tuple.

#### Example:

```python
print(tuple([1, 2, 3]))  # Output: (1, 2, 3)
```

#### 5. **dict()**

- Converts data to a dictionary (if the input is compatible).

#### Example:

```python

data = [("key1", "value1"), ("key2", "value2")]
print(dict(data))      # Output: {'key1': 'value1', 'key2': 'value2'}

```

## Important Notes:

### 1. Not all typecasting is valid.

Some type conversions will raise an error if the data cannot be properly converted.

#### Example:

```python
print(int("abc"))  # This will raise a ValueError.

```

### 2. Loss of Data:

When converting a float to an integer, the decimal part is **truncated** (it is simply removed, not rounded).

#### Example:

```python
print(int(5.9))  # Output: 5

```

### 3. **Performance Impact:**

- Avoid excessive typecasting in loops or conditions for better performance.

###### Example Code to Try:

- Python script to test different typecasting methods:

```python

# Implicit Typecasting
x = 10
y = 2.5
z = x + y
print("Implicit Typecasting:", z)  # Output: 12.5

# Explicit Typecasting
a = "123"
b = int(a)
c = float(a)
print("Explicit Typecasting (int):", b)  # Output: 123
print("Explicit Typecasting (float):", c)  # Output: 123.0

# Other Examples
print(list("hello"))  # Output: ['h', 'e', 'l', 'l', 'o']
print(tuple([1, 2, 3]))  # Output: (1, 2, 3)
print(dict([("a", 1), ("b", 2)]))  # Output: {'a': 1, 'b': 2}


```
